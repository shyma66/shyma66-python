from flask import Flask

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello,world'
# @app.route('/hello')
# def hello():
#     return 'Hello, s'
@app.route('/edit2', methods=['GET','POST'])

def SecondEdit():

    return 'Second Edit'
@app.route('/edit', methods=['GET','POST'])

def FirstEdit():

    return 'First Edit'




#     # app.run(host="0.0.0.0", port=5555)
#


if __name__ == '__main__':
    app.run()