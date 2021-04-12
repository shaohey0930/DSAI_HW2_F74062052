# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 21:46:54 2021

@author: h8273
"""
if __name__ == '__main__':
    # You should not modify this part, but additional arguments are allowed.
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--training',
                       default='training_data.csv',
                       help='input training data file name')
    
    parser.add_argument('--testing',
                        default='testing_data.csv',
                        help='input testing data file name')

    parser.add_argument('--output',
                        default='output.csv',
                        help='output file name')
    args = parser.parse_args()


import numpy as np
import pandas as pd
from statsmodels.tsa.arima_model import ARIMA

# load data
df_training = pd.read_csv(args.training, header = None)
df_testing = pd.read_csv(args.testing, header = None)
data = np.array(df_training)[:, 0]
test_data = np.array(df_testing)[:, 0]
data = np.append(data, test_data[0])
training_data = data[-80:]
test_data = test_data[1:]
#%%
history = [x for x in training_data]
model_predictions = []
N_test_observations = len(test_data)

decision = []
holding = 0
for time_point in range(N_test_observations):
    model = ARIMA(history, order=(4,1,0))
    model_fit = model.fit(disp=0)
    output = model_fit.forecast()
    yhat = output[0]
    if yhat > history[-1]:
        if holding != -1:
            decision.append(-1)
            holding -= 1
        else:
            decision.append(0)
    elif yhat < history[-1]:
        if holding != 1:
            decision.append(1)
            holding += 1
        else:
            decision.append(0)
    else:
        decision.append(0)
    model_predictions.append(yhat)
    true_test_value = test_data[time_point]
    history.append(true_test_value)

#%%
decision = np.array(decision)
output = pd.DataFrame(decision)
output.to_csv(args.output, index = 0, header= None)

















