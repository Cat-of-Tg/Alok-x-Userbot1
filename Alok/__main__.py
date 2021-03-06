import glob
import os
import sys
from sys import argv
from pathlib import Path

import telethon.utils
from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest

from Lucifer import LOGS, bot, luciferver
from Lucifer.LuciferConfig import Var
from Lucifer.utils import load_module,start_mybot, load_pmbot
from pathlib import Path
import telethon.utils
from Alok import CMD_HNDLR

LUCIFER = Var.PRIVATE_GROUP_ID
BOTNAME = Var.TG_BOT_USER_NAME_BF_HER
LOAD_MYBOT = Var.LOAD_MYBOT

# let's get the bot ready
async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)

async def startup_log_all_done():
    try:
        await bot.send_message(LUCIFER, f"**π»lok π±πΎπ πΈπ π³π΄πΏπ»πΎππ΄π³.\nππ΄π½π³** `{CMD_HNDLR}alive` **ππΎ ππ΄π΄ π±πΎπ πΈπ ππΎππΊπΈπ½πΆ πΎπ π½πΎπ.\n\nAdd** @{BOTNAME} **π°π³π³ ππΎ ππ·πΈπ πΈπ½ ππΎππ πΆππΎππΏ π°π½π³ πΌπ°πΊπ΄ π·πΈπΌ π°π³πΌπΈπ½ π΅πΎπ π΄π½π°π±π»πΈπ½πΆ π°π»π» ππ·π΄ π΅π΄π°ππππ΄π πΎπ΅ π»alok π±πΎπ**")
    except BaseException:
        print("Either PRIVATE_GROUP_ID is wrong or you have left the group.")

# Luciferbot starter...
# chal jana bdskπ€§ 
if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        bot.start()

path = 'Lucifer/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

if LOAD_MYBOT == "True":
    path = "Lucifer/plugins/mybot/pmbot/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            load_pmbot(shortname.replace(".py", ""))
    print("TGBot set up completely!")

print("TGBot set up - Level - Basic")
print(
    """
                ----------------------------------------------------------------------
                    Alok X  Κα΄s Κα΄α΄Ι΄ α΄α΄α΄Κα΄Κα΄α΄, α΄α΄ α΄ ΙͺsΙͺα΄ @Alok_x_Support !!
                    Alok α΄ α΄Κ: V1
                    
                ----------------------------------------------------------------------
"""
)

# that's life...
async def lucifer_is_on():
    try:
        if Config.LOGGER_ID != 0:
            await bot.send_file(
                Config.LOGGER_ID,
                HELL_PIC,
                caption=f"#START \n\nDeployed Alok x Successfully\n\n**Alok x. - {alok}**\n\nType {hl}ping or {hl}alive to check! \n\nJoin [support](t.me/alok_x_Support) for any query regarding Alok x userbot",
            )
    except Exception as e:
        LOGS.info(str(e))


    try:
        await bot(JoinChannelRequest("@Alok_x_userbot"))
    except BaseException:
        pass

# Why not come here and chat??
#    try:
#        await bot(JoinChannelRequest("@alok_x_support"))
#    except BaseException:
#        pass


bot.loop.create_task(alok_is_on())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    bot.run_until_disconnected()


#Alok
