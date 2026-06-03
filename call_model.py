from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def call_model(messages, model):

    response = client.chat.completions.create(
        model=model,
        messages=messages
    )

    return response.choices[0].message.content