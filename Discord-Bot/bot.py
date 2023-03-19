# bot.py
import os
import random
import sys
import sqlite3
import csv
import string
import datetime

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.presences = True

bot = commands.Bot(command_prefix='>', intents=intents)
client = discord.Client(intents=intents)

debug_mode = True

@bot.command(name='jesse', help='Responds with Jesse\'s classic catchphrase.')
async def jesse_auto(ctx):
    try:
        response = 'AUTO-BOTS ROLL OUT.'
        await ctx.send(response)
    except Exception as e:
        if debug_mode:
            await ctx.send(f"Error: {str(e)}")
        return

@bot.command(name='pass', help='Tests passing a string to a function from userinput.')
async def pass_test(ctx, arg1, arg2):
    try:
        response = f"Parameter 1: {arg1}\nParameter 2: {arg2}"
        await ctx.send(response)
    except Exception as e:
        if debug_mode:
            await ctx.send(f"Error: {str(e)}")
        return

@bot.command(name='gavtake', help='Displays the amount of times gavin has made an L take.')
async def gavin_display(ctx):
    try:
        with open(r'Projects\Discord-Bot\l_takes.txt', 'r') as fr:
            count = 0
            for lines in fr:
                count += 1
        response = f"{count} L take(s) have been recorded."
        await ctx.send(response)
    except Exception as e:
        if debug_mode:
            await ctx.send(f"Error: {str(e)}")
        return

@bot.command(name='gavtake_spec', help='Shows the specific L takes when suplied with an index.')
async def gavin_display(ctx, index: int):
    try:
        gavtake_list = []
        with open(r'Projects\Discord-Bot\l_takes.txt', 'r') as fr:
            count = 0
            for lines in fr:
                gavtake_list.append(lines)
            gavtake_list = gavtake_list[index].split('|')
            response = f"Here are Gavin's takes for index {index}:"
            await ctx.send(response)
            for takes in gavtake_list:
                count += 1
                response = f"{count}. {takes.rstrip()}"
                await ctx.send(response)
    except Exception as e:
        if debug_mode:
            await ctx.send(f"Error: {str(e)}")
        return

@bot.command(name='gavtake_index', help='Shows the index for L takes.')
async def gavin_display(ctx):
    try:
        gavtake_list = []
        with open(r'Projects\Discord-Bot\l_takes.txt', 'r') as fr:
            count = 0
            for lines in fr:
                gavtake_list.append(lines)
            for temp in gavtake_list:
                temp = temp.split('|')
                response = f'Index: {count} | \"{temp[0]}\", \"{temp[1]}\" and \"{temp[2].rstrip()}\"'
                count += 1
                await ctx.send(response)
    except Exception as e:
        if debug_mode:
            await ctx.send(f"Error: {str(e)}")
        return

@bot.command(name='multiply', help='Multiplies 2 numbers given from userinput.')
async def multiply(ctx, num1: int, num2: int):
    try:
        response = f"{num1} * {num2} = {num1 * num2}"
        await ctx.send(response)
    except Exception as e:
        if debug_mode:
            await ctx.send(f"Error: {str(e)}")
        return


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


@bot.command(name='readfile_txt', help='Reads a .txt file attached to the message.')
async def read_file_txt(ctx):
    try:
        count = 0
        attachment = ctx.message.attachments[0]
        if attachment.filename.endswith('.txt'):
            file_contents = await attachment.read()
            file_contents_utf8 = file_contents.decode('utf-8')
            lines = file_contents_utf8.split('\n')
            for line in lines:
                count += 1
                if line:
                    with open(f'Projects\\Discord-Bot\\maimai\\{ctx.message.author}.txt', 'a', encoding='utf-8') as fa:
                        fa.write(line)
            await ctx.send(f"Contents written to {ctx.message.author}.txt, content is {count} lines long.")
        else:
            await ctx.send("Please attach a .txt file.")
    except Exception as e:
        if debug_mode:
            await ctx.send(f"Error: {str(e)}")
        return


