import streamlit as st
import time
import re
from downloader import fetch_transcript
from utils import clean_text
from keyword_extractor import load_word2vec, extract_keywords_word2vec
from summarizer import summarize_by_keywords

st.set_page_config(page_title="🎧 YouTube Summarizer", layout="centered")
st.title("🎧 YouTube / Podcast Summarizer")

st.markdown(""" 
Paste a YouTube link to extract the transcript, highlight top keywords, and generate a clean extractive summary using NLP + Word2Vec.
""")

st.markdown("---")

# Input
st.subheader("🔗 Enter YouTube Video URL")
video_url = st.text_input("Paste the YouTube video link here:")

st.markdown("")

# Sliders
st.subheader("⚙️ Customize Settings")
col1, col2 = st.columns(2)
with col1:
    top_n_keywords = st.slider("🎯 Top Keywords", 5, 20, 10)
with col2:
    top_n_sentences = st.slider("📝 Summary Sentences", 3, 15, 5)

st.markdown("")

# Summarize button
if st.button("🔍 Run Summarizer"):
    if not video_url:
        st.warning("Please paste a valid YouTube video URL.")
        st.stop()

    # Fetch transcript
    with st.spinner("🔄 Fetching transcript from YouTube..."):
        try:
            raw_transcript = fetch_transcript(video_url)
            raw_transcript = re.sub(r'(?<![.?!])\n', ' ', raw_transcript)
            raw_transcript = re.sub(r'\s{2,}', ' ', raw_transcript)
        except Exception as e:
            st.error(f"❌ Error: {e}")
            st.stop()

    st.success("✅ Transcript fetched successfully.")
    st.markdown("---")

    # Show transcript in expander
    with st.expander("📜 Full Transcript"):
        st.text_area("Transcript", raw_transcript, height=300)

    # Clean text
    cleaned = clean_text(raw_transcript)

    # Load model
    with st.spinner("⚙️ Loading model (may take a moment)..."):
        start = time.time()
        model = load_word2vec()
        st.caption(f"✅ Model loaded in {time.time() - start:.2f} seconds.")

    # Extract keywords
    keywords = extract_keywords_word2vec(cleaned, model, top_n=top_n_keywords)

    if not keywords:
        st.warning("⚠️ No keywords found. Transcript may be too short or noisy.")
        st.stop()

    # Show keywords
    st.markdown("### 🔑 Top Keywords")
    st.markdown(" ".join([f"`{kw}`" for kw in keywords]))

    st.markdown("---")

    # Summarize
    summary = summarize_by_keywords(raw_transcript, keywords, top_n=top_n_sentences)

    st.markdown("### 📝 Extractive Summary")
    if not summary:
        st.warning("⚠️ Couldn't generate summary. Try adjusting keyword count.")
    else:
        for i, sent in enumerate(summary, 1):
            st.markdown(f"**{i}.** {sent}")

        st.markdown("")

        # Downloads
        st.download_button("⬇️ Download Cleaned Transcript", cleaned.encode(), "transcript_cleaned.txt")
        st.download_button("⬇️ Download Summary", "\n".join(summary).encode(), "summary.txt")

    st.markdown("---")
    st.success("✅ All done! Scroll up to view the full summary and keywords.")
