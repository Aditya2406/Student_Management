from flask import Flask, render_template, request

app = Flask(__name__)
std_l = []
teacher = []
maths_teacher=""
phy_teacher=""
chem_teacher=""


class student:
    def __init__(self, Name, rollno, subject_1, subject_2, subject_3):
        self.Name= Name
        self.rollno= rollno
        self.subject_1= subject_1
        self.subject_2= subject_2
        self.subject_3= subject_3
k=[]

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        rn = request.form['rn']
        sub_1 = request.form['sub_1']
        sub_2 = request.form['sub_2']
        sub_3 = request.form['sub_3']
        std_l.append(name)
        k.append(student(name,rn,sub_1,sub_2,sub_3))

        return "NEW STUDENT ADDED"
    else:
        return render_template('students_all.html', std=std_l)

@app.route("/teachers" , methods=['POST', 'GET'])
def teachers():
    if request.method == 'POST':
        sub=request.form['sub']
        if(sub=='maths'):
            tname = request.form['tname']
            global maths_teacher
            maths_teacher = tname
            teacher.append(tname)
        elif (sub == 'physics'):
            tname = request.form['tname']
            global phy_teacher
            phy_teacher = tname
            teacher.append(tname)
        elif (sub =='chemsitry'):
            tname = request.form['tname']
            global chem_teacher
            chem_teacher = tname
            teacher.append(tname)
            return "NEW TEACHER ADDED"
    else:
        return render_template("teachers.html", te=teacher)

    return"new teacher added"

def finder(x):
    for i in range(len(k)):
        if k[i].rollno == x:
             return (i+1)


@app.route("/student_det" , methods=['POST', 'GET' ])
def ENTER_DETAILS():
    for i in range(len(k)):
     if request.method=='POST':
        srn = (request.form['srn'])
        status=finder(srn)
        if status:
            index=status-1
            return render_template("studentid.html", index=index, name=k[index].Name, rollno=k[index].rollno,
                                       sub1=k[index].subject_1, sub2=k[index].subject_2,
                                       sub3=k[index].subject_3,
                                       MT=maths_teacher, PT=phy_teacher, CT=chem_teacher)
        else:
            return"you did't register yourself"

    else:
         return render_template("enterdetails.html")


if __name__=="__main__":
    app.run(host="127.0.0.1",port=8000,debug=True)
