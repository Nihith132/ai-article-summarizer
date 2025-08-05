import os
from dotenv import load_dotenv
import google.generativeai as genai
from requests_html import HTMLSession

load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv("GOOGLE_API_KEY")

if api_key is None:
    raise ValueError("API key not found. Please set the GOOGLE_API_KEY in your .env file.")

genai.configure(api_key=api_key)

def fetch_article_text(url: str) -> str:
    """
    Fetches the content of a URL and extracts the main article text.
    """
    try:
        session = HTMLSession()
        response = session.get(url)
        # response.html.render(sleep=1, timeout=20)
        
        article = response.html.find('article', first=True)
        
        if article:
            print("Successfully fetched and found the article content.")
            return article.text
        else:
            print("Warning: Could not find an <article> tag. Falling back to body text.")
            body = response.html.find('body', first=True)
            return body.text if body else ""

    except Exception as e:
        print(f"An error occurred while fetching the URL: {e}")
        return ""

def summarize_text(text: str) -> str:
    """
    Uses the Gemini API to summarize the provided text.
    """
    if not text:
        return "Error: No text was provided to summarize."

    print("Sending text to Gemini for summarization...")
    # This is the standard, current syntax for instantiating the model
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    prompt = f"Please provide a concise, easy-to-read summary of the following article text. Focus on the key points and conclusions. Here is the text:\n\n{text}"
    
    try:
        response = model.generate_content(prompt)
        print("Summary received!")
        return response.text
    except Exception as e:
        return f"An error occurred with the Gemini API: {e}"

# --- Main Execution ---
if __name__ == "__main__":
    target_url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
    
    print(f"Starting summarizer for URL: {target_url}")
    
    article_text = fetch_article_text(target_url)
    
    if article_text:
        summary = summarize_text(article_text)
        print("\n--- SUMMARY ---")
        print(summary)
        print("\n---------------\n")
    else:
        print("Could not generate summary because no text could be fetched from the URL.")
