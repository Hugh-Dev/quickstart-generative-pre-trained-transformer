import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import time
import sys

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

dataset_title_videos = pd.read_csv('channel_videos.csv')  # Load the dataset

channel_videos = dataset_title_videos['title'].tolist()
channel_videos_embeddings = model.encode(channel_videos)

def search_titles(query, k=1):
    query_embedding = model.encode([query])
    similarities = cosine_similarity(query_embedding, channel_videos_embeddings)
    indices = similarities.argsort()[0][-k:][::-1]
    similar_titles = dataset_title_videos.iloc[indices]
    return similar_titles

query = input("keywords: ")
result = search_titles(query, k=1)

print("Most relevant titles\n")
for char in str(result):
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)
