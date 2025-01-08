import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss
import logging
from tqdm import tqdm
import os
import argparse
import psutil

# Setup logging for better debugging and progress tracking
logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_memory_usage():
    """
    Logs the current memory usage for monitoring purposes.
    """
    process = psutil.Process(os.getpid())
    mem_usage = process.memory_info().rss / (1024 ** 2)  # Convert to MB
    logging.info(f"Current memory usage: {mem_usage:.2f} MB")

def load_data(file_path):
    """
    Loads the dataset from the given file path.
    """
    if not os.path.exists(file_path):
        logging.error(f"File not found: {file_path}")
        raise FileNotFoundError(f"Input file does not exist at: {file_path}")
    
    logging.info(f"Loading data from {file_path}...")
    
    try:
        # Try reading with 'ISO-8859-1' encoding to handle special characters
        return pd.read_csv(file_path, encoding='ISO-8859-1')
    except Exception as e:
        logging.error(f"Error loading the CSV file: {e}")
        raise


def clean_data(df):
    """
    Cleans and validates the course data.
    Removes rows with missing or empty critical columns and trims whitespace.
    """
    logging.info("Cleaning course data...")
    df = df.dropna(subset=['course_title', 'course_description'])  # Remove rows with missing critical data
    df['course_title'] = df['course_title'].str.strip()
    df['course_description'] = df['course_description'].str.strip()
    df = df[(df['course_title'] != '') & (df['course_description'] != '')]  # Remove empty rows
    
    logging.info(f"Data cleaned. Remaining courses: {len(df)}")
    return df

def generate_embeddings(texts, model, batch_size=32):
    """
    Generates embeddings for the given texts in batches.
    """
    logging.info("Generating embeddings...")
    embeddings = []
    for i in tqdm(range(0, len(texts), batch_size), desc="Embedding batches"):
        batch_texts = texts[i:i + batch_size]
        batch_embeddings = model.encode(batch_texts, show_progress_bar=False)
        embeddings.append(batch_embeddings)
    embeddings = np.vstack(embeddings)
    logging.info(f"Generated embeddings for {len(texts)} texts.")
    return embeddings

def create_faiss_index(embeddings):
    """
    Creates a FAISS index from the given embeddings.
    """
    logging.info("Creating FAISS index...")
    dimension = embeddings.shape[1]  # Embedding dimensionality
    index = faiss.IndexFlatL2(dimension)  # L2 distance for similarity search
    index.add(embeddings)
    logging.info("FAISS index created successfully.")
    return index

def save_embeddings_and_index(embeddings, index, embeddings_path, index_path):
    """
    Saves the embeddings and FAISS index to the specified file paths.
    """
    logging.info("Saving embeddings and FAISS index...")
    os.makedirs(os.path.dirname(embeddings_path), exist_ok=True)
    os.makedirs(os.path.dirname(index_path), exist_ok=True)

    np.save(embeddings_path, embeddings)  # Save embeddings
    faiss.write_index(index, index_path)  # Save index
    logging.info(f"Embeddings saved at: {embeddings_path}")
    logging.info(f"FAISS index saved at: {index_path}")

def main(args):
    # Parameters from arguments
    input_csv_path = args.input_csv_path
    embeddings_path = args.embeddings_path
    index_path = args.index_path
    embedding_model_name = args.embedding_model_name
    embedding_batch_size = args.batch_size

    try:
        # Load course data
        df = load_data(input_csv_path)

        # Clean the data
        df = clean_data(df)

        # Combine relevant fields for embedding
        df['combined_text'] = (
            df['course_title'] + " " +
            df['course_description'] + " " +
            df.get('course_curriculum', '').fillna("")  # Add curriculum if present
        )

        # Initialize the embedding model
        logging.info(f"Initializing embedding model: {embedding_model_name}")
        model = SentenceTransformer(embedding_model_name)

        # Log memory usage before generating embeddings
        log_memory_usage()

        # Generate embeddings
        embeddings = generate_embeddings(df['combined_text'].tolist(), model, batch_size=embedding_batch_size)

        # Create FAISS index
        index = create_faiss_index(embeddings)

        # Save embeddings and index
        save_embeddings_and_index(embeddings, index, embeddings_path, index_path)

        logging.info("Process completed successfully.")
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    # Argument parser for dynamic input/output
    parser = argparse.ArgumentParser(description="Generate embeddings and create a FAISS index for courses.")
    parser.add_argument("--input_csv_path", type=str, required=True, help="Path to the input CSV file.")
    parser.add_argument("--embeddings_path", type=str, required=True, help="Path to save the embeddings file.")
    parser.add_argument("--index_path", type=str, required=True, help="Path to save the FAISS index file.")
    parser.add_argument("--embedding_model_name", type=str, default="paraphrase-MiniLM-L6-v2", help="Name or path of the embedding model.")
    parser.add_argument("--batch_size", type=int, default=32, help="Batch size for embedding generation.")
    args = parser.parse_args()

    main(args)
