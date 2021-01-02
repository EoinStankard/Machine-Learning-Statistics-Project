# flask for web app.
import flask as fl
# numpy for numerical work.
import numpy as np
import tensorflow as tf
from tensorflow import keras as kr
import sklearn.preprocessing as pre
import sklearn.model_selection as mod
import pandas as pd

# Create a new web app.
app = fl.Flask(__name__)

# Add root route.
@app.route("/")
def home():
  return app.send_static_file('power.html')

# Add uniform route.
@app.route('/api/predict')
def turbinePower():
  df = pd.read_csv("powerproduction.csv")
  inputs_train, inputs_test, outputs_train, outputs_test = mod.train_test_split(df['speed'], df['power'], test_size=0.2)
  model = kr.models.Sequential()
  model.add(kr.layers.Dense(50, input_shape=(1,), activation='sigmoid', kernel_initializer="glorot_uniform", bias_initializer="glorot_uniform"))
  model.add(kr.layers.Dense(1, activation='linear', kernel_initializer="glorot_uniform", bias_initializer="glorot_uniform"))
  model.compile(kr.optimizers.Adam(lr=0.001), loss='mean_squared_error')
  model.fit(inputs_train, outputs_train, epochs=500)
  print("%.2f" %model.predict([5]))
  s = float(model.predict([8.238]))
  print(s)
  #np.random.uniform()
  return {"value": s}
