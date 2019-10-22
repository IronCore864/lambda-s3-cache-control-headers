# Set Cache Control Headers on S3 Origin

Integrate S3 event with this lambda function and it will set Cache-Control max-age headers for each file created/updated in the S3 bucket.

In this case you don't need to use default TTL in CloudFront, but rather use origin settings.

## Dependency

- python3
- venv

## Build
 
```
# at the root directory of this repo
virtualenv venv
. ./venv/bin/activate
pip3 install -r requirements.txt
rm ~/set_cache_control.zip
cd venv/lib/python3.7/site-packages  
zip -r ~/set_cache_control.zip .
cd -
zip -g ~/set_cache_control.zip main.py
```

Upload to s3, and publish new version of lambda:

```
aws s3 cp ~/set_cache_control.zip s3://your-bucket-for-lambda-package/
aws lambda update-function-code --s3-bucket your-bucket-for-lambda-package --s3-key set_cache_control.zip --function-name your_lambda_function_name
aws lambda publish-version --function-name your_lambda_function_name
```

## TEST
```
python -m unittest discover test
```
