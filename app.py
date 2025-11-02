import streamlit as st
import pandas as pd
import joblib
from preprocess import clean_text
import plotly.express as px

# --- Page Config ---
st.set_page_config(page_title="Sentiment Dashboard", layout="wide")

# --- Sidebar ---
st.sidebar.title("🎛️ Filters ")
selected_ratings = st.sidebar.multiselect(
    "Show Ratings",
    options=[1, 2, 3, 4, 5],
    default=[1, 2, 3, 4, 5]
)

# --- Main Page ---
st.title("💬 Reviews Sentiment Dashboard")
st.write("Use the filters and upload your dataset to explore review ratings and sentiment distribution.")

# Upload dataset
uploaded_file = st.file_uploader("📂 Upload your dataset (Excel)", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
else:
    st.info("No dataset uploaded. Using default sample file.")
    st.write("Displaying output using sample file -> chatgpt_style_reviews_dataset.")
    st.info("Click -> Show Sentiment Distribution.")
    df = pd.read_excel("chatgpt_style_reviews_dataset.xlsx")

# Filter dataset
df = df[df['rating'].isin(selected_ratings)]

# --- Sentiment Distribution Visualization ---
if st.button("Show Sentiment Distribution"):

    # Map ratings (1–5)
    rating_counts = df['rating'].value_counts().sort_index()
    rating_colors = {
        1: "#8B0000",  # Dark Red
        2: "#FF4500",  # Orange-Red
        3: "#FFD700",  # Yellow
        4: "#90EE90",  # Light Green
        5: "#006400",  # Dark Green
    }

    # Horizontal bar chart for Ratings
    fig_ratings = px.bar(
        x=rating_counts.values,
        y=rating_counts.index.astype(str),
        orientation='h',
        color=rating_counts.index.astype(str),
        color_discrete_map={str(k): v for k, v in rating_colors.items()},
        title="📊 Rating Distribution",
        labels={'x': 'Count', 'y': 'Rating'},
    )
    st.plotly_chart(fig_ratings, use_container_width=True)

    # Convert ratings to sentiment
    df['Sentiment'] = df['rating'].apply(
        lambda x: 'Positive' if x >= 4 else ('Negative' if x <= 2 else 'Neutral')
    )
    sentiment_counts = df['Sentiment'].value_counts()

    sentiment_colors = {
        'Positive': "#008000",  # Green
        'Neutral': "#FFD700",   # Yellow
        'Negative': "#FF0000",  # Red
    }

    # Horizontal bar chart for Sentiments
    fig_sentiment = px.bar(
        x=sentiment_counts.values,
        y=sentiment_counts.index,
        orientation='h',
        color=sentiment_counts.index,
        color_discrete_map=sentiment_colors,
        title="😊 Sentiment Distribution",
        labels={'x': 'Count', 'y': 'Sentiment'},
    )
    st.plotly_chart(fig_sentiment, use_container_width=True)

# --- Footer Section ---
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; padding-top: 10px; color: #000000;">
        <h4>👨‍💻 Developed by <b>Joshua</b></h4>
        <a href="https://www.linkedin.com/in/joshua-samuel11/" target="_blank" style="text-decoration:none; margin-right: 20px;">
            <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/linkedin.svg" width="25" height="25" style="vertical-align:middle; margin-right:5px;">
            LinkedIn
        </a>
        <a href="https://github.com/joshuasam11" target="_blank" style="text-decoration:none;">
            <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/github.svg" width="25" height="25" style="vertical-align:middle; margin-right:5px;">
            GitHub
        </a>
    </div>
    """,
    unsafe_allow_html=True
)