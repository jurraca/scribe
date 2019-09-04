## README 

A script that sends text to AWS Translate and returns the translated text. Handles arbritrary text lengths. 

#### Required fields

  * text filepath 
  * target language code: two-character code for the language you're translating into. 

Optionally, you can specify the name (not filepath) of a Custom Terminology csv file hosted in your AWS account. 

#### Usage

python3 script.py <txt_file_path> <target_language>
