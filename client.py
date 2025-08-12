from openai import OpenAI

client = OpenAI(api_key="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") 

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "tell me the wheather."}
    ],
    temperature=0.7
)

print(response.choices[0].message.content)
