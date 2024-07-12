from openai import OpenAI
from openai.types.chat import ChatCompletion


prompt = "You are a professional translator specialized in translating texts from English to Portuguese. The provided text must be translated accurately, maintaining the original meaning and the natural flow of the Portuguese language."


def access(api_key):
    return OpenAI(api_key=api_key)


def talk(client, text) -> ChatCompletion:
    return client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": text},
        ],
        temperature=0.7,
    )


# while True:
#     prompt = input("Usuario: ")
#     resposta_chatgpt = conversar(prompt)
#     print(f"Bot: {resposta_chatgpt}")
