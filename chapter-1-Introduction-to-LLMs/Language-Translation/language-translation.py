import os
import pdb
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


def main():

    english_text = " Are you going to office "

    client = OpenAI(
        api_key = os.environ.get("OPENAI_API_KEY")
    )

    chat_completion = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
        {"role": "system", "content": "You are helpfull assistant."},
        {"role": "user", "content":f'''Translate the following English text to Telugu: "{english_text}"'''}]
    )

    print(chat_completion.choices[0].message.content)

if __name__ == "__main__":
    main()
