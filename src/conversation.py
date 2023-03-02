import openai
import os
from utils import wrapped_api,print_response
openai.api_key = "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"


def main():
    while True:
        question=input("You:")
        if question == "stop":
            print("conversation closed")
            break
        response,text=wrapped_api(question)
        print_response(text)



main()