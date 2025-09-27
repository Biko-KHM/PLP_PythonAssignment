# app.py
# Streamlit app to explore CORD-19 metadata
# Bikila Keneni

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Streamlit page setup
st.set_page_config(page_title="CORD-19 Explorer", layout="wide")

# Function to load and clean data
@st.cache_data
def load_data(path="data/cleaned_metadata.csv", nrows=None):
    df = pd.read_csv(path, nrows=nrows, low_memory=False)
    # Ensure datetime/year even if file is pre-cleaned
    if "publish_time" in df.columns:
        df['publish_time'] = pd.to_datetime(df['publish_time'], errors="coerce")
        df['year'] = df['publish_time'].dt.year
    df['journal'] = df['journal'].fillna("Unknown")
    df['title'] = df['title'].fillna("")
    return df

# Title and description
st.title("📊 CORD-19 Data Explorer")
st.write("Interactive dashboard for exploring COVID-19 research metadata.")

# ✅ Load data correctly (adds 'year' column automatically)
df = load_data("data/cleaned_metadata.csv")

# Sidebar filters
st.sidebar.header("Filters")

# Handle missing or invalid 'year' values gracefully
if "year" in df.columns and not df['year'].dropna().empty:
    min_year = int(df['year'].min())
    max_year = int(df['year'].max())
else:
    min_year, max_year = 2019, 2022

year_range = st.sidebar.slider("Select year range", min_year, max_year, (min_year, max_year))

# Journal filter
journal_list = df['journal'].value_counts().head(15).index.tolist()
selected_journal = st.sidebar.selectbox("Filter by journal", ["All"] + journal_list)

# Apply filters
filtered = df.copy()
if "year" in df.columns:
    filtered = filtered[(filtered['year'] >= year_range[0]) & (filtered['year'] <= year_range[1])]

if selected_journal != "All":
    filtered = filtered[filtered['journal'] == selected_journal]

# Show filtered data
st.subheader("📑 Sample Data")
if not filtered.empty:
    st.dataframe(filtered[['title', 'journal', 'publish_time']].head(20))
else:
    st.warning("No records found for the selected filters.")

# Publications per year
st.subheader("📈 Publications per Year")
if "year" in filtered.columns and not filtered['year'].dropna().empty:
    year_counts = filtered['year'].value_counts().sort_index()
    fig, ax = plt.subplots()
    ax.bar(year_counts.index, year_counts.values, color="#f97316")
    ax.set_xlabel("Year")
    ax.set_ylabel("Publication Count")
    st.pyplot(fig)
else:
    st.info("No valid 'year' data available to display publication trends.")

# Top journals
st.subheader("🏛️ Top Journals")
if not filtered.empty:
    top_j = filtered['journal'].value_counts().head(10)
    fig2, ax2 = plt.subplots()
    sns.barplot(x=top_j.values, y=top_j.index, ax=ax2, palette="flare")
    ax2.set_xlabel("Publications")
    ax2.set_ylabel("Journal")
    st.pyplot(fig2)
else:
    st.info("No journal data available.")

# Word cloud
st.subheader("☁️ Word Cloud of Titles")
text = " ".join(filtered['title'].astype(str).tolist())
if text.strip():
    wc = WordCloud(width=800, height=300, background_color="white").generate(text)
    fig3, ax3 = plt.subplots()
    ax3.imshow(wc, interpolation="bilinear")
    ax3.axis("off")
    st.pyplot(fig3)
else:
    st.write("No titles available for word cloud.")
