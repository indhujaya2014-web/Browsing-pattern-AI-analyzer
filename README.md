# Time-Based Browsing Pattern Analyzer using Deep Learning with RAM Usage Correlation 🧠💻  
An intelligent system designed to analyze browser history and correlate digital habits with system performance. This tool extracts data from local SQLite databases, categorizes web activity, clusters user sessions, and utilizes Deep Learning to identify anomalies and predict future behavior.  
# 🎯Features
  ## Data Collection  
    > Browser history extraction from SQLite (Chrome/Edge)
    > RAM monitoring using psutil every 5 seconds
  ## Data Processing
    > URL cleaning and domain extraction
    > Domain → category mapping
    > Sessionization using inactivity threshold (15 minutes)
  ## Behavior Analytics
    > Hourly and day-wise browsing patterns
    > Category distribution
    > Session feature engineering
  ## Unsupervised Learning
    Session clustering using:
    > KMeans
    > Feature scaling
    > Behavioral feature vectors
  ## Deep Learning Options
    1. LSTM Next Category Predictor
    2. Autoencoder Anomaly Detection
  ## RAM Correlation Analysis
    > Memory usage per browsing category
    > Peak and mean browser RAM
  ## Recommendation Engine
    Generates actionable insights such as:
    > Late night social media alerts
    > Memory heavy websites
    > Productivity recommendations  
    
# 📂 Project Structure  
├── Project_doc/  
│   ├── browsing_pattern_sample_1lac  
│   ├── DS105_Final_Project  
│   ├── info_graphics  
├── data/  
│   ├── browsing_history.csv     # Extracted Browser History  
│   ├── ram_logs.csv             # System Performance Logs  
│   ├── domain_category_map.csv  # Domain category mapped
├── report/
│   ├── final_report.pdf         # Final project report in pdf 
├── notebooks/  
│   ├── Browsing_pattern_AI_analyzer.ipynb # Main Analysis & DL Model  
├── ├── dashboard.py             # Streamlit Dashboard code  
├── requirements.txt             # Environment dependencies  
└── README.md  

# 🛠️ Tech Stack
- **Language**: Python 3.10+
- **Data Handling**: Pandas, NumPy, SQLite3
- **System Monitoring**: Psutil (System metrics)
-	**Machine Learning**: Scikit-Learn (K-Means)
-	**Deep Learning**: TensorFlow/Keras (Autoencoders/LSTM)
- **Visualization**: Matplotlib, Plotly, Seaborn, Streamlit(UI Optional Dashboard)

# 📊Output Results  
The system produces:  
•	Top domains and categories  
•	Hourly browsing patterns  
•	Session clusters  
•	RAM usage correlations  
•	Deep learning predictions  
•	Behavior recommendations  

# ⚙️Installation & Setup
## Install dependencies
pip install -r requirements.txt  

## Optional Dashboard
Run Streamlit dashboard:
streamlit run dashboard.py

## Run the extraction and AI analysis
jupyter notebook notebooks/Browsing_pattern_AI_analyzer.ipynb

# 🛡️ Privacy & Security  
•	Local Processing: All SQLite extraction happens locally on your machine.  
•	Data Obfuscation: The system is designed to strip sensitive query strings from URLs before analysis.  
•	Git Safety: The .gitignore file is pre-configured to ensure no .db or .csv files are ever uploaded to public repositories.  

# 📈 Future Scope  
•	Active Tab Tracking: Estimating precise "Focus Time" vs. "Idle Time."  
•	LSTM Integration: Predicting the next category of browsing to nudge the user toward productivity.  
•	Multi-Browser Support: Integrating Firefox and Safari history paths.  

# 👤 Author  
Jayapoorani M  
Data Science Enthusiast  

