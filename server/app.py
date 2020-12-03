from flask import Flask, request,jsonify,json
from bson import ObjectId
import pymongo
import uuid
from bson import ObjectId
from bson.json_util import dumps
from flask_cors import CORS, cross_origin


app = Flask(__name__)
Cors = CORS(app)
CORS(app, resources={r'/*': {'origins': '*'}},CORS_SUPPORTS_CREDENTIALS = True)
app.config['CORS_HEADERS'] = 'Content-Type'



client = pymongo.MongoClient(databaseurlhere)
db = client.#database_name
dbenter = db.#collection_name

#hi 
#@cross_origin()




@app.route("/dataentry", methods=["POST","GET"])
def submitData():
    response_object = {'status':'success'}
    if request.method == "POST":
        post_data = request.get_json()
        jason_data={}
       
        jason_data['name']=post_data.get('name'),
        jason_data['about']=post_data.get('about')
        dbenter.insert_one(jason_data)
        response_object['message'] ='Data added!'
        return jsonify(response_object)
        

@app.route("/dataview", methods=["GET"])
def ViewData(): 
   data=dumps(dbenter.find())
   return data

@app.route("/dataview/<dataid>",methods=["DELETE"]) 
def DeleteData(dataid):
    if request.method =="DELETE":
       dbenter.delete_one({"_id":ObjectId(dataid)}) 
       response_object = {'status':'success'}
       return jsonify(response_object)

@app.route("/dataview/<dataid>",methods=["PUT"])
def ModifyData(dataid):
    if request.method == "PUT":
        post_data = request.get_json()
        name=post_data.get('name'),
        about=post_data.get('about')
        dbenter.update_one({'_id':ObjectId(dataid)},{'$set':{"name":name,"about":about}})
        response_object = {'status':'success'}
        return jsonify(response_object)

    
     

if __name__ == '__main__':
    app.run(debug=True)
