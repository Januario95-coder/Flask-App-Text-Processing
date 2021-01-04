from flask import jsonify

from init_app import app


from models import Result


@app.route('/')
def hello():
    return "Hello World!"
    

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)
    
    
@app.route('/user/<name>/<email>')
def user(name, email):
    data = {
        'name': name,
        'email': email
    }
    return jsonify(data)
    

if __name__=='__main__':
    app.run(debug=True)