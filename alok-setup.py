#!/usr/bin/env python3
# (c) https://t.me/TelethonChat/37677
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html

from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("""๐ฟ๐ป๐ด๐ฐ๐๐ด ๐ถ๐พ ๐๐พ my.telegram.org
๐ป๐พ๐ถ๐ธ๐ฝ ๐๐๐ธ๐ฝ๐ถ ๐๐พ๐๐ ๐๐ด๐ป๐ด๐ถ๐๐ฐ๐ผ ๐ฐ๐ฒ๐ฒ๐พ๐๐ฝ๐
๐ฒ๐ป๐ธ๐ฒ๐บ ๐พ๐ฝ ๐ฐ๐ฟ๐ธ ๐ณ๐ด๐๐ด๐ป๐พ๐ฟ๐ผ๐ด๐ฝ๐ ๐๐พ๐พ๐ป๐
๐ฒ๐๐ด๐ฐ๐๐ด ๐ฐ ๐ฝ๐ด๐ ๐ฐ๐ฟ๐ฟ๐ป๐ธ๐ฒ๐ฐ๐๐ธ๐พ๐ฝ, ๐ฑ๐ ๐ด๐ฝ๐๐ด๐๐ธ๐ฝ๐ถ ๐๐ด๐๐๐ธ๐๐ด๐ณ ๐ณ๐ด๐๐ฐ๐ธ๐ป๐
๐๐ด๐ฐ๐ผ  Alok x 
 

Running alok Fire on Termux ๐ฅ๐ฅ๐ฅ๐ฅ....
""")
print("")

APP_ID = int(input("๐ด๐ฝ๐๐ด๐ ๐๐พ๐๐ ๐ฐ๐ฟ๐ธ ๐ท๐ด๐๐ด โ "))
API_HASH = input("๐ด๐ฝ๐๐ด๐ ๐๐พ๐๐ ๐ฐ๐ฟ๐ธ ๐ท๐ฐ๐๐ท ๐ท๐ด๐๐ด โ ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    tele = client.send_message("me", client.session.save())
    tele.reply(
        "โ Hแดสแด ษชs สแดแดส `STRING_SESSION` Oา แดสแดแด แดsแดสสแดแด โ.\n@Alok_x_Support")
    print("")
    print("Bแดสแดแดก ษชs สแดแดส STRING_SESSION. Wแด สแดแด แด แดสsแด sแดแดสแดแด ษชษด แดแดสแดษขสแดแด sแดแด แด แดแดssแดษขแดs")
    print("")
    print("")
    print(client.session.save())
