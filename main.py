import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_workflow(user_input):
    prompt = f"""
    You are an AI workflow optimization expert.

    Analyze the following workflow:
    {user_input}

    Identify:
    - Inefficiencies
    - Bottlenecks
    - Suggested improvements
    - Optimized version of the workflow

    Keep it clear and structured.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    user_input = input("Enter your workflow: ")
    print(analyze_workflow(user_input))
