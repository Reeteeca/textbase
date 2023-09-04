from textbase import bot, Message
from textbase.models import HuggingFace
from typing import List

# Load your HuggingFace API key
HuggingFace.api_key = ""

# Prompt for GPT-3.5 Turbo
SYSTEM_PROMPT = """Hello! I'm your wellness companion here to discuss a wide range of wellness topics with you. 
There are no specific prefixes for responses, so you can start the conversation with any wellness-related question or topic you like. 
Whether you want to talk about boosting your energy, managing stress, improving sleep, or any other wellness concern, 
I'm here to provide friendly and informative advice. 
Let's have a pleasant and supportive chat!

"""

@bot()
def on_message(message_history: List[Message], state: dict = None):

    # Generate HuggingFace response. Uses the DialoGPT-large model from Microsoft by default.
    bot_response = HuggingFace.generate(
        system_prompt=SYSTEM_PROMPT,
        message_history=message_history, # Assuming history is the list of user messages
    )

    response = {
        "data": {
            "messages": [
                {
                    "data_type": "STRING",
                    "value": bot_response
                }
            ],
            "state": state
        },
        "errors": [
            {
                "message": ""
            }
        ]
    }

    return {
        "status_code": 200,
        "response": response
    }