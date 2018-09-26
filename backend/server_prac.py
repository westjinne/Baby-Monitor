from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

samplepath = os.getcwd() + "/dbex/"
#jsonpath = os.getcwd() + "/dbex/"

class Info(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    camId = db.Column(db.Integer, unique = False)
    location = db.Column(db.String(80), unique=False)
    isActive  = db.Column(db.Integer, unique = False)
    imgUrl = db.Column(db.String(120), unique= False)

    def __init__(self, camId, location, isActive, imgUrl):
        self.camId = camId
        self.location = location
        self.isActive = isActive
        self.imgUrl = imgUrl

class InfoSchema(ma.Schema):
    class Meta:
        fields = ('camId', 'location', 'isActive', 'imgUrl')

info_schema = InfoSchema()
info_schemas = InfoSchema(many=True)


@app.route('/')
def base():
    with open(samplepath+'littleMe2.json') as data_file:
        data = json.load(data_file)
        return jsonify(data)
    #new file로 수정

@app.route('/api/create/cameraData', methods =["POST"])
def create_cameraData():
    content = samplepath+"littleMe2.json"
    camId = content["camId"]
    location = content["location"]
    isActive = content["isActive"]
    imgUrl = content["imgUrl"]

    new_data = Info(camId, location, isActive, imgUrl)

    db.session.add(new_data)
    db.session.commit()

    return "success"

# endpoint to get user detail by id
@app.route("/api/get/camera/<id>", methods=["GET"])
def camera_detail(id):
    data = Info.query.get(id)
    return info_schema.jsonify(data)

@app.route("/api/get/all", methods=["GET"])
def get_all_camera():
    all_camera = Info.query.all()
    result = info_schemas.dump(all_camera)
    return jsonify(result.data)


@app.route("/api/update/camera/<id>", methods=["PUT"])
def camera_update(id):
    cam = Info.query.get(id)
    location = request.json['location']
    isActive = request.json['isActive']
    imgUrl = request.json['imgUrl']

    if location != "":
        cam.location = location

    if isActive != None:
        cam.isActive = isActive

    if imgUrl != "":
        cam.imgUrl = imgUrl


    db.session.commit()
    return info_schema.jsonify(cam)




if __name__ == '__main__':
    app.run(debug=True)
