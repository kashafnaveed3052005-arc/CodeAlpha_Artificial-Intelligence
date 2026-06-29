# Simple FAQ Chatbot using NLP

A lightweight, terminal-based FAQ Chatbot built in Python. This project utilizes Natural Language Processing (NLP) concepts to understand user queries and match them with the most relevant Frequently Asked Questions (FAQs) using **TF-IDF Vectorization** and **Cosine Similarity**.

## 🚀 Features
* **Text Preprocessing:** Automatically cleans text by converting it to lowercase and removing punctuation.
* **Smart Keyword Matching:** Uses `scikit-learn`'s built-in English stop-word removal to filter out filler words (e.g., "what", "is", "the").
* **Mathematical Matching:** Uses Cosine Similarity to find the best question match based on context, even if the user phrases the question differently.
* **Fallback Safety net:** Features a confidence threshold fallback. If the user's question doesn't match any known FAQs, the bot gracefully offers human agent support instead of guessing blindly.

---

## 🛠️ Tech Stack & Concepts
* **Language:** Python 3.x
* **NLP Techniques:** Tokenization, Punctuation Removal, Stop-word Filtering
* **Vectorization:** TF-IDF (Term Frequency-Inverse Document Frequency)
* **Algorithm:** Cosine Similarity via `scikit-learn`

---

## 📋 Prerequisites & Installation

1. Make sure you have Python installed. You can check your version using:
   ```bash
   python --version