import streamlit as st
import pandas as pd
import hashlib
from streamlit_option_menu import option_menu
import streamlit_authenticator as stauth
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()
def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management
import sqlite3 
conn = sqlite3.connect("data.db", check_same_thread=False)
c = conn.cursor()

# DB  Functions


def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(name TEXT,username TEXT,semester TEXT,mobile_no TEXT,password TEXT)')
# def match():
# 	c.execute('WHERE EXISTS (SELECT username FROM userstable WHERE  username==)')
def add_userdata(name,username,semester,mobile_no,password):
	c.execute('INSERT INTO userstable(name,username,semester,mobile_no,password) VALUES (?,?,?,?,?)',(name,username,semester,mobile_no,password))
	conn.commit()
def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data
def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data
def view_all_user_names():
	c.execute('SELECT username FROM userstable')
	data = c.fetchall()
	return data
def view_all_pass():
	c.execute('SELECT password FROM userstable')
	data = c.fetchall()
	return data
def view_all_name():
	c.execute('SELECT name FROM userstable')
	data = c.fetchall()
	return data
def main(selected):
	if ('password_ad' not in st.session_state):
		st.session_state['password_ad'] = 0
	"""Simple Login App"""
	if selected == "Log in/Log out":
		if st.session_state['ans'] != 1:
			st.subheader("Login Section")
			
			username = st.text_input("User Name")
			password = st.text_input("Password",type='password')
			

			if st.button("Login"):
				create_usertable()
				hashed_pswd = make_hashes(password)

				result = login_user(username,check_hashes(password,hashed_pswd))
				if result:
					

					st.session_state['ans'] = 1

					st.success("Logged In as {}".format(username))
					st.session_state['loggedin_name'] = username

				else:
					st.warning("Incorrect Username/Password Or You are not sign up yet, if yes then do that first")
		
		else:
			st.subheader("Logout Section")
			if st.button("Logout"):
				st.session_state['ans'] = 0
				st.info("You are sucessfully logged out")
			

	if selected =="Sign Up":
		if st.session_state['ans'] ==1:
			st.info("You are sucessfully logged in")
		else:
			st.subheader("Create New Account")
			name = st.text_input("Name")
			new_user = st.text_input("Username")
			semester =st.selectbox("Choose Semester",['I','II' ,'III','IV' ,'V' ,'VI' ])
			mobile_no = st.text_input("Enter Mobile No. ",value="91",max_chars=12)
			new_password = st.text_input("Password",type='password')
			new_password2 = st.text_input("Confirm Password",type='password')
			if st.checkbox("Club Admin"):
				st.session_state['password_ad'] = st.text_input("Admin Password",type='password')
			if st.button("Signup"):
				usernames = []
				for user in view_all_user_names():
					usernames.append(user[0])
				if new_user in usernames:
					st.error("Occupied Username,Try with another Username")
				elif new_password != new_password2:
					st.error("Password Not Match")
				elif 4>len(new_password):
					st.error("Weak Password,Try with strong password")
				elif name == None or mobile_no ==None or name == '' or mobile_no =='':
					st.error('Please fill the information')
				
				elif not mobile_no.isdigit() or " " == mobile_no:
					st.error('Invalid mobile number') 
				else:
					create_usertable()
					add_userdata(name,new_user,semester,mobile_no,make_hashes(new_password))
					st.success(
	"""
	You have successfully created a valid Account
	Do Login
	""")


def page_authenticator():
	usernames = []
	passwords =[]
	for user in view_all_user_names():
		usernames.append(user[0])
	print(usernames)
	for ps in view_all_pass():
		passwords.append(ps[0])
	print(passwords)
	names =[]
	for name in view_all_user_names():
		names.append(name[0])

	# usernames = [for user in usernames]
	# names = [user["name"] for user in users]
	# hashed_passwords = [passwords for user in passwords]
	authenticator = stauth.Authenticate(names,usernames,passwords,
		"stdapp", "nilesh", cookie_expiry_days=30)

	name, authentication_status,usernames = authenticator.login("Login", "main")

	if authentication_status == False:
		st.error("You are not Sign up yet")

	if authentication_status == None:
		st.warning("Please enter your username and password")
	if authentication_status == True:
		st.session_state['ans'] = 1
		if ('username_login' not in st.session_state):
			st.session_state['username_login'] = name
		st.success("Logged In as {}".format( name))
	