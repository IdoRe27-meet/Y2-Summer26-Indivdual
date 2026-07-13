# Importing the necessary libraries
import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY')) # setting up the API key for the Anthropic client

def run_chat():
    
    print('You: (type exit to quit)')
    '''system_message = "Your name is Alex. You are a helpful and friendly assistant who helps students learn about technology and computer science. You explain things clearly and always encourage curiosity."'''
    system_message = input("Type a short description of your Assistant's personality: ") # allouwing the user to set the assistant's personality
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

        response = client.messages.create(   #API call and setting the parameters for the response
            model='claude-haiku-4-5-20251001',
            max_tokens=300,
            temperature=0.7,
            system=system_message,
            messages=history
        )

        reply = response.content[0].text
        print(f'Assistant: {reply}')
        history.append({'role': 'assistant', 'content': reply})

run_chat()


'''
## Reflection: ##
Imagine making a pasta, and becuase you suck at cooking like me, you have to buy a pasta sauce fro the store, so it will taste good.
Your code is the pasta, that you make, and the API is the sauce - something from outside that makes your pasta, code, taste better.

I had no bugs today (except of the wrong API key...), so I will look into a line of code I wasn't sure about: "message_num = 1" 
I was struggling with this because I kept getting an error that said "message_num is not defined" and that is when
I understood that I had to define it before the while loop, so that it would be defined when I called it in the input function.


My guess if I remove line 39:
I guess that if I remove this one the program will continue running until we reach line 40, were it is going
to crash because reply is not defined.


Now I will try:
NameError: name 'reply' is not defined. Did you mean: 'repr'?   


It is intresting because it seems that python thinks that this is just a variable I spelled wrong, but actually it is just not
defined... 
What I learned: sometimes python does wrong assumptions when it comes to error messages.
'''