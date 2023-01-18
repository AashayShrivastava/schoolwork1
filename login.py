from flask import Flask,request,render_template,redirect,url_for
app=Flask(__name__)
@app.route('/',methods=['POST'])
def hii():
    return 'hii'
@app.route('/login',methods=['POST','GET'])
def log():
    print(request.form)
    if request.method=='GET':
        
        return render_template("LOGIN.html")
        return render_template("index.html")
        
        
@app.route('/login form',methods=['POST'])
def login():
    
    if request.method=='POST':
        User_Name=request.form['USER NAME']
        password=request.form['PASSWORD']
        import mysql.connector
        mycon=mysql.connector.connect(host="localhost",user="root",passwd="cha@#nd321",database="school1")
        if mycon.is_connected():
            print("hii")
        else:
            print("bye")
        cursor=mycon.cursor()
        st="select*from login where username ='{}' and pwd= '{}'".format(User_Name,password)
        cursor.execute(st)
        data=cursor.fetchone()
        print(data)
        if data== None:
            return("You enter a wrong password or username")
        else:
            sk=data[0]
            if sk[0]=='a':
                return render_template("TEACHERS CHOICE .html")
            else:
                return render_template("STUDENT CHOICE.html")
                
                
        

@app.route('/choice for student',methods=['POST'])
def choicestudent():
    
    if request.method=='POST':
        
        choice=request.form['CHOICE']
        
            
        if choice=='1':
            roll=request.form['ROLL']
            import mysql.connector as sqltor
            conn = sqltor.connect(host='localhost', user="root", passwd="cha@#nd321", database="school1")
            if conn.is_connected():
                print("hii")
            else:
                print("bye")
            cursor=conn.cursor()
            st="select*from marks where roll_no ='{}'".format(roll)
            cursor.execute(st)
            
            data=cursor.fetchone()
            print(data)
            return render_template("subjectsmarks.html",roll=data[0],maths=data[1],physics=data[2],chemistry=data[3],english=data[4],cs=data[5])
        if choice=='2':
            roll=request.form['ROLL']
        
            import mysql.connector as sqltor
            conn = sqltor.connect(host='localhost', user="root", passwd="cha@#nd321", database="school1")
            if conn.is_connected():
                print("hii")
            else:
                print("bye")
            cursor = conn.cursor()
            st="Select * from student where rollno=\""+str(roll)+"\""
            cursor.execute(st)
            data = cursor.fetchall()
            print(data)
            cursor = conn.cursor()
            sk="Select * from marks where roll_no=\""+str(roll)+"\""
            cursor.execute(sk)
            
            tata = cursor.fetchall()
    
            print(tata)
            return render_template("marksheet.html",roll=tata[0][0],maths=tata[0][1],physics=tata[0][2],chemistry=tata[0][3],english=tata[0][4],cs=tata[0][5],FIRSTNAME=data[0][0],LASTNAME=data[0][1],FATHERSNAME=data[0][2],rn=data[0][3],clss=data[0][4],db=data[0][5],add=data[0][6])
        if choice=='3':
            roll=request.form['ROLL']
            clss=request.form['CLASS']
            import mysql.connector as sqltor
            conn = sqltor.connect(host='localhost', user="root", passwd="cha@#nd321", database="school1")
            if conn.is_connected():
                print("hii")
            else:
                print("bye")
            cursor = conn.cursor()
            cursor.execute("Select rollno,total,class from  marks ,student where student.rollno=marks.roll_no and class={} order by total desc".format(clss))
            data = cursor.fetchall()
            print(data)
            return render_template("Ranklist.html",rt1=data[0][0],rt2=data[1][0],rt3=data[2][0],rt4=data[3][0],rt5=data[4][0],rtm1=data[0][1],rtm2=data[1][1],rtm3=data[2][1],rtm4=data[3][1],rtm5=data[4][1],rtc1=data[0][2],rtc2=data[1][2],rtc3=data[2][2],rtc4=data[3][2],rtc5=data[4][2])
         
        if choice=='4':
            return render_template("LOGIN.html")
        
@app.route('/choice for teachers',methods=['POST'])
def choiceteacher():
    print(request.form)
    if request.method=='POST':
        
        choice=request.form['CHOICE']
        if choice=='4':
            return render_template("LOGIN.html")
        if choice=='1':
            return render_template("NUMBERTOENTER.html")
        if choice=='2':
            return render_template("studentdetails.html")
        if choice=='3':
            return render_template("delete.html")
        
            
@app.route('/studentdetails',methods=['POST'])
def studentdetails():
    print(request.form)
    if request.method=='POST':
        fname=request.form['FIRSTNAME']
        lname =request.form['LASTNAME']
        fatname=request.form['FATHERSNAME']
        rollnum=request.form['ROLL']
        classes=request.form['CLASS']
        dateofb=request.form['DOB']
        add=request.form['ADDRESS']
            
        import mysql.connector
        mycon=mysql.connector.connect(host="localhost",user="root",passwd="cha@#nd321",database="school1")
        if mycon.is_connected():
            print("hii")
        else:
            print("bye")
        cursor=mycon.cursor()
        a="INSERT INTO student(firstname,lastname,fathername,rollno,class,dob, address)VALUES('{}','{}','{}',{},{},'{}','{}')".format(fname,lname,fatname,rollnum,classes,dateofb,add)
        cursor.execute(a)
        mycon.commit()
        return "YOU ENTERED THE STUDENT DETAILS SUCCESSFULLY"
            
@app.route('/marks',methods=['POST'])
def marks():
    print(request.form)
    if request.method=='POST':
        roll=request.form['ROLL']
        math =request.form['MATHS']
        physic=request.form['PHYSICS']
        chem=request.form['CHEMISTRY']
        eng=request.form['ENGLISH']
        cse=request.form['CS']
            
        import mysql.connector
        mycon=mysql.connector.connect(host="localhost",user="root",passwd="cha@#nd321",database="school1")
        if mycon.is_connected():
            print("hii")
        else:
            print("bye")
        cursor=mycon.cursor()
        a="INSERT INTO marks( roll_no,maths,physics,chemistry,english,cs)VALUES({},{},{},{},{},{})".format(roll,math,physic,chem,eng,cse)
        cursor.execute(a)
        mycon.commit()
        return "YOU ENTERED THE STUDENT MARKS SUCCESSFULLY"
@app.route('/delete',methods=['POST'])
def fel():
    print(request.form)
    if request.method=='POST':
        roll=request.form['ROLL']
        import mysql.connector
        mycon=mysql.connector.connect(host="localhost",user="root",passwd="cha@#nd321",database="school1")
        if mycon.is_connected():
            print("hii")
        else:
            print("bye")
        cursor=mycon.cursor()
        
        cursor.execute("delete from student where rollno="+str(roll))
        cursor.execute("delete from marks where roll_no="+str(roll))
        mycon.commit()
        return "YOU REMOVED THE STUDENT SUCCESSFULLY"
        
if __name__=='__main__':
    app.run()