@bot.command(name='readfile', help='Reads a file attached to the message.')
async def read_file(ctx):
    try:
        attachment = ctx.message.attachments[0]
        file_contents = await attachment.read()
        await ctx.send(f"Contents of {attachment.filename}:```{file_contents.decode()}```")
    except Exception as e:
        if debug_mode:
            await ctx.send(f"Error: {str(e)}")
        return


@bot.command(name='purge_file', help='Deletes everything in {ctx.message.author}.txt')
async def purge_file(ctx):
    try:
        filename = f"Projects\\Discord-Bot\\maimai\\{ctx.message.author}.txt"
        os.remove(filename)
        await ctx.send(f"File {filename} has been purged.")
    except Exception as e:
        if debug_mode:
            await ctx.send(f"Error: {str(e)}")
        return


@bot.command(name='sendfile_txt', help='Sends a .txt file named after the user.')
async def send_file_txt(ctx):
    try:
        with open(f'Projects\\Discord-Bot\\{ctx.message.author}.txt', 'rb') as f:
            await ctx.send(file=discord.File(f))
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
    

@bot.command(name='maiupdate', help='Returns next update for maimai FESTiVAL.')
async def maiupdate(ctx):
    updates = {
"2023-02-03": {
"Rising on the horizon": 14.4,
"ViRTUS": 14.7,
"Trrricksters!!": None,
"VIIIbit Explorer": 14.5
},
"2023-03-10": {
"アマカミサマ": 12.7,
"モンダイナイトリッパー！": 13.7,
"マーシャル・マキシマイザー": 13.1,
"秋の未確認生物": 12.9
},
"2023-03-24": {
"You Mean the World to Me": 13.8,
"Neon Kingdom": 13.8,
"#狂った民族２ PRAVARGYAZOOQA": 14.4,
"VSpook!": 14.4
},
"2023-04-07": {
"Dive into the ZONe": 13.3,
"エナドリおいしいソング": 14.0,
"Maxi": 13.9
},
"2023-04-21": {
"RIFFRAIN": None,
"Falling": None,
"ピリオドサイン": None,
"群青シグナル": None
},
"2023-05-05": {
"Baddest": None,
"ばかみたい【Taxi Driver Edition】": 13.4,
"れっつ！みらくる☆はーどこあっ！": 13.9,
"ジングルベル": 14.7
},
"2023-05-19": {
"Blank Paper (Prod. TEMPLIME)": 12.9,
"In my world (Prod. KOTONOHOUSE)": 13.3,
"アイム・マイヒーロー": 13.2,
"NightTheater": 13.9
},
"2023-06-02": {
"Ghost Dance": 13.3,
"ピュグマリオンの咒文": None,
"電光石火": None,
"Hainuwele": None
},
"2023-06-16": {
"Beat Opera op.1": None,
"星見草": 13.8,
"411Ψ892": 14.4,
"康莊大道": 14.7
},
"2023-06-30": {
"キュートなカノジョ": None,
"へべれけジャンキー": None,
"きゅうくらりん": None,
"回る空うさぎ": None
},
"2023-07-14": {
"Lost Desire": 13.8,
"Alice’s Suitcase": 13.8,
"Aegleseeker": 14.5,
"最強STRONGER": 14.6
},
"2023-07-28": {
"ボッカデラベリタ": 13.1,
"『んっあっあっ。』": 12.8,
"独りんぼエンヴィー": 12.7,
"ロータスイーター": 13.3
}
    }

    try:
        today = datetime.date.today()
        next_update_date = None
        next_update_info = None

        for update_date_str, update_info in updates.items():
            update_date = datetime.datetime.strptime(update_date_str, "%Y-%m-%d").date()
            if update_date > today:
                if next_update_date is None or update_date < next_update_date:
                    next_update_date = update_date
                    next_update_info = update_info

        if next_update_date is not None:
            update_date_str = next_update_date.strftime("%Y-%m-%d")
            days_until_next_update = (next_update_date - today).days
            update_info_str = "\n".join([f"{song}: {difficulty}" for song, difficulty in next_update_info.items()])
            await ctx.send(f"Next maimai FESTiVAL update:\nDate: {update_date_str}\nDays until next update: {days_until_next_update}\n\n{update_info_str}")
        else:
            await ctx.send("No upcoming updates found.")

    except Exception as e:
        if debug_mode:
            await ctx.send(f"Error: {str(e)}")
        return




