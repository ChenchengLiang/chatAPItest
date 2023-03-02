import openai
from utils import wrapped_api,print_response
openai.api_key = "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"


def main():
    question = "how to perform conversation using chatGPT API"

    response, response_text = wrapped_api(question)
    print_response(response_text)



main()
