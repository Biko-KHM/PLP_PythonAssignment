# analysis.py
# Data preprocessing for CORD-19 metadata
# Bikila Keneni

import pandas as pd

def load_and_clean(path="data/metadata.csv", nrows=None, save_path="data/cleaned_metadata.csv"):
    print("Loading data...")
    df = pd.read_csv(path, nrows=nrows, low_memory=False)

    print("Initial shape:", df.shape)
    print(df.info())

    # Convert publish_time to datetime
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors="coerce")
    df['year'] = df['publish_time'].dt.year

    # Fill missing values
    df['journal'] = df['journal'].fillna("Unknown")
    df['title'] = df['title'].fillna("")
    df['abstract'] = df['abstract'].fillna("")

    # Abstract word count
    df['abstract_word_count'] = df['abstract'].apply(lambda x: len(x.split()))

    # Save cleaned version for Streamlit app
    df.to_csv(save_path, index=False)
    print(f"✅ Cleaned data saved to {save_path}")
    print("Preview after cleaning:")
    print(df[['year', 'abstract_word_count']].head())

    return df

if __name__ == "__main__":
    load_and_clean()
