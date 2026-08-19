from openai import OpenAI
client = OpenAI()
prompt = input("Enter prompt: ")
response = client.responses.create(
    model="gpt-4o-mini",
    input=prompt
)
print("Generated Text:")
print(response.output_text)

Input:
Enter prompt: Write one sentence about Python.

Output:
Generated Text:
Python is a versatile programming language.
