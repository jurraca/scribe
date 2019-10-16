#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import time
import boto3
import sys 
import requests 
import json 
import argparse 

def parse_args(): 
	args = parser.parse_args()	
	s3_bucket = args.s3_bucket
	job_name = args.job_name
	audio_format = args.audio_format
	return s3_bucket, job_name, audio_format

def scribe(transcribe): 
	transcribe.start_transcription_job(
	    TranscriptionJobName=job_name,
	    Media={'MediaFileUri': s3_bucket},
	    MediaFormat=audio_format,
	    LanguageCode='en-US'
	)	

	while True:
	    status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
	    if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
	        break
	    print("Working...")
	    time.sleep(10)
	status  	
	return parse_response(status)

def parse_response(status): 
	url = status['TranscriptionJob']['Transcript']['TranscriptFileUri']	
	r = requests.get(url)	
	transcript = json.loads(r.text)['results']['transcripts'][0]
	return transcript  

if __name__ == '__main__':

	parser = argparse.ArgumentParser(prog='transcribe.py', description='Transcribe an audio file using AWS.')
	parser.add_argument('s3_bucket', type=str, help='a path to an audio file in an s3 bucket.')
	parser.add_argument('job_name', type=str, help='a unique name for the transcription job.')
	parser.add_argument('audio_format', type=str, help='the audio format for the file (mp3, wav, aif...)')

	s3_bucket, job_name, audio_format = parse_args()
	transcribe = boto3.client('transcribe') 
	scribe(transcribe)