from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager

#authentication
from resources.register_user import RegisterUser
from resources.my_login import MyLogin
from resources.get_users import GetUsers

# create flask app instance
app = Flask(__name__)

#set config for jwt
app.config['PROPAGATE_EXCEPTIONS']=True
app.config['JWT_SECRET_KEY'] = 'qp-cbit'

#initialize api
api = Api(app)

api.add_resource(RegisterUser, '/user-register') #user register
api.add_resource(MyLogin, '/my-login') #my login
api.add_resource(GetUsers, '/get-users') #my login

jwt=JWTManager(app)

#return an error response if JWT is missing
@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        'error': 'authorization_required',
        "description": "Request does not contain an access token."
    }), 401

#return an error response if JWT is invalid
@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        'error': 'invalid_token',
        'message': 'Signature verification failed.'
    }), 401

#a welcome route to test if the flask app is working.
@app.route('/')
def home():
    return(f"""<h1 style="font-family: 'Palatino Linotype';">This is an API for the CBIT question paper management utility.</h1>
                <p style="font-size:2em">Developed by Harish Akula</p>""")

# set debug = False while deploying. debug = True is not safe in production environments
if __name__ == '__main__':
    app.run(debug=False)