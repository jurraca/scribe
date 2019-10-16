import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd 
import base64
import io
import re 

app = dash.Dash()

app.layout = html.Div([
	dcc.Upload( 
		id='upload-data', 
		children=html.Div([
		   'Drag and Drop or ',
			html.A('Select Files')
		]),
		style={
			'width': '100%',
			'height': '60px',
			'lineHeight': '60px',
			'borderWidth': '1px',
			'borderStyle': 'dashed',
			'borderRadius': '5px',
			'textAlign': 'center',
			'margin': '10px'
		},
		),
	html.Div(id='output-data-upload'),
	])

def parse_contents(contents, filename): 
	content_type, content_string = contents.split(',')

	ftype = get_filetype(filename)

	try: 
		if ftype == 'text':
			decoded = base64.b64decode(content_string)
			txt = decoded.decode('utf-8')

			# Translate text ? 
	
		if ftype == 'audio': 
			return "todo"
		# "Transcribe Audio file? " 

	except Exception as e:
		print(e)
		return html.Div([
			'There was an error processing this file.'
		])

	return txt

def get_filetype(filename): 

	# extract extension and return file type. 
	r = '^.+\.(\S+)' 
	pattern = re.compile(r) 
	ext = pattern.match(filename).group(1)

	if ext in ['txt']:
		return "text"
	if ext in ['wav', 'aif', 'aac', 'mp3']:
		return "audio"


@app.callback(Output('output-data-upload', 'children'),
			  [Input('upload-data', 'contents')], 
			  [State('upload-data', 'filename')]) 


def update_output(contents, filename): 
	if contents is not None: 
		children = [parse_contents(contents, filename)]
		return children 

if __name__ == '__main__': 
	app.run_server(debug=True)
