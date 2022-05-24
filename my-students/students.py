#students.py
#connects database students.db

import sqlite3
import pdb

connection = sqlite3.connect('/Users/vaibhavblayer/sqlite-projects/my-students/students.db')
cursor = connection.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS students(name, birthday, phone, email, address);')
connection.commit()

def info():
	global name
	name = input(' Name : Vaibhav Blayer : ') or "Vaibhav Blayer"
	global birthday
	birthday = input(' Birthday : 18 October : ') or "18 October"
	global phone
	phone = input(' Phone : 7765974537 : ') or "7765974537"
	global email
	email = input(' Email : vaibhavblayer@gmail.com : ') or "vaibhavblayer@gmail.com"
	global address
	address = input(' Address : Bihar Sharif : ') or "Bihar Sharif"


def insert(name, birthday, phone, email, address):
	cursor.execute('INSERT INTO students(name, birthday, phone, email, address) VALUES(\"{0}\", \"{1}\", \"{2}\", \"{3}\", \"{4}\");'.format(name, birthday, phone, email, address))
	connection.commit()



if __name__=='__main__':
	info()
	insert(name, birthday, phone, email, address)



