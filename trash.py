import discord
from main1 import gen_pass

# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hai, {client.user}! Apa yang saya bisa bantu dengan kau?')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$waktu'):
        await message.channel.send("Inilah 1 tip untuk mengurus waktu dengan baik: Buatlah rencana yang teratur tentang apa yang kau akan melakukan dalam 1 hari.")
    elif message.content.startswith('$uang'):
        await message.channel.send("Inilah 1 tip untuk manajemen uang: Tulis semua pemasukan dan pengeluaran di buku kas fisik/digital. Biasakan diri akan praktis ini.")
    elif message.content.startswith('$bhyplastik'):
        await message.channel.send("Sampah plastik memerlukan waktu ratusan waktu untuk diurai, dapat dimakan secara tidak sengaja oleh hewan laut, dan ketika dibakar, dapat menyebabkan beberapa penyakit mematikan")
    elif message.content.startswith("$bhyrokok"):
        await message.channel.send("Merokok dapat menyebabkan kanker paru-paru bagi perokok dan penghisap asap rokok. Asap rokok mengandung zat-zat bahaya yang bisa merusak paru-paru. Kerusakan tersebut dapat menyebabkan kematian")
    else:
        await message.channel.send(message.content)


client.run("#tokenhere")