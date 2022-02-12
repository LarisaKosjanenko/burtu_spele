from flask import Flask, json, request
from flask_cors import CORS
from operator import itemgetter


# print(__name__)
app = Flask(__name__)
#app.debug = True

CORS(app)  # enable crossdomain access


@app.route('/', methods=['GET', 'POST'])  # what to return at base
def route():
    if (request.method == 'GET'):
        f = open("rezultati.txt", "r")
        dati = f.read()
        f.close()
        datiJSON = json.loads(dati)
        newlist = sorted(datiJSON, key=itemgetter('punkti'), reverse=True)
        return json.dumps(newlist)
    if (request.method == 'POST'):
        jaunsIeraksts = request.get_json(force=True)
        f = open("rezultati.txt", "r")
        dati = f.read()
        f.close()
        datiJSON = json.loads(dati)
        print(datiJSON)
        print(request.get_json(force=True))
        datiJSON.append(jaunsIeraksts)
        f = open("rezultati.txt", "w")
        f.write(json.dumps(datiJSON))
        f.close()
        newlist = sorted(datiJSON, key=itemgetter('punkti'), reverse=True)
        return json.dumps(newlist)


app.run(host='127.0.0.1', port=8020)
# http serv start


# f = open("rezultati.txt","a+")
# f.write("Pēteris, 55\n")
# f.close()
