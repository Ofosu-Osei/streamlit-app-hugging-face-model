import streamlit as st
from transformers import pipeline

model_name = "gpt2"

text_generator = pipeline("text-generation", model=model_name)

def main():
    # Updated page configuration for dark mode appearance
    st.set_page_config(
        page_title="Streamlit Chatbot - Demo",
        page_icon="🤖",
        layout="centered",
        initial_sidebar_state="collapsed"
    )

    st.markdown(
    """
    <style>
        .main {background-color: #FFFFFF;} 
        h1 {text-align: center; color: #000000;} 
        /* Text area focus state */
        .stTextArea>div>div>textarea:focus {
            border: 2px solid #4C9AFF !important; /
        }
        .stTextArea>div>div>textarea {
            background-color: #FFFFFF; 
            color: #000000; 
            border-radius: 10px;
            border: 2px solid #D38936; 
        }
        .stButton>button {
            border: 2px solid #D38936;
            border-radius: 10px;
            color: #FFFFFF; 
            background-color: #4C9AFF; 
            font-size: 18px;
            transition: background-color 0.3s, color 0.3s;
        }
        /* Button hover state */
        .stButton>button:hover {
            border: 2px solid #D38936;
            background-color: #1C6DD0; 
            color: #FFFFFF;
        }
    </style>
    """, unsafe_allow_html=True
)


   # Header section 
    st.markdown(
        """
        <div style="background-color: #4C9AFF; padding: 25px; border-radius: 15px;">
            <h1 style="color: #FFFFFF; text-align: center;">Streamlit Chatbot - Demo</h1>
        </div>
        <br>
        """, unsafe_allow_html=True
    )

    # Introduction section 
    st.markdown( 
        """
        <div style="flex: 2; padding-left: 20px;">
            <p style="color: #333333;">Welcome to Streamlit Chatbot - Demo, where the future of conversational AI meets the simplicity of Streamlit.</p>
            <p style="color: #333333;">Dive in and experience the art of conversation with cutting-edge technology at your fingertips.</p>              
            <p style="color: #333333;">Let's start chatting!</p>
        </div>
        """, unsafe_allow_html=True
    )



    # User input area 
    text_input = st.text_area("Message Chatbot...", height=50,
                              placeholder="Message Chatbot...")

    if st.button("Answer"):
        if text_input:
            with st.spinner('Responding ...'):
                generated_texts = text_generator(text_input, max_length=150, do_sample=True)
                generated_res = generated_texts[0]['generated_text']

                last_period_index = generated_res.rfind('. ')
                if last_period_index != -1:
                    generated_res = generated_res[:last_period_index + 1]

                st.markdown("""<div style='color: black;'>Chatbot:</div>""", unsafe_allow_html=True)
                st.markdown(f"<div style='color: black;'>{generated_res}</div>", unsafe_allow_html=True)
        else:
            st.markdown("""<div style="background-color: #EBB8DD; padding: 10px; border-radius: 10px; text-align: center;">
                            <p style="color: red; font-size: 15px;">Please provide a question to receive an answer.</p>
                            </div> """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
