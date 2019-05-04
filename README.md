# A Markdown Blog Post Creator in Python

## Overview

The Markdown Post creator is a command line program written in Python. It will prompt you to input your post Title, Summary, Categor, and Tags. It will then format a markdown template for Pelican blogs with metadata, slug, current date, and author. It will create a `.md` file in your content directory.

## Usage

Clone the repo to your main Pelican folder or create a make_post.py file and copy the code. Run the code by typing `python3 make_post.py`. See example below.

```bash
$ python3 make_post.py
What is the title of your post?
>>> Test Post
What is the summary?
>>> This is a Test Post
What Catagory/s would you like to use?
>>> Python, Blogging
What Tag/s would you like to use?
>>> Programming, Python
Successfully created file Test Post
$
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

