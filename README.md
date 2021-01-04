# Machine-Learning-Statistics-Project

## About the Assignment
In this project you must create a web service that uses machine learning to make predictions based on the data set powerproduction available on Moodle. The goal is to
produce a model that accurately predicts wind turbine power output from wind speed values, as in the data set. You must then develop a web service that will respond with
predicted power values based on speed values sent as HTTP requests. Your submission must be in the form of a git repository containing, at a minimum, the following items:

  1. Jupyter notebook that trains a model using the data set. In the notebook you should explain your model and give an analysis of its accuracy.
  2. Python script that runs a web service based on the model, as above.
  3. Dockerfile to build and run the web service in a container.
  4. Standard items in a git repository such as a README.
  
To enhance your submission, you might consider developing and comparing more than one model. Rest assured, all the above concepts will be explored in lecture videos and other materials in the coming semester.


## How to view the Assignment

The assignment can be viewed the following ways

1. Downloading the Repo and running jupyter notebook in the command line. (Recommended)
2. Clicking on the "MLS-Project.ipynb" file above,

I recommend that you download and run the assignment on your own machine as erros may occur when directly clicking on the "MLS-Project.ipynb" file above

## What is needed to run the Assignment

1. Anaconda Python as it contains all libraries
2. The Repo will need to be cloned or downloaded

## How to run on Windows
set FLASK_APP=power.py

python -m flask run
