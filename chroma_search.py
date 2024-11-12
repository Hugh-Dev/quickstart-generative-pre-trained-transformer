import csv
from sentence_transformers import SentenceTransformer
import chromadb
import pandas as pd

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

client = chromadb.Client()
collection = client.create_collection("youtube_videos")

df = pd.read_csv('channel_videos.csv')
df['embedding'] = df['title'].apply(lambda x: model.encode(x))
videos = df.to_dict(orient='records')

for video in videos:
    collection.add(
        ids=[video['url']],
        documents=[video['title']],
        embeddings=[video['embedding']],
        metadatas=[{'title': video['title'], 'url': video['url']}]
    )

def search_videos(query):
    query_embedding = model.encode(query)
    results = collection.query(query_embeddings=[query_embedding], n_results=1)
    metadatas = results['metadatas'][0]
    df = pd.DataFrame(metadatas)
    return df

query = input("keywords: ")
matching_videos = search_videos(query)
print(matching_videos)
