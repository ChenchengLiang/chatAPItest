import openai
from utils import wrapped_api,print_response
from CONSTANTS import api_key
openai.api_key = api_key


def main():
    question = "how to perform conversation using chatGPT API"

    response, response_text = wrapped_api(question)
    print_response(response_text)



main()
