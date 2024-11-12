
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="transformers")

from transformers import BertTokenizer, BertModel
import torch


tokenizer = BertTokenizer.from_pretrained("bert-base-multilingual-cased")
model = BertModel.from_pretrained("bert-base-multilingual-cased")

word = input('Enter a word: ')
inputs = tokenizer(word, return_tensors="pt")

with torch.no_grad():
    outputs = model(**inputs)

word_vector = outputs.last_hidden_state.mean(dim=1)

print(f"word vector: '{word}':\n{word_vector[0][:10]}...")
