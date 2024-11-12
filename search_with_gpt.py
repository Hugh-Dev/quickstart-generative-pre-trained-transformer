import pandas as pd
import openai
from decouple import config
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from openai import OpenAI
import os

os.environ["TOKENIZERS_PARALLELISM"] = "false"

client = OpenAI(
    api_key=config("OPENAI_API_KEY")
)
dataset_title_videos = pd.read_csv('channel_videos.csv')
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
dataset_title_videos['embedding'] = dataset_title_videos['title'].apply(lambda x: embedding_model.encode(x))

def search_with_rag(query):
    try:
        query_embedding = embedding_model.encode(query).reshape(1, -1)
        embeddings = list(dataset_title_videos['embedding'])
        similarities = cosine_similarity(query_embedding, embeddings).flatten()
        top_indices = similarities.argsort()[-5:][::-1]
        relevant_videos = dataset_title_videos.iloc[top_indices]
        context_text = "\n".join(
            [f"Título: {row['title']}\nURL: {row['url']}" for _, row in relevant_videos.iterrows()]
        )
        prompt = f"Consulta del usuario: '{query}'\n\nA continuación se presentan los videos relevantes:\n{context_text}\n\nUsa esta información para responder de manera precisa y completa."

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Eres un asistente que ayuda a encontrar información en una lista de videos."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7,
        )
        result = response.choices[0].message.content.strip()
        return result
    except openai.exceptions.OpenAIError as e:
        return f"Se produjo un error: {e}"

def main():
    query = input("search: ")
    result = search_with_rag(query)
    print(result)

if __name__ == "__main__":
    main()