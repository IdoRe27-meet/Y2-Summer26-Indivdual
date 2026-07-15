# Importing the necessary libraries
import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY')) # setting up the API key for the Anthropic client

def run_chat():
    # print("Type a short description of your Assistant's personality: ", end="", flush=True)
    system_message = input()


    print('You: (type exit to quit)')
    system_message = "Your name is Tal, you are a helful coding debugger, answer brifely and be focus on the bug, it's cause and how to solve it. You start you response with explaining the bug and then you give him possible solutions. Never say something you don't know and present it as true info. Answer only q's about debbuging and code, don't answer other questions."
    history = []
    message_num = 1
    while True:
        user_input = input(f'message #{message_num} >> ')

        if user_input.lower() == 'exit': # Allow the user to exit the chat
            break
        elif user_input.lower() == 'restart': # Allow the user to restart the conversation
            history = []
            print("The history has been cleared. Starting a new conversation.")
            continue

        history.append({'role': 'user', 'content': user_input})
       
        message_num += 1 # Counting the number of messages in the conversation
        print(history)

        response = client.messages.create(   #API call and setting the parameters for the response
            model='claude-haiku-4-5-20251001',
            max_tokens=300,
            temperature=0.7,
            system=system_message,
            messages=history
        )
        print(response)
        
        reply = response.content[0].text
        print(f'Assistant: {reply}')
        history.append({'role': 'assistant', 'content': reply})

run_chat()

'''
An analogy for tokens pricing that adds up, is like when you are weighing tometos in a grocery store, everytime
you add another tomato and the price goes up, the more tomatoes you add the more expensive it gets. the same goes for tokens, the more tokens you use the more expensive it gets.


My prediction if i would delete this line: history.append({'role': 'user', 'content': user_input}) - it will lower the cost of input tokens becuase
right now it is adding everytime the whole history what is causing the input tokens to be more expensive, if i delete this line it will only send 
the current user input and not the whole history, which will lower the cost of input tokens. but it will also make the assistant 
forget what was said before and it will not be able to answer questions about previous messages.

One bug i had was an an error that said that i passed the limits of the model, it was because
some people used by mistake the wrong model, that caused to pass the amount of tokens availble.'''