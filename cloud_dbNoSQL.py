import os 
import jwt # Get the jwt encode
import json 
from flask import Flask,request,jsonify
user = os.listdir("/home")[0] #Get the user home 
app = Flask(__name__) # Get the flask app setting name 

current_backup = {} # Get the current backup data 
@app.route("/user_db_data",methods=['GET','POST'])
def data_userrequest():
           req = request.get_json(force=True)
           user_name = req.get("email")
           payload_data = req.get("payload_data") 
           current_backup[user_name] = payload_data 
           write_back_up = json.dumps(current_backup)
           write_db = open("/home/"+user+"/roboreactor_db.json",'w')
           write_db.write(write_back_up) # Get the backupcode write down into the system     
           return jsonify(current_backup)

if __name__ == "__main__":
 
             app.run(debug=True,threaded=True,host="0.0.0.0",port=5788)
