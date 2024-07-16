from flask import Flask, render_template, request
import os 
import numpy as np
import pandas as pd
from pricePred.pipeline.prediction import PredictionPipeline


app = Flask(__name__) 


@app.route('/',methods=['GET'])  
def homePage():
    return render_template("index.html")



@app.route('/train',methods=['GET'])  
def training():
    os.system("python main.py")
    return "Training Successful!" 




@app.route('/predict',methods=['POST','GET']) 
def index():
    if request.method == 'POST':
        product_id = 1
        sale = 1
        weight = float(request.form['weight'])
        resolution = float(request.form['resolution'])
        ppi = int(request.form['ppi'])
        cpu_core = int(request.form['cpu_core'])
        cpu_freq = float(request.form['cpu_freq'])
        internal_mem = float(request.form['internal_mem'])
        ram = float(request.form['ram'])
        rear_cam = float(request.form['rear_cam'])
        front_cam = float(request.form['front_cam'])
        battery = int(request.form['battery'])
        thickness = float(request.form['thickness'])


        data = [
            product_id, sale, weight, resolution, ppi,
            cpu_core, cpu_freq, internal_mem, ram,
            rear_cam, front_cam, battery, thickness
        ]
        data = np.array(data).reshape(1, -1)

            
        obj = PredictionPipeline()
        predict = obj.predict(data)
        print(predict)
            
        ans = predict[0]
        ans = f"Rs {ans:.4f}"

        return render_template('results.html', prediction = str(ans))

    else:
        return render_template('index.html')



if __name__ == "__main__":
	app.run(host="0.0.0.0", port = 8080)