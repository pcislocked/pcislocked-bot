# bot.py
import os
import random
import discord
import string
from datetime import datetime
from discord.ext import commands
TOKEN = "TÖRE"
GUILD = "617801724345843742"
intents = discord.Intents(messages=True, guilds=True, members = True)
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    activity = discord.Game(name="Bota bir şey mi eklemek istiyorsun? Git kendin ekle amk: https://github.com/pcislocked/pcislocked-bot")
    await client.change_presence(status=discord.Status.idle, activity=activity)
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    verifych = client.get_channel(764880248336154664)
    
@client.event
async def on_member_join(member):
    verifych = client.get_channel(764880248336154664)
    joinlog = client.get_channel(702503861453193216)
    verifyclone = client.get_channel(780207454846844928)
    ment = member.mention
    mid = member.id
    mpp = member.avatar_url
    mjd = member.joined_at
    mcd = member.created_at
    mdm = member.discriminator
    mnc = member.name
    nou = datetime.now()
    await verifyclone.send(f"SABIKA KAYDI:\n kisi: {ment} nick+discrim: {mnc}#{mdm} \nID: {mid}\n pp: {mpp}\n joined at: {mjd}\n account creation: {mcd}")
    await joinlog.send(f"{ment} katıldı\n ID: {mid}\ntimestamp: {nou}")
    await verifych.send(f"hoşgeldin {ment} şimdi buraya bir şeyler yaz ve bekle. içerde de adam gibi davran. \n \n eğer mesaj yazamıyosan telefon doğrulaması yap \n \n doğrulamada ses kontrolü yapmıyoruz o yüzden sese girmen hiç bir şeyi değiştirmez.")
    def rnid(length):
        letters = '0123456789abcdef'
        return ''.join(random.choice(letters) for i in range(length))
    await member.edit(nick=f"new user {rnid(4)}")

    
@client.event
async def on_member_remove(member):
    verifych = client.get_channel(764880248336154664)
    joinlog = client.get_channel(702503861453193216)
    verifyclone = client.get_channel(780207454846844928)
    ment = member.mention
    mid = member.id
    nou = datetime.now()
    await joinlog.send(f"{ment} geberdi\n ID: {mid}\ntimestamp: {nou}")
    await verifyclone.send(f"{ment} çıktı. \n ID: {mid}\ntimestamp: {nou}")


