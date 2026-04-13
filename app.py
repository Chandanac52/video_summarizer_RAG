# app.py
import streamlit as st
from google import genai
from google.genai import types
import time
import tempfile
from pathlib import Path
from dotenv import load_dotenv
import os


load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    st.error("GOOGLE_API_KEY not found in .env file")
    st.stop()

client = genai.Client(api_key=API_KEY)


st.set_page_config(page_title="Video AI Summarizer", layout="wide")
st.title("🎥 Video AI Summarizer (Gemini 2.5)")

video_file = st.file_uploader("Upload video", type=["mp4", "mov", "avi"])

if video_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp:
        temp.write(video_file.read())
        video_path = temp.name

    st.video(video_path)

    user_query = st.text_area(
        "What insights are you seeking from the video?",
        placeholder="e.g. Summarize the video and list the key points and also search the web about the topic"
    )

    if st.button("Analyze"):
        if not user_query:
            st.warning("Please enter a query.")
        else:
            try:
                with st.spinner("Uploading video to Gemini..."):
                    
                    with open(video_path, "rb") as f:
                        vid = client.files.upload(
                            file=f,
                            config=types.UploadFileConfig(mime_type="video/mp4")
                        )

                   
                    while vid.state.name == "PROCESSING":
                        time.sleep(2)
                        vid = client.files.get(name=vid.name)

                    if vid.state.name == "FAILED":
                        st.error(" Video processing failed.")
                        st.stop()

                with st.spinner("Analyzing with Gemini 2.5 Flash + Web Search..."):
                    prompt = f"""
                    Analyze this video carefully and answer the following:

                    {user_query}

                    Please provide:
                    - A clear summary of the video
                    - Key points and takeaways
                    - Use web search to find additional relevant information or context about the topic
                    - Any useful insights or recommendations
                    """

                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=[
                            types.Content(
                                role="user",
                                parts=[
                                    types.Part(file_data=types.FileData(
                                        file_uri=vid.uri,
                                        mime_type="video/mp4"
                                    )),
                                    types.Part(text=prompt)
                                ]
                            )
                        ],
                        config=types.GenerateContentConfig(
                            tools=[types.Tool(google_search=types.GoogleSearch())],
                            temperature=0.7,
                        )
                    )

                st.subheader(" Analysis Result")
                st.write(response.text)

                client.files.delete(name=vid.name)

            except Exception as e:
                st.error(f" Error: {e}")

            finally:
                Path(video_path).unlink(missing_ok=True)
else:
    st.info(" Upload a video to get started.")