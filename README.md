# 🎧 YouTube / Podcast Summarizer

An NLP-powered web app to extract transcripts, highlight top keywords, and generate clean extractive summaries from **YouTube videos** — all using classical NLP and **Word2Vec**.

Built with **Streamlit**, **NLTK**, and **Gensim**, this project is ideal for summarizing long-form content like podcasts, interviews, and lectures without deep learning.

---

## ✨ Features

- 🔗 Paste any YouTube video URL  
- 📜 Auto-fetches and cleans transcript  
- 🔑 Extracts top semantic keywords using Word2Vec  
- 📝 Generates a sentence-level extractive summary  
- ⬇️ Downloadable transcript and summary files  
- 🎛 Adjustable keyword & summary depth sliders  

---

## 🧠 Tech Stack

| Layer        | Tech                                |
|--------------|--------------------------------------|
| Interface    | `streamlit`                          |
| NLP & Vectors| `gensim`, `nltk`, `sklearn`          |
| Transcripts  | `youtube-transcript-api`             |
| Model        | `word2vec-google-news-300` (via `gensim.downloader`) |

---

## 📂 Folder Structure

```

├── app.py                # Streamlit UI
├── downloader.py         # YouTube transcript fetcher
├── utils.py              # Cleaning & preprocessing
├── keyword\_extractor.py  # Word2Vec-based keyword scoring
├── summarizer.py         # Extractive summarizer
├── requirements.txt

````

---

## ⚠️ Word2Vec Model Note

The project uses the **Google News Word2Vec** model (`~1.5 GB` uncompressed).  
It is automatically downloaded using:

```python
from gensim.downloader import load
model = load("word2vec-google-news-300")
````

✅ You don’t need to manually download it — the app will cache it locally on first use.

---

## 💻 How to Run Locally

1. **Clone the repo:**

```bash
git clone https://github.com/your-username/youtube-podcast-summarizer.git
cd youtube-podcast-summarizer
```

2. **Create virtual environment:**

```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
```

3. **Install requirements:**

```bash
pip install -r requirements.txt
```

4. **Run Streamlit app:**

```bash
streamlit run app.py
```

---

## 📦 Requirements

* Python 3.8+
* Internet access (for transcript + model download)

---

## 🔮 Future Improvements

* [ ] Upload `.txt` transcript manually
* [ ] Add GloVe / TF-IDF as keyword options
* [ ] WordCloud or bar chart for keyword importance
* [ ] Chatbot interface for QA on transcript
* [ ] Whisper support for audio files

---

## 📚 Related Projects

* [Resume Ranking System](https://github.com/frogface539/AI-Powered-Resume-Ranking-System)

---

## 📜 License

MIT © 2025 Lakshay Jain

