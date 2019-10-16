#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: 
# - Enable custom terminology as optional param 
# - Enable custom terminology search via https://docs.aws.amazon.com/translate/latest/dg/API_ListTerminologies.html 
# - Fix output file name syntax 

import boto3 
import sys 
import argparse 

parser = argparse.ArgumentParser('translate.py', description='Send a text file to be translated to a target language.')
parser.add_argument('filepath', type=str, help='a path to a text file.')
parser.add_argument('target_language', type=str, help='the output language, a two letter code (e.g. "fr", "it", "es".')
parser.add_argument('--custom', type=str, help='a tag associated with a csv containing a Custom Vocabulary in your AWS account. See AWS docs for more.')


def parse_args(parser): 
	args = parser.parse_args()	
	filepath = args.filepath
	target_language = args.target_language
	custom_vocab = args.custom 
	return filepath, target_language, custom_vocab


def start_job(filepath, target_language, custom_vocab): 
	with open(filepath, 'r') as f:
		text = f.read() 	

	while len(text) > 4000: 
		print("Text length: " + str(len(text)))
		part = text[:4000] 
		translate = boto3.client(service_name='translate', region_name='us-west-2', use_ssl=True)
		result = translate.translate_text(Text=part, TerminologyNames=[custom_vocab], SourceLanguageCode="en", TargetLanguageCode=target_language) 
		output_text = result.get('TranslatedText')	

		output_path = filepath[:-3] + "_output.txt"

		with open(output_path, "a") as p: 
			p.write(output_text)	

		text = text[4000:]
		return print("Done! file @ " + output_path) 

if __name__ == '__main__': 
	filepath, target_language, custom_vocab = parse_args(parser) 
	start_job(filepath, target_language, custom_vocab)