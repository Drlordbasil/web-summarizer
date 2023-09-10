from transformers import pipeline
from bs4 import BeautifulSoup
import requests
Sure! Here's an example of a Python program that uses the Web Content Summarizer AI model to summarize scraped website content:

```python


def scrape_website(url):
    # Send a GET request to the website URL
    response = requests.get(url)

    # Parse the HTML content of the website
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the text content from the website
    text = soup.get_text()

    return text


def summarize_website_content(website_content, summary_length):
    # Initialize the Web Content Summarizer AI model pipeline
    summarizer = pipeline("summarization")

    # Generate the summary using the AI model
    summary = summarizer(
        website_content, max_length=summary_length, min_length=10, do_sample=False)

    return summary[0]['summary_text']


# Example usage
website_url = "https://example.com"
website_content = scrape_website(website_url)
summary_length = 100  # Number of characters in the summary

summary = summarize_website_content(website_content, summary_length)

print(f"Summary of {website_url}:\n{summary}")
```

In this program, we first define the `scrape_website` function to retrieve the HTML content of a given website URL using the `requests` library and extract the text using `BeautifulSoup`.

Then, we define the `summarize_website_content` function that takes the website content and summary length as input. This function utilizes the Web Content Summarizer AI model to generate a summary by leveraging the `pipeline` from the `transformers` library. The summary is returned as a string.

To use the program, you can replace `website_url` with the desired website URL and specify the desired `summary_length`. The program will then scrape the website, summarize the content, and print the generated summary.

Note that you'll need to have the `requests`, `beautifulsoup4`, and `transformers` libraries installed for this program to work. You can install them using `pip install requests beautifulsoup4 transformers`. Additionally, you may need to install a specific pretrained model for the summarizer pipeline using `pip install transformers[model_name]`, where `model_name` is the name of the desired model(e.g., `pip install transformers[t5]`).

Remember to ensure that you are adhering to ethical guidelines and any legal requirements when scraping websites for their content.
