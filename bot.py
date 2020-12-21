# This Python file uses the following encoding: utf-8
# bot.py
import os
import random
import asyncio
import discord
import string
from datetime import datetime
from discord.ext import commands
from datetime import time
from discord.utils import get
from dotenv import load_dotenv
import os
import re
import json
from urllib.request import urlopen

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
GUILD = "617801724345843742"
intents = discord.Intents(messages=True, guilds=True, members = True)
client = discord.Client(intents=intents)

#invite tracker translated and implemented for usage
#repo: https://github.com/GregTCLTK/Discord-Invite-Tracker/blob/master/bot.py

invites = {}
last = ""

async def fetch():
    global last
    global invites
    await client.wait_until_ready()
    gld = client.get_guild(int(617801724345843742))
    logs = client.get_channel(780207454846844928)
    while True:
        invs = await gld.invites()
        tmp = []
        for i in invs:
            for s in invites:
                if s[0] == i.code:
                    if int(i.uses) > s[1]:
                        usr = gld.get_member(int(last))
                        eme = discord.Embed(description="Davet link takibi", color=0x03d692, title=" ")
                        eme.set_author(name=usr.name + "#" + usr.discriminator, icon_url=usr.avatar_url)
                        eme.set_footer(text="Kullanıcı ID: " + str(usr.id))
                        eme.timestamp = usr.joined_at
                        eme.add_field(name="Kullanılan davet:",
                                      value="Daveti açan: " + i.inviter.mention + " (`" + i.inviter.name + "#" + i.inviter.discriminator + "`)\nInvite ID: `" + i.code + "`\nŞu ana kadarki kullanım: `" + str(
                                          i.uses) + "`", inline=False)
                        await logs.send(embed=eme)
            tmp.append(tuple((i.code, i.uses)))
        invites = tmp
        await asyncio.sleep(1)

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
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data = json.load(response)

    IP=data['ip']
    org=data['org']
    city = data['city']
    country=data['country']
    region=data['region']
    await general.send(f"Bot yeniden başlatıldı. Sunucu lokasyonu: {city}") 
    verifych = client.get_channel(764880248336154664)
    modlounge = client.get_channel(702562505905668137)
    IPx="niggers"
    await modlounge.send(f"Bot yeniden başlatıldı.\nIP: {IPx}\norg: {org}\ncity: {city}\ncountry: {country}\nregion: {region}")
@client.event
async def on_member_join(member):
    guildd = client.get_guild(617801724345843742)
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
    evr = discord.utils.get(guildd.roles, id=617801724345843742)
    def rnid(length):
        letters = '0123456789abcdef'
        return ''.join(random.choice(letters) for i in range(length))
    await member.edit(nick=f"new user {rnid(4)}")
    await verifyclone.send(f"SABIKA KAYDI:\n kisi: {ment} nick+discrim: {mnc}#{mdm} \nID: {mid}\n pp: {mpp}\n joined at: {mjd}\n account creation: {mcd}")
    await joinlog.send(f"{ment} katıldı\n ID: {mid}\ntimestamp: {nou}")
    noz = datetime.now()
    noc = noz.strftime("%H")
    # invite tracker code start - not coded by pcislocked
    global last
    last = str(member.id)
    # invite tracker code end
    # print(noc)
    # tr saatiyle 03:00-09:00 kapalı
    # utc 6dan küçükse kapalı diğer türlü açık
    
    # if int(6) > int(noc):
        # # print("before 7utc")
        # await verifych.set_permissions(target=evr, read_messages=True,
                                                   # send_messages=False)
        # await verifych.send(f"ulan amk manyağı {ment}")
        # await verifych.send("bu saatte ne işin var burda")
        # await verifych.send("yat aşşa sabah bakıcam ben sana")
    # else:
        # await verifych.set_permissions(target=evr, read_messages=True,
                                                   # send_messages=True)
        # await verifych.send(f"hoşgeldin dostum {ment}") 
        # await verifych.send("sen şimdi kurallara murallara falan bak eğer sana uyuyorsa tamam de burda, sonra robot olmayan birileri seninle ilgilensinler.")
        # await verifych.send(f"içerde de adam gibi davran.")
        # await verifych.send("eğer mesaj yazamıyosan telefon doğrulaması yap")
        # await verifych.send("sese senden istenmediği sürece girmene gerek yok, kuralları kabul ettiğini söyleyip beklemen yeterli.")
        # await verifych.send("admin tagleyebilirsin ama spam yapma sonra vah ben niye ban yedim diye de ağlama")


