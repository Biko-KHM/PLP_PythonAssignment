# app.py
# Streamlit app to explore CORD-19 metadata
# Bikila Keneni

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

st.set_page_config(page_title="CORD-19 Explorer", layout="wide")

@st.cache_data
def load_data(path="data/cleaned_metadata.csv", nrows=None):
    df = pd.read_csv(path, nrows=nrows, low_memory=False)
    # Ensure datetime/year in case file is pre-cleaned
    if "publish_time" in df.columns:
        df['publish_time'] = pd.to_datetime(df['publish_time'], errors="coerce")
        df['year'] = df['publish_time'].dt.year
    return df

st.title("📊 CORD-19 Data Explorer")
st.write("Interactive dashboard for COVID-19 research metadata")

# Load data
df = load_data("data/cleaned_metadata.csv")

# Sidebar filters
st.sidebar.header("Filters")
if not df['year'].dropna().empty:
    min_year = int(df['year'].min())
    max_year = int(df['year'].max())
else:
    min_year, max_year = 2019, 2022

year_range = st.sidebar.slider("Select year range", min_year, max_year, (min_year, max_year))

journal_list = df['journal'].value_counts().head(15).index.tolist()
selected_journal = st.sidebar.selectbox("Filter by journal", ["All"] + journal_list)

# Apply filters
filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]
if selected_journal != "All":
    filtered = filtered[filtered['journal'] == selected_journal]

# Show filtered data
st.subheader("📑 Sample Data")
st.dataframe(filtered[['title', 'journal', 'publish_time']].head(20))

# Publications per year
st.subheader("📈 Publications per Year")
year_counts = filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values, color="#f97316")
ax.set_xlabel("Year")
ax.set_ylabel("Count")
st.pyplot(fig)

# Top journals
st.subheader("🏛️ Top Journals")
top_j = filtered['journal'].value_counts().head(10)
fig2, ax2 = plt.subplots()
sns.barplot(x=top_j.values, y=top_j.index, ax=ax2, palette="flare")
ax2.set_xlabel("Publications")
ax2.set_ylabel("Journal")
st.pyplot(fig2)

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
