import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Harish@2001",
  database="day9"
)

from flask import Flask,render_template,request,flash,jsonify
app=Flask('__name__')
app.secret_key='123'
@app.route('/')
def login_page():
    return render_template('login_page.html')
@app.route('/success',methods=['GET','POST'])
def success_page():
    return render_template('login_success.html')
@app.route('/api',methods=['GET','POST'])
def login_page1():
    data={}  
    lis=[]   

    try:
        user_name=''
        password=''
        redirect_url='/'
        check=''
         
        if request.method=='POST':
            user_name=request.form["USERNAME"]
            password=request.form["PASSWORD"]
            data={user_name:password}
            print(data)
            print(user_name,password)
            mycursor=mydb.cursor(buffered=True)
            qurey="SELECT user, password FROM day15.persons WHERE user=%s and password=%s"
            mycursor.execute(qurey,((user_name,password,)))
            cursor=mycursor.fetchall()
            mydb.commit()
            if len(cursor)>0:
                print('THIS IS MY',cursor)
                for tup in cursor:
                    for i in tup :
                        lis.append(i)
                        print(lis)
                    if user_name==lis[0] and password==lis[1]:
                        print("success")
                        redirect_url='/success'
                        check='success'
                        return jsonify({'redirectUrl':redirect_url,'check':check})
            else:
                print("hi")
                check='INVALID CREDENTIALS'
                return jsonify({'redirectUrl':redirect_url,'check':check})     
    except Exception as e:
        print('Exception My Error:', str(e)) 
        return data
    
@app.route('/alert',methods=['GET','POST'])
def login_page2():
    return render_template('alert_page.html')    
    
@app.route('/user',methods=['GET','POST'])
def alert_page():
    data={}   

    try:
        name=''
        user_name=''
        email=''
        password=''
        check_pass=''
         
        if request.method=='POST':
            name=request.form['NAME']
            username=request.form['USERNAME']
            email=request.form['EMAIL']
            password=request.form['PASSWORD']
            check_pass=request.form['CHECK_PASSWORD']
            print(name,user_name,email,password,check_pass)
            mycursor=mydb.cursor(buffered=True)
            if password==check_pass:
             qurey="INSERT INTO day15.persons(name,user,email,password) VALUES (%s,%s,%s,%s);"
             mycursor.execute(qurey,((name,username,email,password)))
             mydb.commit()
             return ('/')   
    except Exception as e:
        print('Exception My Error:', str(e)) 
        return data

           
    
if __name__ == '__main__':
    app.run(debug=True)

app.run()    