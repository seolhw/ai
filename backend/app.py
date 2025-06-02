from dotenv import load_dotenv
from openai import AsyncOpenAI

import chainlit as cl

load_dotenv()

client = AsyncOpenAI()


# Instrument the OpenAI client
cl.instrument_openai()

settings = {
    "model": "deepseek-chat",  # model you want to send litellm proxy
    "temperature": 0,
    # ... more settings
}


@cl.password_auth_callback
def auth_callback(username: str, password: str):
    # Fetch the user matching username from your database
    # and compare the hashed password with the value stored in the database
    if (username, password) == ("admin", "admin"):
        return cl.User(
            identifier="admin", metadata={"role": "admin", "provider": "credentials"}
        )
    else:
        return None


@cl.on_chat_resume
async def on_chat_resume(thread):
    pass


@cl.on_message
async def on_message(message: cl.Message):
    response = await client.chat.completions.create(
        messages=[
            {"content": "用中文回复我", "role": "system"},
            {"content": message.content, "role": "user"},
        ],
        **settings,
    )
    await cl.Message(content=response.choices[0].message.content).send()


@cl.set_starters
async def set_starters():
    return [
        cl.Starter(
            label="Morning routine ideation",
            message="Can you help me create a personalized morning routine that would help increase my productivity throughout the day? Start by asking me about my current habits and what activities energize me in the morning.",
            icon="/public/idea.svg",
        ),
        cl.Starter(
            label="Explain superconductors",
            message="Explain superconductors like I'm five years old.",
            icon="/public/learn.svg",
        ),
        cl.Starter(
            label="Python script for daily email reports",
            message="Write a script to automate sending daily email reports in Python, and walk me through how I would set it up.",
            icon="/public/terminal.svg",
        ),
        cl.Starter(
            label="Text inviting friend to wedding",
            message="Write a text asking a friend to be my plus-one at a wedding next month. I want to keep it super short and casual, and offer an out.",
            icon="/public/write.svg",
        ),
    ]


@cl.set_chat_profiles
async def chat_profile(current_user: cl.User):
    # if current_user.metadata["role"] != "ADMIN":
    #     return None

    return [
        cl.ChatProfile(
            name="My Chat Profile",
            icon="https://picsum.photos/250",
            markdown_description="The underlying LLM model is **GPT-3.5**, a *175B parameter model* trained on 410GB of text data.",
            starters=[
                cl.Starter(
                    label="Morning routine ideation",
                    message="Can you help me create a personalized morning routine that would help increase my productivity throughout the day? Start by asking me about my current habits and what activities energize me in the morning.",
                    icon="/public/idea.svg",
                ),
                cl.Starter(
                    label="Explain superconductors",
                    message="Explain superconductors like I'm five years old.",
                    icon="/public/learn.svg",
                ),
            ],
        )
    ]
