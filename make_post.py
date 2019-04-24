import os
from datetime import datetime

def makePost():
	title = "Title: " + input("What is the title of your post? \n"
	        ">>> ")

	date = "Date: " + datetime.today().strftime("%Y-%m-%d")

	category = "Category: "

	tags = "Tags: "

	slug = "Slug: " + title[7:].lower().strip().replace(' ', '-')

	summary = "Summary: " + input("What is the summary?\n"
	       ">>> ")

	author = "Author: Ian H Keith"

	boilerplate = [title, date, category, tags, author, slug, summary]

	post = '/home/iankeith/Documents/Projects/Pelican_Blog/content/{}.md'.format(slug[6:])

	with open(post, 'w', newline='\r\n') as w:
	    for item in boilerplate:
	    	w.write(item + '\n')

	print("Successfully created file: {}".format(post))


makePost()

