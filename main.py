from  flask import Flask,render_template,url_for,request,redirect
from datetime import  datetime

from flask_sqlalchemy import SQLAlchemy
from BD_core import DB
import html

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
db=SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content=db.Column(db.String(200), nullable=False)
    #completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)


    def __repr__(self):
        return '<Task %r>' %self.id


@app.route('/',methods=['POST','GET'])
def index():
    if request.method== 'POST':
        task_content= request.form['content']
        new_task= Todo(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was a issue adding your task'

    else:
        tasks=Todo.query.order_by(Todo.date_created).all()
        return render_template("index.html",tasks=tasks)







@app.route('/search1',methods = ['POST'])
def login():
      obj=DB()
      uname=request.form['uname']  
      passwrd=request.form['pass']  

      return obj.search(uname,passwrd)

@app.route('/alldonor')
def all():
     OBJ=DB()
     response ='<table border="1px">'
     for donor in OBJ.all_donor():
        response+='<tr><td>'
        for item in donor:
            response+='<td>'+item+'</td>'
        response+='</td></tr>'
     response+='</table>'
     return (response)


@app.route('/search')
def search2():
    obj=DB()
    args = request.args
    print(args)
    no1=args['bg']
    no2=args['loc']
    print(no1)
    print(no2)

    return obj.search(no1,no2)


@app.route('/Add_new')
def add_new():
    obj=DB()
    args = request.args
    print(args)
    no1=args['name']
    no2=args['bg']
    no3=args['loc']
    no4=args['no']
    print(no1)
    print(no2)

    return obj.create(no1,no2,no3,no4)
    # return


@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
    task=Todo.query.get_or_404(id)
    if request.method == 'POST':
        task.content=request.form['content']


        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There is error in updating your file'
    else:
        return render_template('update.html', task=task)




if __name__ == "__main__":
    app.run(debug=True)