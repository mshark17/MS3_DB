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

def appyForJob(database):
    query='''SELECT * FROM job_posting
        '''
    try:
        executeQuery = database.cursor()
        executeQuery.execute(query)
        # database.commit()
        output = pd.DataFrame(executeQuery.fetchall())
        output.columns = ['ID','CompanyID','Title','Salary','Experience Needed','Education Level','Career Level','Description']
        output['ID'] = output['ID'].astype(str)
        output['ID'] = output['ID'].str.replace(',', '')
        output['CompanyID'] = output['CompanyID'].astype(str)
        output['CompanyID'] = output['CompanyID'].str.replace(',', '')        
        st.subheader('Found '+ str(len(output)) + ' Job Postings')
        st.write(output)
        st.subheader("In Salary, '-1' means Confidential")
        jobID=st.text_input("Enter ID of the Job you want to apply to: Ex. 10011001")
        cv=st.file_uploader("Upload CV or Resume")
        if st.button("Submit"):
            st.subheader("You applied to Job:{}".format(jobID))
        # st.subheader('Query Succesful!')
    except:
        st.subheader('ERROR')

def showResults(database):
    st.subheader("Please Select which of the following results you would like to see")
    selection=st.selectbox('Select',('Show all the job postings for a given sector','Show all the job postings for a given set of skills'
                                     'Show the top 5 sectors by number of job posts, and the average salary range for each','Show the top 5 skills that are in the highest demand'
                                     'Show the top 5 growing startups in Egypt by the amount of vacancies they have compared to their foundation date',
                                     'Show the top 5 most paying companies in the field in Egypt','Show all the postings for a given company / organization'
                                     ,'Show the top 5 categories (other than IT/Software Development) that the postings are cross listed under based on the volume of postings'),index=1)
    if selection=='Show all the job postings for a given sector':
        pass
    elif selection=='Show all the job postings for a given set of skills':
        pass
    elif selection=='Show the top 5 sectors by number of job posts, and the average salary range for each':
        pass
    elif selection=='Show the top 5 skills that are in the highest demand':
        pass
    elif selection=='Show the top 5 growing startups in Egypt by the amount of vacancies they have compared to their foundation date':
        pass
    elif selection=='Show the top 5 most paying companies in the field in Egypt':
        pass
    elif selection=='Show all the postings for a given company / organization':
        pass
    elif selection=='Show the top 5 categories (other than IT/Software Development) that the postings are cross listed under based on the volume of postings':
        pass

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
        appyForJob(database)
    elif navi=="Show Results":
        showResults(database)