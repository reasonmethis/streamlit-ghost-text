import time

import streamlit as st

from helpers import make_silly_question, make_silly_reply


def main():
    st.title('Ghost Text Demo "Chatbot"')

    if "chat_history" not in (ss := st.session_state):
        ss.chat_history = []

    for i, msg in enumerate(ss.chat_history):
        with st.chat_message("ai" if i % 2 else "user"):
            # st.empty() # INSERTING THIS FIXES THE GHOST DOUBLE TEXT ISSUE
            st.write(msg)

    user_msg = st.chat_input("Type something to see ghost double text in action")

    # If it's the first run, simulate a user message to trigger the AI response
    if is_first_run := (len(ss.chat_history) == 0):
        user_msg = (
            "This is a simulated user message, but after this you can type your own!"
        )
    if not user_msg:
        st.stop()

    with st.chat_message("user"):
        st.write(user_msg)

    with st.chat_message("ai"):
        bracket_text = "" if is_first_run else " (check out the ghost text above)"
        status = st.status(f"Fake thinking{bracket_text}...")
        
        time.sleep(1 if is_first_run else 5)
        status.update(label="Done!", state="complete")
        
        # NOTE: the line below constructs a silly reply based on the user message,
        # but that doesn't matter for the purposes of showing the ghost text, we might 
        # as well just have done: ai_msg = "SOME TEXT HERE"
        ai_msg = (
            "Hello, I am a fake chatbot that always agrees with you!"
            if is_first_run
            else make_silly_reply(user_msg) 
        ) + f"\n\n{make_silly_question()}"
        st.write(ai_msg)

    ss.chat_history.extend([user_msg, ai_msg])


if __name__ == "__main__":
    main()
