from urllib.parse import unquote_plus
import pathlib
from collections import defaultdict

import boto3

s3 = boto3.resource('s3')

FIVE_MIN = 60 * 5
DAY_IN_SEC = 60 * 60 * 24
YEAR_IN_SEC = DAY_IN_SEC * 365


def _get_max_age_by_file_name(filename):
    extension = pathlib.Path(filename).suffix
    d = defaultdict(lambda: YEAR_IN_SEC)

    d['.html'] = FIVE_MIN

    d['.png'] = YEAR_IN_SEC
    d['.css'] = YEAR_IN_SEC
    d['.js'] = YEAR_IN_SEC

    return d[extension]


def handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = unquote_plus(record['s3']['object']['key'])

        s3_object = s3.Object(bucket, key)
        max_age = _get_max_age_by_file_name(key)
        s3_object.metadata.update({
            "Cache-Control": "public, max-age={}".format(max_age)
        })

        s3_object.copy_from(
            CopySource={"Bucket": bucket, "Key": key},
            ContentType=s3_object.content_type,
            Metadata=s3_object.metadata,
            MetadataDirective='REPLACE'
        )
