# Requires: pip install openai
from openai import OpenAI

client = OpenAI()

prompt = input("Enter prompt: ")

response = client.responses.create(
    model="gpt-4o-mini",
    input=prompt
)

print("Generated Text:")
print(response.output_text)

# Sample Input:
# Enter prompt: Write one sentence about Python.
#
# Sample Output:
# Generated Text:
# Python is a versatile programming language.