@client.event
async def on_message(message):

    #for debugging only
    # pribnt(message.author)
    # print(message.content)

    if message.channel == client.get_channel(764880248336154664):
        disc = message.author.discriminator
        name = message.author.name
        cont = message.content
        mid = message.author.id
        nou = datetime.now()
        logch = client.get_channel(780207454846844928)
        await logch.send(f"{name}#{disc}: {cont}\nID: {mid} - timestamp: {nou}")
        
    if message.author == client.user:
        return
        
    if message.content == 'sa' or message.content == 'SA' or message.content == 'sA' or message.content == 'Sa':
        verifych = client.get_channel(764880248336154664)
        if message.channel == verifych:
            ment=message.author.mention
            member=message.author
            await message.delete()
            await message.channel.send(f"madem verifyda sa yazdın siktir git o zaman {ment}")
            await member.kick(reason="verify sa pcislockedbot")
            await message.channel.send(f"{ment} = atıldı 🕋")
        else:
            n = random.randint(1,3)
            if n == 1 or n == 3:
                await message.channel.send("burası cami mi orospu evladı")
            if n == 2:
                await message.channel.send("devam edersen sonun böyle olur orospu çocuğu https://www.youtube.com/watch?v=PHkL6xGGU_U")

    if message.content == 'as' or message.content == 'AS' or message.content == 'As' or message.content == 'aS':
        ment=message.author.mention
        await message.channel.send(f"ulan allahın selamını almayacaksın demedik mi {ment}")

    if message.content == 'ass':
        ment=message.author.mention
        await message.channel.send("lol")

    if message.content == 'Selamın aleyküm' or message.content == 'selamın aleyküm' or message.content == 'Selamin aleyküm' or message.content == 'selamin aleyküm' or message.content == 'Selamın aleykum' or message.content == 'selamın aleykum' or message.content == 'Selamin aleykum' or message.content == 'selamin aleykum' or message.content == 'Selamın Aleyküm' or message.content == 'selamın Aleyküm' or message.content == 'Selamin Aleyküm' or message.content == 'selamin Aleyküm' or message.content == 'Selamın Aleykum' or message.content == 'selamın Aleykum' or message.content == 'Selamin Aleykum' or message.content == 'selamin Aleykum':
        await message.channel.send("niye zorluyorsun orospu evladı ban yemek için mi")
        
    if message.content == 'ataturk' or message.content == 'atatürk' or message.content == 'Ataturk' or message.content == 'Atatürk':
        await message.channel.send("ağla https://www.youtube.com/watch?v=j1QK2jzy_LI")

    if message.content == 'osmanlı' or message.content == 'osmanli' or message.content == 'Osmanlı' or message.content == 'Osmanli':
        await message.channel.send("ağla https://www.youtube.com/watch?v=8Rvqc4-EWNE")

    if message.content == 'khontkar':
        await message.channel.send("trap müzik değil saçmalıktır")

    if message.content == 'sik kırığı':
        await message.channel.send("ben sana küfretmedim yarramın kafası")

    if message.content == 'allah' or message.content == 'Allah' or message.content == '🕋':
        await message.channel.send("https://cdn.discordapp.com/attachments/629749813440675872/726923126537191424/atat.jpg")

    if message.content == 'aw':
        await message.channel.send("aw kullanmayın dejenere orospu çocukları")

    if message.content == 'tomris':
        await message.add_reaction('♿')
        await message.channel.send("https://media.discordapp.net/attachments/742459973556240386/743092135791820830/unknown.png")

    if message.content == 'tunahan':
        await message.add_reaction('🇬')
        await message.add_reaction('🇦')
        await message.add_reaction('🇾')

    if message.content == 'Fortnite' or message.content == 'fortnite':
        await message.add_reaction('🇬')
        await message.add_reaction('🇦')
        await message.add_reaction('🇾')
        await message.channel.send("when you ask to god for help but god said https://media.discordapp.net/attachments/629749813440675872/741600181253963826/Screenshot_20200808_131408_com.discord.jpg")

    if message.content == 'kurt' or message.content == 'kürt' or message.content == 'Kurt' or message.content == 'Kürt' or message.content == 'kurd' or message.content == 'kürd' or message.content == 'Kurd' or message.content == 'Kürd':
        await message.channel.send("https://www.youtube.com/watch?v=5xyb8uC92pI&t=56")
        
    if message.content == '31'or message.content == '30+1' or message.content == '20+11':
        n = random.randint(8,24)
        def rndmz(length):
            letters = 'ASDASDASDASDASDASDasdasdasdasdasdasdqweqweqweqweqwqweQWEQWEQWEQWEQWEQWEASDASDASDASDASDASDasdasdasdasdasdasdqweqweqweqweqwqweQWEQWEQWEQWEQWEQWEASDASDASDASDASDASDasdasdasdasdasdasdqweqweqweqweqwqweQWEQWEQWEQWEQWEQWE:::::::::::::::::qwerwtyuüıopğüşlkjhgfdsaxzcvbnmöç.1432567890PREWTYUIOPĞÜŞLAFDGHKXMC'
            return ''.join(random.choice(letters) for i in range(length))
        await message.channel.send(f"{rndmz(n)}")

    if message.content == 'dinozor' or message.content == 'dinazor' or message.content == 'Dinozor' or message.content == 'Dinazor':
        await message.channel.send("https://www.youtube.com/watch?v=9pV8tMQ92Dc")
           
    if message.content == 'kadın' or message.content == 'Kadın' or message.content == 'kadınlar' or message.content == 'Kadınlar':
        await message.channel.send("https://media.discordapp.net/attachments/742459973556240386/743147623782940692/unknown.png")
           
    if message.content == 'keloğlan gülüyor' or message.content == 'Keloğlan gülüyor' or message.content == 'Keloğlan Gülüyor' or message.content == 'keloğlan gülüyor.' or message.content == 'KELOĞLAN GÜLÜYOR' or message.content == 'KELOĞLAN GÜLÜYOR.' or message.content == 'Keloğlan gülüyor.' or message.content == 'Keloğlan Gülüyor.':
        await message.channel.send("https://cdn.discordapp.com/attachments/742459973556240386/757715660007538809/keloglan_guluyor.mp4")
           
    if message.content == 'burak oyunda' or message.content == 'Burak oyunda' or message.content == 'burak Oyunda' or message.content == 'Burak Oyunda':
        await message.channel.send("https://forum.donanimhaber.com/merhaba-arkadaslar-ben-burak-maynkraftin-yennnniii-bolumune-hos-geldinizzzzzz--117861123")
           
    if message.content == 'keloğlan' or message.content == 'keloğlan earrape' or message.content == 'Keloğlan' or message.content == 'Keloğlan earrape' or message.content == 'keloğlan geçiş müziği' or message.content == 'Keloğlan geçiş müziği' or message.content == 'keloğlan Earrape' or message.content == 'keloğlan Geçiş müziği' or message.content == 'Keloğlan geçiş Müziği' or message.content == 'Keloğlan Geçiş Müziği':
        await message.channel.send("https://cdn.discordapp.com/attachments/742459973556240386/757731496776826971/keloglan_gecisi_32db_earrape.mp4")
        
    if message.content == 'Siktir git' or message.content == 'Siktir Git' or message.content == 'siktir git' or message.content == 'siktir Git' or message.content == 'Siktirin gidin' or message.content == 'Siktirin Gidin' or message.content == 'siktirin Gidin' or message.content == 'siktirin gidin':
        await message.channel.send("https://www.youtube.com/watch?v=MpDwtSvM32Y")
        
    if message.content == 'peki' or message.content == 'Peki' or message.content == 'pekı' or message.content == 'Pekı' or message.content == 'PEKİ' or message.content == 'PEKI':
        await message.channel.send("ananın amı peki")

    if message.content == 'lan':
        await message.channel.send("lan")
                        
    if message.content == 'Lan':
        await message.channel.send("Lan")
                    
    if message.content == 'LAN':
        await message.channel.send("LAN")
                        
    if message.content == 'ulan':
        await message.channel.send("ulan")
                        
    if message.content == 'Ulan':
        await message.channel.send("Ulan")
                    
    if message.content == 'ULAN':
        await message.channel.send("ULAN")
                        
    if message.content == 'coronavirus':
        await message.channel.send("Do you mean: human malware")
        
    if message.content == 'sansar suicide' or message.content == 'Sansar suicide' or message.content == 'sansar Suicide' or message.content == 'Sansar Suicide' or message.content == 'SANSAR SUICIDE' or message.content == 'SANSAR SUİCİDE' or message.content == 'sansar suıcıde':
        await message.channel.send("https://cdn.discordapp.com/attachments/695562300295217174/743420436141834280/sansar_suicide.mp4")
       
    if message.content == 'ping':
        pbong = client.latency*1000
        await message.channel.send('pong orospu evladı. discord RTT: {0}ms.'.format(round(pbong, 2)))
        
    if message.content == 'kaşık enes batur' or message.content == 'kasık enes batur' or message.content == 'kaşik enes batur' or message.content == 'kasik enes batur' or message.content == 'KAŞIK ENES BATUR' or message.content == 'KASIK ENES BATUR' or message.content == 'KAŞİK ENES BATUR' or message.content == 'KASİK ENES BATUR':
        await message.channel.send("https://media.discordapp.net/attachments/742459973556240386/778388988624764928/kasik_enes_batur-1.png")

    if message.content == 'götöş' or message.content == 'gotöş' or message.content == 'götoş' or message.content == 'gotoş' or message.content == 'GÖTÖŞ' or message.content == 'GÖTOŞ' or message.content == 'GOTÖŞ' or message.content == 'GOTOŞ' or message.content == 'götös' or message.content == 'gotös' or message.content == 'götos' or message.content == 'gotos' or message.content == 'GÖTÖS' or message.content == 'GÖTOS' or message.content == 'GOTÖS' or message.content == 'GOTOS':
        await message.channel.send("https://media.discordapp.net/attachments/742459973556240386/778381895666761738/gotos.png")
       
    if message.content == 'napim':
        ment=message.author.mention
        await message.channel.send(f"duymamış oliyim, kaşınma 🕋 {ment}", delete_after=20)
        await message.delete()
            

    if message.content == '🤡':
        ment=message.author.mention
        member=message.author
        await message.delete()
        await message.channel.send(f"ananı allahını sikerim senin orospu evladı siktir git {ment}")
        await member.ban(reason="clown emoji pcislockedbot", delete_message_days=0)
        await message.channel.send(f"{ment} = banlandı 🕋")
        
    if message.content == 'göte bak kocaman' or message.content == 'Göte bak kocaman' or message.content == 'gote bak kocaman' or message.content == 'Gote bak kocaman' or message.content == 'GÖTE BAK KOCAMAN' or message.content == 'GOTE BAK KOCAMAN':
        n = random.randint(1,8)
        if n == 1 or n == 3 or n == 5 or n == 7:
            await message.channel.send("https://media.discordapp.net/attachments/742459973556240386/779505199780724746/gote_bak_kocaman_2.jpg")
        if n == 2 or n == 4 or n == 6 or n == 8:
            await message.channel.send("https://media.discordapp.net/attachments/742459973556240386/779505203706986536/gote_bak_kocaman.png")
            
    if message.content == 'töre' or message.content == 'tore' or message.content == 'Töre' or message.content == 'Tore' or message.content == 'TÖRE' or message.content == 'TOREN':
        ng = random.randint(1,99)
        if ng == 31:
            await message.channel.send("https://www.youtube.com/watch?v=fThSYeBoPFw")
        else:
            await message.add_reaction('<:tore:739979995094712504>')
            
client.run(TOKEN)
client.run(TOKEN)
