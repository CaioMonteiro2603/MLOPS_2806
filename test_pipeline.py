import pandas as pd 
import joblib
import os
from sklearn.metrics import accuracy_score

def test_placeholder():
    assert os.path.exists("./model.joblib"), "Modelo não encontrado"
    assert os.path.exists("./vectorizer.joblib"), "vetor não encontrado"

def test_vectorizer_output_shape():
    vectorizer = joblib.load("./vectorizer.joblib")
    sample = ["Este é um ótimo produto!"]
    vetor = vectorizer.transform(sample)
    assert vetor.shape[0] == 1, "Vetor retornou de forma incorreta"

def test_model_prediction_labels():
    model = joblib.load("./model.joblib")
    vectorizer = joblib.load("./vectorizer.joblib")
    sample = ["O serviço foi péssimo"]
    vetor = vectorizer.transform(sample)
    pred = model.predict(vetor)[0]
    assert pred in ["positivo", "negativo"], f"Rotulo inesperado {pred}"

def test_data_validation():
    df = pd.read_csv("./data/tweet_limpo.csv")
    assert "text" in df.columns and "label" in df.columns
    assert df["text"].notnull().all()
    assert df["label"].isin(["positivo", "negativo"]).all()