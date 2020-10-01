from flask import *
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

#initiation of the Database called license_plates.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///license_plates.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(app)
db.create_all()


class LicensePlates(db.Model):
    __tablename__ = "license_plates"

    id = db.Column(db.Integer, primary_key=True,nullable=False)
    license_plates = db.Column(db.String(20), unique=True, nullable=False)
    creation_datetime = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"LicensePlates('{self.license_plates}', '{self.creation_datetime}')"


######expected JSON######
# {
#   “plate”: “M-PP123” 
# }
@app.route('/plate', methods=['POST'])
def plate():
    user_plate = request.json
    plate = str(user_plate['plate'])
    print(plate)
    #We retrieve the string before the hyphen
    first_check = str(plate.split('-')[0])
    #We retrieve the string after the hyphen
    second_check = str(plate.split('-')[1])
    is_char = second_check[0:2]
    print(is_char)
    third_check = second_check[2:len(second_check)]
    print(third_check)
    print(third_check.isdigit())
    #All the conditions that make a German plate invalid
    if ( len(first_check) > 3 or (first_check.isalpha() == False) or (second_check[2].isalpha() == True) or (second_check[2] == '0') or (len(third_check) > 4) or (third_check.isdigit() == False)):
        return("Invalid German plate", 201)
    elif (plate is None):
        return("Plate is empty", 400)
    #If the plate is valid we insert it to the Database
    else:
        new_license_plate = LicensePlates(license_plates=plate, creation_datetime=datetime.now())
        db.session.add(new_license_plate)
        db.session.commit()
        db.session.close()
        return("Plate successfully added", 200)


@app.route('/plate', methods=['GET'])
def retrieve_plate(): 
    for lp in LicensePlates.query.all():
        print(lp.license_plates, lp.creation_datetime)
    return("Retrieval of the database completed")