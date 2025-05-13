import streamlit as st
import speech_recognition as sr



def transcribe_speech(option):

    r= sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Speak now ...")

        audio_text = r.listen(source)
        
        if audio_text is None:
            st.error("Could not hear you!... Maybe an issue with the microphone ?")

        st.info("Transcribing...")

        if option == "speech_recognition":
            try:
                text = r.recognize_google(audio_text)
                return text
            except:
                return "Sorry, I did not get that."
        elif option == "deepgram":
            try:
                text = r.recognize_google(audio_text)
                return text
            except:
                return "Sorry, I did not get that."
        elif option == "speechbrain":
            try:
                text = r.recognize_google(audio_text)
                return text
            except:
                return "Sorry, I did not get that."
        elif option == "torchaudio":
            try:
                text = r.recognize_google(audio_text)
                return text
            except:
                return "Sorry, I did not get that."
        
        
def main():
    st.title("Speech Recognition Aoo")
    st.write("Click on the microphone to start speaking:")

    option = st.selectbox("Choose a speech recognition API:", [
        "speech_recognition",
        "deepgram",
        "speechbrain",
        "torchaudio"
    ])


    language = st.selectbox("Choose the language:", [
        "English",
        "French",
        "Arabic",
    ])

    if st.button("Start Recording"):
        text = transcribe_speech(option)
        st.write("Transcription: ", text)

        st.download_button(
            label="Download Transcription as .txt",
            data=text,
            file_name="transcription.txt",
            mime="text/plain"
        )



if __name__ == "__main__":
    main()

