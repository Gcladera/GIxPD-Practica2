import os

from flask import Flask, request
import numpy as np
import joblib

MODEL_PATH = env_var = os.environ["MODEL_PATH"]

mymodel = joblib.load(MODEL_PATH)

app = Flask(__name__)

app.run(host="0.0.0.0", port=5000)
@app.route("/")
def model_documentation():
    return """
<h1>Welcome to customer spent prediction model</h1>

<p>Please use our api to use the model:</p>
<p>curl localhost:5000/model?minutes=5</p>
"""


@app.route("/model")
def model():
	minutes = request.args.get('minutes')
	minutes_valor = np.array([[int(minutes)]])
	spent = mymodel.predict(minutes_valor)
	return {"spent": spent[0][0]}
