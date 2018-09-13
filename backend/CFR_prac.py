import os
import sys
import requests
import json

client_id = json.loads(open('client_secret.json','r').read())['cfr']['client_id']
client_secret = json.loads(open('client_secret.json','r').read())['cfr']['client_secret']
url = "https://openapi.naver.com/v1/vision/face"
#얼굴감지


# 얼굴 인식 결과 JSON 파일 생성하는 함수
def main():
    filepath = os.getcwd() + "/img/"
    jsonpath = os.getcwd() + "/json/"
    if not os.path.exists(jsonpath):
        os.makedirs(jsonpath)

    for imgfile in os.listdir(filepath):
        files = {'image': open(filepath+imgfile, 'rb')}
        #print(filepath+imgfile)
        headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret}
        response = requests.post(url,  files=files, headers=headers)
        rescode = response.status_code
        if(rescode == 200):
            f = open(jsonpath+imgfile[:-5]+".json", "w")
            f.write(response.text)
            f.close()
        else:
            print("Error Code:" + rescode)


main()
