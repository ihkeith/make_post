#!/usr/bin/env python3

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


def clear_screen():
	os.system("cls" if os.name == "nt" else "clear")


def menu():
	welcome = "Markdown Post Creator Command Line Tool"
	print("*" * len(welcome))
	print(welcome)
	print("*" * len(welcome))
	input("\n\nPress enter to continue.")


def main():
	clear_screen()
	menu()
	print("\n\n")
	post = Post()
	post.make_post()
	while True:
		another_post = input("Would you like to create another post? Y/n  ")
		if another_post.lower()  == 'y':
			clear_screen()
			menu()
			print("\n\n")
			post = Post()
			post.make_post()
			continue
		elif another_post.lower() == 'n':
			print("Thank you. Have a great day {}".format(post.author))
			break
		else:
			print("That is not a valid option. Please try again.")
			continue
		

if __name__ == "__main__":
	main()
