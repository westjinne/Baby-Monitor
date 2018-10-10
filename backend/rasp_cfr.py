import os
import sys
import requests
import json
import time
from flask import jsonify

client_id = json.loads(open('client_secret.json','r').read())['cfr']['client_id']
client_secret = json.loads(open('client_secret.json','r').read())['cfr']['client_secret']
url = "https://openapi.naver.com/v1/vision/face"


def main():
    filepath = os.getcwd() + "/img01/" #rasp용으로 file dir 수정

    before = dict ([f, None] for f in os.listdir(filepath))
    while 1:
        time.sleep(0.5)

        for imgfile in before:
            files = {'image': open(filepath+imgfile, 'rb')}

            headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret}
            response = requests.post(url,  files=files, headers=headers)
            rescode = response.status_code

            if(rescode == 200):
                result = response.json()
                faceNum = result["info"]["faceCount"]

                for i in range(faceNum):
                    gender = result["faces"][i]["gender"]["value"]
                    age = int(result["faces"][i]["age"]["value"][-1:])
                    value = result["faces"][i]["age"]["value"]
                    print(value)
                    print(type(value))
                    line = value.split("~")
                    print(line)
                    print(line[1])

                    #if((gender == "child") or (age < 6)):
                        #r = requests.put("http://babymonitor.pythonanywhere.com/api/update/camera/1", json = {"camId": 1, "gender": gender, "age": age})
                        #print("gender: "+gender+", age: " + str(age))


main()
