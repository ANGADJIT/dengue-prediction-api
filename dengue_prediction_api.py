from flask import Flask, request
import joblib

app = Flask(__name__)

#* url - http://192.168.1.5:5000/dengue_prediction_model_api?symtoms=98.6-5.0-0-0-0-0-0-0-0-0-14.5-23.0-250.0

#* method for root api page 
@app.route('/')
def root_page():
    return 'TEST API : http://192.168.1.5:5000/dengue_prediction_model_api?symtoms=98.6-5.0-0-0-0-0-0-0-0-0-14.5-23.0-250.0'

# * api method
@app.route('/dengue_prediction_model_api', methods=['GET'])
def dengue_prediction_model_api():
    # * dict to be returned
    model_ouput = dict()

    symtoms_string = str(request.args['symtoms'])
    symtoms_list = symtoms_string.split('-')

    current_temp = float(symtoms_list[0])
    wbc = float(symtoms_list[1])
    headache = int(symtoms_list[2])
    pain_behind_eyes = int(symtoms_list[3])
    joint_muscle_aches = int(symtoms_list[4])
    mettalic_taste_in_mouth = int(symtoms_list[5])
    appetite_loss = int(symtoms_list[6])
    addominal_pain = int(symtoms_list[7])
    nausea_vomiting = int(symtoms_list[8])
    diarrhea = int(symtoms_list[9])
    hemoglobin = float(symtoms_list[10])
    hematocri = float(symtoms_list[11])
    platelet = float(symtoms_list[12])

    symtoms_list = [
        current_temp,
        wbc,
        headache,
        pain_behind_eyes,
        joint_muscle_aches,
        mettalic_taste_in_mouth,
        appetite_loss,
        addominal_pain,
        nausea_vomiting,
        diarrhea,
        hemoglobin,
        hematocri,
        platelet
    ]

    # * loading model
    dengue_prediction_model = joblib.load('model/dengue_prediction_model.pkl')
    model_ouput['is_dengue'] = bool(dengue_prediction_model.predict([symtoms_list])[0])

    return model_ouput


if __name__ == '__main__':
    app.run(debug=False)
