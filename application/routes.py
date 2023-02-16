from flask import current_app as app
from config import Config
from application.database.models.models import User
from flask import jsonify, request
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from werkzeug.security import generate_password_hash, check_password_hash

config = Config()

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)


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


users = []   

@app.route("/user", methods=['POST'])  
def create_user(): 
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Missing username or password'}), 400  

    hashed_password = generate_password_hash(password, method='sjw123')   
    user = {  
        'username': username,   
        'password': hashed_password
    }
    users.append(user)
    return jsonify({'message': 'User created successfully'}), 201



@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = request.json.get('username')
    password = request.json.get('password')
    if not username or not password:
        return jsonify({'message': 'Missing username or password'}), 400

    user = next((u for u in users if u['username'] == username), None)
    if not user or not check_password_hash(user['password'], password):
        return jsonify({'message': 'Invalid username or password'}), 401

    access_token = create_access_token(identity=username)
    return jsonify({'access_token': access_token}), 200



@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify({'message': 'This is a protected endpoint'}), 200
