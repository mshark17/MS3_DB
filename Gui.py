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

def register_user(mydb):
    
    name=st.text_input("Enter Name: John Doe")
    email = st.text_input("Enter Email:")
    username = st.text_input("Enter User Name:")
    dateofbirth = st.text_input("Enter Date of Birth: YYYY-MM-DD")
    gender = st.text_input("Enter Gender: M or F")
    gpa = st.text_input("Enter GPA:")
    temp = st.text_input("Enter list of skills (seperate by comma and space): Skill1, Skill2")
    listofskills = temp.split(", ")
    
    try:
        if st.button("Submit"):
            
            # query= """
            #     INSERT INTO user VALUES (\'"""+email+"""\', \'"""+username+"""\', \'"""+gender+ """\', \'"""+dateofbirth+"""\',\'"""+gpa+"""\', \'"""+name+"""\')
            #     """
            
            # try:
            #     mycursor = mydb.cursor()
            #     mycursor.execute(query)
            #     mydb.commit()
            #     st.subheader('user Added Succesfully!')
            # except:
            #     st.subheader('ERROR')

            query= """
                INSERT INTO user_list_of_skills VALUES (\'"""+listofskills+"""\',\'"""+username+"""\')
                """
            try:
                mycursor = mydb.cursor()
                mycursor.execute(query)
                mydb.commit()
                st.subheader('user_list_of_skills Added Succesfully!')
            except:
                st.subheader('ERROR')
    except:
        st.subheader('ERROR')
    return 

if __name__=="__main__":
    register_user(connect_to_database())