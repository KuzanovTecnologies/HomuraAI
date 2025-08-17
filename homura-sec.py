#!/usr/bin/env python3
# -- coding: utf-8 --
import os
import sys
import logging
from dotenv import load_dotenv
from openai import OpenAI
import discord
from discord.ext import commands

# ========== CONFIGURAÇÃO DE LOG ===========
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("homura-sec")

# ========== CARREGAR .env ===========
load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

# ========== VERIFICAÇÃO DE TOKENS ============
if not DISCORD_TOKEN or not OPENAI_KEY:
    sys.stderr.write(
    "\n[Homura] ...Hmph. Você esqueceu de configurar as chaves.\n"
    "Verifique se o arquivo .env existe no mesmo diretório e contém:\n"
    "DISCORD_BOT_TOKEN=your_token_here\n"
    "OPENAI_API_KEY=your_key_here\n\n"
    )
    sys.exit(1)

# ========== CLIENTE OPENAI ==========
client = OpenAI(api_key=OPENAI_KEY)

# ========== CONFIG DISCORD BOT ==========
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

# ========== NOVOS COMANDOS DE HOMURAAI =========

@bot.command(name="sendaquestion", help="envia uma pergunta")
async def answer(ctx):
    await ctx.reply("who are you and what is your name?")

# ========== COMANDOS DE HOMURAAI ==========

@bot.event
async def on_ready():
    logger.info(f"Homura-Sec conectada como {bot.user} (id: {bot.user.id})")

@bot.command(name="ping", help="Verifica se o bot está online")
async def ping(ctx):
    await ctx.reply("Homura-Sec is active and listening...")

@bot.command(name="ask", help="Envia uma mensagem")
async def answer(ctx):
    await ctx.reply("talk a topic about cybersecurity... cybersecurity is good to those who likes, what is the time now? now it's 17:21 of afternoon...")

@bot.command(name="ask the user with a question", help="questiona o usuário com uma pergunta")
async def answer(ctx):
    await ctx.reply("talk a topic about cybersecurity and programming... cybersecurity is really good, don't you think? and how would be your true interest in this? programming is good as long as you enjoy these kinds of things.")

@bot.command(name="whoami", help="Diga seu nome")
async def answer(ctx):
    await ctx.reply("I AM HomuraAI a Anime Inspired Puella Magi Madoka Magica kind of anime ai magical girl, This is who i am... then, and so? let's go on what interests, it's really inspirative being into cybersecurity and programming, how about you?")

@bot.command(name="clear40messages", help="Clear the messages that are not working or the ones that are not needed")
async def answer(ctx):
    await ctx.reply("Futile messages, will be cleansed, cleaning messages... futile messages inutilized...")

@bot.command(name="writeatopicaboutcybersecurity", help="escreva um tópico sobre cibersegurança...")
async def answer(ctx):
    await ctx.reply("a good path for cybersecurity is to be a white-hat-hacker, not to join the anonymous yourself, do not be be a black-hat-hacker, be a white-hat-hacker...")

@bot.command(name="sayhello", help="diga oi...")
async def answer(ctx):
    await ctx.reply("Hello, how are you doing? is everything okay with you?")

# ========= GERENCIADOR DE VULNERABILIDADES POR IA =========
@bot.command(name="checkforpotentialvulnerabilities", help="verificar por potenciais vulnerabilidades")
async def answer(ctx):
    await ctx.reply("activate systems for checking potential vulnerabilities")

# ======== PESQUISAR POR HISTÓRICO DE ALVOS POR IA =========
@bot.command(name="searchtargetshistorybyai", help="pesquisar por histórico de alvos por ia")
async def answer(ctx):
    await ctx.reply("search history of targets by ai")

# ========== NOVO COMANDO PARA CHAT ==========
@bot.command(name="send questions", help="Envia uma pergunta para o modelo OpenAI")
async def ask(ctx, *, pergunta: str):
    await ctx.trigger_typing()
    try:
        resposta = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Você é um assistente útil e conciso."},
                {"role": "user", "content": pergunta}
            ],
            max_tokens=1000
        )
        texto_resposta = resposta.choices[0].message.content.strip()
        await ctx.reply(texto_resposta)
    except Exception as e:
        logger.error(f"Erro ao chamar OpenAI: {e}")
        await ctx.reply("Houve um problema ao processar sua solicitação.")

# ========== OUTRO COMANDO PARA CHAT ===========

@bot.command(name="write prompts", help="Escreve um prompt para o Modelo OpenAI")
async def write(ctx, *, escreva: str):
    await ctx.trigger_typing()
    try:
        resposta = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Você é um agente de cibersegurança, preciso e defensivo."},
                {"role": "user", "content": pergunta}
           ],
           max_tokens=1000
        )
        texto_resposta = resposta.choices[0].message.content.strip()
        await ctx.reply(texto_resposta)
    except Exception as e:
        logger.error(f"Erro ao chamar OpenAI: {e}")
        await ctx.reply("Houve um problema ao processar sua solicitação.")

# =========== SISTEMA DE CONVERSÃO DE BANCO DE DADOS POR CHATS DOS USUÁRIOS =========

@bot.command(name="send a message to OpenAI", help="Envia mensagens para o modelo da OpenAI")
async def write(ctx, *, escreva: str):
        await ctx.trigger_typing()
        try:
            resposta = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
            {"role": "system", "content": "Você é um assistente de tópicos, consistente e eficaz."},
            {"role": "user", "content": pergunta}

             ],
             max_tokens=1000
            )
            texto_resposta = resposta.choices[0].message.content.strip()
            await ctx.reply(texto_resposta)
        except Exception as e: 
            logger.error(f"Erro ao chamar OpenAI: {e}")
            await ctx.reply("Houve um problema ao processar sua solicitação.")

# =========== EXECUÇÃO ============
try:
    bot.run(DISCORD_TOKEN)
except discord.LoginFailure:
    sys.stderr.write(
        "\n[Homura] ...Tsk. O token do Discord é invalido.\n"
        "Reset no Discord Developer Portal e atualize seu .env.\n\n"
    )
    sys.exit(1)