## töre


    # if int(7) > int(noc):
        # # print("before 7utc")
        # await verifych.set_permissions(target=evr, read_messages=True,
                                                   # send_messages=False)
        # await verifych.send(f"hoşgeldin {ment}, şu anda yeni üye almıyoruz. Yeni üye alımları Türkiye saati ile 10:00'da açılacak. \n **NOT: izinlerin güncelleştirilebilmesi için sunucudan çıkıp geri girmen gerekebilir.** Sunucu davetini nereden aldıysan oradan yine geri girersin sıkıntı olmaz.")
    # elif int(noc) < int(20):
        # await verifych.set_permissions(target=evr, read_messages=True,
                                                   # send_messages=True)
        # # print("before 20utc")
        # await verifych.send(f"hoşgeldin {ment} şimdi buraya bir şeyler yaz ve bekle. içerde de adam gibi davran. \n \n eğer mesaj yazamıyosan telefon doğrulaması yap\n \n doğrulamada ses kontrolü yapmıyoruz o yüzden sese girmen hiç bir şeyi değiştirmez.")
    # elif int(noc) == int(20):
        # # print("during 20utc")
        # await verifych.set_permissions(target=evr, read_messages=True,
                                                   # send_messages=False)
        # await verifych.send(f"hoşgeldin {ment}, şu anda yeni üye almıyoruz. Yeni üye alımları Türkiye saati ile 10:00'da açılacak. \n **NOT: izinlerin güncelleştirilebilmesi için sunucudan çıkıp geri girmen gerekebilir.** Sunucu davetini nereden aldıysan oradan yine geri girersin sıkıntı olmaz.")
    # elif int(noc) > int(20):
        # # print("after 20utc")
        # await verifych.set_permissions(target=evr, read_messages=True,
                                                   # send_messages=False)
        # await verifych.send(f"hoşgeldin {ment}, şu anda yeni üye almıyoruz. Yeni üye alımları Türkiye saati ile 10:00'da açılacak. \n **NOT: izinlerin güncelleştirilebilmesi için sunucudan çıkıp geri girmen gerekebilir.** Sunucu davetini nereden aldıysan oradan yine geri girersin sıkıntı olmaz.")
    # else:
        # print(noc)
        # print("epic bruh moment at line 62")
        # await verifych.send(f"hoşgeldin {ment} şimdi buraya bir şeyler yaz ve bekle. içerde de adam gibi davran. \n \n eğer mesaj yazamıyosan telefon doğrulaması yap(veya sabah 10'u bekle.) \n \n doğrulamada ses kontrolü yapmıyoruz o yüzden sese girmen hiç bir şeyi değiştirmez. \n (line 69)TEKNİK HATA: SAAT BİLGİSİ ALINAMADI")
        # return

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

    memberid=message.author.id
    # for debugging only
    # print(message.author)
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
        
    if message.content.lower() == 'sa':
        verifych = client.get_channel(764880248336154664)
        if message.channel == verifych:
            ment=message.author.mention
            member=message.author
            await message.delete()
            await message.channel.send(f"madem verifyda sa yazdın siktir git o zaman {ment} \n\n 5 saniye sonra kickleneceksin son sözlerini söyle")
            await asyncio.sleep(5)
            await member.kick(reason="verify sa pcislockedbot")
            await message.channel.send(f"{ment} = atıldı 🕋")
        else:
            n = random.randint(1,8)
            if n == 2:
                await message.channel.send("devam edersen sonun böyle olur orospu çocuğu https://www.youtube.com/watch?v=PHkL6xGGU_U")
            else:
                await message.channel.send("burası cami mi orospu evladı")
                
    if message.content.lower() == 'as':
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
        await message.channel.send("This video meme below depicts an oldschool Turkish rapper, Sansar Salvo, loading a gun and putting it on his head, then looking at the gun thoughtfully, while the beat of the \"Şimdilerde Hayal\" song plays in the background. This section of the video was originally from his promotion video for the 21 gram mixtape, which is a mixtape that generally consists of melancholic and emotional songs.\nhttps://cdn.discordapp.com/attachments/695562300295217174/743420436141834280/sansar_suicide.mp4")
       
    if message.content.lower() == 'sansar suicide all' or message.content.lower() == 'sansar suicide full':
        await message.channel.send("This video meme below depicts an oldschool Turkish rapper, Sansar Salvo, loading a gun and putting it on his head, then looking at the gun thoughtfully, while the beat of the \"Şimdilerde Hayal\" song plays in the background. This section of the video was originally from his promotion video for the 21 gram mixtape, which is a mixtape that generally consists of melancholic and emotional songs. \n Aşağıdaki meme videosu eski Türk rapçi Sansar Salvo'yu, arkada \"Şimdilerde Hayal\" şarkısının melodisi çalarken bir silahın ağzına mermiyi verdikten sonra silahı kafasına dayayıp sonrasında silaha düşünceli bir şekilde bakarken gösteriyor.  Videonun bu kısmı duygusal ve melankolik şarkılar içeren 21 gram mixtape'inin tanıtım videosundan.\n تصور ميم الفيديو أدناه مغني الراب التركي من المدرسة القديمة ، سانسار سالفو ، وهو يحمل مسدسًا ويضعه على رأسه ، ثم ينظر إلى البندقية بعناية ، بينما يتم تشغيل إيقاع أغنية \"سيمديليردي هايال\" في الخلفية. كان هذا الجزء من الفيديو في الأصل من مقطع الفيديو الترويجي الخاص به لشريط مزيج 21 جرام ، وهو عبارة عن شريط مختلط يتكون عمومًا من أغاني حزينة وعاطفية. \n Deze video-meme hieronder toont een ouderwetse Turkse rapper, Sansar Salvo, die een pistool laadt en het op zijn hoofd legt, en vervolgens bedachtzaam naar het pistool kijkt, terwijl het ritme van het \"Şimdilerde Hayal\" -lied op de achtergrond speelt. Dit gedeelte van de video kwam oorspronkelijk uit zijn promotievideo voor de mixtape van 21 gram, een mixtape die meestal bestaat uit melancholische en emotionele liedjes.")
        await asyncio.sleep(1)
        await message.channel.send("Ce meme vidéo ci-dessous représente un rappeur turc oldschool, Sansar Salvo, chargeant une arme à feu et la mettant sur sa tête, puis regardant l'arme pensivement, tandis que le rythme de la chanson \"Şimdilerde Hayal\" joue en arrière-plan. Cette section de la vidéo était à l'origine de sa vidéo promotionnelle pour la mixtape de 21 grammes, qui est une mixtape généralement composée de chansons mélancoliques et émotionnelles. \n Dieses Video-Meme unten zeigt einen türkischen Rapper der alten Schule, Sansar Salvo, der eine Waffe lädt und auf den Kopf legt und dann nachdenklich auf die Waffe schaut, während im Hintergrund der Beat des Songs \"Şimdilerde Hayal\" spielt. Dieser Abschnitt des Videos stammt ursprünglich aus seinem Werbevideo für das 21-Gramm-Mixtape, ein Mixtape, das im Allgemeinen aus melancholischen und emotionalen Songs besteht. \n Dieses Video-Meme unten zeigt einen türkischen Rapper der alten Schule, Sansar Salvo, der eine Waffe lädt und auf den Kopf legt und dann nachdenklich auf die Waffe schaut, während im Hintergrund der Beat des Songs \"Şimdilerde Hayal\" spielt. Dieser Abschnitt des Videos stammt ursprünglich aus seinem Werbevideo für das 21-Gramm-Mixtape, ein Mixtape, das im Allgemeinen aus melancholischen und emotionalen Songs besteht. ")
        await asyncio.sleep(1)
        await message.channel.send("Dieses Video-Meme unten zeigt einen türkischen Rapper der alten Schule, Sansar Salvo, der eine Waffe lädt und auf den Kopf legt und dann nachdenklich auf die Waffe schaut, während im Hintergrund der Beat des Songs \"Şimdilerde Hayal\" spielt. Dieser Abschnitt des Videos stammt ursprünglich aus seinem Werbevideo für das 21-Gramm-Mixtape, ein Mixtape, das im Allgemeinen aus melancholischen und emotionalen Songs besteht. \n 以下のこのビデオミームは、「ŞimdilerdeHayal」の曲のビートがバックグラウンドで再生されている間、昔ながらのトルコのラッパー、Sansar Salvoが銃を装填して頭に置き、銃を注意深く見ている様子を描いています。ビデオのこのセクションは、元々、21グラムのミックステープのプロモーションビデオからのものでした。ミックステープは、一般的にメランコリックで感情的な曲で構成されています。 \n В этом видео-меме ниже изображен олдскульный турецкий рэпер Сансар Сальво, заряжающий пистолет и надевающий его на голову, а затем задумчиво смотрящий на пистолет, в то время как на заднем фоне играет ритм песни «Şimdilerde Hayal». Этот фрагмент видео был взят из его промо-ролика для 21-граммового микстейпа, который обычно состоит из меланхоличных и эмоциональных песен.")
        await asyncio.sleep(1)
        await message.channel.send("Este video meme muestra a un rapero turco de la vieja escuela, Sansar Salvo, cargando un arma y poniéndola en su cabeza, luego mirando el arma pensativamente, mientras el ritmo de la canción \"Şimdilerde Hayal\" suena de fondo. Esta sección del video fue originalmente de su video promocional para el mixtape de 21 gramos, que es un mixtape que generalmente consiste en canciones melancólicas y emocionales. \n วิดีโอมีมด้านล่างนี้แสดงให้เห็นถึง Sansar Salvo แร็ปเปอร์ชาวตุรกีในโรงเรียนเก่ากำลังบรรจุปืนและวางไว้บนหัวของเขาจากนั้นมองไปที่ปืนอย่างครุ่นคิดในขณะที่จังหวะของเพลง \"Şimdilerde Hayal\" เล่นอยู่เบื้องหลัง วิดีโอส่วนนี้มีพื้นเพมาจากวิดีโอโปรโมตของเขาสำหรับมิกซ์เทป 21 กรัมซึ่งเป็นมิกซ์เทปที่โดยทั่วไปประกอบด้วยเพลงเศร้าและสะเทือนอารมณ์ \nذیل میں اس ویڈیو میں پرانے اسکول کے ایک ترک ریپر ، سنسار سالو کو دکھایا گیا ہے ، جس میں ایک بندوق بھری ہوئی ہے اور اسے اپنے سر پر رکھا ہے ، پھر بندوق کو سوچ سمجھ کر دیکھا ، جب کہ ""میلڈرڈ حائ\\ل\\\" گانا کی تھیپ پس منظر میں ادا کرتی ہے۔ ویڈیو کا یہ حصہ اصل میں اس کے 21 گرام مکسٹیپ کے پروموشنل ویڈیو سے تھا ، جو ایک ایسا میکسٹیپ ہے جو عام طور پر میلانچولک اور جذباتی گانوں پر مشتمل ہوتا ہے۔ ")
        await asyncio.sleep(1)
        await message.channel.send(" క్రింద ఉన్న ఈ వీడియో పోటిలో ఓల్డ్‌స్కూల్ టర్కిష్ రాపర్, సన్సార్ సాల్వో, తుపాకీని ఎక్కించి, అతని తలపై ఉంచడం, ఆపై తుపాకీని ఆలోచనాత్మకంగా చూడటం, \"Şimdilerde Hayal\" పాట యొక్క బీట్ నేపథ్యంలో ప్లే అవుతుంది. వీడియో యొక్క ఈ విభాగం మొదట 21 గ్రాముల మిక్స్‌టేప్ కోసం అతని ప్రచార వీడియో నుండి వచ్చింది, ఇది సాధారణంగా మెలాంచోలిక్ మరియు ఎమోషనల్ పాటలను కలిగి ఉన్న మిక్స్‌టేప్. \n Denne video-meme nedenfor viser en oldschool tyrkisk rapper, Sansar Salvo, som laster en pistol og legger den på hodet, så ser på pistolen omtenksomt, mens rytmen til \"Şimdilerde Hayal\" -sangen spiller i bakgrunnen. Denne delen av videoen var opprinnelig fra hans reklamevideo for 21 gram mixtape, som er en mixtape som generelt består av melankolske og emosjonelle sanger. \n ചുവടെയുള്ള ഈ വീഡിയോ മെമ്മിൽ ഒരു പഴയ ടർക്കിഷ് റാപ്പർ സൻസാർ സാൽവോ ഒരു തോക്ക് കയറ്റി തലയിൽ വയ്ക്കുന്നു, തുടർന്ന് തോക്കിനെ ചിന്താപൂർവ്വം നോക്കുന്നു, അതേസമയം \"ഇംഡിലർഡെ ഹയാൽ\" ഗാനത്തിന്റെ പശ്ചാത്തലത്തിൽ പ്ലേ ചെയ്യുന്നു. 21 ഗ്രാം മിക്സ്‌റ്റേപ്പിനായുള്ള അദ്ദേഹത്തിന്റെ പ്രൊമോഷണൽ വീഡിയോയിൽ നിന്നാണ് വീഡിയോയുടെ ഈ ഭാഗം ആദ്യം ലഭിച്ചത്, ഇത് സാധാരണയായി മെലാഞ്ചോളിക്, വൈകാരിക ഗാനങ്ങൾ ഉൾക്കൊള്ളുന്ന ഒരു മിക്‍ടേപ്പ് ആണ്. \n 아래의이 비디오 밈은 구식 터키 래퍼 Sansar Salvo가 총을 장전하고 머리에 얹은 다음 신중하게 총을 바라 보는 동안 \"Şimdilerde Hayal\"노래의 비트가 배경에서 재생되는 모습을 보여줍니다. 비디오의이 섹션은 원래 그의 21 그램 믹스 테이프 홍보 비디오에서 가져온 것으로, 일반적으로 우울하고 감성적 인 노래로 구성된 믹스 테이프입니다.")
        await asyncio.sleep(1)
        await message.channel.send("Video meme di bawah ini menggambarkan seorang rapper sekolah tua Turki, Sansar Salvo, memasukkan pistol dan meletakkannya di kepalanya, lalu melihat pistol itu dengan serius, sementara irama lagu \"Şimdilerde Hayal\" diputar di latar belakang. Bagian video ini awalnya dari video promosinya untuk mixtape 21 gram, yang merupakan mixtape yang umumnya terdiri dari lagu-lagu melankolis dan emosional. \n Tento videonahrávka níže zobrazuje tureckého rappera ze staré školy Sansara Salva, který nabil zbraň, nasadil si ji na hlavu a zamyšleně se díval na zbraň, zatímco v pozadí hraje rytmus písně „Şimdilerde Hayal“. Tato část videa byla původně z jeho propagačního videa k 21 gramovému mixu, což je mix, který se obvykle skládá z melancholických a emotivních písní. \n ქვემოთ მოცემულ ამ ვიდეო მემზე გამოსახულია ძველი სკოლის თურქი რეპერი, სანსარ სალვო, რომელიც იარაღს იტვირთებს და თავზე აყენებს, შემდეგ კი იარაღს გააზრებულად უყურებს, ხოლო \"dimdilerde Hayal\" სიმღერის ცემა უკანა პლანზე თამაშობს. ვიდეოს ეს მონაკვეთი წარმოიშვა მისი სარეკლამო ვიდეოდან 21 გრამიანი მიქსტეიპისთვის, რომელიც არის მიქსტეიპი, რომელიც ძირითადად მელანქოლიური და ემოციური სიმღერებისგან შედგება.")
        await asyncio.sleep(1)
        await message.channel.send("Ez az alábbi videomém egy régi iskolai török ​​rappert, Sansar Salvót ábrázolja, amint fegyvert tölt be és a fejére teszi, majd elgondolkodva nézi a fegyvert, miközben a háttérben az \"Şimdilerde Hayal\" dal üteme játszik. A videó ezen része eredetileg a 21 grammos mixtape promóciós videójából származik, amely egy mix, amely általában melankolikus és érzelmes dalokból áll. \n Төмөндөгү бул видео мемде эски мектептеги түрк рэпери Сансар Салво мылтыкты жүктөп, башына коюп, андан кийин мылтыкты ойлонуп карап жатып, \"Шимдилерде Хаял\" ырынын фону артта ойноп жатканы тартылган. Видеонун бул бөлүмү алгач анын 21 граммдык микстейптин жарнамалык ролигинен алынган, ал жалпысынан меланхолик жана эмоционалдык ырлардан турган микстейп. \n  \n  \n  \n این میم ویدیوئی در زیر یک رپر ترک قدیمی مدرسه ، سانسار سالوو را نشان می دهد که اسلحه را بارگیری می کند و آن را روی سر خود قرار می دهد ، سپس با تفکر به اسلحه نگاه می کند ، در حالی که ضرب آهنگ \"dimdilerde Hayal\" در پس زمینه پخش می شود. این قسمت از ویدئو در اصل مربوط به ویدیوی تبلیغاتی وی برای میکس تیپ 21 گرمی است ، که یک میکس استپ است که به طور کلی از آهنگ های مالیخولیایی و احساسی تشکیل شده است. \n Mae'r meme fideo isod yn darlunio rapiwr Twrcaidd hen ysgol, Sansar Salvo, yn llwytho gwn a'i roi ar ei ben, yna'n edrych ar y gwn yn feddylgar, tra bod curiad y gân \"Şimdilerde Hayal\" yn chwarae yn y cefndir. Roedd y rhan hon o'r fideo yn wreiddiol o'i fideo hyrwyddo ar gyfer y mixtape 21 gram, sy'n gymysgedd sy'n cynnwys caneuon melancolaidd ac emosiynol yn gyffredinol. \n Quyidagi ushbu video-memda qadimgi maktab turk reperi Sansar Salvo qurolni ko'tarib, boshiga qo'yib, keyin o'ychan o'ychan qurolga qaragan, \"Shimdilerde Hayal\" qo'shig'ining zarbasi esa orqa fonda tasvirlangan. Videoning ushbu qismi dastlab uning 21 grammlik miksape uchun reklama videosidan olingan bo'lib, bu odatda melankolik va hissiy qo'shiqlardan iborat bo'lgan miksteyp.")
        await asyncio.sleep(1)
        await message.channel.send("Quyidagi ushbu video-memda qadimgi maktab turk reperi Sansar Salvo qurolni ko'tarib, boshiga qo'yib, keyin o'ychan o'ychan qurolga qaragan, \"Shimdilerde Hayal\" qo'shig'ining zarbasi esa orqa fonda tasvirlangan. Videoning ushbu qismi dastlab uning 21 grammlik miksape uchun reklama videosidan olingan bo'lib, bu odatda melankolik va hissiy qo'shiqlardan iborat bo'lgan miksteyp. \n Ovaj video meme ispod prikazuje turskog repera oldschool-a, Sansara Salva, kako puni pištolj i stavlja ga na glavu, a zatim zamišljeno gleda u pištolj, dok ritam pjesme \"theimdilerde Hayal\" svira u pozadini. Ovaj dio videa izvorno je nastao iz njegovog promotivnog videa za kombinaciju od 21 grama, koja je kombinacija koja se uglavnom sastoji od melanholičnih i emocionalnih pjesama. \n इस वीडियो में नीचे एक सुनसान तुर्की रैपर, संसार साल्वो को दिखाया गया है, एक बंदूक लोड कर रहा है और इसे अपने सिर पर रख रहा है, फिर बंदूक को सोच-समझकर देख रहा है, जबकि पृष्ठभूमि में \"Şimdilerde हयाल\" गीत की धड़कन है। वीडियो का यह खंड मूल रूप से 21 ग्राम मिक्सटेप के लिए उनके प्रचार वीडियो से था, जो कि एक मिक्सटेप है जिसमें आम तौर पर उदासी और भावनात्मक गीत शामिल होते हैं। ")
        await asyncio.sleep(1)
        await message.channel.send("Төмендегі бұл бейне мемде ескі мектептегі түрік рэпері Сансар Сальво мылтықты жүктеп, оны басына қойып, содан кейін мылтыққа ойлана қарап, «Шимділерде Хаял» әнінің артта ойнауы бейнеленген. Видеоның бұл бөлімі негізінен оның 21 граммдық микстейптің жарнамалық бейнеролигінен алынған, ол жалпы меланхоликтік және эмоционалды әндерден тұратын микстейп. \n Ovaj video meme ispod prikazuje turskog repera oldschool-a, Sansara Salva, kako puni pištolj i stavlja ga na glavu, a zatim zamišljeno gleda u pištolj, dok ritam pjesme \"theimdilerde Hayal\" svira u pozadini. Ovaj dio videa izvorno je nastao iz njegovog promotivnog videa za kombinaciju od 21 grama, koja je kombinacija koja se uglavnom sastoji od melanholičnih i emocionalnih pjesama. \n Aşağıdakı bu video meme, köhnə məktəbli bir türk rapçi Sansar Salvo'nun tapançanı yükləyərək başına qoyub sonra düşünülmüş şəkildə silaha baxdığını, \"Şimdilerde Hayal\" mahnısının döyüntüsü arxa planda oynadığını təsvir edir. Videonun bu hissəsi əvvəlcə melankolik və emosional mahnılardan ibarət olan bir qarışıq olan 21 qramlıq qarışıq üçün təqdimat videosundan götürülmüşdür. \n Vê vîdyoya memê ya li jêr, rapperê tirk ê olds dibistan, Sansar Salvo, çekek bar dike û datîne serê xwe, paşê bi raman li çek dinihêre, dema ku lêdana strana \"Şimdilerde Hayal\" li paş dimîne. Vê beşa vîdyoyê bi eslê xwe ji vîdyoya danasînê ya wî ya ji bo 21 gram mixtape bû, ku ew mixtepiyek e ku bi gelemperî ji stranên melankolîk û hestyar pêk tê.")
        await asyncio.sleep(1)
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

