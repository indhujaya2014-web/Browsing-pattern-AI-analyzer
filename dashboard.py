import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide")
st.title("🚀 Browsing Behavior Analytics Dashboard")

# LOAD DATA
@st.cache_data
def load_data():
    hist = pd.read_csv("browsing_history.csv")
    ram = pd.read_csv("ram_log.csv")
    domain_map = pd.read_csv("domain_category_map.csv")

    hist["timestamp"] = pd.to_datetime(hist["timestamp"])
    ram["timestamp"] = pd.to_datetime(ram["timestamp"])

    hist = hist.merge(domain_map, on="domain", how="left")
    hist["category"].fillna("other", inplace=True)

    return hist, ram

hist, ram = load_data()

# TIME FEATURES
hist["hour"] = hist["timestamp"].dt.hour
hist["day"] = hist["timestamp"].dt.day_name()

# SESSIONIZATION
hist = hist.sort_values("timestamp")
hist["time_diff"] = hist["timestamp"].diff().fillna(pd.Timedelta(seconds=0))
hist["new_session"] = hist["time_diff"] > pd.Timedelta(minutes=15)
hist["session_id"] = hist["new_session"].cumsum()

session_lengths = hist.groupby("session_id").size()

# MERGE RAM
merged = pd.merge_asof(
    hist.sort_values("timestamp"),
    ram.sort_values("timestamp"),
    on="timestamp",
    direction="nearest"
)

# LAYOUT
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Behavior", "💻 RAM", "🧠 ML Insights", "💡 Recommendations"
])

# 📊 TAB 1 — BEHAVIOR ANALYTICS
with tab1:
    st.subheader("📊 Overview")
    col1s, col2s = st.columns(2)

    col1s.metric("Total Visits", len(hist))
    col2s.metric("Unique Domains", hist["domain"].nunique())

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🌐 Top Domains")
        st.bar_chart(hist["domain"].value_counts().head(10))

    with col2:
        st.subheader("📊 Top Categories")
        st.bar_chart(hist["category"].value_counts().head(10))

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("⏰ Hourly Usage")
        st.line_chart(hist.groupby("hour").size())

    with col4:
        st.subheader("📅 Day-wise Usage")
        st.bar_chart(hist["day"].value_counts())

    st.subheader("📈 Session Length Distribution")
    fig, ax = plt.subplots()
    sns.histplot(session_lengths, bins=20, ax=ax)
    st.pyplot(fig)

# 💻 TAB 2 — RAM ANALYTICS
with tab2:
    st.subheader("📊 Ram Overview")
    col1s, col2s = st.columns(2)

    col1s.metric("Avg RAM (MB)", int(ram["browser_ram_mb"].mean()))
    col2s.metric("Peak RAM (MB)", int(ram["browser_ram_mb"].max()))

    st.subheader("💻 RAM Usage Over Time")
    st.line_chart(ram[["ram_used_mb","browser_ram_mb"]])

    st.subheader("📊 Category-wise RAM Usage")

    cat_ram = merged.groupby("category")["browser_ram_mb"].mean().sort_values(ascending=False)
    st.bar_chart(cat_ram)

    st.subheader("📉 RAM vs Session Length")

    session_ram = merged.groupby("session_id")["browser_ram_mb"].mean()
    df_plot = pd.DataFrame({
        "session_length": session_lengths,
        "avg_ram": session_ram
    })

    fig, ax = plt.subplots()
    sns.scatterplot(x="session_length", y="avg_ram", data=df_plot, ax=ax)
    st.pyplot(fig)

# 🧠 TAB 3 — ML INSIGHTS
with tab3:

    st.subheader("🔹 Session Clustering")

    from sklearn.preprocessing import StandardScaler
    from sklearn.cluster import KMeans

    features = merged.groupby("session_id").agg({
        "hour":"mean",
        "category":"count",
        "browser_ram_mb":"mean"
    })

    scaler = StandardScaler()
    X = scaler.fit_transform(features)

    kmeans = KMeans(n_clusters=4, random_state=42)
    features["cluster"] = kmeans.fit_predict(X)

    fig, ax = plt.subplots()
    sns.scatterplot(
        x=features["hour"],
        y=features["browser_ram_mb"],
        hue=features["cluster"],
        palette="viridis",
        ax=ax
    )
    st.pyplot(fig)

    st.subheader("🚨 Anomaly Detection")

    from tensorflow.keras.models import Model
    from tensorflow.keras.layers import Input, Dense

    X = features.drop("cluster", axis=1)

    inp = Input(shape=(X.shape[1],))
    encoded = Dense(8, activation='relu')(inp)
    decoded = Dense(X.shape[1], activation='linear')(encoded)

    autoencoder = Model(inp, decoded)
    autoencoder.compile(optimizer='adam', loss='mse')
    autoencoder.fit(X, X, epochs=5, verbose=0)

    recon = autoencoder.predict(X)
    mse = np.mean((X - recon)**2, axis=1)

    features["anomaly_score"] = mse

    st.write("Top Anomalous Sessions")
    st.dataframe(features.sort_values("anomaly_score", ascending=False).head())

# 💡 TAB 4 — RECOMMENDATIONS
with tab4:

    st.subheader("💡 Smart Recommendations")

    recs = []

    late_night = hist[(hist["hour"] > 22) & (hist["category"] == "social")]
    if len(late_night) > 20:
        recs.append("🌙 Reduce late-night social media usage")

    high_ram = merged.groupby("category")["browser_ram_mb"].mean().sort_values(ascending=False).head(3)

    for cat in high_ram.index:
        recs.append(f"💻 '{cat}' category uses high RAM")

    if len(recs) == 0:
        st.success("✅ Healthy browsing behavior detected")
    else:
        for r in recs:
            st.warning(r)
