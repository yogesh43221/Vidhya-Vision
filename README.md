# Vidhya-Vision
A smart search tool for Analytics Vidhya Courses.

your_project/ ├── app/ │ └── app2.py # Streamlit app containing all the app code ├── data/ │ └── your_file.csv # Scraped course data in CSV format ├── scripts/ │ ├── scrape_courses.py # Script to scrape course data │ ├── generate_embeddings.py # Script to generate embeddings ├── vector_store/ │ ├── course_index.index # FAISS index file for course embeddings │ └── course_embeddings.npy # Numpy file storing embedding vectors ├── venv/ # Virtual environment (excluded in .gitignore) └── requirements.txt # List of dependencies
