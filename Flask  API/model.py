import pickle
import gzip

# 載入模型
with gzip.open('./model/xgboost-secom.pgz', 'rb') as f:
    xgboostModel = pickle.load(f)

# 將模型預測寫成一個 function 
def predict(input):
    pred = xgboostModel.predict(input)[0]
    pred_prob = xgboostModel.predict_proba(input)[0][1]
    return pred,pred_prob