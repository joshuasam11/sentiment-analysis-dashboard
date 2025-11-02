# sentiment-analysis-dashboard
Streamlit app for analyzing and visualizing customer sentiment from reviews.

💬 Sentiment Analysis Dashboard

This project is a **Streamlit-based Sentiment Analysis App** that visualizes customer review sentiments.  
It converts review ratings into **Positive**, **Neutral**, or **Negative** sentiments and displays them using interactive charts.

🚀 Features
- Upload your own Excel dataset (must contain a `rating` column)
- Filter reviews by rating
- View rating and sentiment distribution with visual charts
- Clean and interactive Streamlit dashboard

⚙️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/sentiment-analysis-dashboard.git
   cd sentiment-analysis-dashboard

2.Create a virtual environment and activate it:
python -m venv .venv
.venv\Scripts\activate      # On Windows
source .venv/bin/activate   # On Mac/Linux

3.Install required packages:
pip install -r requirements.txt

4.Run the app:
streamlit run app.py

📊 Sentiment Mapping

Rating	  Sentiment

4–5	         Positive

3	           Neutral

1–2	         Negative
