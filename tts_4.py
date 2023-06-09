import streamlit as st
import pyttsx3
from PIL import Image
import os


def generate_audio(text, rate, volume, voice_index):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice_index].id)
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)
    engine.save_to_file(text, 'test.mp3')
    engine.runAndWait()


def main():
    # Custom CSS styles
    with st.beta_container():
        st.markdown(
            """
            <style>
            .stApp {
                max-width: 800px;
                margin: 0 auto;
                padding-top: 2rem;
            }
            .stButton button {
                background-color: #FF5722 !important;
                color: white !important;
                font-weight: bold !important;
            }
            .stTextInput textarea {
                height: 200px !important;
            }
            .stText {
                color: #333333 !important;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

    # App title and description
    st.markdown("# Text to Speech App")
    st.markdown("Enter text and convert it to speech!")

    # Upload banner image
    image = Image.open('Apple VR.png')
    st.image(image, use_column_width=True)

    # Sidebar with sliders
    st.sidebar.markdown("## Speech Settings")

    rate = st.sidebar.slider("Rate of Speech (words per minute)", min_value=50, max_value=200, value=170)
    volume = st.sidebar.slider("Volume (0-1)", min_value=0, max_value=1, value=1)

    voices = pyttsx3.init().getProperty('voices')
    voice_names = [voice.name for voice in voices]
    voice_index = st.sidebar.selectbox("Select Voice", voice_names)

    # Get text input from user
    text = st.text_area("Enter the text you want to convert to speech:", height=200)

    # Play button
    if st.button('Play'):
        st.text('Generating audio...')
        generate_audio(text, rate, volume, voice_names.index(voice_index))
        st.success('Audio generated successfully!')
        st.audio("test.mp3", format='audio/mp3')
        st.markdown('## Download Audio')
        file_path = 'test.mp3'
        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                file_data = file.read()
                st.download_button(label='Download Audio', data=file_data, file_name='audio.mp3', mime='audio/mpeg')


if __name__ == "__main__":
    main()
