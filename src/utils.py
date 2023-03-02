import openai
def wrapped_api(question):
    '''
    models:
    text-davinci-002: The most capable GPT model, able to perform a wide variety of tasks including language translation, question-answering, and content creation.
    text-curie-001: A highly capable GPT model, similar to text-davinci-002 but with a smaller parameter size.
    text-babbage-001: A GPT model with a smaller parameter size, suitable for simpler language generation tasks.
    text-ada-001: A GPT model fine-tuned for conversational response generation, optimized for generating high-quality, contextually relevant responses.
    text-codex-002: A GPT model fine-tuned on a large code corpus, able to generate code snippets, and perform other programming-related tasks.
    davinci-codex: The most capable Codex model, a combination of GPT and other AI technologies, designed to provide advanced programming assistance.

    parameter:temperature
    The temperature parameter is a scalar value between 0 and 1.
    A higher temperature value means the model is more likely to generate more creative and diverse responses, including responses that may not be directly related to the input prompt.
    A lower temperature value means the model is more likely to generate responses that are closely related to the input prompt.

    :param question:
    :return:
    '''
    response = openai.Completion.create(
        engine="text-ada-001",
        prompt=question,
        max_tokens=1000,
        temperature=0.2
    )
    return response, response.choices[0].text.strip()


def print_response(response_text):
    for x in response_text.split(". "):
        print(x)