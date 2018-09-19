import json
import pymongo
import os
from pymongo import MongoClient
from flask import jsonify

dbclient = MongoClient()
db = dbclient.babypr

def main():
    with open (os.getcwd() + '/json/littleMe2.json', 'r') as data_file:
        data = json.load(data_file)

    result = db.littleMe2.insert_one(data)
    #위 부분 자동화하기 applicaion의 dict list
    print('Inserted post id %s' % result.inserted_id)


if __name__ == "__main__":
    main()
