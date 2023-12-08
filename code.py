import openai
import requests

# Set your OpenAI GPT-3 API key
openai.api_key = 'your-api-key'

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def process_file(input_file, output_file):
    with open(input_file, 'r') as f:
        input_text = f.read()

    # You can customize the prompt as needed
    prompt = f"Generate a response for the following input:\n{input_text}\n\nResponse:"

    # Generate response using ChatGPT API
    output_text = generate_response(prompt)

    # Write the output to a text file
    with open(output_file, 'w') as f:
        f.write(output_text)

if __name__ == "__main__":
    input_file_path = "input.txt"  # Change this to the path of your input file
    output_file_path = "output.txt"  # Change this to the desired path for the output file

    process_file(input_file_path, output_file_path)
