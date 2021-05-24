from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json
import lightgbm as lgb
import shap
import pandas as pd

app = Flask(__name__)

def good_input(X, col_names):
    #print(len(X[0]), len(col_names), X[0], min(X[0]))
    if len(X[0]) != len(col_names):
        return False
    elif None in X[0]:
        return False
    elif min(X[0]) < 0:
        return False
    else:
        return True


@app.route('/voa-api/', methods=['POST'])
def evalmodel():
    X = request.get_json()
    if good_input(X,col_names):
        X_df = pd.DataFrame(X, columns=col_names).astype(schema)
        prediction = np.array2string(gbm.predict(X_df)[0])
        shap_values = explainer.shap_values(X_df)
        result = {}
        result['predicted_rv'] = prediction
        result['shap_values'] = { c:shap_values[0][i] for i,c in enumerate(col_names) }
        return jsonify(result)
    else:
        return {'message': "the data failed validation checks"}, 400

if __name__ == '__main__':
    model_path = 'models/'
    #modelfile = 'models/model.txt'
    gbm = lgb.Booster(model_file=model_path+'model.txt')
    if 'objective' not in gbm.params:
        gbm.params['objective'] = 'regression'
        
    # read schema and build dataframe for prediction
    # with open(model_path+'X_column_names', 'rb') as fp:
    #     col_names = p.load(fp)
    #     print(col_names)
    # with open(model_path+'X_column_types', 'rb') as fp:
    #     col_types = p.load(fp)
    with open('models/X_column_names.json', 'r') as fp:
        col_names = json.load(fp)
    with open('models/X_column_types.json', 'r') as fp:
        col_types = json.load(fp)
    schema = {c: col_types[i] for i, c in enumerate(col_names)}

    
    explainer = shap.TreeExplainer(gbm)
    app.run(debug=True)