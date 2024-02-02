from flask import *
from flask_login import LoginManager, UserMixin, login_user
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


############################### models ###############################


db = SQLAlchemy(app)


class Product(db.Model):
      id    = db.Column('product_id', db.Integer, primary_key=True, serializable=False)
      title = db.Column(db.String(50), nullable=False)
      price = db.Column(db.String(21), nullable=False)
      
      def __init__(self, title, price) -> None:
           self.title = title
           self.price = price


class User(UserMixin, db.Model):
      id       = db.Column('user_id', db.Integer, primary_key = True, serializable=False)
      username = db.Column(db.String(30), nullable=False, unique=True)
      password = db.Column(db.String(50), nullable=False)


db.init_app(app)

 
with app.app_context():
    db.create_all()


############################### Security warnings ###############################


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.sqlite3'
app.config["FLASK_SECRET_KEY"] = "ENTER YOUR SECRET KEY"


############################### User login ###############################


login_manager = LoginManager()

login_manager.init_app(app)

@login_manager.user_loader
def loader_user(user_id):
    return User.query.get(user_id)


############################### handle requests ###############################


@app.route('/login',methods = ['POST'])
def login():
      if request.method == "POST":
        user = User.query.filter_by(username=request.data.get("username")).first()
        if user.password == request.data.get("password"):
            if login_user(user):
                  return jsonify(user)
            else:
                  return jsonify("Error")


@app.route("product/<integer:id>/", methods=['GET', 'POST'])
def getProduct(id, user):
      return jsonify()


@app.route("", methods=["POST", "GET"])
def searchProduct(id):
      if request.method == "":
            return jsonify()


############################### app run ###############################


if __name__ == '__main__':  
   app.run(debug = True, port=5000, host="http://127.0.0.1") 
