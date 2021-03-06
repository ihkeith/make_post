# A Markdown Blog Post Creator in Python

## Overview

The Markdown Post creator is a command line program written in Python. It will prompt you to input your post Title, Summary, Categor, and Tags. It will then format a markdown template for Pelican blogs with metadata, slug, current date, and author. It will create a `.md` file in your content directory.

## Usage

Clone the repo to your main Pelican folder or create a make_post.py file and copy the code. Move the _make_post.py_ file to the root of your Pelican folder or update the file variable to reflect the path to your content folder. Run the code by typing `python3 make_post.py` wherever the file is located. See example below.

```bash
$ python3 make_post.py
```

```python
***************************************
Markdown Post Creator Command Line Tool
***************************************


Press enter to continue.



What is the title of your post? 
>>>  Test Post
What is the summary?
>>>  This is a Test Post
What Category/s would you like to use? (Separate with a comma)
>>>  Python, Markdown
What Tag/s would you like to use? (Separate with a comma)
>>>  Programming, Pelican, Markdown, Python
Successfully created file Test Post
Would you like to create another post? Y/n  
```

## The Output

```markdown
Title: Test Post
Date: 2019-05-03
Category: Python, Blogging
Tags: Programming, Python
Author: Ian H Keith
Slug: test-post
Summary: This is a Test Post
```

