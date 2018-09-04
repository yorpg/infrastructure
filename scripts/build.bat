set code_path=code
pip install  -qq -r requirements.txt -t build/%code_path%/
cp %code_path%/*.py build/%code_path%/

sam package --template-file template.yaml --output-template-file build\packaged.yaml --s3-bucket yorpg-develop
aws cloudformation deploy --template-file build\packaged.yaml --stack-name yorpg-develop --capabilities CAPABILITY_IAM