from flask import current_app as app
from flask import jsonify, request
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity
)
from werkzeug.security import check_password_hash, generate_password_hash

from application.database.models.models import User, Post, db
from config import Config
from datetime import datetime


config = Config()

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




@app.route("/user", methods=["POST"])
def create_user():
    data = request.get_json()  
    username = data.get("username")   
    email = data.get("email")   
    password = data.get("password")

    if not username:
        return jsonify({"message": "Username is required"}), 400

    if not password:
        return jsonify({"message": "Password is required"}), 400

    if not email:
        return jsonify({"message": "Email is required"}), 400

    user = User.get_user_serialize(email)
    if user:
        return jsonify({"error": "Email already in use"}), 409

     

    data = {
        "username": username,   
        "email": email, 
        "password": generate_password_hash(password)
    }
    try:
        User.create_user(**data)
        return jsonify({"messege":"user create succesfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400 



@app.route("/login", methods=["POST"])   
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"message": "Invalid Credentials"}), 401

    # @TODO update below to have the user model, not a list
    user = User.get_user_serialize(email)
    if not user:
        return jsonify({"message": "Invalid Credentials"}), 401



    # @TODO check if the user vailable, breake in to two if conditions
    
    if not check_password_hash(user.password, password):
        return jsonify({"message": "Invalid  Credentials"}), 401

    return (
        jsonify(    
            {
                "access_token": create_access_token(identity=user.email),
                "refresh_token": create_refresh_token(identity=user.email),
            }
        ),
        200,
    )


# @app.route("/protected", methods=["GET"])   
# @jwt_required()  
# def protected():   
#     return jsonify({"message": "This is a protected endpoint"}), 200
  

@app.route('/post', methods=['POST'])
@jwt_required()
def create_post():
    data = request.get_json()
    post_text = data.get("post_text")
    post_image = data.get("post_image")
    user = get_jwt_identity()
    print("Hewe")
    print(type(user))
    
    user = User.get_user_serialize(user)
    data = {
        "user_id": user,
        "post": post_text,
        "image": post_image
    }
    try:
        post = Post.create_post(data)
        return_data = {
            "id": post.id, "post_text": post.post, "post_image": post.image
        }
        return jsonify({'message': return_data}), 201
    except Exception as e:
        return jsonify({"error":(e)}), 400
    
    


@app.route('/post/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    data = request.get_json()
    post_text =data.get('post_text') 
    post_image = data.get('post_image')

    upadte_data = {
        "post": post_text,
        "image": post_image
    }
    
    try:
        data, status = Post.update_post(post_id, upadte_data)
        return jsonify({'data': data}), status
    except Exception as e:
        return jsonify({"error":(e)}), 400
   
    
 
@app.route('/post/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    
    try:
        response, status = Post.delete_post(post_id)
        return jsonify({'message': response}), status
    except Exception as e:
        return jsonify({"error":(e)}), 400



@app.route('/post/<int:user_id>', methods=['GET'])
def get_user_posts(user_id):
    posts = Post.query.filter_by(user_id=user_id, is_deleted=False).all()
    if not posts:
        return jsonify({'message': 'No posts available'}), 404
    return jsonify({'data': [{"post_id": post.id, "post_text": post.text, "post_image": post.image} for post in posts]}), 200


@app.route('/post/<int:post_id>', methods=['GET'])
def get_post(post_id):
   post_id = request.args.get('post_id')
   post = Post.query.filter_by(post_id=post_id, is_deleted=False).first()
   if not post:
        return jsonify({'message': 'Post not available'}), 404
   return jsonify({'data': {"post_id": post.id, "post_text": post.text, "post_image": post.image}}), 200
