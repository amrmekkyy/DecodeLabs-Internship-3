# 🎬 AI Movie Recommendation System

---

## 📌 Project Overview
This project is an AI-based Movie Recommendation System that suggests movies based on user interests.

---

## 🧠 How It Works

1. Each movie is described using keywords.
2. The user enters their interests (keywords).
3. The system converts text into numerical vectors using TF-IDF.
4. Cosine Similarity is used to measure how close the user interests are to each movie.
5. The top 5 most similar movies are recommended.

---

## 🎯 Key Idea

Each movie is stored as:

- **Key:** Movie name
- **Value:** Description (keywords like action, romance, horror, etc.)

The system compares:
> User interests vs Movie descriptions

and returns the best matches.

---

## 📂 Dataset Example

Movies are represented like this:

- Avengers Endgame → action, superhero, marvel
- Titanic → romance, drama, emotional
- John Wick → action, fight, crime
- Frozen → animation, disney, family
- Harry Potter → magic, fantasy, wizard

---

## ⚙️ Technologies Used

- Python
- Scikit-learn
- TfidfVectorizer
- Cosine Similarity

---

## 🧠 Concepts Used

- Natural Language Processing (NLP)
- TF-IDF (Term Frequency - Inverse Document Frequency)
- Cosine Similarity
- Recommendation Systems

---

## 🚀 How It Works (Step-by-Step)

1. Load movie dataset (keywords-based)
2. Take user input (interests)
3. Combine all movie descriptions + user input
4. Convert text into vectors using TF-IDF
5. Compute similarity between user and all movies
6. Rank movies based on similarity score
7. Display top 5 recommended movies
