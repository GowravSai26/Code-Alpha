import json
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')

# ---- Load FAQs from JSON file ----
with open("faqs.json", "r") as f:
    faqs = json.load(f)

faq_questions = list(faqs.keys())

vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(faq_questions)

def get_answer(user_query):
    user_vec = vectorizer.transform([user_query])
    similarities = cosine_similarity(user_vec, question_vectors)

    index = similarities.argmax()
    best_score = similarities[0][index]

    if best_score < 0.3:
        return "Sorry, I couldn't understand your question."

    best_question = faq_questions[index]
    return faqs[best_question]


if __name__ == "__main__":
    print("\nRun `streamlit run app.py` to use the UI.\n")