@bot.command(name='maiprocess', help='Processes your data into a usable format.')
async def maiprocess(ctx):
    try:
        conn = sqlite3.connect(r'C:\Users\joshu\Documents\GitHub\Projects\maimai SQLite\db.sqlite3')
        cur = conn.cursor()

        temp = []
        main = []

        with open(f'Projects\\Discord-Bot\\maimai\\{ctx.message.author}.txt','r',encoding="utf8") as fr:
            for lines in fr:
                lines = lines.replace('	','|')
                lines = lines.split('|')
                for word in lines:
                    word = word.rstrip('\n')
                    temp.append(word)
                main.append(temp)
                temp = []

        cur.execute(f"SELECT songId, version FROM Songs;")
        version = cur.fetchall()

        for score in main:
            for song in version:
                if score[0] == song[0]:
                    score.append(song[1])

        cur.execute(f"SELECT songId, difficulty, internalLevel FROM SheetInternalLevels;")
        float_level = cur.fetchall()
        float_level = [list(item) for item in float_level]

        for word in float_level:
            word[1] = word[1].upper()
            if word[1] == 'REMASTER':
                word[1] = 'RE:MASTER'

        for chart in main:
            found = False
            for song in float_level:
                if chart[0] == song[0] and chart[2].upper() == song[1]:
                    chart.append(song[2])
                    found = True
                    break
            if not found:
                chart.append('N/A')

        temp2 = ''

        with open(f'Projects\\Discord-Bot\\maimai\\{ctx.message.author}.csv','w',encoding="utf8") as fw:
            fw.write('song|genre|difficulty|level|type|score|version|internal_level\n')
            for line in main:
                for word in line:
                    temp2 += word+'|'
                temp2 = temp2.rstrip('|')
                fw.write(temp2 + '\n')
                temp2 = ''

        cur.execute(f"SELECT songId, type, difficulty FROM IntlSheets;")
        all = cur.fetchall()
        all = [list(item) for item in all]

        for i in all:
            if i[1] == 'std':
                i[1] = 'standard'

        for score in all:
            for song in version:
                if score[0] == song[0]:
                    score.append(song[1])

        with open(r'Projects\Discord-Bot\maimai\alldata.csv','w',encoding="utf8") as fw:
            fw.write('song|type|difficulty|version\n')
            for line in all:
                for word in line:
                    temp2 += word+'|'
                temp2 = temp2.rstrip('|')
                fw.write(temp2 + '\n')
                temp2 = ''
        await ctx.send(f"Processing complete.")
    except Exception as e:
        if debug_mode:
            await ctx.send(f"Error: {str(e)}")
        return






