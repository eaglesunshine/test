from flask import Flask,make_response, jsonify,request

# 计数
#success_count = 0

app = Flask(__name__)

# callback
@app.route('/callback', methods=['POST'])
def callback():
    if request.method == 'POST':
        success_count = 0
        success_count = success_count + 1
        print(success_count)
        resp = make_response(jsonify({"status":200, "message":"success", "data":''}))
        return resp

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 3000, debug = False)    # 开放http接口
