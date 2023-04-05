# bot.py
import os
import random
import sys
import sqlite3
import csv
import string
import datetime
import requests
import json

import discord
from discord.ext import commands

TOKEN = 

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.presences = True

bot = commands.Bot(command_prefix='>', intents=intents)
client = discord.Client(intents=intents)

debug_mode = True

'''
@bot.command(name='reload', help='Restarts the bot')
async def reload(ctx):
    try:
        response = 'Restarting bot...'
        await ctx.send(response)
        python = sys.executable
        os.execl(python, python, *sys.argv)
    except Exception as e:
        if debug_mode:
            await ctx.send(f"Error: {str(e)}")
        return


@bot.command(name='debug', help='Toggles debug mode.')
async def debug(ctx):
    global debug_mode
    debug_mode = not debug_mode
    if debug_mode:
        await ctx.send("Debug mode enabled.")
    else:
        await ctx.send("Debug mode disabled.")


@bot.command(name='ping', help='Returns the latency of the bot.')
async def ping(ctx):
    try:
        response = f"Pong! {round(bot.latency * 1000)}ms"
        await ctx.send(response)
    except Exception as e:
        if debug_mode:
            await ctx.send(f"Error: {str(e)}")
        return


#Axolotl API
@bot.command(name='axolotl', help='Returns a random axolotl image.')
async def axolotl(ctx):

'''
@bot.command(name='dog', help='Returns the latency of the bot.')
async def dog(ctx):
    # specify endpoint
    url = 'https://dog.ceo/api/breeds/image/random'
    # make GET request
    response = requests.get(url)
    # load response content into a dictionary
    data = json.loads(response.content)

    await ctx.send(data['message'])


@bot.command(name='bird', help='Returns the latency of the bot.')
async def bird(ctx):

    # specify endpoint
    url = 'https://xeno-canto.org/api/2/recordings'

    # specify parameters
    params = {'query': 'cnt:australia'}

    # make GET request
    response = requests.get(url, params=params)

    #print(response.content)

    # load response content into a Python dictionary
    data = json.loads(response.content)

    # dump data into a JSON file
    #with open('xenocanto.json', 'w') as f:
    #    json.dump(data, f, indent=4)

    bird = random.choice(data['recordings'])

    output = f"Common Name: {bird['en']}\nScientific Name: {bird['gen'].title()} {bird['sp'].lower()}\nLocation: {bird['loc']}\nDate Recorded: {bird['date']}\nRemark: {bird['rmk']}\n{bird['type'].title()}: {bird['file']}\nUrl: {bird['url']}"

    await ctx.send(output)


#optomise f string output to use dictionary of dictionaries
@bot.command(name='air_quality', help='Returns the latency of the bot.')
async def air_quality(ctx):
    def AQI_string(site):
        AQI_list = ['aqi_no2', 'aqi_o3_8hr', 'aqi_pm10', 'aqi_pm2_5', 'aqi_co']
        AQI_dict = {}
        for AQI in AQI_list:
            if site['name'] == 'Civic' and (AQI == 'aqi_no2' or AQI == 'aqi_co'):
                AQI_dict[AQI] = 'Data not available'
            else:
                try:
                    if int(site[AQI]) < 34:
                        AQI_dict[AQI] = 'Very Good'
                    elif int(site[AQI]) < 67:
                        AQI_dict[AQI] = 'Good'
                    elif int(site[AQI]) < 100:
                        AQI_dict[AQI] = 'Fair'
                    elif int(site[AQI]) < 150:
                        AQI_dict[AQI] = 'Poor'
                    elif int(site[AQI]) < 201:
                        AQI_dict[AQI] = 'Very Poor'
                    else:
                        AQI_dict[AQI] = 'Hazardous'
                except:
                    AQI_dict[AQI] = 'Data not available'
        return AQI_dict

    def exists(site, element):
        if site['name'] == 'Civic' and (element == 'aqi_no2' or element == 'co' or element == 'aqi_co'):
            return 'Data not available'
        else:
            try:
                site[element]
                return site[element]
            except:
                return 'Data not available'

    # specify endpoint
    url = 'https://www.data.act.gov.au/resource/94a5-zqnn.json'

    # specify parameters
    params = {}

    # make GET request
    response = requests.get(url, params=params)

    # load response content into a Python dictionary
    data = json.loads(response.content)

    # dump data into a JSON file
    with open('air_qual.json', 'w') as f:
        json.dump(data, f, indent=4)

    output = []
    for i in range(3):
        site = data[i]
        AQI_dict = AQI_string(site)
        output.append(f"Site: {site['name']}\nCO PM: {exists(site, 'co')}\nCO AQI: {exists(site, 'aqi_co')} ({AQI_dict['aqi_co']})\nNO2 PM: {exists(site, 'no2')}\nNO2 AQI: {exists(site, 'aqi_no2')} ({AQI_dict['aqi_no2']})\nO3 8hr PM: {exists(site, 'o3_8hr')}\nO3 AQI 8hr: {exists(site, 'aqi_o3_8hr')} ({AQI_dict['aqi_o3_8hr']})\nPM10: {exists(site, 'pm10')}\nPM10 AQI: {exists(site, 'aqi_pm10')} ({AQI_dict['aqi_pm10']})\nPM2.5: {exists(site, 'pm2_5')}\nPM2.5 AQI: {exists(site, 'aqi_pm2_5')} ({AQI_dict['aqi_pm2_5']})\nTime Recorded: {site['datetime']}\n")
        output_dict = site['name'] {

        }
        #print(AQI_string(site))

    output = output[0] + '\n' + output[1] + '\n' + output[2]

    await ctx.send(output)


bot.run(TOKEN)
