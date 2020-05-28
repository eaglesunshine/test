import json, requests, logging
from flask import Flask

app = Flask(__name__)

videos = [
    'ad_1.mp4',  
    'childabuse_1.mp4',  
    'contraband_1.mp4',  
    'ocr_1.mp4', 
    'politics_1.mp4',
    'porn_1.mp4',
    'religion_1.mp4',
    'religion_2.mp4',
    'terror_1.mp4',
    'terror_2.mp4'
]

# 计数
success_count = 0

# callback 
@app.route('/callback', methods=['POST'])
def callback():
    if request.method == 'POST':
        success_count += 1
        print(success_count)
        pass

def sendRequest(video_url):
    print(video_url)

    request_url = "http://10.9.244.203:8081/api/v1/tasks"
    headers = {'Content-Type':'application/json'}
    
    # 配置参数
    values = {}
    values['type'] = 'video'
    values['url'] = video_url
    values['callback_url'] = '172.20.23.218:50064/callback'
    values_json = json.dumps(values, ensure_ascii=False)

    # send request
    req = requests.post(request_url, data=values_json, headers=headers)

    # return 
    status = json.dumps(req.json(), ensure_ascii=False)
    return status


def run():
    base_url = '172.20.23.218:50063/video/'
    for i in range(1, 2):
        for video_path in videos:
            video_url = base_url + video_path
            status = sendRequest(video_url)
            print(status)

if __name__ == '__main__':
    run()
    app.run(host = '0.0.0.0', port = '50064', debug = False)    # 开放http接口