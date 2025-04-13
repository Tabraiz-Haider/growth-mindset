# app.py

import streamlit as st # type: ignore

# Page setup
st.set_page_config(page_title="Growth Mindset Quiz 🌱", layout="centered")

# Title and intro
st.title("🌱 Growth Mindset Quiz App")
st.write("Welcome! Answer the following questions to reflect on your mindset.")

# Questions and options
questions = [
    {
        "question": "1. Jab tum fail hote ho to kya soch te ho?",
        "options": {
            "a": "Main isme kabhi achha nahi ho sakta.",
            "b": "Main mehnat karunga toh sudhar ho sakta hai."
        },
        "correct": "b"
    },
    {
        "question": "2. Tum dusron ki success ko kaise dekhte ho?",
        "options": {
            "a": "Wo lucky hain.",
            "b": "Unhone mehnat ki hogi."
        },
        "correct": "b"
    },
    {
        "question": "3. Agar koi kaam mushkil lage to tum kya karte ho?",
        "options": {
            "a": "Chhod deta hoon.",
            "b": "Koshish karta hoon seekhne ki."
        },
        "correct": "b"
    },
    {
        "question": "4. Tum galti se kya seekhte ho?",
        "options": {
            "a": "Main bas confuse ho jata hoon.",
            "b": "Galtiyon se seekhna normal hai."
        },
        "correct": "b"
    },
    {
        "question": "5. Tumhara belief kya hai talent ke baare mein?",
        "options": {
            "a": "Talent fixed hota hai.",
            "b": "Practice se talent develop hota hai."
        },
        "correct": "b"
    }
]

score = 0
user_answers = []

# Form for quiz
with st.form("quiz_form"):
    for q in questions:
        user_choice = st.radio(
            q["question"],
            list(q["options"].values()),
            key=q["question"]
        )
        correct_answer = q["options"][q["correct"]]
        user_answers.append((user_choice, correct_answer))

    submitted = st.form_submit_button("Submit Quiz")

# Show result after submission
if submitted:
    for user_choice, correct_answer in user_answers:
        if user_choice == correct_answer:
            score += 1

    st.markdown("---")
    st.subheader(f"🎯 Your Score: {score} / {len(questions)}")

    if score == len(questions):
        st.success("🎉 You have a strong Growth Mindset! Keep it up!")
    elif score >= len(questions) // 2:
        st.info("🙂 You have some Growth Mindset traits. You're on the right track!")
    else:
        st.warning("🧠 It looks like you have a Fixed Mindset right now, but remember—mindset can grow with effort!")
