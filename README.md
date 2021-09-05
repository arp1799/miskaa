# miskaa
 very basic restful API's for cart using flask,mongodb
 for now env variables are included in main file only for easy access

--------------------------------------------How To Run------------------------------------------------------------

1)clone the floder

2)"cd miskaa"

3)install required libraries(flask,flask_pymongo) if not there

4)"venv\Scripts\activate" enter this in terminal to switch to virtual enviorment of this folder

5)"py app.py" to run the app at http://127.0.0.1:80/

at http://127.0.0.1:80/get_products ->to view all products

at http://127.0.0.1:80/cart-> to view cart


--------------------------------------------API's------------------------------------------------------------

these API's are created for particular user i.e; it is assumed in each user object there is cart array(checkout assumed DB)

API's Explained

list all products: list all the products in db.products

add product to cart : adding particular product in particular user cart array

delete product from cart: delete particular product from user cart array

update quantity of produ: update quantity of previusly added product in particular user array

--------------------------------------------Assumed DB------------------------------------------------------------

User:{firstname:string,lastname:string, cart:zarray}

Products:{title:string, price:string, image:string}

Example: user:{"_id":{"$oid":"6133365ba3374e1ab7a170b2"},

    "fname":"Arpit",
    
    "lname":"Agrawal",
    
    "mobileNo":"9873188447",
        
    "cart":[
              {"id":{"$oid":"61324c1d490954343aaeced7"},
                "quantity":{"$numberInt":"1"}
              },
              {"id":{"$oid":"61324e722eb56bbdf7fa142c"},"quantity":{"$numberInt":"1"}},
              {"id":{"$oid":"6132593b7932a4f638e2949b"},"quantity":{"$numberInt":"1"}}
           ]
 }
 
products:{ 
           "_id":{"$oid":"61324c1d490954343aaeced7"},
           
           "name":"samsung mobile", 
           "price":{"$numberInt":"20000"}
         }


