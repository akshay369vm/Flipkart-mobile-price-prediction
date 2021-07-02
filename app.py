
from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd




app = Flask(__name__)

model=pickle.load(open("flipkart_price_prediction.pkl",'rb'))
df=pd.read_csv('flipkart_mobile_detals.csv')

#result=model.predict(pd.DataFrame(columns=['Name', 'RAM', 'ROM', 'Extended_memory', 'Battery', 'Processor'], data=np.array(['POCO M3', 4, 64, 256, 5000, 'Qualcomm Snapdragon 662 Processor']).reshape(1,6)))
#print(result)
      
      
@app.route('/')
def home():
    Names=sorted(df['Name'].unique())
    Processors=sorted(df['Processor'].unique())
    return render_template('home.html', Names=Names, Processosr=Processors)



@app.route('/predict', methods=['POST'])
def predict():
    Name = str(request.form.get('Name'))
    RAM = int(request.form.get('RAM'))
    ROM = int(request.form.get('ROM'))
    Extended_memory = int(request.form.get('Extended_memory'))
    Battery = int(request.form.get('Battery'))
    Processor = str(request.form.get('Processor'))
    
    prediction=model.predict(pd.DataFrame(columns=['Name', 'RAM', 'ROM', 'Extended_memory', 'Battery', 'Processor'],
                              data=np.array([Name, RAM, ROM, Extended_memory, Battery, Processor]).reshape(1, 6)))
    
    print(prediction)
    return flask.render_template('home.html', result=prediction)

if __name__ == "__main__":
    app.run(debug=False)





