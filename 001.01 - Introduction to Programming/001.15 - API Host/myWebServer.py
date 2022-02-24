import json
import flask
import waitress

class myWebResponse():
    def __init__(self):
        self.body = {"message": "Success!"}
        self.statusCode = 200
    def response(self):
        output = flask.Response(json.dumps(self.body), status=self.statusCode)
        output.headers['Content-Type'] = 'application/json'
        return output

app = flask.Flask(__name__)
@app.route('/')
def myHome():
    try:
        thisResponse = myWebResponse()
        thisResponse.body['message'] = "Success! This is the home URL"
    except:
        thisResponse.statusCode = 500
        thisResponse.body['message'] = "Error!"
    finally:
        return thisResponse.response()

@app.route('/other')
def myOther():
    try:
        thisResponse = myWebResponse()
        thisResponse.body['message'] = "Success! This is the other URL"
    except:
        thisResponse.statusCode = 500
        thisResponse.body['message'] = "Error!"
    finally:
        return thisResponse.response()

waitress.serve(app, host='0.0.0.0', port=8080, threads=1)
# localhost:8080
# localhost:8080/other