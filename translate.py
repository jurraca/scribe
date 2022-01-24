#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: 
# - Enable custom terminology as optional param 
# - Enable custom terminology search via https://docs.aws.amazon.com/translate/latest/dg/API_ListTerminologies.html 

import boto3 
import sys 
import argparse 

parser = argparse.ArgumentParser('translate.py', description='Send a text file to be translated to a target language.')
parser.add_argument('filepath', type=str, help='a path to a text file.')
parser.add_argument('base_language', type=str, help='the input language, a two letter code (e.g. "fr", "it", "es".')
parser.add_argument('target_language', type=str, help='the output language, a two letter code (e.g. "fr", "it", "es".')
parser.add_argument('-o', '--output', nargs='?', type=str, help='the output path to write the translated file under.')
parser.add_argument('--custom', type=str, help='a tag associated with a csv containing a Custom Vocabulary in your AWS account. See AWS docs for more.')

def parse_args(parser):
	args = parser.parse_args()
	filepath = args.filepath
	base_language = args.base_language
	target_language = args.target_language
	custom_vocab = args.custom
	outpath=args.output
	return filepath, base_language, target_language, custom_vocab, outpath

def start_job(filepath, base_language, target_language, custom_vocab, outpath):
	with open(filepath, 'r') as f:
		text = f.read()

	translate = boto3.client(service_name='translate', region_name='us-west-2', use_ssl=True)

	parts = split_text(text)
	for p in parts:
		print("Text length: " + str(len(p)))
		result = translate.translate_text(Text=p, SourceLanguageCode=base_language, TargetLanguageCode=target_language, TerminologyNames=[ "bitcoin_terminology" ])
		output_text = result.get('TranslatedText')
		if outpath is None:
			output_path = "{}-{}.txt".format(filepath, target_language)
			print(output_path)
		else:
			output_path = "{}-{}.txt".format(outpath, target_language)

		with open(output_path, "a") as out: 
			out.write(output_text)	

	return print("Done! output file located @ " + output_path)

# AWS only accepts ~ 4000 words at a time, so we split it up and return an array of text blobs. 
def split_text(text): 
	parts = []
	while len(text) > 4000:
		parts.append(text[:4000])
		text = text[4000:] 
	else:
		parts.append(text)
	return parts

if __name__ == '__main__':
	filepath, base_language, target_language, custom_vocab, outpath = parse_args(parser)
	start_job(filepath, base_language, target_language, custom_vocab, outpath)
