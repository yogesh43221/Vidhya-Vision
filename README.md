# Vidhya-Vision
A smart search tool for Analytics Vidhya Courses.

---

## Analytics Vidhya Free Courses Search Tool

Welcome to the **Analytics Vidhya Free Courses Search Tool**! This project provides a smart search feature for free courses on Analytics Vidhya’s platform. It leverages Natural Language Processing (NLP) techniques using **LangChain**, **FAISS**, and **Streamlit** to create an intuitive, efficient search experience.

---

## 🛠️ Project Structure

```plaintext
your_project/
├── app/
│   └── app.py                  # Streamlit app containing all the app code        
│   └── script.py
│   └── visualizations.py       # Streamlit app second page code            
├── data/
│   └── courses_data_final.csv           # Scraped course data in CSV format
├── scripts/
│   ├── scrape_courses.py       # Script to scrape course data
│   ├── generate_embeddings.py  # Script to generate embeddings
├── vector_store/
│   ├── course_index.index      # FAISS index file for course embeddings
│   └── course_embeddings.npy   # Numpy file storing embedding vectors
├── venv/                       # Virtual environment (excluded in .gitignore)
└── requirements.txt            # List of dependencies



🌟 Features
🚀 RAG-Based Search
Combines retrieval mechanisms with generative responses for highly accurate and contextualized results.
Uses embeddings to enhance search precision by understanding semantic similarities between user queries and course data.
💡 Other Highlights
Comprehensive Course Search: Users can search free courses by title, description, curriculum, and more.
Efficient Embedding Search: Built on FAISS for fast and scalable semantic search.
User-Friendly Frontend: A web-based Streamlit app provides an intuitive search interface.
Dynamic Course Data: Scrapes and processes real-time course information.
🚀 Getting Started
Prerequisites
Python 3.8+
Virtual Environment (recommended)

Installation
1. Clone the repository:
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
2. Create and activate a virtual environment:
# On Windows
python -m venv venv
.\venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
3. Install dependencies:
pip install -r requirements.txt

🧑‍💻 Usage
Run the Streamlit app:
streamlit run app/app2.py
Access the app in your browser at http://localhost:8501.

Explore and search courses using the RAG-based smart search feature!

📂 Data Source
The project utilizes data scraped from the Analytics Vidhya platform.
Scraped attributes include:

Course Title
Description
Curriculum
Level (Beginner, Intermediate, Advanced)
Rating, Reviews, Duration, Lesson Count
Instructor Name, Price, and Enrollment Info
🛠️ Technical Details
RAG Framework: Combines retrieval using FAISS with a generative layer powered by an embedding model.
Embedding Model: Uses a state-of-the-art sentence embedding model to represent course data in vector format.
Vector Database: FAISS is employed for efficient similarity search.
Frontend: Built with Streamlit for an interactive user experience.
🙌 Contribution
Contributions are welcome! Feel free to open issues or submit pull requests.

📄 License
This project is licensed under the MIT License.

📧 Contact
For any questions or issues, please reach out to Yogesh Jadhav.

🔍 Explore, Learn, and Grow! 🚀

This markdown code can be directly pasted into your `README.md` file in the GitHub repository. Let me know if you need further adjustments!
