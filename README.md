## README 

"_Traduttore, traditore_" - Italian saying

Set of scripts to work with AWS [Translate](https://aws.amazon.com/translate/) and [Transcribe](https://docs.aws.amazon.com/transcribe/latest/dg/what-is-transcribe.html). Some s3 wrappers are provided to work with batch file uploads and downloads.

Machine-learning-generated translation has gotten quite good, especially in the last several years (as of 2022). In the realm of technical translation, we have the explicit goal to disseminate knowledge without losing technical correctness. Assuming the basic translation is satisfactory, the main problem is that the default model will fail to accurately translate highly specific technical terminology (for example, in cryptocurrency parlance: "fork", "cold storage", "uncle blocks"). AWS has a feature which solves for this, [Custom Vocabularies](https://docs.aws.amazon.com/transcribe/latest/dg/how-vocabulary.html), effectively a CSV mapping of source language to target language referenced via S3.

More generally, I believe the workflow of (non-literary) translation should maximize automation on the front end, and leverage a community of native speakers to review the translation. The goal is NOT to generate a perfect transcript or translation via AWS, but to get 97% of the way there, for a human to clean up the mistakes, add formatting, and/or punctuation, and be the final arbiter of whether the translation is good enough for public release. This cuts the time necessary to produce a translation from days to hours or minutes without sacrificing quality. This approach was developed while considering how to translate [Chaincode Labs'](chaincode.com) [seminar material](https://chaincode.gitbook.io/seminars/) as well as the [btctranscripts](https://btctranscripts.com/) repository--a true gold mine which deserves to be translated and disseminated.

#### Translate.py usage:

To start a basic translation of a local txt file, you'll need:
- the local text filepath
- source and target language code: two-character code for the language you're translating from and into (eg: "en" "es"). 

Optionally, you can specify the S3 name (not filepath) of a Custom Terminology csv file hosted in your AWS account. 

Usage: 
`python3 translate.py <txt_file_path> <source_language> <target_language> --custom <custom_vocab>`

