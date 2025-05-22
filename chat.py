from openai import OpenAI

client = OpenAI()  # Assumes your API key is set in the OPENAI_API_KEY environment variable

def chat():
    print("Chat with GPT-4. Type 'exit' to quit.")
    messages = [{"role": "system", "content": "You are a helpful assistant."}]

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        messages.append({"role": "user", "content": user_input})
        

        completion = client.chat.completions.create(
            model="gpt-4.1",  # or "gpt-4.0" or "gpt-4.1" depending on availability
            messages=messages
        )

        reply = completion.choices[0].message.content
        print(f"GPT-4: {reply}")
        messages.append({"role": "assistant", "content": reply})

if __name__ == "__main__":
    chat()
