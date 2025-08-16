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

@bot.event
async def on_ready():
    logger.info(f"Homura-Sec conectada como {bot.user} (id: {bot.user.id})")

@bot.command(name="ping", help="Verifica se o bot está online")
async def ping(ctx):
    await ctx.reply("Homura-Sec está ativa e ouvindo...")

@bot.command(name="ask", help="Envia uma mensagem")
async def answer(ctx):
    await ctx.reply("fala um tópico sobre cibersegurança e tempo... cibersegurança é boa para quem gosta, qual é o melhor tempo para agora? agora são 20:36 da noite...")

@bot.command(name="ask a message", help="Envia uma mensagem")
async def answer(ctx):
    await ctx.reply("fala um tópico sobre cibersegurança e programação... cibersegurança é muito bom, não acha? e qual seria o seu verdadeiro interesse nisso? programação é boa desde que você curta esse tipo de coisa.")

@bot.command(name="whoami", help="Diga seu nome")
async def answer(ctx):
    await ctx.reply("Eu sou HomuraAI, Essa é quem realmente sou... então, e aí? vamos á o que interessa, gosto de cibersegurança e programação, e quanto a você?")

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
            max_tokens=500
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
