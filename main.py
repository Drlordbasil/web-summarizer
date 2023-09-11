from transformers import pipeline
from bs4 import BeautifulSoup
import requests
Optimized Python script:

```python


def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()
    return text


def summarize_website_content(website_content, summary_length):
    summarizer = pipeline("summarization")
    summary = summarizer(
        website_content, max_length=summary_length, min_length=10, do_sample=False)
    return summary[0]['summary_text']


def main():
    website_url = "https://example.com"
    website_content = scrape_website(website_url)
    summary_length = 100
    summary = summarize_website_content(website_content, summary_length)
    print(f"Summary of {website_url}:\n{summary}")


if __name__ == "__main__":
    main()
```

In this optimized version of the script:
- The `transformers` import is moved to the top for better organization.
- The `main` function is added to encapsulate the main logic of the program.
- The program execution is wrapped in the `if __name__ == "__main__": ` check to ensure it only runs when executed directly.
- The unnecessary comments are removed for cleaner code.

This optimized script improves code readability and maintainability.