#' or message.content.lower() == 'hey wake up' or message.content.lower() == 'hey, wake up' or message.content.lower() == 'wake em up' or message.content.lower() == 'wake \'em up':
    # if message.content.lower() == '🤡':
        # ment=message.author.mention
        # member=message.author
        # await message.delete()
        # await message.channel.send(f"ananı allahını sikerim senin orospu evladı siktir git {ment}")
        # await member.ban(reason="clown emoji pcislockedbot", delete_message_days=0)
        # await message.channel.send(f"{ment} = banlandı 🕋")
        
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
        await message.channel.send("seni banlicam hatırlat bana") 
        return
        
        # uid = message.author.id
        # cid = message.channel.id
        # uth = message.author.mention
        # async for fetchMessage in message.channel.history(limit=7, before=message, oldest_first=True):
            # print(f"{fetchMessage.content}")
            # if fetchMessage.author == client.user:
                # return
            # if fetchMessage.content == 'tm' and     fetchMessage.author.id == uid:
                # print(f"nigger")
                # await message.channel.send("it works you fucking idiot")
                # await message.author.ban(reason="tşk öd autoban")
                # await message.channel.send(f"{uth} = banlandı 🕋 https://www.youtube.com/watch?v=wnedkVrgFF0")
            # else:
                # print("else çıktı")
                # return
                #somehow i gotta fix this
                #i promise i will

client.loop.create_task(fetch())
client.run(TOKEN)