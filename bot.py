import os
import discord
import asyncio
from mcstatus import MinecraftServer
from discord.ext import commands

TOKEN = os.getenv(MTI2MDkyOTgyMzUzOTIwMDAxMA.GzaYdK.rGj-Yj8TWuoLWEEXjKvAtOKv-RaFAxSREvhkhQ)
MC_SERVER_IP = os.getenv(luigiparons.aternos.me)
UPDATE_INTERVAL = int(os.getenv('UPDATE_INTERVAL', 60))
CHANNEL_ID = int(os.getenv(1260926124842549359))

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connesso come {bot.user}')
    channel = bot.get_channel(CHANNEL_ID)
    if channel is None:
        print("Il canale specificato non è stato trovato.")
        return

    while True:
        await update_server_status(channel)
        await asyncio.sleep(UPDATE_INTERVAL)

async def update_server_status(channel):
    server = MinecraftServer.lookup(MC_SERVER_IP)
    
    try:
        status = server.status()
        message = f"Server Minecraft è online con {status.players.online} giocatori e {status.latency}ms di latenza."
    except Exception as e:
        message = "Server Minecraft è offline o non raggiungibile."
        print(e)

    await channel.send(message)

bot.run(TOKEN)
