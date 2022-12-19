# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask, jsonify
from flask import make_response
from flask import request
import pandas as pd

if __name__ == '__main__':
    app = Flask(__name__)
    datas = pd.read_csv('colornames.txt', sep=",", names=['hexCode', 'bestName', 'votes'], skiprows=1)

    print(datas)


    @app.route('/api/datas', methods=['GET'])
    def get_datas():
        return jsonify({'DATA': datas})


    @app.route('/api/datas/<string:hexCode>', methods=['GET'])
    def get_hexcode(hexCode):
        data = [data for data in datas if data['hexCode'] == hexCode]
        if len(data) == 0:
            return jsonify({'data': 'Not found'}), 404
        return jsonify({'hexCode': hexCode})


    @app.route('/api/datas', methods=['POST'])
    def create_color():
        newColor = {
            'hexCode': datas[-1]['hexCode'] + 1,
            'bestName': request.json['bestName'],
            'votes': request.json['votes'],

        }
        datas.append(newColor)
        return jsonify({'data': newColor}), 201


    @app.route('/api/datas/<string:hexCode>', methods=['DELETE'])
    def delete_color(hexCode):
        data = [data for data in datas if datas['hexCode'] == hexCode]
        if len(hexCode) == 0:
            return jsonify({'product': 'Not found'}), 404
        datas.remove(datas[hexCode[hexCode]])
        return jsonify({'result': True})

# Aykut ECER 
