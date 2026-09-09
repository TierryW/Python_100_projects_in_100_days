import streamlit as st
from question_model import Question
from data import question_data
from quiz_brain_2 import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)

    question_bank.append(new_question)

if "quiz" not in st.session_state:
    st.session_state.quiz = QuizBrain(question_bank)

if "answer_checked" not in st.session_state:
    st.session_state.answer_checked = False

if "last_answer_correct" not in st.session_state:
    st.session_state.last_answer_correct = False

quiz = st.session_state.quiz

st.set_page_config(page_title="True or False Quiz",page_icon="❓",layout="centered")

st.title("❓ True or False Quiz")
st.write("Test your knowledge by answering the questions below!")

if quiz.still_has_questions():

    current_question = quiz.get_current_question()

    st.write(
        f"### Question {quiz.question_number + 1} "
        f"of {len(quiz.question_list)}"
    )

    st.progress(quiz.question_number / len(quiz.question_list))

    st.markdown("---")

    st.subheader(current_question.text)

    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("✅ True", use_container_width=True):

            correct = quiz.check_answer("True", current_question.answer)

            st.session_state.last_answer_correct = correct
            st.session_state.answer_checked = True

            quiz.next_question()
            st.rerun()

    with col2:

        if st.button("❌ False", use_container_width=True):

            correct = quiz.check_answer("False", current_question.answer)

            st.session_state.last_answer_correct = correct
            st.session_state.answer_checked = True

            quiz.next_question()
            st.rerun()

    st.markdown("---")

    st.write(f"**Score: {quiz.score}/{quiz.question_number}**")

else:

    st.success("🎉 You've completed the quiz!")

    st.header("Final Score")

    st.metric(label="Score", value=f"{quiz.score}/{len(quiz.question_list)}")

    percentage = (quiz.score / len(quiz.question_list)) * 100

    st.write(f"### You scored {percentage:.0f}%!")

    st.markdown("---")

    if percentage == 100:
        st.balloons()
        st.success("🏆 Perfect score!")

    elif percentage >= 70:
        st.success("👏 Great job!")

    elif percentage >= 50:
        st.info("👍 Not bad! Keep practicing.")

    else:
        st.warning("📚 Keep studying and try again!")

    if st.button("🔄 Restart Quiz", use_container_width=True):

        st.session_state.quiz = QuizBrain(question_bank)
        st.session_state.answer_checked = False
        st.session_state.last_answer_correct = False

        st.rerun()
