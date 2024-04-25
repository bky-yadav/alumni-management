from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
import sqlite3

conn=sqlite3.connect('dbsproject.db')
cursor=conn.cursor()

app = Flask(__name__)
cursor.execute('''CREATE TABLE IF NOT EXISTS ALUMNI(
               ID INTEGER PRIMARY KEY,
               FULL_NAME TEXT NOT NULL,
               GENDER TEXT NOT NULL,
               PHONE_NUMBER INTEGER NOT NULL,
               EMAIL TEXT NOT NULL,
               LINKEDIN_URL TEXT NOT NULL,
               WORK_ADD TEXT NOT NULL,
               POSITION TEXT NOT NULL,
               OFFER_INTERNSHIP TEXT NOT NULL,
               INTERNSHIP_TYPE TEXT NOT NULL
)'''
)
conn.commit()
cursor.execute('''CREATE TABLE IF NOT EXISTS STUDENT(
               ID INTEGER PRIMARY KEY,
               FULL_NAME TEXT NOT NULL,
               GENDER TEXT NOT NULL,
               PHONE_NUMBER INTEGER NOT NULL,
               EMAIL TEXT NOT NULL,
               LINKEDIN_URL TEXT NOT NULL,
               BRANCH TEXT NOT NULL,
               MAIN_SKILL TEXT NOT NULL,
               AGE INTEGER NOT NULL,
               CGPA INTEGER NOT NULL
)'''
)
conn.commit()
cursor.execute('''CREATE TABLE IF NOT EXISTS ALUMNI1(
               FULL_NAME TEXT NOT NULL,
               PHONE_NUMBER INTEGER NOT NULL,
               EMAIL TEXT NOT NULL,
               LINKEDIN_URL TEXT NOT NULL,
               WORK_ADD TEXT NOT NULL
)'''
)
conn.commit()
cursor.execute('''CREATE TABLE IF NOT EXISTS STUDENT1(
               FULL_NAME TEXT NOT NULL,
               PHONE_NUMBER INTEGER NOT NULL,
               EMAIL TEXT NOT NULL,
               LINKEDIN_URL TEXT NOT NULL,
               MAIN_SKILL TEXT NOT NULL
)'''
)




@app.route("/",)
def hello_world():
    
    return render_template('index.html')


@app.route('/alumnipage',methods=['GET','POST'])
def alumnipage():
    conn=sqlite3.connect('dbsproject.db')
    cursor=conn.cursor()
    if request.method=='POST':
        name=request.form['field2']
        gender=request.form['field3']
        phone_no=request.form['field4']
        email=request.form['field5']
        linkedin=request.form['field6']
        work_add=request.form['field7']
        position=request.form['field8']
        offer=request.form['INTERN']
        type=request.form['TYPE']
        sql='''INSERT INTO ALUMNI(FULL_NAME,GENDER,PHONE_NUMBER,EMAIL,LINKEDIN_URL,WORK_ADD,POSITION,OFFER_INTERNSHIP,INTERNSHIP_TYPE) VALUES(?,?,?,?,?,?,?,?,?)'''
        data=(name,gender,phone_no,email,linkedin,work_add,position,offer,type)
        cursor.execute(sql,data)
        conn.commit()
    return render_template('alumnipage.html')

@app.route('/studentpage',methods=['GET','POST'])
def studentpage():
    conn=sqlite3.connect('dbsproject.db')
    cursor=conn.cursor()
    if request.method=='POST':
        name=request.form['field2']
        gender=request.form['GENDER']
        phone_no=request.form['field4']
        email=request.form['field5']
        linkedin=request.form['field9']
        branch=request.form['field7']
        main_skill=request.form['field8']
        age=request.form['field6']
        cgpa=request.form['field10']
        sql='''INSERT INTO STUDENT(FULL_NAME,GENDER,PHONE_NUMBER,EMAIL,LINKEDIN_URL,BRANCH,MAIN_SKILL,AGE,CGPA) VALUES(?,?,?,?,?,?,?,?,?)'''
        data=(name,gender,phone_no,email,linkedin,branch,main_skill,age,cgpa)
        cursor.execute(sql,data)
        conn.commit()
    return render_template('studentpage.html')

@app.route("/redirect1",methods=['GET','POST'])
def redirect1():
    conn=sqlite3.connect('dbsproject.db')
    cursor=conn.cursor()
    if request.method=='POST':
        city=request.form['CITY']
        type=request.form['TYPE']
        cursor.execute('''SELECT FULL_NAME,PHONE_NUMBER,EMAIL,LINKEDIN_URL,WORK_ADD FROM ALUMNI WHERE WORK_ADD LIKE ? AND INTERNSHIP_TYPE = ?''',(city,type))
        results=cursor.fetchall()
        for i in results:
            sql='''INSERT INTO ALUMNI1(FULL_NAME,PHONE_NUMBER,EMAIL,LINKEDIN_URL,WORK_ADD) VALUES(?,?,?,?,?)'''
            data=(i[0],i[1],i[2],i[3],i[4])
            cursor.execute(sql,data)
            conn.commit()
        return redirect('/fromredirect')

    return render_template('redirect.html')

@app.route("/fromredirect")
def fromredirect():
    conn=sqlite3.connect('dbsproject.db')
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM ALUMNI1")
    result=cursor.fetchall()
    cursor.execute("DELETE FROM ALUMNI1")
    conn.commit()
    return render_template('fromredirect.html',result=result)

@app.route("/redirect2",methods=['POST','GET'])
def redirect2():
    conn=sqlite3.connect('dbsproject.db')
    cursor=conn.cursor()
    if request.method=='POST':
        branch=request.form['BRANCH']
        main_skill=request.form['field4']
        cursor.execute('''SELECT FULL_NAME,PHONE_NUMBER,EMAIL,LINKEDIN_URL,MAIN_SKILL FROM STUDENT WHERE BRANCH LIKE ? AND MAIN_SKILL = ?''',(branch,main_skill))
        results=cursor.fetchall()
        print(results)
        for i in results:
            sql='''INSERT INTO STUDENT1(FULL_NAME,PHONE_NUMBER,EMAIL,LINKEDIN_URL,MAIN_SKILL) VALUES(?,?,?,?,?)'''
            data=(i[0],i[1],i[2],i[3],i[4])
            cursor.execute(sql,data)
            conn.commit()
        return redirect('/fromredirect2')
    return render_template('redirect2.html')


@app.route("/fromredirect2")
def fromredirect2():
    conn=sqlite3.connect('dbsproject.db')
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM STUDENT1")
    result=cursor.fetchall()
    cursor.execute("DELETE FROM STUDENT1")
    conn.commit()
    return render_template('fromredirect2.html',result=result)


conn.close()
if __name__=="__main__":
    app.run(debug=True)