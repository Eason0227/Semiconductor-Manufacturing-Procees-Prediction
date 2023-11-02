import numpy as np
import model

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# 開放跨網域CORS權限，跨來源資源共享(Cross-Origin Resource Sharing, CORS)是讓目前瀏覽網站的使用者能訪問不同來源網域的伺服器
# 前端使用者在不同網域利用 ajax 或 fetch 存取 API 時就會有讀取權限。
CORS(app)

# 單引號內的內容即代表使用者在呼叫 API 的路徑位置
@app.route('/')
def index():
    return 'hello!!'

# 設定他的路徑為 /predict，且HTTP Requesst 的方法指定 methods=['POST']。
@app.route('/predict', methods=['POST'])
def postInput():
    # 取得前端傳過來的數值
    insertValues = request.get_json()
    x1,x2,x3,x4,x5,x6,x7 = insertValues["0"] ,insertValues["1"] , insertValues["2"] , insertValues["14"],insertValues["16"],insertValues["22"],insertValues["23"]
    x8,x9,x10,x11,x12,x13,x14 = insertValues['28'],insertValues['32'],insertValues['39'],insertValues['40'],insertValues['41'],insertValues['51'],insertValues['55']
    x15,x16,x17,x18,x19,x20,x21 = insertValues['59'],insertValues['68'],insertValues['71'],insertValues['72'],insertValues['73'],insertValues['83'],insertValues['88']
    x22,x23,x24,x25,x26,x27,x28 = insertValues['90'],insertValues['110'],insertValues['111'],insertValues['115'],insertValues['117'],insertValues['129'],insertValues['133']
    x29,x30,x31,x32,x33,x34,x35 = insertValues['134'],insertValues['200'],insertValues['336'],insertValues['345'],insertValues['346'],insertValues['412'],insertValues['418']
    x36,x37,x38,x39,x40,x41,x42 = insertValues['423'],insertValues['460'],insertValues['468'],insertValues['472'],insertValues['480'],insertValues['485'],insertValues['486']
    x43,x44,x45,x46,x47,x48,x49= insertValues['488'],insertValues['489'],insertValues['490'],insertValues['500'],insertValues['510'],insertValues['547'], insertValues['548']
    x50,x51 = insertValues['562'],insertValues['581']

    input = np.array([[x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,
    x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32,x33,x34,x35,x36,x37,x38,x39,x40,
    x41,x42,x43,x44,x45,x46,x47,x48,x49,x50,x51]])
    
    # 將這些數值放到 Numpy 陣列中送到稍早以封裝好的 mpdel.py 中的 predict() 方法。
    result,pred_prob = model.predict(input)
    return jsonify({'product fail': str(result),'product fail prob  ': str(pred_prob) } )
    
if __name__ == '__main__':
    # 將此 API 部署在伺服器的3000 PORT當中。host='0.0.0.0' 表示預設路由將會自動幫你取得目前伺服器的固定 IP 位置
    # debug 設定為 True 即表示 API 被啟動時會自動監聽程式是否有變動
    app.run(host='0.0.0.0', port=3000, debug=True)
