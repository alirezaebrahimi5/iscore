from flask import Flask
from flask import request
  

app = Flask(__name__)


# GET database info
@app.route('/', methods=['GET'])
def home(request):
    return 


@app.route("/login", methods=['POST'])
def loginUser():
    if request.method=='POST':
        uname = request.data.get('username')
        password = request.data.get("password")


@app.route('/send/<product:id>/', methods=['POST'])
def getProduct(product):
    return 


if __name__ =='__main__':
    # SECURITY WARNING: don't run with debug turned on in production!
    app.run(debug = True)
