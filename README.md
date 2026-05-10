# 📝 Empowering Blind Students: Handwritten Note to Audio Converter

This project provides an AI-powered end-to-end pipeline to transform physical, handwritten educational materials into accessible, high-quality audio formats. It is specifically designed to help blind and visually impaired students convert classroom notes into structured, navigable audio segments.

## 🚀 Key Features

* **High-Resolution OCR:** Utilizes Google Cloud Vision AI to extract dense handwritten text from PDF scans.
* **Intelligent Refinement:** Leverages **Gemini 1.5 Pro/Flash** to correct OCR errors, fix grammar, and logically structure raw text into Markdown.
* **Natural Speech Synthesis:** Converts cleaned text into lifelike audio using Google Cloud **Text-to-Speech (Chirp3-HD)**.
* **Smart Segmentation:** Automatically splits long documents into manageable audio chapters (e.g., 12-minute segments) for easier navigation.

## 🛠️ Technical Stack

* **Language:** Python
* **OCR:** Google Cloud Vision API
* **LLM:** Google Gemini API (Generative AI)
* **TTS:** Google Cloud Text-to-Speech
* **Environment:** Google Colab / Jupyter Notebook

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
