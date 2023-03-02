import os
import requests

DISCORD_API_URL = "https://discord.com/api/v10"


def get_server_info(server_id: str) -> dict:
    response = requests.get("{}/guilds/{}?with_counts=true".format(DISCORD_API_URL, server_id), headers={
        "Authorization": "Bot {}".format(os.getenv("DISCORD_BOT_TOKEN"))
    })
    response.raise_for_status()
    return response.json()