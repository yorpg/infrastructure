set code_path=code
pip install  -qq -r requirements.txt -t build/%code_path%/
cp -Rv %code_path%/* build/%code_path%/
