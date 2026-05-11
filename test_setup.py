# test_setup.py
from config.llm_config import get_llm, get_embeddings
import chromadb
import os

# Test LLM
llm = get_llm()
response = llm.invoke("Confirm you're working")
print(f"✓ LLM working: {response.content[:50]}...")

embeddings = get_embeddings()

test_embed = embeddings.embed_query("test")
print(f"✓ Embeddings working: {len(test_embed)} dimensions")

# Test ChromaDB
client = chromadb.Client()
print("✓ ChromaDB working")
