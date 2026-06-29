import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Collect FAQs (Questions and Answers)
faq_data = {
    "What is your return policy?": "You can return any product within 30 days of purchase for a full refund.",
    "How long does shipping take?": "Standard shipping takes 3-5 business days. Express shipping takes 1-2 days.",
    "Do you ship internationally?": "Yes, we ship to over 50 countries worldwide. Shipping fees vary by location.",
    "How can I track my order?": "Once your order ships, we will email you a tracking link to monitor your delivery.",
    "What payment methods do you accept?": "We accept Visa, MasterCard, American Express, PayPal, and Apple Pay."
}

faq_questions = list(faq_data.keys())

# 2. Simple, Pure-Python Preprocessing Function
def preprocess_text(text):
    """Converts to lowercase and removes punctuation."""
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # Removes punctuation like ?, !, ., etc.
    return text

# Preprocess all FAQ questions
preprocessed_faqs = [preprocess_text(q) for q in faq_questions]

# 3. Vectorize using TF-IDF (With built-in English stop words removal)
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(preprocessed_faqs)

# 4. Chatbot Response Logic
def get_bot_response(user_query):
    cleaned_query = preprocess_text(user_query)
    
    if not cleaned_query.strip():
        return "I'm sorry, I didn't quite catch that. Could you rephrase?"

    # Transform user query into the same TF-IDF vector space
    query_vector = vectorizer.transform([cleaned_query])
    
    # Calculate cosine similarity
    similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()
    
    # Find the best match
    best_match_idx = similarities.argmax()
    highest_score = similarities[best_match_idx]
    
    # Set a confidence threshold (0.2 is safe for basic keywords)
    if highest_score > 0.2:
        matched_question = faq_questions[best_match_idx]
        return faq_data[matched_question]
    else:
        return "I'm sorry, I couldn't find an answer to that. Would you like to speak to a human agent?"

# 5. Chat UI
print("🤖 FAQ Bot: Hello! I'm here to answer your questions. (Type 'exit' to quit)\n" + "-"*50)

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print("🤖 FAQ Bot: Goodbye!")
        break
    
    response = get_bot_response(user_input)
    print(f"🤖 FAQ Bot: {response}\n")