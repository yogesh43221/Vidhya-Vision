# 🚀 Vidhya Vision
<p align="center">
  <img src="https://github.com/yogesh43221/Vidhya-Vision/blob/58d02254989a0f45ce1a1b690a2f955bdf5334b5/App_pics/imagevv.png" alt="Vidhya Vision Image" />
</p>
The smart search tool has been deployed on Hugging Face. You can access and explore it through the following link:

[**Explore the App on Hugging Face**](https://huggingface.co/spaces/yogeshjadhav666/Vidhya_Vision)

---
## Analytics Vidhya Free Courses Search Tool

## Overview
This project provides a smart search feature for free courses on Analytics Vidhya’s platform. It leverages Natural Language Processing (NLP) techniques using **LangChain**, **FAISS**, and **Streamlit** to create an intuitive, efficient search experience.

The tool is powered by a **Retrieval-Augmented Generation (RAG)** framework, which combines a retrieval mechanism with generative responses for accurate and contextualized search results.

## Tech Stack
- **LangChain**: For building and managing NLP pipelines.
- **FAISS**: A vector database used to store and search embeddings.
- **Streamlit**: Web framework for building the interactive search tool.
- **Python**: For scripting and data processing.
- **NumPy**: For array manipulation, especially embeddings.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FAISS](https://img.shields.io/badge/FAISS-0062FF?style=for-the-badge&logo=faiss&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-2566E0?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

## Project Workflow

### Step 1: Data Scraping (Python)
- Scraped free course data from Analytics Vidhya.
- Collected data including course titles, descriptions, ratings, reviews, and other attributes.

### Step 2: Embedding Generation (Python)
- Generated sentence embeddings for each course using an embedding model.
- Saved the embeddings to a `.npy` file for efficient search.

### Step 3: Search Functionality (LangChain & FAISS)
- Built a retrieval mechanism using **FAISS** to index and search course embeddings.
- Integrated with **LangChain** to handle user queries and generate relevant course suggestions based on semantic similarity.

### Step 4: User Interface (Streamlit)
- Developed a simple, interactive Streamlit web app to enable users to search courses.
- Users can enter queries, and the app will return the most relevant courses based on their search.

## Screenshots and Demo
### Streamlit App Preview
![Streamlit App Preview](https://github.com/yogesh43221/Vidhya-Vision/blob/167c1ccccb4d8fd076f28983b659610bd4a34973/App_pics/image1.png)
![Streamlit App Preview](https://github.com/yogesh43221/Vidhya-Vision/blob/167c1ccccb4d8fd076f28983b659610bd4a34973/App_pics/image2.png)
![Streamlit App Preview](https://github.com/yogesh43221/Vidhya-Vision/blob/167c1ccccb4d8fd076f28983b659610bd4a34973/App_pics/image3.png)
![Streamlit App Preview](https://github.com/yogesh43221/Vidhya-Vision/blob/167c1ccccb4d8fd076f28983b659610bd4a34973/App_pics/image4.png)

### Course Search Results
![Search Results](https://github.com/yogesh43221/Vidhya-Vision/blob/a27843e050d97126b54a5df6d0bd9b72259f147c/App_pics/imagesc.png)

## Key Features
- **RAG-Based Search**: Combines retrieval with generative models to deliver highly relevant course suggestions.
- **Efficient Embedding Search**: Uses **FAISS** for fast and scalable search.
- **User-Friendly UI**: A clean, interactive **Streamlit** app allows users to explore courses easily.
- **Dynamic Course Data**: Real-time scraping ensures up-to-date course information.

## Getting Started

### Prerequisites
Ensure the following Python libraries are installed:
- `python`
- `langchain`
- `faiss-cpu`
- `streamlit`
- `numpy`

```bash
pip install langchain faiss-cpu streamlit numpy

```
## Installation

### Clone the repository:
```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/yogesh43221/Vidhya-Vision.git)
cd YOUR_REPO_NAME
```
## Create and activate a virtual environment:
# On Windows
```bash
python -m venv venv
.\venv\Scripts\activate
```
# On macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```
## Install dependencies:
```bash
pip install -r requirements.txt
```
## 🧑‍💻 Usage
### Run the Streamlit app:
```bash
streamlit run app/app2.py
```
Access the app in your browser at ```http://localhost:8501```
Explore and search courses using the RAG-based smart search feature!

## 📂 Data Source
The project utilizes data scraped from the **Analytics Vidhya** platform.
Scraped attributes include:
- Course Title
- Description
- Curriculum
- Level (Beginner, Intermediate, Advanced)
- Rating, Reviews, Duration, Lesson Count
- Instructor Name, Price, and Enrollment Info

## 🛠️ Technical Details
- **RAG Framework**: Combines retrieval using FAISS with a generative layer powered by an embedding model.
- **Embedding Model**: Uses a state-of-the-art sentence embedding model to represent course data in vector format.
- **Vector Database**: FAISS is employed for efficient similarity search.
- **Frontend**: Built with Streamlit for an interactive user experience.
- 
## 🙌 Contribution
Contributions are welcome! Feel free to open issues or submit pull requests.

## 📄 License
This project deployment is licensed under the MIT License.

## 📧 Contact
For any questions or issues, please reach out to Yogesh Jadhav.

## 🔍 Explore, Learn, and Grow! 🚀


