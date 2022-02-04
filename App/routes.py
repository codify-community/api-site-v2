from utils.response import res
from utils.dbconnect import mongoConnect
from flask import request, Blueprint

app: Blueprint = Blueprint("routes", __name__)

cluster = mongoConnect()
db = cluster["discord"]
site = db["site"]
conta = db["conta"]


@app.route('/api/home', methods=['GET'])
def staff():
    print('request recived')
    try:
        obj = {}
        result = site.find_one({"_id": 0})
        obj['staff'] = result['staffs']
        obj['booster'] = result['boosters']
        obj['info'] = {}
        obj['info']['channel_count'] = (result['channel_count'])
        obj['info']['member_count'] = (result['member_count'])
        obj['info']['staff_count'] = (len(obj['staff']))
        return res(data=obj, status=200)
    except:
        import traceback
        traceback.print_exc()
        return res(data="Erro", status=500)

@app.route('/api/ranking')
def ranking():
    try:
        obj = {}
        obj['ranking'] = conta.find().sort("xp", -1)[:10]
        return res(data=obj)
    except:
        return res(data="Erro", status=500)

def favicon():
    return app.send_static_file("favicon.ico")