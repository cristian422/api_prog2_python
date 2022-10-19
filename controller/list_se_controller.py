from flask import Blueprint,Response, request
import json

from model.kidDTO import KidByPositionDTO
from view.list_se_service import ListSEService
from util.util_encoder import UtilEncoder

app_list_se = Blueprint("app_list_se",__name__)

list_se_service = ListSEService()

@app_list_se.route('/listse')
def get_list():  # put application's code here
    #return list_se_service.list.head

    return Response(status=200,
                    response=json.dumps(list_se_service.list.head
                                        , cls=UtilEncoder), mimetype="application/json")

@app_list_se.route('/listse',methods=['POST'])
def save_kid():
    data = request.json
    return Response(status=200,response=json.dumps({"message":
                    list_se_service.add_kid(data)}),
                    mimetype="application/json")

@app_list_se.route('/listse/byposition', methods=['POST'])
def save_by_position():
    data = request.json
    kidByPositionDTO = KidByPositionDTO(data['position'],data['kid'])
    return  Response(status=200,response=json.dumps({"message":
                    list_se_service.add_by_position(kidByPositionDTO)}),
                    mimetype="application/json")

@app_list_se.route('/listse/mixbygender')
def mix_by_gender():
    return Response(status=200, response=json.dumps({"message":
                 list_se_service.mix_by_gender()}),
                    mimetype="application/json")

@app_list_se.route('/listse/delet_3years_kids')
def mix_by_gender():
    return Response(status=200, response=json.dumps({"message":
                 list_se_service.delet_3years_kids()}),
                    mimetype="application/json")

@app_list_se.route('/listse/less_7_years')
def mix_by_gender():
    return Response(status=200, response=json.dumps({"message":
                 list_se_service.less_7_years()}),
                    mimetype="application/json")

@app_list_se.route('/listse/delet_position')
def mix_by_gender():
    data=request.json
    return Response(status=200, response=json.dumps({"message":
                 list_se_service.delet_position(data)}),
                    mimetype="application/json")

@app_list_se.route('/listse/male_female')
def mix_by_gender():
    return Response(status=200, response=json.dumps({"message":
                 list_se_service.male_female()}),
                    mimetype="application/json")

@app_list_se.route('/listse/count')
def mix_by_gender():
    return Response(status=200, response=json.dumps({"message":
                 list_se_service.count()}),
                    mimetype="application/json")

@app_list_se.route('/listse/invert')
def mix_by_gender():
    return Response(status=200, response=json.dumps({"message":
                 list_se_service.invert()}),
                    mimetype="application/json")