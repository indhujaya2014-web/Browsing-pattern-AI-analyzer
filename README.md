# Time-Based Browsing Pattern Analyzer using Deep Learning with RAM Usage Correlation 🧠💻  
An intelligent system designed to analyze browser history and correlate digital habits with system performance. This tool extracts data from local SQLite databases, categorizes web activity, clusters user sessions, and utilizes Deep Learning to identify anomalies and predict future behavior.  
## Features
  # Data Collection  
    > Browser history extraction from SQLite (Chrome/Edge)
    > RAM monitoring using psutil every 5 seconds
  # Data Processing
    > URL cleaning and domain extraction
    > Domain → category mapping
    > Sessionization using inactivity threshold (15 minutes)
  # Behavior Analytics
    > Hourly and day-wise browsing patterns
    > Category distribution
    > Session feature engineering
  # Unsupervised Learning
    Session clustering using:
    > KMeans
    > Feature scaling
    > Behavioral feature vectors
  # Deep Learning Options
    1. LSTM Next Category Predictor
    2. Autoencoder Anomaly Detection
  # RAM Correlation Analysis
    > Memory usage per browsing category
    > Peak and mean browser RAM
  # Recommendation Engine
    Generates actionable insights such as:
    > Late night social media alerts
    > Memory heavy websites
    > Productivity recommendations
## 🛠️ Tech Stack
- **Languages**: Python 3.9+
- **Data**: Pandas, SQLite, NumPy
- **ML/DL**: Scikit-Learn, TensorFlow/Keras
- **Monitoring**: Psutil (System metrics)
- **UI**: Streamlit (Optional Dashboard)
