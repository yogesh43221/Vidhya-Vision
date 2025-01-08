import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer

# Function to test data quality by checking for missing values
def test_data_quality(csv_file_path):
    print("Testing data quality...")
    try:
        # Try reading with a different encoding
        data = pd.read_csv(csv_file_path, encoding='ISO-8859-1')
    except UnicodeDecodeError as e:
        print(f"Error reading the file with encoding 'ISO-8859-1': {e}")
        print("Trying with utf-16 encoding...")
        data = pd.read_csv(csv_file_path, encoding='utf-16')

    # Check for missing values
    missing_data = data.isnull().sum()
    print("Missing data in each column:")
    print(missing_data)
    
    # Ensure there are no empty or invalid entries in key fields like course_title
    invalid_entries = data[data['course_title'].isnull() | (data['course_title'] == '')]
    print(f"Found {len(invalid_entries)} invalid course titles.")
    
    return data

# Function to validate embeddings by checking their size
def test_embeddings(embeddings_path, data):
    print("Testing embeddings...")
    embeddings = np.load(embeddings_path)
    
    # Check that embeddings match the number of courses
    if embeddings.shape[0] != len(data):
        print(f"Error: Number of embeddings ({embeddings.shape[0]}) does not match number of courses ({len(data)}).")
    else:
        print(f"Embeddings validated: {embeddings.shape[0]} embeddings match {len(data)} courses.")
    
    # Check embedding dimensions (should be consistent with model output)
    embedding_dim = embeddings.shape[1]
    print(f"Embedding dimension: {embedding_dim}")
    
    return embeddings

# Main function to run data and embedding validation
if __name__ == "__main__":
    # Define file paths
    csv_file_path = r"F:\MyProjects_YJ\smart_search_tool\data\courses_data_final.csv"  # Input CSV path
    embeddings_path = r"F:\MyProjects_YJ\smart_search_tool\vector_store\course_embeddings.npy"  # Embeddings path
    
    # Test data quality
    data = test_data_quality(csv_file_path)
    
    # Test embeddings
    embeddings = test_embeddings(embeddings_path, data)
    
    # Optionally, test if embeddings and data match (for example, by checking the first row)
    print("First course title:", data.iloc[0]['course_title'])
    print("First embedding shape:", embeddings[0].shape)
