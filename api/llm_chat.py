from openai import OpenAI
from openai.types.chat import ChatCompletion

prompt = "You are a professional translator specialized in translating texts from English to Portuguese. The provided text must be translated accurately, maintaining the original meaning and the natural flow of the Portuguese language."


def access():
    return OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")


def talk(client, text) -> ChatCompletion:
    return client.chat.completions.create(
        model="lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": text},
        ],
        temperature=0.7,
    )


# while True:
#     prompt = input("Usuario: ")
#     resposta_chatgpt = conversar(prompt)
#     print(f"Bot: {resposta_chatgpt.choices[0].message.content}")
