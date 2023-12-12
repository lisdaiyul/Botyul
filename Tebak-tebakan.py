# belom diedit dan diubah ke kelas bot

import discord
import random
import asyncio


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('$tebak'):
            await message.channel.send('Tebak angka 1 sampai 10.')

            def benar(btul):
                return btul.author == message.author and btul.content.isdigit()

            angka = random.randint(1, 10)

            try:
                tebak = await self.wait_for('message', check=benar, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send(f'lama amat tinggal jawab.')

            if int(tebak.content) == angka:
                await message.channel.send('kamu benar!')
            else:
                await message.channel.send(f'Kamu salah, yang bener {angka}.')


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('token')
