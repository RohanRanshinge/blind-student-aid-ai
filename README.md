
# 📝 Empowering Blind Students: Handwritten Note to Audio Converter

An AI-powered pipeline designed to bridge the accessibility gap for visually impaired students by transforming handwritten study materials into structured, consistent, and high-quality audio podcasts.

## 🌟 Motivation

In India, many bright and capable blind students—including those preparing for highly competitive exams like the **UPSC**—lack access to digitized study materials. They often rely on volunteers to manually dictate handwritten notes from other students. 

This process has a significant hurdle: every volunteer has a different accent, cadence, and speaking style. For a student trying to focus on complex subjects for hours, this inconsistency is a major cognitive drain. 

**This project was born to solve that.** By using AI to digitize handwriting and synthesize it into a singular, high-definition voice, we provide students with a consistent, "podcast-like" learning experience. Now, a student can listen to 100 pages of notes and know that the voice, speed, and quality will remain identical throughout.

## 🚀 Key Features

* **Handwriting to Digital:** Uses Google Cloud Vision AI to extract text from dense, handwritten PDF scans.
* **Intelligent Refinement:** Employs **Gemini 1.5** to fix OCR errors and structure raw notes into logical Markdown.
* **Consistent Audio Experience:** Converts text into lifelike speech using **Google Cloud TTS (Chirp3-HD)**.
* **Podcast-Style Segmentation:** Automatically splits long topics into manageable 12-minute audio "chapters" for easier navigation.

## 🛠️ Technical Stack

* **Core:** Python, Google Colab
* **Vision:** Google Cloud Vision API (OCR)
* **Intelligence:** Google Gemini API (Text Correction & Structuring)
* **Speech:** Google Cloud Text-to-Speech (Chirp3-HD - `en-IN` voice)

## 📋 How to Use

1. **Prerequisites:**
   - A Google Cloud Project with Vision and Text-to-Speech APIs enabled.
   - A Gemini API Key from [Google AI Studio](https://aistudio.google.com/).
   - A service account JSON key for Google Cloud authentication.

2. **Setup:**
   - Upload your handwritten notes (PDF) to the environment.
   - Store your `GEMINI_API_KEY` in your environment secrets.
   - Update the `PDF_FILE_PATH` and `GOOGLE_CLOUD_SERVICE_ACCOUNT_KEY_PATH` in the configuration cell.

3. **Execution:**
   - Run all cells in the `BlindStudentAid.ipynb` notebook.
   - The workflow will output a `cleaned_text.txt` file and a folder of `.mp3` audio segments.

## 📂 Project Structure
```text
├── BlindStudentAid.ipynb   # Main execution notebook
├── audio_segments/         # Generated MP3 files (output)
├── extracted_images/       # Intermediate page scans for OCR
└── cleaned_text.txt        # The AI-corrected transcript
```

*Created to ensure that a student's ambition is never limited by their access to knowledge.*
