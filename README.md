## README 

Set of scripts to work AWS [Transcribe](https://docs.aws.amazon.com/transcribe/latest/dg/what-is-transcribe.html) and [Translate](https://aws.amazon.com/translate/). Nothing elaborate, just extending the basic examples from the docs. 

The goal is to provide a pipeline from audio to (global) text-based content from conferences, meetups, presentations, making it easier for organizers to intake and distribute their content worldwide. The goal is NOT to have a perfect transcript or translation, but to get 90% of the way there, for a human to clean up the mistakes, add formatting, and/or punctuation. I believe it's much better to provide a transcript that can be readily fixed by a native speaker than not provide one at all. 

The principal hurdle for transcriptions & translations is the field-specific and technical terminology. For this, one can build [Custom Vocabularies](https://docs.aws.amazon.com/transcribe/latest/dg/how-vocabulary.html) to tell Transcribe how to handle those terms, and Translate how to translate them. 

Transcribing from audio can be very slow, depending on the length of the audio clip and the bit rate. Use `ffmpeg` or a similar tool to resize the file and make it as small as possible. 

(The Transcribe module also offers a way transcribe from an audio stream which I didn't explore here.)  

Transcribe.py usage: 
    *s3_bucket: the s3 bucket address for the audio to transcribe 
    *job_name: a unique name for the transcription job  
    *audio_format: 'wav', 'mp3', etc

python3 transcribe.py <s3_bucket> <job_name> <audio_format> 

Translate.py usage: 
    *text filepath 
    *target language code: two-character code for the language you're translating into. 

Optionally, you can specify the name (not filepath) of a Custom Terminology csv file hosted in your AWS account. 

Usage: 
python3 translate.py <txt_file_path> <target_language> --custom <custom_vocab>

