# AI Article Summarizer (TL;DR)

A simple yet powerful Python script that takes a URL of a web article and uses Google's Gemini API to generate a concise "Too Long; Didn't Read" (TL;DR) summary.

## Features

- Fetches article text directly from a URL.
- Handles modern, JavaScript-rendered websites.
- Uses the latest Gemini models (`gemini-1.5-flash-latest`) for fast and high-quality summarization.
- Securely manages API keys using a `.env` file.

## Technology Stack

- **Language:** Python 3
- **AI Model:** Google Gemini API (`google-generativeai`)
- **Web Scraping:** `requests-html`
- **Environment Management:** `python-dotenv`

## Setup and Installation

Follow these steps to get the project running on your local machine.

**1. Clone the repository:**
```bash
git clone [https://github.com/your-username/ai-article-summarizer.git](https://github.com/your-username/ai-article-summarizer.git)
cd ai-article-summarizer
