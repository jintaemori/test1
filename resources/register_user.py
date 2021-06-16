from flask_restful import Resource, reqparse
from db import query
from flask_jwt_extended import create_access_token, jwt_required
from werkzeug.security import safe_str_cmp


# This resource is defined for the user to login.
class RegisterUser(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('uname', type=str, required=True,
                            help="uname cannot be left blank!")
        parser.add_argument('password', type=str, required=True,
                            help="password cannot be left blank!")
        data = parser.parse_args()
        qstr = f"""insert into users values('{data["uname"]}', '{data["password"]}');"""
        result = query(qstr)
        try:
            query(qstr)
            return{"Message": "oorodas"}
        except Exception as e:
            return{"Message": "LOL!"}