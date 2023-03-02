import openai
import os
from utils import wrapped_api,print_response
from CONSTANTS import api_key
openai.api_key = api_key


def main():
    while True:
        question=input("You:")
        if question in ["stop","exit"]:
            print("conversation closed")
            break
        response,text=wrapped_api(question)
        print_response(text)



main()