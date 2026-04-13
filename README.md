# Video AI Summarizer

> Analyze and summarize any video using Google Gemini 2.5 Flash with built-in web search — powered by Streamlit.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red?logo=streamlit)
![Gemini](https://img.shields.io/badge/Google%20Gemini-2.5%20Flash-orange?logo=google)
![License](https://img.shields.io/badge/License-MIT-green)



##  About

**Video AI Summarizer** is a Streamlit web app that lets you upload any video and ask questions about it. It uses **Google Gemini 2.5 Flash** to analyze the video content and optionally search the web for additional context — all in one place.



##  Features

-  Upload videos (MP4, MOV, AVI)
-  Powered by **Gemini 2.5 Flash** multimodal model
-  Built-in **Google Search** for web-enriched answers
-  Returns summary, key points, and insights
-  Auto-cleans temp files after processing



##  Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| AI Model | Google Gemini 2.5 Flash |
| SDK | `google-genai` |
| Config | `python-dotenv` |



##  Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/video-ai-summarizer.git
cd video-ai-summarizer
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

>  Get your free API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

### 5. Run the App

```bash
streamlit run app.py
```

Then open your browser at `http://localhost:8501`

---

##  Project Structure

```
video-ai-summarizer/
│
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
├── .env                 # API key (not committed to Git)
├── .gitignore           # Git ignore rules
└── README.md            # Project documentation
```

---

##  Requirements

```
streamlit
google-genai
python-dotenv
```



##  Environment Variables

| Variable | Description |
|---|---|
| `GOOGLE_API_KEY` | Your Google Gemini API key from AI Studio |

>  **Never commit your `.env` file or API key to GitHub.** The `.gitignore` already excludes it.



##  Usage Example

1. Launch the app and upload an `.mp4` video
2. Type your query, e.g.:
   > *"Summarize this video, list key points, and search the web for more about the topic"*
3. Click **Analyze** and wait for Gemini to process
4. Get a detailed summary with web-enriched insights 



##  Notes

- Large videos may take a minute to upload and process via the Gemini Files API
- Gemini 1.5 models are deprecated — this project uses the current **Gemini 2.5 Flash**
- Temporary video files are automatically deleted after analysis


##  Acknowledgements

- [Google Gemini API](https://ai.google.dev/)
- [Streamlit](https://streamlit.io/)
- [Google AI Studio](https://aistudio.google.com/)
