# import logging
# import requests
# import pypandoc
# from readability import Document

import azure.functions as func


# def convert_html_to_md(url):
#     response = requests.get(url)
#     doc = Document(response.text)

#     html = doc.summary()

#     return pypandoc.convert_text(html, 'md', format='html')


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    url = req.params.get('url')
    if not url:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            url = req_body.get('url')

    if url:
        # md = convert_html_to_md(url)
        return func.HttpResponse(f"Hello, {url}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )