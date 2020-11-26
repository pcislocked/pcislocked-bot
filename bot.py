# bot.py
import os
import random
import discord
import string
from datetime import datetime
from discord.ext import commands
TOKEN = "türkçe rap"
GUILD = "617801724345843742"
intents = discord.Intents(messages=True, guilds=True, members = True)
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    activity = discord.Game(name="Bota bir şey mi eklemek istiyorsun? Git kendin ekle amk: github: pcislocked-bot")
    await client.change_presence(status=discord.Status.idle, activity=activity)
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    general = client.get_channel(629749813440675872)
    await general.send(f"Bot yeniden başlatıldı.")
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
        
    if message.content.lower() == 'sa' or message.content.lower() == 'SA' or message.content.lower() == 'sA' or message.content.lower() == 'Sa':
        verifych = client.get_channel(764880248336154664)
        if message.channel == verifych:
            ment=message.author.mention
            member=message.author
            await message.delete()
            await message.channel.send(f"madem verifyda sa yazdın siktir git o zaman {ment}")
            await member.kick(reason="verify sa pcislockedbot")
            await message.channel.send(f"{ment} = atıldı 🕋")
        else:
            n = random.randint(1,8)
            if n == 2:
                await message.channel.send("devam edersen sonun böyle olur orospu çocuğu https://www.youtube.com/watch?v=PHkL6xGGU_U")
            else:
                await message.channel.send("burası cami mi orospu evladı")
                
    if message.content.lower() == 'as' or message.content.lower() == 'AS' or message.content.lower() == 'As' or message.content.lower() == 'aS':
        ment=message.author.mention
        await message.channel.send(f"ulan allahın selamını almayacaksın demedik mi {ment}")

    if message.content.lower() == 'ass':
        ment=message.author.mention
        await message.channel.send("lol")

    if message.content.lower() == 'Selamın aleyküm' or message.content.lower() == 'selamın aleyküm' or message.content.lower() == 'Selamin aleyküm' or message.content.lower() == 'selamin aleyküm' or message.content.lower() == 'Selamın aleykum' or message.content.lower() == 'selamın aleykum' or message.content.lower() == 'Selamin aleykum' or message.content.lower() == 'selamin aleykum' or message.content.lower() == 'Selamın Aleyküm' or message.content.lower() == 'selamın Aleyküm' or message.content.lower() == 'Selamin Aleyküm' or message.content.lower() == 'selamin Aleyküm' or message.content.lower() == 'Selamın Aleykum' or message.content.lower() == 'selamın Aleykum' or message.content.lower() == 'Selamin Aleykum' or message.content.lower() == 'selamin Aleykum':
        await message.channel.send("niye zorluyorsun orospu evladı ban yemek için mi")
        
    if message.content.lower() == 'ataturk' or message.content.lower() == 'atatürk' or message.content.lower() == 'Ataturk' or message.content.lower() == 'Atatürk':
        await message.channel.send("ağla https://www.youtube.com/watch?v=j1QK2jzy_LI")

    if message.content.lower() == 'osmanlı' or message.content.lower() == 'osmanli' or message.content.lower() == 'Osmanlı' or message.content.lower() == 'Osmanli':
        await message.channel.send("ağla https://www.youtube.com/watch?v=8Rvqc4-EWNE")

    if message.content.lower() == 'khontkar':
        await message.channel.send("trap müzik değil saçmalıktır")

    if message.content.lower() == 'sik kırığı':
        await message.channel.send("ben sana küfretmedim yarramın kafası")

    if message.content.lower() == 'allah' or message.content.lower() == 'Allah' or message.content.lower() == '🕋':
        await message.channel.send("https://cdn.discordapp.com/attachments/629749813440675872/726923126537191424/atat.jpg")

    if message.content.lower() == 'aw':
        await message.channel.send("aw kullanmayın dejenere orospu çocukları")

    if message.content.lower() == 'tomris':
        await message.add_reaction('♿')
        await message.channel.send("https://media.discordapp.net/attachments/742459973556240386/743092135791820830/unknown.png")

    if message.content.lower() == 'tunahan':
        await message.add_reaction('🇬')
        await message.add_reaction('🇦')
        await message.add_reaction('🇾')

    if message.content.lower() == 'Fortnite' or message.content.lower() == 'fortnite':
        await message.add_reaction('🇬')
        await message.add_reaction('🇦')
        await message.add_reaction('🇾')
        await message.channel.send("when you ask to god for help but god said https://media.discordapp.net/attachments/629749813440675872/741600181253963826/Screenshot_20200808_131408_com.discord.jpg")

    if message.content.lower() == 'kurt' or message.content.lower() == 'kürt' or message.content.lower() == 'Kurt' or message.content.lower() == 'Kürt' or message.content.lower() == 'kurd' or message.content.lower() == 'kürd' or message.content.lower() == 'Kurd' or message.content.lower() == 'Kürd':
        await message.channel.send("https://www.youtube.com/watch?v=5xyb8uC92pI&t=56")
        
    if message.content.lower() == '31'or message.content.lower() == '30+1' or message.content.lower() == '20+11':
        n = random.randint(8,24)
        def rndmz(length):
            letters = 'ASDASDASDASDASDASDasdasdasdasdasdasdqweqweqweqweqwqweQWEQWEQWEQWEQWEQWEASDASDASDASDASDASDasdasdasdasdasdasdqweqweqweqweqwqweQWEQWEQWEQWEQWEQWEASDASDASDASDASDASDasdasdasdasdasdasdqweqweqweqweqwqweQWEQWEQWEQWEQWEQWE:::::::::::::::::qwerwtyuüıopğüşlkjhgfdsaxzcvbnmöç.1432567890PREWTYUIOPĞÜŞLAFDGHKXMC'
            return ''.join(random.choice(letters) for i in range(length))
        await message.channel.send(f"{rndmz(n)}")

    if message.content.lower() == 'dinozor' or message.content.lower() == 'dinazor' or message.content.lower() == 'Dinozor' or message.content.lower() == 'Dinazor':
        await message.channel.send("https://www.youtube.com/watch?v=9pV8tMQ92Dc")
           
    if message.content.lower() == 'kadın' or message.content.lower() == 'Kadın' or message.content.lower() == 'kadınlar' or message.content.lower() == 'Kadınlar':
        await message.channel.send("https://media.discordapp.net/attachments/742459973556240386/743147623782940692/unknown.png")
           
    if message.content.lower() == 'keloğlan gülüyor' or message.content.lower() == 'Keloğlan gülüyor' or message.content.lower() == 'Keloğlan Gülüyor' or message.content.lower() == 'keloğlan gülüyor.' or message.content.lower() == 'KELOĞLAN GÜLÜYOR' or message.content.lower() == 'KELOĞLAN GÜLÜYOR.' or message.content.lower() == 'Keloğlan gülüyor.' or message.content.lower() == 'Keloğlan Gülüyor.':
        await message.channel.send("https://cdn.discordapp.com/attachments/742459973556240386/757715660007538809/keloglan_guluyor.mp4")
           
    if message.content.lower() == 'burak oyunda' or message.content.lower() == 'Burak oyunda' or message.content.lower() == 'burak Oyunda' or message.content.lower() == 'Burak Oyunda':
        await message.channel.send("https://forum.donanimhaber.com/merhaba-arkadaslar-ben-burak-maynkraftin-yennnniii-bolumune-hos-geldinizzzzzz--117861123")
           
    if message.content.lower() == 'keloğlan' or message.content.lower() == 'keloğlan earrape' or message.content.lower() == 'Keloğlan' or message.content.lower() == 'Keloğlan earrape' or message.content.lower() == 'keloğlan geçiş müziği' or message.content.lower() == 'Keloğlan geçiş müziği' or message.content.lower() == 'keloğlan Earrape' or message.content.lower() == 'keloğlan Geçiş müziği' or message.content.lower() == 'Keloğlan geçiş Müziği' or message.content.lower() == 'Keloğlan Geçiş Müziği':
        await message.channel.send("https://cdn.discordapp.com/attachments/742459973556240386/757731496776826971/keloglan_gecisi_32db_earrape.mp4")
        
    if message.content.lower() == 'Siktir git' or message.content.lower() == 'Siktir Git' or message.content.lower() == 'siktir git' or message.content.lower() == 'siktir Git' or message.content.lower() == 'Siktirin gidin' or message.content.lower() == 'Siktirin Gidin' or message.content.lower() == 'siktirin Gidin' or message.content.lower() == 'siktirin gidin':
        await message.channel.send("https://www.youtube.com/watch?v=MpDwtSvM32Y")
        
    if message.content.lower() == 'peki' or message.content.lower() == 'Peki' or message.content.lower() == 'pekı' or message.content.lower() == 'Pekı' or message.content.lower() == 'PEKİ' or message.content.lower() == 'PEKI':
        await message.channel.send("ananın amı peki")

    if message.content.lower() == 'lan':
        await message.channel.send("lan")
                        
    if message.content.lower() == 'Lan':
        await message.channel.send("Lan")
                    
    if message.content.lower() == 'LAN':
        await message.channel.send("LAN")
                        
    if message.content.lower() == 'ulan':
        await message.channel.send("ulan")
                        
    if message.content.lower() == 'Ulan':
        await message.channel.send("Ulan")
                    
    if message.content.lower() == 'ULAN':
        await message.channel.send("ULAN")
                        
    if message.content.lower() == 'coronavirus':
        await message.channel.send("Do you mean: human malware")
        
    if message.content.lower() == 'sansar suicide' or message.content.lower() == 'Sansar suicide' or message.content.lower() == 'sansar Suicide' or message.content.lower() == 'Sansar Suicide' or message.content.lower() == 'SANSAR SUICIDE' or message.content.lower() == 'SANSAR SUİCİDE' or message.content.lower() == 'sansar suıcıde':
        await message.channel.send("https://cdn.discordapp.com/attachments/695562300295217174/743420436141834280/sansar_suicide.mp4")
       
    if message.content.lower() == 'ping':
        pbong = client.latency*1000
        await message.channel.send('pong orospu evladı. discord RTT: {0}ms.'.format(round(pbong, 2)))
        
    if message.content.lower() == 'kaşık enes batur' or message.content.lower() == 'kasık enes batur' or message.content.lower() == 'kaşik enes batur' or message.content.lower() == 'kasik enes batur' or message.content.lower() == 'KAŞIK ENES BATUR' or message.content.lower() == 'KASIK ENES BATUR' or message.content.lower() == 'KAŞİK ENES BATUR' or message.content.lower() == 'KASİK ENES BATUR':
        await message.channel.send("https://media.discordapp.net/attachments/742459973556240386/778388988624764928/kasik_enes_batur-1.png")

    if message.content.lower() == 'götöş' or message.content.lower() == 'gotöş' or message.content.lower() == 'götoş' or message.content.lower() == 'gotoş' or message.content.lower() == 'GÖTÖŞ' or message.content.lower() == 'GÖTOŞ' or message.content.lower() == 'GOTÖŞ' or message.content.lower() == 'GOTOŞ' or message.content.lower() == 'götös' or message.content.lower() == 'gotös' or message.content.lower() == 'götos' or message.content.lower() == 'gotos' or message.content.lower() == 'GÖTÖS' or message.content.lower() == 'GÖTOS' or message.content.lower() == 'GOTÖS' or message.content.lower() == 'GOTOS':
        await message.channel.send("https://media.discordapp.net/attachments/742459973556240386/778381895666761738/gotos.png")
       
    if message.content.lower() == 'napim':
        ment=message.author.mention
        await message.channel.send(f"duymamış oliyim, kaşınma 🕋 {ment}", delete_after=20)
        await message.delete()
            

    if message.content.lower() == '🤡':
        ment=message.author.mention
        member=message.author
        await message.delete()
        await message.channel.send(f"ananı allahını sikerim senin orospu evladı siktir git {ment}")
        await member.ban(reason="clown emoji pcislockedbot", delete_message_days=0)
        await message.channel.send(f"{ment} = banlandı 🕋")
        
    if message.content.lower() == 'göte bak kocaman' or message.content.lower() == 'gote bak kocaman':
        n = random.randint(1,8)
        if n == 1 or n == 3 or n == 5 or n == 7:
            await message.channel.send("https://media.discordapp.net/attachments/742459973556240386/779505199780724746/gote_bak_kocaman_2.jpg")
        if n == 2 or n == 4 or n == 6 or n == 8:
            await message.channel.send("https://media.discordapp.net/attachments/742459973556240386/779505203706986536/gote_bak_kocaman.png")
            
    if message.content.lower() == 'töre' or message.content.lower() == 'tore':
        ng = random.randint(1,99)
        if ng == 31:
            await message.channel.send("https://www.youtube.com/watch?v=fThSYeBoPFw")
        else:
            await message.add_reaction('<:tore:739979995094712504>')
            
    if message.content.lower() == 'pu' or message.content.lower() == 'pü' or message.content.lower() == 'puh' or message.content.lower() == 'püh':
        await message.channel.send('https://media.giphy.com/media/3o6Mb6n1senEQtbgdy/giphy.gif')
        
    if message.content.lower() == 'tm':
        await message.channel.send("tşk")
        
    if message.content.lower() == 'öd' or message.content.lower() == 'od':
        uid = message.author.id
        uth = message.author.mention
        fetchMessage = await channel.history(limit=5).find(lambda m: m.author.id == uid)
        if fetchMessage.content == 'tşk':
            await message.author.ban(reason="tşk öd autoban")
            await message.channel.send(f"{uth} = banlandı 🕋 https://www.youtube.com/watch?v=wnedkVrgFF0")
        else:       
            return
            

client.run(TOKEN)
client.run(TOKEN)