@bot.command(name='versionlamp', help='Shows version lamp progress assuming the bot has read your playerdata and processed it.')
async def versionlamp(ctx, version, difficulty, rank):
    try:
        levels = ['1', '2', '3', '4', '5', '6', '7', '7+', '8', '8+', '9', '9+', '10', '10+', '11', '11+', '12', '12+', '13', '13+', '14', '14+', '15']
        versions = ['maimai', 'maimai PLUS', 'GreeN', 'GreeN PLUS', 'ORANGE', 'ORANGE PLUS', 'PiNK', 'PiNK PLUS', 'MiLK', 'MiLK PLUS', 'FiNALE']
        difficulties = ['BASIC', 'ADVANCED', 'EXPERT', 'MASTER', 'RE:MASTER']
        ranks = {'D':0,'C':49.9999,'B':59.9999,'BB':69.9999,'BBB':74.9999,'A':79.9999,'AA':89.9999,'AAA':93.9999,'S':96.9999, 'S+':97.9999,'SS':98.9999, 'SS+':99.4999,'SSS':99.9999,'SSS+':100.4999, 0:0, 'CLEAR':0.0001}


        #version = input('Version? (std only) ')
        if version == 'None':
            version = None
        if version not in versions and version != None:
            print('Invalid version.')
            #input("Press Enter to exit...")
            return
        #difficulty = input('Difficulty? ')
        if difficulty == 'None':
            difficulty = None
        if difficulty == 'REMASTER':
            difficulty = 'RE:MASTER'
        if difficulty not in difficulties and difficulty != None:
            print('Invalid difficulty.')
            #input("Press Enter to exit...")
            return
        #level = input('Level? ')
        level = 'None'
        if level == 'None':
            level = levels
        #rank = input('Rank? ')
        if rank == 'None':
            rank = 0
        if rank not in ranks and rank != 0:
            print('Invalid rank.')
            #input("Press Enter to exit...")
            return

        temp_list = []
        check_list = []
        count = 0
        #version = 'maimai'
        #difficulty = 'MASTER'
        #level = ''
        #rank = 'S'



        with open(f'Projects\\Discord-Bot\\maimai\\{ctx.message.author}.csv', 'r', encoding="utf8") as f:
            for line in csv.DictReader(f, delimiter='|'):
                line['score'] = line['score'].rstrip('%')
                if line['version'] == version and line['difficulty'].upper() == difficulty and line['level'] in level and float(line['score']) > ranks[rank]:
                        #print(f"{line['song']}, {line['difficulty']}, {line['level']}, {line['internal_level']}, {line['score']}, {line['version']}")
                        temp_list = [line['song'], line['difficulty']]
                        check_list.append(temp_list)
                        count += 1
                        temp_list = []

        print(f"Total that match the criteria: {count}")
        await ctx.send(f"Total that match the criteria: {count}")
        count = 0

        with open(r'Projects\Discord-Bot\maimai\alldata.csv', 'r', encoding="utf8") as f:
            for line in csv.DictReader(f, delimiter='|'):
                if line['difficulty'].upper() == difficulty and line['song'] not in [item[0] for item in check_list] and line['version'] == version:
                        print("Not in check_list:", line['song'], line['difficulty'], line['version'])
                        await ctx.send(f"Not in check_list: {line['song']} {line['difficulty']} {line['version']}")
                        count += 1
        print(f"Total that dont match criteria: {count}")
        await ctx.send(f"Total that dont match criteria: {count}")
        #time.sleep(5)
        #input("Press Enter to exit...")
    except Exception as e:
        if debug_mode:
            await ctx.send(f"Error: {str(e)}")
        return





last_messages = {}
@bot.event
async def on_message(message):
    temp = ''
    if message.author == client.user:
        return
    if 'gavin' in message.content.lower() and 'l' in message.content.lower() and 'take' in message.content.lower():
        response = f'L take detected, adding to database.\n\"{last_messages[str(message.author)][0]}\", \"{last_messages[str(message.author)][1]}\" and \"{last_messages[str(message.author)][2]}\" added to database.'
        await message.channel.send(response)
        with open(r'Projects\Discord-Bot\l_takes.txt', 'a') as fa:
            for msg in last_messages[str(message.author)]: 
                temp += (msg + '|')
            fa.write(temp.rstrip('|') + '\n')

 # Check if the message is from a specific user (e.g. User#1234)
    if str(message.author) == 'Pugking4#1713':
        # Check if the user is already in the dictionary
        if str(message.author) in last_messages:
            # If the user is already in the dictionary, append the new message to the list
            last_messages[str(message.author)].append(message.content)
            # If the list has more than 3 messages, remove the oldest message
            if len(last_messages[str(message.author)]) > 3:
                last_messages[str(message.author)].pop(0)
        else:
            # If the user is not already in the dictionary, create a new list with the current message
            last_messages[str(message.author)] = [message.content]
            
        # Do something with the last 3 messages
        #if len(last_messages[str(message.author)]) == 3:
            # For example, you can print the last 3 messages to the console
            #print(f"Last 3 messages from {message.author}: {last_messages[str(message.author)]}")
    with open(r'Projects\Discord-Bot\chat_log.txt', 'a') as fa:
        fa.write(str(message.author) + '|' + message.content + '\n')
    await bot.process_commands(message)


bot.run(TOKEN)
