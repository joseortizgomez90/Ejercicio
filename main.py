from flask import Flask, jsonify, request,g
import pickle
import psycopg2
import os
import pandas as pd 
from sklearn.metrics import mean_squared_error



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
@app.route('/api/v1/predict/', methods=['POST'])
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
    
    # Definimos la ruta para el endpoint /api/v1/retrain
@app.route('/api/v1/retrain', methods=['POST'])
def retrain():
    # Obtenemos los nuevos datos de entrenamiento del cuerpo de la solicitud POST
    new_data = request.get_json()
    X_new = pd.DataFrame.from_dict(new_data['X'])
    y_new = pd.Series(new_data['y'])

    # Cargamos el modelo existente
    loaded_model = pickle.load(open('model.pkl', 'rb'))

    # Entrenamos el modelo con los nuevos datos
    loaded_model.fit(X_new, y_new)

    # Guardamos el modelo actualizado
    pickle.dump(loaded_model, open('model.pkl', 'wb'))

    # Calculamos la métrica de evaluación MSE con los datos de prueba originales
    X_test = pd.DataFrame.from_dict(new_data['X_test'])
    y_test = pd.Series(new_data['y_test'])
    y_pred = loaded_model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)

    # Retornamos la métrica de evaluación MSE en formato Json
    return jsonify({'mse': mse})
    
    
    
    
    
# Realizamos la predicción
    prediction = loaded_model.predict([new_data])
    # Retornamos la predicción en formato JSON
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
     app.run(debug=True)
    
    
    
    
    
    
    
  