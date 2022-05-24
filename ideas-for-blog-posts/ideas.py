#ideas.py
#connects database ideas.db

import sqlite3
import time

connection = sqlite3.connect('/Users/vaibhavblayer/sqlite-projects/ideas-for-blog-posts/ideas.db')
cursor = connection.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS ideas(topic, title, keywords);')
connection.commit()

def info():
	global topic
	topic = input(' Topic : ')
	global title
	title = input(' Title : ')
	global keywords
	keywords = input(' Keywors : ')


def insert(topic, title, keywords):
	cursor.execute('INSERT INTO ideas(topic, title, keywords) VALUES(\"{0}\", \"{1}\", \"{2}\");'.format(topic, title, keywords))
	connection.commit()



if __name__=='__main__':
	info()
	insert(topic, title, keywords)



