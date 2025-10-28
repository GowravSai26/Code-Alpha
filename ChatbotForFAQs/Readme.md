
# ✅ Chatbot for FAQs

This project is a simple **FAQ Chatbot** that answers user questions based on a predefined FAQ dataset.  
It uses **NLP preprocessing and cosine similarity** to match user queries with the closest FAQ and return the most relevant answer.  
A **Streamlit UI** is provided for easy user interaction.

---

## 📌 Features
- Collects and stores FAQs in a separate JSON file  
- Preprocesses and vectorizes text using **TF-IDF**
- Matches user input using **cosine similarity**
- Returns the **best matching answer**
- Includes a **simple and clean Streamlit UI**

---

## 🗂️ Project Structure
```

ChatbotForFAQs/
│
├── app.py            # Streamlit UI
├── chatbot.py        # Backend logic (NLP + Similarity Matching)
├── faqs.json         # FAQ dataset (Q/A pairs)
└── requirements.txt  # Dependencies

````

---

## 📄 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
````

---

## ▶️ How to Run

### 1️⃣ Run the Chatbot UI

```bash
streamlit run app.py
```

### 2️⃣ The UI will open at:

```
http://localhost:8501
```

---

## 🧠 How It Works

1. FAQ dataset is stored in `faqs.json`
2. Questions are **vectorized** using `TfidfVectorizer`
3. User input is compared against FAQ vectors using **cosine similarity**
4. The answer to the most similar question is displayed in the UI

---

## ✨ Example FAQ Entry (faqs.json)

```json
{
  "What is your return policy?": "You can return any product within 30 days of purchase."
}
```

To add more FAQs, simply edit `faqs.json` — no code changes required ✅

---

## 🧩 Technologies Used

| Technology   | Purpose                      |
| ------------ | ---------------------------- |
| Python       | Core programming             |
| Scikit-Learn | TF-IDF & Similarity matching |
| Streamlit    | Frontend UI                  |
| NLTK         | Text preprocessing           |

---

## 🎯 Completed Requirements (as per task)

| Task Requirement                        | Status                         |
| --------------------------------------- | ------------------------------ |
| Collect FAQs                            | ✅ Done                         |
| Preprocess text (tokenization/cleaning) | ✅ Done via TF-IDF              |
| Match user questions with FAQ           | ✅ Done using cosine similarity |
| Display best matching answer            | ✅ Implemented                  |
| Create simple chat UI                   | ✅ Streamlit UI added           |

---

## ✅ Final Output

A functional FAQ chatbot that can answer common questions with a clean web interface.

---