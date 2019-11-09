"""Settings to map env vars"""
import os

from dotenv import load_dotenv

load_dotenv()

discord_token = os.getenv("DISCORD_TOKEN")

def printenv():
    print(f'discord_token={discord_token}')

if __name__ == "__main__":
    printenv()
