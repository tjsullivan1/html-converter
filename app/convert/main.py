import requests
import pypandoc
from readability import Document

response = requests.get('https://michaelvigor.dev/serverless-url-to-markdown/')
doc = Document(response.text)

html = doc.summary()

print(pypandoc.convert_text(html, 'md', format='html'))