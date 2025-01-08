import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Function to load the FAISS index and embeddings
def load_faiss_index(index_path, embeddings_path):
    print("Loading FAISS index and embeddings...")
    index = faiss.read_index(index_path)
    embeddings = np.load(embeddings_path)
    return index, embeddings

# Function to perform similarity search
def search_courses(query, index, embeddings, top_k=5):
    # Embed the query using the same model used for embedding courses
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
    query_embedding = model.encode([query])

    # Perform the search in the FAISS index
    _, indices = index.search(query_embedding, top_k)
    
    # Get the results from the course embeddings
    search_results = []
    for idx in indices[0]:
        search_results.append(embeddings[idx])
    
    return search_results

# Main function to test search functionality
if __name__ == "__main__":
    # Define file paths
    index_path = "vector_store/course_index.index"
    embeddings_path = "vector_store/course_embeddings.npy"
    
    # Load index and embeddings
    index, embeddings = load_faiss_index(index_path, embeddings_path)
    
    # Example query
    query = "data analysis with Python"
    
    # Perform search
    results = search_courses(query, index, embeddings, top_k=5)
    
    # Display the top search results
    print("Top 5 similar courses to the query:")
    for i, result in enumerate(results):
        print(f"Result {i+1}: {result}")
