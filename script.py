#!/usr/bin/env python
# -*- coding: utf-8 -*-

# read text file
# break up text file in 5K bytes increments (leaving sentences intact) 
# load custom terminology 
# call translate 
# get result 
# write result 

import boto3 
import sys 

filepath = sys.argv[1]
target_language = sys.argv[2]

with open(filepath, 'r') as f:
	text = f.read() 

while len(text) > 4000: 
	print("Text length: " + str(len(text)))
	part = text[:4000] 
	translate = boto3.client(service_name='translate', region_name='us-west-2', use_ssl=True)
	result = translate.translate_text(Text=part, TerminologyNames=['lightning'], SourceLanguageCode="en", TargetLanguageCode=target_language) 
	output_text = result.get('TranslatedText')

	with open(filepath + "_output.txt", "a") as p: 
		p.write(output_text)

	text = text[4000:]
