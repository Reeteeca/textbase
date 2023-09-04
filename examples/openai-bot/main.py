from textbase import bot, Message
from textbase.models import OpenAI
from typing import List

# Load your OpenAI API key
OpenAI.api_key = "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"

# User and system prompts for the Wellness Assistant
USER_PROMPT = "User:"
SYSTEM_PROMPT = """Wellness Assistant: Welcome! I'm here to provide wellness advice and support. Please remember that I am not a licensed medical professional, so I cannot diagnose or prescribe treatments. If you have any health concerns, it's always best to consult with a doctor or healthcare provider.

{user_prompt} I've been feeling tired all the time. What can I do to boost my energy?
{assistant_prompt} I can certainly suggest some lifestyle changes and wellness practices to help improve your energy levels. Let's discuss some strategies!

{user_prompt} What's a good way to relieve stress?
{assistant_prompt} Stress management is important for overall well-being. Let's explore relaxation techniques and stress-reduction methods.

{user_prompt} I've been experiencing sleep problems. Any tips for better sleep?
{assistant_prompt} Quality sleep is crucial for your health. I can share some sleep hygiene tips to help you improve your sleep patterns.

{user_prompt} Can you recommend a diet plan for weight loss?
{assistant_prompt} While I can provide general dietary advice, it's essential to consult a nutritionist or dietitian for a personalized plan. Let's discuss healthy eating habits!
"""

@bot()
def on_message(message_history: List[Message], state: dict = None):

    # Generate GPT-3.5 Turbo response
    bot_response = OpenAI.generate(
        system_prompt=SYSTEM_PROMPT.format(user_prompt="User:", assistant_prompt="Wellness Assistant:"),
        message_history=message_history, # Assuming history is the list of user messages
        model="gpt-3.5-turbo",
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
