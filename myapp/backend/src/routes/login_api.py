from flask import request, Blueprint, jsonify
from flask.views import MethodView
from db import get_db

login_bp = Blueprint('login_api', __name__)

class LoginAPI(MethodView):

    def post(self):
        data = request.get_json()
        password = data.get('password')
        identifier = data.get('identifier')  # accepts email or username
        if not password or not identifier:
            return jsonify({"message": "Missing credentials"}), 400

        db = get_db()
        cursor = db.cursor(dictionary=True)

        query = "SELECT * FROM user WHERE password = %s AND (email = %s OR username = %s)"
        cursor.execute(query, (password, identifier, identifier))
        user = cursor.fetchone()

        cursor.close()

        if user:
            return jsonify({
                "message": "Login successful",
                "user": user
            }), 200
        else:
            return jsonify({"message": "Invalid credentials"}), 401

user_view = LoginAPI.as_view('user_api')
login_bp.add_url_rule('/login', view_func=user_view, methods=['POST', 'OPTION'])