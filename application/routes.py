from flask import current_app as app
from config import Config
from application.database.models.models import User
from flask import jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash

config = Config()


@app.route("/hello", methods=["GET"])
def route_base():
    # data  = {
    #     "username": "janiw",
    #     "email": "sajaniwijesekara@gmail.com",
    #     "password": "1722@s"
    # }
    # User.create_user(**data)
    # User.get_user_serialize(1)
    return {"message": "Hello"}


@app.route("/user", methods=["POST"])
def create_user():
    try:
        json_data = request.get_json()
        user = User.create_user(**json_data)
        return jsonify ({
            "username": user.username,
            "email": user.email
            "password_hash": generate_password_hash('password')
        })
    except Exception as e:
        return jsonify({
            "message": str(e)
        })

@app.route('/login', methods=['POST'])
def login():
    request_data = request.get_json()
    username = request_data.get('username')
    password = request_data.get('password')

    for user in user:
        if username == user['username'] and user['email'] and check_password_hash(user['password_hash'], password):
            return jsonify({'message': 'Successfully logged in'}), 

    return jsonify({'message': 'Invalid username or password'}), 
    

