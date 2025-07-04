from gensim.downloader import load
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from utils import clean_text

def load_word2vec():
    print("[INFO] Loading Word2Vec model (300d)...")
    return load("word2vec-google-news-300")

def extract_keywords_word2vec(text, model, top_n=10):
    words = list(set(text.split()))
    word_vectors = []
    valid_words = []

    for word in words:
        if word in model:
            vec = model[word]
            word_vectors.append(vec)
            valid_words.append(word)
        
    if not word_vectors:
        return []
        
    word_vectors = np.array(word_vectors)
    avg_vector = np.mean(word_vectors, axis=0).reshape(1,-1)

    similarities = cosine_similarity(word_vectors,avg_vector).flatten()
    distances = 1 - similarities

    ranked = sorted(zip(valid_words, distances), key=lambda x: x[1], reverse=True)
    top_keywords = [word for word, score in ranked[:top_n]]
    return top_keywords 
    

    ## Testing
# if __name__ == "__main__":
#     raw_text = """
#     Artificial intelligence and machine learning are transforming the world.
#     Technologies like GPT-4, neural networks, and reinforcement learning are becoming mainstream.
#     """
#     cleaned = clean_text(raw_text)
#     model = load_word2vec()
#     keywords = extract_keywords_word2vec(cleaned, model, top_n=5)
#     print("\nTop Keywords:\n", keywords)

