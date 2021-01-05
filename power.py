# https://linuxize.com/post/python-check-if-file-exists/

# flask for web app.
import flask as fl
# numpy for numerical work.
import numpy as np
import tensorflow as tf
from tensorflow import keras as kr
import pandas as pd
from pathlib import Path

# Create a new web app.
app = fl.Flask(__name__)

# Add root route.
@app.route("/")
def home():
  return app.send_static_file('power.html')

# Add uniform route.
@app.route('/api/predict/<speed>')
def turbinePower(speed):
    modelSaved = kr.models.load_model('powerProductionModel.h5')
    #print("£££££££££££££££££££££££££  SPEED: ", float(speed))
    ss = float(speed)
    print("SPEED: ",ss)
    s = float(modelSaved.predict([ss]))
    if ss > 0.0 and ss < 25 and s > 0:
      print("PREDICTED: ",s)
      return {"value": s}
    else:
      return {"value": 0}

def createModel():
  if Path('powerProductionModel.h5').is_file():
    print ("File exist")
  else:
    df = pd.read_csv("powerproduction.csv")
    inputs_train, inputs_test, outputs_train, outputs_test = mod.train_test_split(df['speed'], df['power'], test_size=0.2)
    model = kr.models.Sequential()
    model.add(kr.layers.Dense(50, input_shape=(1,), activation='sigmoid', kernel_initializer="glorot_uniform", bias_initializer="glorot_uniform"))
    model.add(kr.layers.Dense(1, activation='linear', kernel_initializer="glorot_uniform", bias_initializer="glorot_uniform"))
    model.compile(kr.optimizers.Adam(lr=0.001), loss='mean_squared_error')
    model.fit(inputs_train, outputs_train, epochs=500)
    model.save('powerProductionModel.h5')
    #s = float(model.predict([8.238]))

createModel()