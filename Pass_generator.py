import random

@bot.command()
async def buat_pass(hasil, panjang_pass = 10):
    elemen = "1234567890!@#$%^&*()~`_-+=|\}]{[';:,<.>/?qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    password = ""

    for i in range(panjang_pass):
        password += random.choice(elemen)

    await hasil.send("password kamu adalah =>   " + password)

bot.run("TOKEN")
