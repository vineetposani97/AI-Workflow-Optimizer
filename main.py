from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_workflow(user_input):
    prompt = f"""You are an expert productivity coach.

    Analyze the following workflow and respond in this EXACT format:

    Workflow Breakdown:
    - Step-by-step breakdown

    Inefficiencies:
    - Bullet points

    Improvements:
    - Actionable suggestions

    Optimized Workflow:
    - Numbered improved workflow

    Productivity Score:
    - Score out of 10 with a short explanation

    Workflow:
    {user_input}
    """

    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt
)

    return response.output[0].content[0].text