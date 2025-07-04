import nltk
from nltk.tokenize import sent_tokenize
from utils import clean_text
from keyword_extractor import load_word2vec, extract_keywords_word2vec
from utils import clean_text

nltk.download('punkt')

def summarize_by_keywords(transcript: str, keywords: list, top_n=5) -> list:

    sentences = sent_tokenize(transcript)
    scored = []

    for sentence in sentences:
        cleaned = clean_text(sentence)
        score = sum(1 for word in cleaned.split() if word in keywords)
        scored.append((sentence, score)) 

    # Sort by score (descending), then preserve order
    top_sentences = sorted(scored, key=lambda x: x[1], reverse=True)[:top_n]

    # Re-sort to keep original transcript order
    top_sentences.sort(key=lambda x: sentences.index(x[0]))
    return [s for s, _ in top_sentences]


## Testing
# if __name__ == "__main__":
#     text = """
#     Artificial intelligence is reshaping industries. Tools like GPT and neural networks are growing fast.
#     Reinforcement learning plays a key role in real-world decision making.
#     Many people are becoming interested in AI safety and interpretability.
#     """

#     cleaned = clean_text(text)
#     model = load_word2vec()
#     keywords = extract_keywords_word2vec(cleaned, model, top_n=5)
#     print("Top Keywords:", keywords)

#     summary = summarize_by_keywords(text, keywords, top_n=2)
#     print("\nSummary:")
#     for i, sentence in enumerate(summary, 1):
#         print(f"{i}. {sentence}")
