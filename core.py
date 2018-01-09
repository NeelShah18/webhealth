import falcon
import json

# backend of webhealth server

class login(object):
    
    def on_get(self, req, resp):
        # This is default statu by User request:
        resp.status = falcon.HTTP_200
        wh_username = str(req.params['usernmae'])
        wh_password = str(req.params['password'])
        result_json = {}
        try:
            if  ((wh_username == str("neel")) and (wh_password == str("shah"))):
                result_json = {"Response": True}
            else:
                result_json = {"Response": "Alert!!! Wrong username and password. Please check again and try"} 
        except:
            result_json = {"Response": "Don't  try any prank. We know what are you doing!"}
        
        resp.body = json.dumps(result_json)


app = falcon.API()
app.add_route('/login', login())