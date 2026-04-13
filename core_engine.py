import pandas as pd
from openai import OpenAI

client = OpenAI()

# Load data
df = pd.read_csv("data/agriculture_data.csv")

def get_relevant_data(region):
    return df[df['region'].str.lower() == region.lower()].to_dict(orient="records")

def generate_response(user_query, data):
    
    context = f"""
    You are an AI assistant.
    Return output in JSON format:

    {{
        "recommendation": "",
        "reason": "",
        "risks": ""
    }}
    
    Data:
    {data}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": user_query}
        ]
    )

    return response.choices[0].message.content

def evaluate_response(response):
    
    checks = {
        "length": len(response),
        "has_bias_words": any(word in response.lower() for word in ["always", "never"]),
    }
    
    return checks