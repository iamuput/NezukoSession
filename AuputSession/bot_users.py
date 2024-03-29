from pyrogram.types import Message
from pyrogram import Client, filters

from env import DATABASE_URL


if DATABASE_URL != '':
    from AuputSession.database import SESSION
    from AuputSession.database.users_sql import Users, num_users


@Client.on_message(~filters.service, group=1)
async def users_sql(_, msg: Message):
    if DATABASE_URL == '':
        return
    if msg.from_user:
        q = SESSION.query(Users).get(int(msg.from_user.id))
        if not q:
            SESSION.add(Users(msg.from_user.id))
            SESSION.commit()
        else:
            SESSION.close()


@Client.on_message(filters.user(1860375797) & filters.command("user"))
async def _stats(_, msg: Message):
    if DATABASE_URL == '':
        return
    users = await num_users()
    await msg.reply(f"Total Users : {users}", quote=True)
