# (©)Codexbotz
# Recode by @mrismanaziz
# Clone by @ItsMeYons
# t.me/SharingUserbot & t.me/Lunatic0de

import pyromod.listen
import sys

from pyrogram import Client

from config import (
    API_HASH,
    APP_ID,
    CHANNEL_ID,
    FORCE_SUB_1,
    FORCE_SUB_2,
    FORCE_SUB_3,
    FORCE_SUB_4,
    LOGGER,
    OWNER,
    TG_BOT_TOKEN,
    TG_BOT_WORKERS,
)


class Bot(Client):
    def init(self):
        super().init(
            "Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={"root": "plugins"},
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN,
        )
        self.LOGGER = LOGGER

    async def start(self):
        try:
            await super().start()
            usr_bot_me = await self.get_me()
            self.username = usr_bot_me.username
            self.namebot = usr_bot_me.first_name
        except Exception as a:
            self.LOGGER(name).warning(a)
            self.LOGGER(name).info(
                "Bot Berhenti. Gabung Group https://t.me/SharingUserbot untuk Bantuan"
            )
            sys.exit()

        if FORCE_SUB_1:
            try:
                link = (await self.get_chat(FORCE_SUB_1)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_1)
                    link = (await self.get_chat(FORCE_SUB_1)).invite_link
                self.invitelink = link
            except Exception as a:
                self.LOGGER(name).warning(a)
                self.LOGGER(name).warning(
                    "Bot tidak dapat Mengambil link invite dari FORCE_SUB_1!"
                )
                self.LOGGER(name).warning(
                    f"Pastikan @{self.username} adalah admin di Channel Tersebut, Chat ID F-Subs Channel Saat Ini: {FORCE_SUB_1}"
                )
                self.LOGGER(name).info(
                    "Bot Berhenti. Gabung Group https://t.me/SharingUserbot untuk Bantuan"
                )
                sys.exit()

        if FORCE_SUB_2:
            try:
                link = (await self.get_chat(FORCE_SUB_2)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_2)
                    link = (await self.get_chat(FORCE_SUB_2)).invite_link
                self.invitelink2 = link
            except Exception as a:
                self.LOGGER(name).warning(a)
                self.LOGGER(name).warning(
                    "Bot tidak dapat Mengambil link invite dari FORCE_SUB_2!"
                )
                self.LOGGER(name).warning(
                    f"Pastikan @{self.username} adalah admin di Group Tersebut, Chat ID F-Subs Group Saat Ini: {FORCE_SUB_2}"
                )
                self.LOGGER(name).info(
                    "Bot Berhenti. Gabung Group https://t.me/SharingUserbot untuk Bantuan"
                )
                sys.exit()

        if FORCE_SUB_3:
            try:
                link = (await self.get_chat(FORCE_SUB_3)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_3)
                    link = (await self.get_chat(FORCE_SUB_3)).invite_link
                self.invitelink3 = link
            except Exception as a:
                self.LOGGER(name).warning(a)
                self.LOGGER(name).warning(
                    "Bot tidak dapat Mengambil link invite dari FORCE_SUB_3!"
                )
                self.LOGGER(name).warning(
                    f"Pastikan @{self.username} adalah admin di Group Tersebut, Chat ID F-Subs Group Saat Ini: {FORCE_SUB_3}"
                )
                self.LOGGER(name).info(
                    "Bot Berhenti. Gabung Group https://t.me/SharingUserbot untuk Bantuan"
                )
                sys.exit()
                
           if FORCE_SUB_4:
            try:
                link = (await self.get_chat(FORCE_SUB_4)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_4)
                    link = (await self.get_chat(FORCE_SUB_4)).invite_link
                self.invitelink4 = link
            except Exception as a:
                self.LOGGER(name).warning(a)
                self.LOGGER(name).warning(
                    "Bot tidak dapat Mengambil link invite dari FORCE_SUB_4!"
                )
                self.LOGGER(name).warning(
                    f"Pastikan @{self.username} adalah admin di Group Tersebut, Chat ID F-Subs Group Saat Ini: {FORCE_SUB_4}"
                )
                self.LOGGER(name).info(
                    "Bot Berhenti. Gabung Group https://t.me/SharingUserbot untuk Bantuan"
                )
                sys.exit()

        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id=db_channel.id, text="Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(name).warning(e)
            self.LOGGER(name).warning(
                f"Pastikan @{self.username} adalah admin di Channel DataBase anda, CHANNEL_ID Saat Ini: {CHANNEL_ID}"
            )
            self.LOGGER(name).info(
                "Bot Berhenti. Silahkan mencari Bantuan"
            )
            sys.exit()

        self.set_parse_mode("html")
        self.LOGGER(name).info(
            f"[🔥 BERHASIL DIAKTIFKAN! 🔥]\n\nBOT Dibuat oleh @{OWNER}\nJika @{OWNER} Membutuhkan Bantuan, Silahkan Minta Bantuan"
        )

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(name).info("Bot stopped.")     






