from flask import *
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


############################### models ###############################


db = SQLAlchemy(app)


class Product(db.Model):
      id = db.Column(db.String(30), db.Integer, primary_key=True, serializable=False)
      title = db.Column(db.String(50), nullable=False)


class User(db.Model):
      id = db.Column('user_id', db.Integer, primary_key = True)
      username = db.Column(db.String(30), nullable=False, unique=True)
      password = db.Column(db.String(50), nullable=False)


db.init_app(app)

 
with app.app_context():
    db.create_all()


############################### Security warnings ###############################


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.sqlite3'
app.config["FLASK_SECRET_KEY"] = "ENTER YOUR SECRET KEY"


############################### handle requests ###############################


@app.route('/login',methods = ['POST'])
def login():
      if request.method == "POST":
            username=request.data.get('username')
            password=request.data.get('password')
            return 


@app.route("product/<integer:id>/", methods=['GET'])
def getProduct(id, user):
      return


@app.route("", methods=["POST"])
def unnamed():
      return 


############################### app run ###############################


if __name__ == '__main__':  
   app.run(debug = True, port=5000, host="http://127.0.0.1") 
