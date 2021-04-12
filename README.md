# DSAI_HW2_F74062052
## Run Code 
  python trader.py --training "training_data.csv" --testing "testing_data.csv" --output output.csv
## data analysis:
  這邊因模型簡易緣故，僅使用開盤價格來做訓練及預測。
  因測試資料僅19筆，故訓練資料只往前拿80筆，符合80/20法則。
## model selecting:
  使用ARIMA Model, ARIMA parameters: p=4, d=1, q=0
## processing:
  * 使用逐點預測，每一天預測下一天的結果比較後，隨即將下一天的資料丟入模型Re-Train
  * 當明天預測價格比今天高時，如果手上不是賣空情況即賣掉；
  * 如果比今天低時，手上又沒持有股票即買進。
  * 如果預測結果相同，則不做動作。
