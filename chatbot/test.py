import json
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import load_model
import unittest

class TestChatbot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Cargar el modelo, vectorizador y clases una vez antes de todas las pruebas."""
        cls.model = load_model('chatbot_model.h5')
        cls.classes = np.load('classes.npy')
        with open('vectorizer.pkl', 'rb') as f:
            cls.vectorizer = pickle.load(f)
        cls.label_encoder = LabelEncoder()
        cls.label_encoder.classes_ = cls.classes

    def predict_class(self, sentence):
        x = self.vectorizer.transform([sentence])
        predictions = self.model.predict(x.toarray())
        class_idx = np.argmax(predictions)
        class_label = self.label_encoder.inverse_transform([class_idx])[0]
        return class_label

    def test_intents(self):
        """Probar cada intent en el archivo intents.json."""
        with open('intents.json', 'r', encoding='utf-8') as file:
            intents = json.load(file)
        
        errors = []
        for intent in intents['intents']:
            tag = intent['tag']
            patterns = intent['patterns']
            found_match = False
            for pattern in patterns:
                predicted_tag = self.predict_class(pattern)
                if predicted_tag == tag:
                    found_match = True
                    break
            if not found_match:
                errors.append(f"El intent '{tag}' no se reconoció correctamente con los patrones proporcionados.")
        
        if errors:
            self.fail("\n".join(errors))

if __name__ == "__main__":
    unittest.main()
