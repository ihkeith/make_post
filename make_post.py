import os
from datetime import datetime

class Post:
	def __init__(self):
		self.title = input("What is the title of your post? \n>>>  ")
		self.date = datetime.today().strftime("%Y-%m-%d")
		self.summary = input("What is the summary?\n>>>  ")
		self.category = input("What Category/s would you like to use? (Separate with a comma)\n>>>  ")
		self.tags = input("What Tag/s would you like to use? (Separate with a comma)\n>>>  ")
		self.author = 'Ian H Keith'
		self.slug = "-".join(self.title.split()).lower()

	def make_post(self):
		self.file = './content/{}.md'.format(self.slug)
		self.post_info = [self.title, self.date, self.summary, self.category, self.tags, self.author, self.slug]
		self.meta_data = ["Title", "Date", "Summary", "Category", "Tags", "Author", "Slug"]
		self.boilerplate = dict(zip(self.meta_data, self.post_info))
		with open(self.file, 'w', newline='\r\n') as w:
			for key, value in self.boilerplate.items():
				w.write("{}: {}\n".format(key, value))
		print("Successfully created file: {}".format(self.title))


def main():
		post = Post()
		post.make_post()

if __name__ == "__main__":
	main()
