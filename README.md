## Background

One of the main points of this blog is to serve as an aid to learning Python and to log what I've been doing. I created this script as a way to jumpstart my posts.

## The Code

I threw this one together in between cooking and chasing a screaming toddler around the house. It ain't pretty, but it gets the job done. I put it in a function, but it really doesn't need to be at this point. It will help when I get around to refactor it.

The code is straight forward. Variables hold on the various strings that will make up metadata with a couple of inputs from the user rounding it out.  The user provides the title, which is then used to generate the slug and the file name. A datetime creates the date.  All of this gets put in a list and a for loop writes it to the .md file.

```Python
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

	post = '/home/ian/Documents/Projects/Pelican_Blog/content/{}.md'.format(slug[6:])

	with open(post, 'w', newline='\r\n') as w:
	    for item in boilerplate:
	        w.write(item + '\n')

makePost()
```

## Running the code
	:::bash
	$ python makePost.py
	What is the title of your post?
	>>> Test Post
	What is the summary?
	>>> This is a Test Post
	$ 

## The Output

```markdown
Title: Test Post
Date: 2017-12-17
Category: 
Tags: 
Author: Ian H Keith
Slug: test-post
Summary: This is a Test Post
```

And here is my post stub. I can then go and fill out the rest: Category, Tags, and the post itself.

## Improvements for the Future

* I'm sure a lot of this can be simplified and cut down to reduce verbosity.
* Refactor to take a commandline argument for the Title and optionally for the Summary
* Objects. Objects. Objects
