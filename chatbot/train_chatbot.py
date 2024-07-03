import json
import pickle
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping

# Cargar el archivo intents.json
with open('intents.json', 'r', encoding='utf-8') as file:
    intents = json.load(file)

# Preprocesamiento de datos
training_data = []
training_labels = []
responses = {}

for intent in intents['intents']:
    for pattern in intent['patterns']:
        training_data.append(pattern)
        training_labels.append(intent['tag'])
    responses[intent['tag']] = intent['responses']

# Convertir training_labels a valores numéricos usando LabelEncoder
label_encoder = LabelEncoder()
encoded_labels = label_encoder.fit_transform(training_labels)

# Vectorización del texto usando TfidfVectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(training_data)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, encoded_labels, test_size=0.2, random_state=42)

# Crear modelo secuencial de Keras
model = Sequential([
    Dense(128, input_shape=(X.shape[1],), activation='relu'),
    Dropout(0.5),
    Dense(64, activation='relu'),
    Dropout(0.5),
    Dense(len(label_encoder.classes_), activation='softmax')
])

# Compilar el modelo
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Early stopping para prevenir overfitting
early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

# Entrenar el modelo
model.fit(X_train.toarray(), y_train, epochs=100, batch_size=8, verbose=1, validation_data=(X_test.toarray(), y_test), callbacks=[early_stopping])

# Guardar el modelo y otros artefactos necesarios
model.save('chatbot_model.h5')
np.save('classes.npy', label_encoder.classes_)
with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

print("Entrenamiento completado y modelos guardados.")
