import os
import sys
import requests
client_id = "WRKZl5L8otsA0Oolnv91"
client_secret = "qVUP4ef0kW"
url = "https://openapi.naver.com/v1/vision/face"
#얼굴감지


def main():
    fileroot = os.getcwd()
    files = {'image': open(fileroot+'/img/pic03.jpeg', 'rb')}
    savefileroot = os.getcwd()+'/jsons'
    headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret}
    response = requests.post(url,  files=files, headers=headers)
    rescode = response.status_code
    if(rescode == 200):
        #print (response.text)
        f = open(savefileroot+"/result_pic03.json", "w")
        f.write(response.text)
        f.close()
    else:
        print("Error Code:" + rescode)


main()
