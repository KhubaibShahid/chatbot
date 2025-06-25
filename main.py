import os
import chainlit as cl
from dotenv import load_dotenv
from httpx import Response
from litellm import completion

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

@cl.on_chat_start
async def start():

    cl.user_session.set("messages", [])
    await cl.Message(content="Hello, how can I help you today?").send()

@cl.on_message
async def on_message(message: cl.Message):
    msg = cl.Message(content="Thinking...")
    await msg.send()

    history = cl.user_session.get("messages") or []
    history.append({"role": "user", "content": message.content})

    try:
        response = completion(
            model="gemini/gemini-2.0-flash",
            api_key = api_key,
            messages = history,
        )

        response_content = response.choices[0].message.content

        msg.content = response_content
        await msg.update()

        history.append({"role": "assistant", "content": response_content})
        cl.user_session.set("messages", history)

    except Exception as err:
        msg.content = f"Sorry, I encountered an error: {err}"
        await msg.update()
        print(err)

