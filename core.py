import falcon
import json
import login

# backend of webhealth server

class login_api(object):
    
    def on_get(self, req, resp):
        # This is default statu by User request:
        resp.status = falcon.HTTP_200
        result_json = {}
        try:
            wh_username = str(req.params['username'])
            wh_password = str(req.params['password'])
            result_json = login.login(wh_username,wh_password)
             
        except:
            result_json = {
                "flag" : False,
                "Note": "Don't  try any prank. We know what are you doing!"
                }
        
        resp.body = json.dumps(result_json)

class singup_api(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        wh_username = str(req.params['username'])
        wh_password = str(req.params['password'])
        result_json = {}
        try:
            feedback = login.singup(wh_username, wh_password)
            result_json = feedback
        except:
            result_json = {
                "flag" : False,
                "Note" : "Main api error, Sorry!"
            }
        resp.body = json.dumps(result_json)
app = falcon.API()
app.add_route('/login', login_api())
app.add_route('/singup',singup_api())