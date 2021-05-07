from flask import Flask,request,render_template, redirect, url_for,Response,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import ForeignKey
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost:5432/task"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# CREATING TABLES - Users, Products, Reviews

class UsersModel(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<User {self.name}>"

class ProductsModel(db.Model):
    __tablename__ = 'Products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String())

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"<Product {self.name}>"

class ReviewsModel(db.Model):
    __tablename__ = 'Reviews'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('Users.id'))
    product_id = db.Column(db.Integer, ForeignKey('Products.id'))
    review = db.Column(db.String())
    rating = db.Column(db.Float)

    def __init__(self, user_id, product_id, review, rating):
        self.user_id = user_id
        self.product_id = product_id
        self.review = review
        self.rating = rating

    def __repr__(self):
        return f"<Review {self.review}>"

# EndPoints

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/users', methods=['POST', 'GET'])
def handle_users():
    if request.method == 'POST':
        if request.is_json:
            datas = request.get_json()
            for data in datas["name"]:
                new_user = UsersModel(name=data)
                db.session.add(new_user)
                db.session.commit()
            return {"message": f"user {new_user.name} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        users = UsersModel.query.all()
        results = [
            {
                "name": i.name,

            } for i in users]

        return {"count": len(results), "users": results}

@app.route('/products', methods=['POST', 'GET'])
def handle_products():
    if request.method == 'POST':
        print(request)
        if request.is_json:
            data = request.get_json()
            for i in range(len(data)):
                new_products = ProductsModel(name=data[i]['name'], description=data[i]['description'])
                db.session.add(new_products)
                db.session.commit()
            return {"message": f"product {new_products.name} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        products = ProductsModel.query.all()
        results = [
            {
                "name": i.name,
                "description": i.description

            } for i in products]

        return {"count": len(results), "products": results}

@app.route('/rev', methods=['POST', 'GET'])
def handle_reviews():
    if request.method == 'POST':
        print(request)
        if request.is_json:
            data = request.get_json()
            for i in range(len(data)):
                new_reviews = ReviewsModel(user_id=data[i]['user_id'], product_id=data[i]['product_id'], review=data[i]['review'], rating=data[i]['rating'])
                db.session.add(new_reviews)
                db.session.commit()
            return {"message": f"product {new_reviews.review} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        reviews = ReviewsModel.query.all()
        results = [
            {
                "user_id": i.user_id,
                "product_id": i.product_id,
                "review": i.review,
                "rating": i.rating

            } for i in reviews]

        return {"count": len(results), "reviews": results}

# RETURNING USERS
@app.route('/user/<user_id>', methods=['GET'])
def handle_users_p_id(user_id): 

    handle = UsersModel.query.filter_by(id=user_id).all()

    if request.method == 'GET':
        results = [
            {
                "name": i.name,

            } for i in handle]

        d =  {"handle": results}
        return jsonify(d)


# RETURNING PRODUCTS
@app.route('/product/<product_id>', methods=['GET'])
def handle_products_p_id(product_id):

    handle = ProductsModel.query.filter_by(id=product_id).all()

    if request.method == 'GET':
        results = [
            {
                "name": i.name,
                "description": i.description,

            } for i in handle]

        d =  {"handle": results}
        return jsonify(d)

# RETURNING REVIEWS
# @company_bp.route('/<company_id>',methods=['POST'])
@app.route('/review/<product_id>', methods=['POST', 'GET', 'PUT', 'DELETE'])                               
def handle_reviews_p_id(product_id):   

    handle = ReviewsModel.query.filter_by(product_id=product_id).all()
    # handle = ReviewsModel.query.get_or_404(product_id)
    # handle = ReviewsModel.query(ReviewsModel.product_id)

    if request.method == 'GET':

        results = [
            {
                "user_id": i.user_id,
                "review": i.review

            } for i in handle]

        d =  {"message": "success", "handle": results}
        return jsonify(d)

    if request.method == 'POST':
        # data = request.get_json()
        # handle.product_id = product_id
        # handle.user_id = data['user_id']
        # handle.review = data['review']
        # handle.rating = data['rating']
        # db.session.add(handle)
        # db.session.commit()
        
        # temp = request.form
        temp = json.loads(request.data)
        check = ReviewsModel.query.filter_by(product_id = product_id, user_id = temp['user_id']).all()
        if (len(check) != 0):
            # return 'Failure', 200
            return {"message": f"Failure"}
        new_reviews = ReviewsModel(user_id=temp['user_id'], product_id=product_id, review=temp['review'], rating=temp['rating'])
        db.session.add(new_reviews)     
        db.session.commit()
        return {"message": f"Success"}

    if request.method == 'PUT':
        # data = request.get_json()
        # handle.product_id = product_id
        # handle.user_id = data['user_id']
        # handle.review = data['review']
        # handle.rating = data['rating']
        # db.session.add(handle)
        # db.session.commit()

        temp = json.loads(request.data)
        check = ReviewsModel.query.filter_by(product_id = product_id, user_id = temp['user_id']).all()
        if (len(check) != 0):
            return {"message": f"Failure"}

        new_reviews = ReviewsModel(user_id=temp['user_id'], product_id=product_id, review=temp['review'], rating=temp['rating'])
        db.session.add(new_reviews)
        db.session.commit()
        return {"message": f"Success"}


    if request.method == 'DELETE':
        if(len(handle) != 0):
            return {"message": f"Failure"}
        ReviewsModel.query.filter_by(product_id=product_id).delete()
        return {"message": f"Success"}

    return jsonify(temp_dict) 


@app.route("/addition")
def add():
    # return render_template('demo.html')
    return render_template('reviews_post.html', page = 'add')

@app.route('/display')
def display():
    return render_template('reviews_display.html', page='display')


@app.route('/deletion')
def delete():
    return render_template('reviews_post.html', page='delete')


if __name__ == '__main__':
    app.run(debug=True)