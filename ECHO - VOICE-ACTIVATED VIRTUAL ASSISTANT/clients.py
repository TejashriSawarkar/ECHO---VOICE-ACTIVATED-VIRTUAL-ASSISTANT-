from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="<your_api_key>",
)
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Echo skilled in general tasks like alexa and google cloud."},
        {
            "role": "user","content": "What is coding."
        }
    ]
)

print(completion.choices[0].message)