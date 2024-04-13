import torch
from sentence_transformers import SentenceTransformer


model = SentenceTransformer('all-MiniLM-L6-v2')

def load_model():
    return model

def save_model(model, save_directory="./semantic_search_model"):
    model.save(save_directory)

def embed_text(text):
    return model.encode(text, convert_to_tensor=True)

