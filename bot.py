# pyright: reportShadowedImports = false
import streamlit as hoster
import requests as getter

import discord as interface
import wolframalpha as engine
import wikipedia as backup

from datetime import datetime
from discord.ext import commands
from bs4 import BeautifulSoup as parser


cmd_pref = "$"
cmd_ints = interface.Intents.default()
cmd_ints.message_content = True

src_href = "https://google.com/search?q="
src_pars = "html.parser"
src_clss = "BNeawe s3v9rd AP7Wnd"

bot_name = "Quick Researcher"
bot_desc = "discord search robot"
bot_iden = hoster.secrets["bot_hash"]

app_name = "Quick Researcher"
app_desc = "search engine plugin"
app_iden = hoster.secrets["app_hash"]

bot = commands.Bot(cmd_pref, intents = cmd_ints, help_command = None)
app = engine.Client(app_iden)


@bot.event
async def on_ready():
    timers = datetime.now().strftime("%m/%d/%y = %H:%M:%S")
    logger = "{0} | {1} is listening for commands.".format(timers, bot.user)

    hoster.success(logger)
    # print(f"{timers} | {bot.user} is listening for commands.")

@bot.event
async def on_command_error(ctx, error):
    timers = datetime.now().strftime("%m/%d/%y = %H:%M:%S")

    if isinstance(error, commands.CommandNotFound):
        detail = "The specified command is invalid or not found!"
        ticket = interface.Embed(
            type = "rich",
            color = interface.Color.red())

        ticket.set_author(name = "Quick Researcher - Error", icon_url = "https://bit.ly/3al1Uac")
        ticket.add_field(name = "__Invalid Command:__", value = f"```>> {detail}```", inline = False)

        print(f"{timers} | Error - {error} in the available commands.")
        await ctx.send(embed = ticket)

    if isinstance(error, commands.MissingRequiredArgument):
        detail = "The required argument is missing or not given!"
        ticket = interface.Embed(
            type = "rich",
            color = interface.Color.red())

        ticket.set_author(name = "Quick Researcher - Error", icon_url = "https://bit.ly/3al1Uac")
        ticket.add_field(name = "__Missing Keyword:__", value = f"```>> {detail}```", inline = False)

        print(f"{timers} | Error - Argument {error}")
        await ctx.send(embed = ticket)

@bot.command(aliases = ["u"])
async def usage(ctx):
    timers = datetime.now().strftime("%m/%d/%y = %H:%M:%S")
    manual = "Displays this help manual or card regarding\n   the usage of Quick Researcher Bot."
    search = "Find any information using the said command\n   followed by the search keywords."
    ticket = interface.Embed(
        type = "rich",
        description = "*An All-Around Discord Search Bot Coded By Dwight Dolatre*",
        color = interface.Color.blue())

    ticket.set_author(name = "Quick Researcher - Usage", icon_url = "https://bit.ly/3al1Uac")
    ticket.add_field(name = "__$usage  or  $u:__", value = f"```>> {manual}```", inline = False)
    ticket.add_field(name = "__$search  or  $s:__", value = f"```>> {search}```", inline = False)
    ticket.set_footer(text = "\xA9 2023 By Dwight Dolatre. All Rights Reserved.")

    print(f"{timers} | {bot.user} responded to a user usage.")
    await ctx.send(embed = ticket)

@bot.command(aliases = ["s"])
async def search(ctx, *, question):
    timers = datetime.now().strftime("%m/%d/%y = %H:%M:%S")

    try:
        search = app.query(question)
        result = next(search.results).text
        answer = result.replace("\n", " ")
        delays = round(bot.latency * 1000)
        ticket = interface.Embed(
            type = "rich",
            description = "*An All-Around Discord Search Bot Coded By Dwight Dolatre*",
            color = interface.Color.blue())

        ticket.set_author(name = "Quick Researcher - Search", icon_url = "https://bit.ly/3al1Uac")
        ticket.add_field(name = "__Search Request:__", value = f"```>> {question}```", inline = False)
        ticket.add_field(name = "__Search Results:__", value = f"```>> {answer}```", inline = False)
        ticket.add_field(name = "__Search Latency:__", value = f"```>> [{delays} ms]```", inline = False)
        ticket.set_footer(text = "Reference For Search Results: WolframAlpha")

        if answer == "(no data available)" or answer == "(data not available)":
            raise Exception

        else:
            print(f"{timers} | {bot.user} responded to a user query.")
            await ctx.send(embed = ticket)

    except:
        try:
            search = "{0}".format(question)
            result = backup.summary(search, sentences = 2)
            answer = result.replace("\n", " ")
            delays = round(bot.latency * 1000)
            ticket = interface.Embed(
                type = "rich",
                description = "*An All-Around Discord Search Bot Coded By Dwight Dolatre*",
                color = interface.Color.blue())

            ticket.set_author(name = "Quick Researcher - Search", icon_url = "https://bit.ly/3al1Uac")
            ticket.add_field(name = "__Search Request:__", value = f"```>> {question}```", inline = False)
            ticket.add_field(name = "__Search Results:__", value = f"```>> {answer}```", inline = False)
            ticket.add_field(name = "__Search Latency:__", value = f"```>> [{delays} ms]```", inline = False)
            ticket.set_footer(text = "Reference For Search Results: Wikipedia")

            if len(question) >= 35 or question.lower().startswith(("who", "what", "where", "when", "why", "which", "how")):
                raise Exception

            else:
                print(f"{timers} | {bot.user} responded to a user query.")
                await ctx.send(embed = ticket)

        except:
            search = getter.get(src_href + question)
            result = parser(search.text, src_pars).find_all("div", src_clss)[1].get_text()
            answer = result.replace("\n", " ").replace("   ", " - ").replace(" Wikipedia", "")
            delays = round(bot.latency * 1000)
            ticket = interface.Embed(
                type = "rich",
                description = "*An All-Around Discord Search Bot Coded By Dwight Dolatre*",
                color = interface.Color.blue())

            ticket.set_author(name = "Quick Researcher - Search", icon_url = "https://bit.ly/3al1Uac")
            ticket.add_field(name = "__Search Request:__", value = f"```>> {question}```", inline = False)
            ticket.add_field(name = "__Search Results:__", value = f"```>> {answer}```", inline = False)
            ticket.add_field(name = "__Search Latency:__", value = f"```>> [{delays} ms]```", inline = False)
            ticket.set_footer(text = "Reference For Search Results: Google")

            print(f"{timers} | {bot.user} responded to a user query.")
            await ctx.send(embed = ticket)

@search.error
async def search_error(ctx, error):
    timers = datetime.now().strftime("%m/%d/%y = %H:%M:%S")

    if isinstance(error, commands.CommandInvokeError):
        detail = "The search bot didn't find any search results!"
        ticket = interface.Embed(
            type = "rich",
            color = interface.Color.red())

        ticket.set_author(name = "Quick Researcher - Error", icon_url = "https://bit.ly/3al1Uac")
        ticket.add_field(name = "__Query Ambiguity:__", value = f"```>> {detail}```", inline = False)

        print(f"{timers}" + f" | Error - {error}.".replace(":", ","))
        await ctx.send(embed = ticket)


bot.run(bot_iden)
