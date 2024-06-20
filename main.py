import discord
import argparse
import yaml
import os
from dotenv import load_dotenv
from minecraft import mcserverstatus

load_dotenv()
TOKEN = os.getenv("TOKEN")
intents = discord.Intents.all()
bot = discord.Bot(intents=intents)

def main():
    @bot.event
    async def on_ready():
        print(f"logged in as {bot.user.name}") 

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str,
                        help="yaml")
    args = parser.parse_args()
    with open ('config.yaml', "r") as f:
        config = yaml.safe_load(f) # configをyamlとして定義
    mcserverstatus(bot, config)
    main()
    bot.run(TOKEN)