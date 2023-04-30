from flask import Flask, jsonify, request,g
import pickle
import psycopg2

# Instanciamos la clase Flask
app = Flask(__name__)

# Urilizamos decoradores para definir las rutas de nuestro servidor web
# Definimos la ruta principal y el método HTTP que va a escuchar
@app.route('/', methods=['GET'])
def home():
    return """
    <h1>APP para calcular Sales</h1>

    """

# Definimos la ruta para el endpoint /api/v1/predictions
@app.route('/api/v1/predictions', methods=['GET'])
def predictions():
    # Obtenemos los datos de la URL
    TV = request.args['TV']
    radio = request.args['radio']
    newspaper = request.args['newspaper']
    
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


# 2.Ruta para añadir datos

@app.route('/api/v1/retrain', methods=['POST'])
def add_datos():
    # Obtener datos del cuerpo de la petición
    new_data = request.get_json()

    # Almacenar los datos en variables
    TV = new_data['TV']
    radio = new_data['radio']
    newspaper =['newspaper']
    sales= new_data['sales']
   

    # Crear la conexión a la base de datos
    conn = get_Adverstising.csv()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Adverstising.csv (TV,radio,newspaper,sales) VALUES (%s, %s, %s, %s, %s)", (TV,radio,newspaper,sales))
    conn.commit()
    cursor.close()

    return jsonify({'message': 'los datos han sido añadidos correctamente'})

# Realizamos la predicción
    new_prediction = loaded_model.predict([add_datos])
    # Retornamos la predicción en formato JSON
    return jsonify({'prediction': prediction[0]})

    

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
    
    
    
  