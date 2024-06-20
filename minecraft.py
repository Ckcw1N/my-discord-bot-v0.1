import discord
from mcstatus import JavaServer
import math
import os

def mcserverstatus(bot, yml_config):
    server = JavaServer.lookup("{}:{}".format(
            yml_config["minecraft_server"]["host_name"],
            yml_config["minecraft_server"]["host_port"]
    ))   

    @bot.command(name="mcserver", description="Serverの稼働状況を表示します")
    async def ping(ctx: discord.ApplicationContext):

        status = server.status()
        ping = math.floor(status.latency * 100) / 100 # 小数点第2位以下を繰り上げ処理

        embed=discord.Embed(
            title="サーバー稼働状況",
            colour=discord.Colour.dark_green()
            )
        embed.add_field(name="参加人数", value=f"{status.players.online} 人")
        embed.add_field(name="ping", value=f"{ping} ms")

        await ctx.respond(embed=embed) # mcstatusで取得した情報をembedにinjectして出力
