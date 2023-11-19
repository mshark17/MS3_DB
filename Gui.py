import streamlit as st
import mysql.connector
import pandas as pd

def connect_to_database():  
    mydb = mysql.connector.connect(
    host = "db4free.net",
    user = "mshark",
    password = "Mostafa23#",
    database = "wuzzuf900184043",
    )
    return mydb

def register_user(database):
    name=st.text_input("Enter Name: John Doe")
    email = st.text_input("Enter Email:")
    username = st.text_input("Enter User Name:")
    dateofbirth = st.text_input("Enter Date of Birth: YYYY-MM-DD")
    gender = st.text_input("Enter Gender: M or F")
    gpa = st.text_input("Enter GPA:")
    listofskills = st.text_input("Enter list of skills (seperate by comma and space): Skill1, Skill2")
    try:
        if st.button("Submit"):
            query= """
                INSERT INTO user VALUES (\'"""+email+"""\', \'"""+username+"""\', \'"""+gender+ """\', \'"""+dateofbirth+"""\',\'"""+gpa+"""\', \'"""+name+"""\')
                """
            try:
                executeQuery = database.cursor()
                executeQuery.execute(query)
                database.commit()
                st.subheader('user Added Succesfully!')
            except:
                st.subheader('ERROR')

            query= """
                INSERT INTO user_list_of_skills (List_Of_Skills,User_Name) VALUES (\'"""+listofskills+"""\',\'"""+username+"""\')
                """
            try:
                executeQuery = database.cursor()
                executeQuery.execute(query)
                database.commit()
                st.subheader('user_list_of_skills Added Succesfully!')
            except:
                st.subheader('ERROR')
    except:
        st.subheader('ERROR')
    return 

def appyForJob():
    query='''SELECT * FROM job_posting
        '''
    try:
        executeQuery = database.cursor()
        executeQuery.execute(query)
        # database.commit()
        output = pd.DataFrame(executeQuery.fetchall())
        st.subheader('Found '+ str(len(output)) + ' Job Postings')
        st.write(output[:5])
        # st.subheader('Query Succesful!')
    except:
        st.subheader('ERROR')

if __name__=="__main__":
    database=connect_to_database()
    st.write ('''
    # Milestone 3 Database Project
    ''')
    st.sidebar.header("Navigation")
    navi=st.sidebar.selectbox('Choose',  ('Register a user', 'Apply for Job', 'Show Results'), index=1)
    if navi=="Register a user":
        register_user(database)
    elif navi=="Apply for Job":
        pass
    elif navi=="Show Results":
        pass