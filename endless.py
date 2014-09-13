from flask import Flask, render_template
from flask.ext.restful import Api, Resource

app = Flask(__name__)
api = Api(app)


@app.route('/')
def control():
    return render_template('handheld_control.html')

class Right(Resource):
    def post(self):
        print 'right!!'
api.add_resource(Right, '/right/')

class Left(Resource):
    def post(self):
        print 'right!!'
api.add_resource(Left, '/left/')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
