from flask_restful import Resource, reqparse
from db import query
from flask_jwt_extended import create_access_token, jwt_required
from werkzeug.security import safe_str_cmp

# This resource is defined for the user to login.
class GetUsers(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        data = parser.parse_args()
        qstr = f"""Select * from users;"""
        try:
            return query(qstr)
        except Exception as e:
            return{"Message": "LOL!"}
    
    @jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('uname', type=str, required=True, help="uname cannot be left blank!")
        data = parser.parse_args()
        qstr = f"""Select * from users where uname = '{data['uname']}';"""
        try:
            return query(qstr, json_array= False)
        except Exception as e:
            return{"Message": "LOL!"}