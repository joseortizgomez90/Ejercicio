from flask import Flask, jsonify, request,g
import pickle
import psycopg2
import os
import pandas as pd 


# Instanciamos la clase Flask
app = Flask(__name__)



# Urilizamos decoradores para definir las rutas de nuestro servidor web
# Definimos la ruta principal y el método HTTP que va a escuchar
@app.route('/', methods=['GET'])
def home():
    return """
    <h1>APP para calcular Sales</h1>

    """

# Definimos la ruta para el endpoint /api/v1/predict
@app.route('/api/v1/predict/', methods=['GET'])
def predict():
    # Obtenemos los datos de la URL
    TV = float(request.args['TV'])
    radio = float(request.args['radio'])
    newspaper = float(request.args['newspaper'])
    
 # Cargamos el modelo
    loaded_model = pickle.load(open('model.pkl', 'rb'))
    
# El orden de los datos debe ser el mismo que el del modelo
    new_data = [TV, 
                radio, 
                newspaper]
    
# Realizamos la predicción
    prediction = loaded_model.predict([new_data])
    # Retornamos la predicción en formato JSON
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
     app.run(debug=True)
    
    
    
    
    
    
    
  