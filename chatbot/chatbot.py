import json
import numpy as np
import random
import spacy
from tensorflow.keras.models import load_model
from sklearn.feature_extraction.text import CountVectorizer
from flask import Flask, request, jsonify


# Cargar el archivo intents.json
with open('intents.json', 'r', encoding='utf-8') as file:
    intents = json.load(file)

# Cargar artefactos necesarios
model = load_model('chatbot_model.h5')
classes = np.load('classes.npy', allow_pickle=True)
vectorizer = np.load('vectorizer.npy', allow_pickle=True).item()

# Cargar modelo de spaCy en español
nlp = spacy.load('es_core_news_sm')

app = Flask(__name__)

# Función para predecir respuestas del chatbot
def predict_intent(text):
    # Preprocesamiento del texto de entrada
    tokens = nlp(text)
    lemmatized_tokens = [token.lemma_ for token in tokens if not token.is_stop]
    preprocessed_text = " ".join(lemmatized_tokens)
    
    # Vectorización del texto preprocesado
    input_vector = vectorizer.transform([preprocessed_text])
    
    # Predicción usando el modelo entrenado
    predictions = model.predict(input_vector.toarray())
    
    # Obtener la etiqueta predicha
    predicted_label_idx = np.argmax(predictions)
    predicted_label = classes[predicted_label_idx]
    
    # Obtener una respuesta aleatoria del intent correspondiente
    for intent_item in intents['intents']:
        if intent_item['tag'] == predicted_label:
            return random.choice(intent_item['responses'])

# Ruta para la raíz del servicio
@app.route('/')
def index():
    return 'Servicio de Chatbot en funcionamiento'

# Ruta para procesar las solicitudes del chatbot
@app.route('/get_response', methods=['POST'])
def chatbot():
    data = request.get_json()
    user_input = data['message']
    response = predict_intent(user_input)
    return jsonify({'response': response})

# Ejecutar la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)