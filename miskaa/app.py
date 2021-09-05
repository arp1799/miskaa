
from bson.objectid import ObjectId
from flask import Flask, Response,request,render_template,redirect, url_for
from flask_pymongo import PyMongo
import json

app = Flask(__name__)


#MONGO SETUP(it has been setup here for convience but can be moved to .env file)
#-------------------------------------------------------------------------------------------------------------
DB_NAME="miskaa"
DB_URI="mongodb+srv://arpit:miskaa567qwerty@cluster0.bzife.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
database_name=DB_NAME
app.config['MONGO_URI']=DB_URI
mongo = PyMongo(app)
#-------------------------------------------------------------------------------------------------------------

#=============================================ROUTES==========================================================



# GET ALL PRODUCTS AVAILABLE IN DB
#-------------------------------------------------------------------------------------------------------------
@app.route('/get_products',methods=['GET'])
def get_products():
    data=list(mongo.db.products.find())
    return render_template('./products.html',products=data)
#-------------------------------------------------------------------------------------------------------------


#ADD PRODUCT TO USER CART
#-------------------------------------------------------------------------------------------------------------
@app.route('/add_product',methods=['POST'])
async def add_to_cart():
    try:
        product=mongo.db.products.find_one(ObjectId(request.form["id"]))
        mongo.db.user.update_one({"_id":ObjectId("6133365ba3374e1ab7a170b2")},{ "$push": { "cart":{"id":product["_id"],"quantity":1} } })
        return redirect(url_for('.get_products'))
    except Exception as ex:
        print(ex)
        return Response(response=json.dumps({"message":"error while adding"}),status=500,mimetype="application/json")
#-------------------------------------------------------------------------------------------------------------

#GET USER CART ITEMS 
#-------------------------------------------------------------------------------------------------------------
@app.route('/cart',methods=['GET'])
def fetch_cart():
    try:
        user=mongo.db.user.find_one(ObjectId("6133365ba3374e1ab7a170b2"))
        cart=user["cart"]
        data=[]
        for obj in cart:
            data.append({"product":mongo.db.products.find_one(obj["id"]),"quantity":obj["quantity"]})
        print(data)
        return render_template('./cart.html',products=data)
    except Exception as ex:
        print(ex)
        return Response(response=json.dumps({"message":"error while retriving your cart"}),status=500,mimetype="application/json")
#-------------------------------------------------------------------------------------------------------------



#UPDATE QUANTITY OF PRODUCT IN CART
#-------------------------------------------------------------------------------------------------------------
@app.route('/update_quantity',methods=['POST'])
def update_quantity_cart():
    try:
        if(request.form["update"]=="1"):
            dbRes=mongo.db.user.update_one({"_id":ObjectId("6133365ba3374e1ab7a170b2"),"cart.id":ObjectId(request.form["id"])} ,{"$inc":{"cart.$.quantity":1}})
        elif(request.form["update"]=="0"):
            dbRes=mongo.db.user.update_one({"_id":ObjectId("6133365ba3374e1ab7a170b2"),"cart.id":ObjectId(request.form["id"])} ,{"$inc":{"cart.$.quantity":-1}})
        return redirect(url_for('.fetch_cart')) #send along error messgae
    except Exception as ex:
        print(ex)
        return Response(response=json.dumps({"message":"error while updating your cart"}),status=500,mimetype="application/json")

#-------------------------------------------------------------------------------------------------------------


#DELETE ITEM FROM CART
#-------------------------------------------------------------------------------------------------------------
@app.route('/delete_product',methods=['POST'])
def delete_item_cart():
    try:
        mongo.db.user.update({"_id":ObjectId("6133365ba3374e1ab7a170b2")},{ "$pull": { "cart":{"id":ObjectId(request.form["id"])} } })
        return redirect(url_for('.fetch_cart'))
    except Exception as ex:
        print(ex)
        return Response(response=json.dumps({"message":"error while deleting item from your cart"}),status=500,mimetype="application/json")

#-------------------------------------------------------------------------------------------------------------



if __name__=='__main__':
    app.run(port="80",debug="True")