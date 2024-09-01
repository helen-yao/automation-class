from typing import Final
from discord import Intents, Client, Message


TOKEN = "your token"


#Step 1: BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

#Step 2: Message Function
async def send_message(message: Message,user_message: str) -> None:
    # ---------------------------------------------------------------------
    # WRITE FUNCTIONS HERE !!

    # example message: sends "Hello!" when a user says "hi"
    if user_message.lower().startswith('hi'):
        await message.channel.send("Hello!")
        return
    

    # ---------------------------------------------------------------------

#Step 3: Handle the startup of the bot
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

#Step 4:  Handles the messages: waits for a message to be sent, then calls "send_message()" to send a response
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user: #The bot wrote the message, or the bot talks to itself
        return

    username: str= str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)

#Step 5 Main Starting point
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()