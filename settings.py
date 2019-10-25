"""Settings to map env vars"""
import os

from dotenv import load_dotenv

load_dotenv()

discord_token = os.getenv("DISCORD_TOKEN")
client_id = os.getenv("CLIENT_ID")

def printenv():
    print(f'discord_token={discord_token}')
    print(f'client_id={client_id}')

if __name__ == "__main__":
    printenv()
