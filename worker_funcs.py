#! /usr/bin/python3
from flask import Flask, render_template

app = Flask(__name__)
host = '0.0.0.0'
port = '5000'

def at(args):
	location, html = args[0], args[1]
	dynamic_view = lambda template: (lambda: render_template(template))
	app.add_url_rule(location, view_func=dynamic_view(html), endpoint=location)
	print(f"Created page at {location} with HTML {html}")
	
def run(args):
	if args:
		print("Usage: run")
	app.run(debug=True)
