import openai

# Set your OpenAI API key
openai.api_key = 'your-api-key'

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="text-davinci-002",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

def main():
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = chat_with_gpt(user_input)
        print("ChatGPT:", response)

if __name__ == "__main__":
    main()
