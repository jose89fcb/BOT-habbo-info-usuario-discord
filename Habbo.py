import discord, asyncio
from discord.ext import commands
import requests
import json
import discord
from urllib import parse, request
from requests import get
import datetime
import asyncio
import requests, json, discord, datetime, asyncio, aiohttp
from urllib import parse, request







with open('config.json') as f: 
    config = json.load(f) 


bot = commands.Bot(command_prefix=config['prefijo']) #Añadir un prefijo si gustas
bot.remove_command("help") #Borramos el comando !help por defecto




#Comienza el codigo de habbo.es
@bot.command()
async def HabboES(ctx,  *, Habboinfo):
  async with ctx.typing():
    await asyncio.sleep(0)
    
    
    response = requests.get(f'https://www.habbo.es/api/public/users?name={Habboinfo}')
    Habboinfo = response.json()['uniqueId']
   

    
    
   
   
    
    
   
    url= f'https://www.habbo.es/api/public/users/{Habboinfo}/badges'
    

    
    
    r= requests.get(url)
   
    habbo = r.json()
    placas = len(habbo)

    url= f'https://www.habbo.es/api/public/users/{Habboinfo}/friends'
    r= requests.get(url)
    habbo1 = r.text
    habbo1 = r.json()
    amigos = len(habbo1)

    url = f'https://www.habbo.es/extradata/public/users/{Habboinfo}/photos'
    r= requests.get(url)
    habbo2 = r.text
    habbo2 = r.json()
    fotos = len(habbo2)

    url = f'https://www.habbo.es/api/public/users/{Habboinfo}/rooms'
    r= requests.get(url)
    habbo3 = r.text
    habbo3 = r.json()
    salas = len(habbo3)

    url = f'https://www.habbo.es/api/public/users/{Habboinfo}/groups'
    r= requests.get(url)
    habbo4 = r.text
    habbo4 = r.json()
    grupos = len(habbo4)



    Habbokeko = response.json()['name']
    

    mision = response.json()['motto']
    
    
    #####
    

   
    ####

    MiembroDesde = response.json()['memberSince']
    registrado = MiembroDesde
    miembro = registrado.split("T")[0].split("-")
    fecha = "/".join(reversed(miembro))
    MiembroDesde = MiembroDesde.replace("."," ")
    MiembroDesde = MiembroDesde.replace("000+0000","")
    
    
    registradodesde = MiembroDesde
    miembro1 = registradodesde.split("T")[1].split(" ")
    hora = " ".join(reversed(miembro1))


    
  

    

    NivelActual = response.json()['currentLevel']
    TotalXP = response.json()['totalExperience']
    GemasHabbo = response.json()['starGemCount']
    siguientenivel = response.json()['currentLevelCompletePercent']
    embed = discord.Embed(title="\n\n\nEstá es la info de 🡺 " + Habbokeko, description="•ID🡺 " + Habboinfo + "\n\n•Missión🡺 " + mision   + "\n\n•Miembro Desde🡺 " + " Fecha: " + fecha + " Hora: " + hora + "\n\n•Nivel actual🡺 " + (str(NivelActual) + "\n\n•Total placas🡺 " +('{:,}'.format(placas)).replace(",",".") + "\n\n•Total Amigos🡺 " + ('{:,}'.format(amigos)).replace(",",".") + "\n\n•Fotos Totales🡺 "  +(str(fotos))+ "\n\n•Gemas Obtenidas (Estrellas)🡺 " + ('{:,}'.format(GemasHabbo)).replace(",",".") +"\n\n•Total XP🡺 ")  + ('{:,}'.format(TotalXP)).replace(",",".") + "\n\n•Siguiente nivel🡺 " +(str(siguientenivel)) +   "\n\n•Salas totales🡺 " + (str(salas)) + "\n\n•Grupos totales🡺 " + (str(grupos)) + "\n\n[Visita el perfil de " + Habbokeko + "](https://habbo.es/profile/"+ Habbokeko + ")"  "\n\n[twitter oficial](https://twitter.com/ESHabbo) | " "[facebook oficial](https://www.facebook.com/Habbo) | " "[instagram oficial](https://www.instagram.com/habboofficial)", timestamp=datetime.datetime.utcnow(), color=discord.Colour.random())
    embed.set_thumbnail(url="https://www.habbo.es/habbo-imaging/avatarimage?user=" + Habbokeko + "&&headonly=1&size=b&gesture=sml&head_direction=4&action=std")
    embed.set_author(name="Habbo [ES]", icon_url="https://i.imgur.com/0UDuO3n.png")
    embed.set_footer(text="habbo[ES]", icon_url="https://i.imgur.com/6ePWlHz.png")
    await ctx.send(embed=embed)
    
    
#FIN del codigo de habbo.es
#########  
#Comienza el codigo de habbo.com

@bot.command()
async def HabboCOM(ctx, *, Habboinfo):
  async with ctx.typing():
    await asyncio.sleep(0)
    
    response = requests.get(f'https://www.habbo.com/api/public/users?name={Habboinfo}')
    Habboinfo = response.json()['uniqueId']
   
    url= f'https://www.habbo.com/api/public/users/{Habboinfo}/badges'
    

    
    
    r= requests.get(url)
   
    habbo = r.json()
    placas = len(habbo)

    url= f'https://www.habbo.com/api/public/users/{Habboinfo}/friends'
    r= requests.get(url)
    habbo1 = r.text
    habbo1 = r.json()
    amigos = len(habbo1)

    url = f'https://www.habbo.com/extradata/public/users/{Habboinfo}/photos'
    r= requests.get(url)
    habbo2 = r.text
    habbo2 = r.json()
    fotos = len(habbo2)

    url = f'https://www.habbo.com/api/public/users/{Habboinfo}/rooms'
    r= requests.get(url)
    habbo3 = r.text
    habbo3 = r.json()
    salas = len(habbo3)

    url = f'https://www.habbo.com/api/public/users/{Habboinfo}/groups'
    r= requests.get(url)
    habbo4 = r.text
    habbo4 = r.json()
    grupos = len(habbo4)



    Habbokeko = response.json()['name']
    

    mision = response.json()['motto']
    
    
    #####
    

   
    ####

    MiembroDesde = response.json()['memberSince']
    registrado = MiembroDesde
    miembro = registrado.split("T")[0].split("-")
    fecha = "/".join(reversed(miembro))
    MiembroDesde = MiembroDesde.replace("."," ")
    MiembroDesde = MiembroDesde.replace("000+0000","")
    
    
    registradodesde = MiembroDesde
    miembro1 = registradodesde.split("T")[1].split(" ")
    hora = " ".join(reversed(miembro1))

    

    
  



    NivelActual = response.json()['currentLevel']
    TotalXP = response.json()['totalExperience']
    GemasHabbo = response.json()['starGemCount']
    siguientenivel = response.json()['currentLevelCompletePercent']
    embed = discord.Embed(title="\n\n\nEstá es la info de 🡺 " + Habbokeko, description="•ID🡺 " + Habboinfo + "\n\n•Missión🡺 " + mision   + "\n\n•Miembro Desde🡺 " + " Fecha: " + fecha + " Hora: " + hora + "\n\n•Nivel actual🡺 " + (str(NivelActual) + "\n\n•Total placas🡺 " +('{:,}'.format(placas)).replace(",",".") + "\n\n•Total Amigos🡺 " + ('{:,}'.format(amigos)).replace(",",".") + "\n\n•Fotos Totales🡺 "  +(str(fotos))+ "\n\n•Gemas Obtenidas (Estrellas)🡺 " + ('{:,}'.format(GemasHabbo)).replace(",",".") +"\n\n•Total XP🡺 ")  + ('{:,}'.format(TotalXP)).replace(",",".") + "\n\n•Siguiente nivel🡺 " +(str(siguientenivel)) + "\n\n•Salas totales🡺 " + (str(salas)) + "\n\n•Grupos totales🡺 " + (str(grupos)) + "\n\n[Visita el perfil de " + Habbokeko + "](https://habbo.com/profile/"+ Habbokeko + ")" "\n\n[twitter oficial](https://twitter.com/Habbo) | " "[facebook oficial](https://www.facebook.com/Habbo) | " "[instagram oficial](https://www.instagram.com/habboofficial)", timestamp=datetime.datetime.utcnow(), color=discord.Colour.random())
    embed.set_thumbnail(url="https://www.habbo.com/habbo-imaging/avatarimage?user=" + Habbokeko + "&&headonly=1&size=b&gesture=sml&head_direction=4&action=std")
    embed.set_author(name="Habbo [COM]", icon_url="https://i.imgur.com/y00rjVS.png")
    embed.set_footer(text="habbo[COM]", icon_url="https://i.imgur.com/6ePWlHz.png")
    await ctx.send(embed=embed)

#FIN DEL CODIGO DE HABBO.COM
########

#COMIENZA EL CODIGO DE HABBO.DE

@bot.command()
async def HabboDE(ctx, *, Habboinfo):
  async with ctx.typing():
    await asyncio.sleep(0)
    
    response = requests.get(f'https://www.habbo.de/api/public/users?name={Habboinfo}')
    Habboinfo = response.json()['uniqueId']
   
    url= f'https://www.habbo.de/api/public/users/{Habboinfo}/badges'
    

    
    
    r= requests.get(url)
   
    habbo = r.json()
    placas = len(habbo)

    url= f'https://www.habbo.de/api/public/users/{Habboinfo}/friends'
    r= requests.get(url)
    habbo1 = r.text
    habbo1 = r.json()
    amigos = len(habbo1)

    url = f'https://www.habbo.de/extradata/public/users/{Habboinfo}/photos'
    r= requests.get(url)
    habbo2 = r.text
    habbo2 = r.json()
    fotos = len(habbo2)

    url = f'https://www.habbo.de/api/public/users/{Habboinfo}/rooms'
    r= requests.get(url)
    habbo3 = r.text
    habbo3 = r.json()
    salas = len(habbo3)

    url = f'https://www.habbo.de/api/public/users/{Habboinfo}/groups'
    r= requests.get(url)
    habbo4 = r.text
    habbo4 = r.json()
    grupos = len(habbo4)



    Habbokeko = response.json()['name']
    

    mision = response.json()['motto']
    
    
    #####
    

   
    ####

    MiembroDesde = response.json()['memberSince']
    registrado = MiembroDesde
    miembro = registrado.split("T")[0].split("-")
    fecha = "/".join(reversed(miembro))
    MiembroDesde = MiembroDesde.replace("."," ")
    MiembroDesde = MiembroDesde.replace("000+0000","")
    
    
    registradodesde = MiembroDesde
    miembro1 = registradodesde.split("T")[1].split(" ")
    hora = " ".join(reversed(miembro1))

    

    
  



    NivelActual = response.json()['currentLevel']
    TotalXP = response.json()['totalExperience']
    GemasHabbo = response.json()['starGemCount']
    siguientenivel = response.json()['currentLevelCompletePercent']
    embed = discord.Embed(title="\n\n\nEstá es la info de 🡺 " + Habbokeko, description="•ID🡺 " + Habboinfo + "\n\n•Missión🡺 " + mision   + "\n\n•Miembro Desde🡺 " + " Fecha: " + fecha + " Hora: " + hora + "\n\n•Nivel actual🡺 " + (str(NivelActual) + "\n\n•Total placas🡺 " +('{:,}'.format(placas)).replace(",",".") + "\n\n•Total Amigos🡺 " + ('{:,}'.format(amigos)).replace(",",".") + "\n\n•Fotos Totales🡺 "  +(str(fotos))+ "\n\n•Gemas Obtenidas (Estrellas)🡺 " + ('{:,}'.format(GemasHabbo)).replace(",",".") +"\n\n•Total XP🡺 ")  + ('{:,}'.format(TotalXP)).replace(",",".") + "\n\n•Siguiente nivel🡺 " +(str(siguientenivel)) + "\n\n•Salas totales🡺 " + (str(salas)) + "\n\n•Grupos totales🡺 " + (str(grupos)) + "\n\n[Visita el perfil de " + Habbokeko + "](https://habbo.de/profile/"+ Habbokeko + ")" "\n\n[twitter oficial](https://twitter.com/De_Habbo) | " "[facebook oficial](https://www.facebook.com/Habbo) | " "[instagram oficial](https://www.instagram.com/habboofficial)", timestamp=datetime.datetime.utcnow(), color=discord.Colour.random())
    embed.set_thumbnail(url="https://www.habbo.de/habbo-imaging/avatarimage?user=" + Habbokeko + "&&headonly=1&size=b&gesture=sml&head_direction=4&action=std")
    embed.set_author(name="Habbo [DE]", icon_url="https://i.imgur.com/Bn4y5du.png")
    embed.set_footer(text="habbo[DE]", icon_url="https://i.imgur.com/6ePWlHz.png")
    await ctx.send(embed=embed)


#fin del codigo de habbo.de

####
#Comienza el codigo de habbo.fr

@bot.command()
async def HabboFR(ctx, *, Habboinfo):
  async with ctx.typing():
    await asyncio.sleep(0)
    
    response = requests.get(f'https://www.habbo.fr/api/public/users?name={Habboinfo}')
    Habboinfo = response.json()['uniqueId']
   
    url= f'https://www.habbo.fr/api/public/users/{Habboinfo}/badges'
    

    
    
    r= requests.get(url)
   
    habbo = r.json()
    placas = len(habbo)

    url= f'https://www.habbo.fr/api/public/users/{Habboinfo}/friends'
    r= requests.get(url)
    habbo1 = r.text
    habbo1 = r.json()
    amigos = len(habbo1)

    url = f'https://www.habbo.fr/extradata/public/users/{Habboinfo}/photos'
    r= requests.get(url)
    habbo2 = r.text
    habbo2 = r.json()
    fotos = len(habbo2)

    url = f'https://www.habbo.fr/api/public/users/{Habboinfo}/rooms'
    r= requests.get(url)
    habbo3 = r.text
    habbo3 = r.json()
    salas = len(habbo3)

    url = f'https://www.habbo.fr/api/public/users/{Habboinfo}/groups'
    r= requests.get(url)
    habbo4 = r.text
    habbo4 = r.json()
    grupos = len(habbo4)



    Habbokeko = response.json()['name']
    

    mision = response.json()['motto']
    
    
    #####
    

   
    ####

    MiembroDesde = response.json()['memberSince']
    registrado = MiembroDesde
    miembro = registrado.split("T")[0].split("-")
    fecha = "/".join(reversed(miembro))
    MiembroDesde = MiembroDesde.replace("."," ")
    MiembroDesde = MiembroDesde.replace("000+0000","")
    
    
    registradodesde = MiembroDesde
    miembro1 = registradodesde.split("T")[1].split(" ")
    hora = " ".join(reversed(miembro1))

    

    
  



    NivelActual = response.json()['currentLevel']
    TotalXP = response.json()['totalExperience']
    GemasHabbo = response.json()['starGemCount']
    siguientenivel = response.json()['currentLevelCompletePercent']
    embed = discord.Embed(title="\n\n\nEstá es la info de 🡺 " + Habbokeko, description="•ID🡺 " + Habboinfo + "\n\n•Missión🡺 " + mision   + "\n\n•Miembro Desde🡺 " + " Fecha: " + fecha + " Hora: " + hora + "\n\n•Nivel actual🡺 " + (str(NivelActual) + "\n\n•Total placas🡺 " +('{:,}'.format(placas)).replace(",",".") + "\n\n•Total Amigos🡺 " + ('{:,}'.format(amigos)).replace(",",".") + "\n\n•Fotos Totales🡺 "  +(str(fotos))+ "\n\n•Gemas Obtenidas (Estrellas)🡺 " + ('{:,}'.format(GemasHabbo)).replace(",",".") +"\n\n•Total XP🡺 ")  + ('{:,}'.format(TotalXP)).replace(",",".") + "\n\n•Siguiente nivel🡺 " +(str(siguientenivel)) + "\n\n•Salas totales🡺 " + (str(salas)) + "\n\n•Grupos totales🡺 " + (str(grupos)) + "\n\n[Visita el perfil de " + Habbokeko + "](https://habbo.fr/profile/"+ Habbokeko + ")" "\n\n[twitter oficial](https://twitter.com/HabboFR) | " "[facebook oficial](https://www.facebook.com/Habbo) | " "[instagram oficial](https://www.instagram.com/habboofficial)", timestamp=datetime.datetime.utcnow(), color=discord.Colour.random())
    embed.set_thumbnail(url="https://www.habbo.fr/habbo-imaging/avatarimage?user=" + Habbokeko + "&&headonly=1&size=b&gesture=sml&head_direction=4&action=std")
    embed.set_author(name="Habbo [FR]", icon_url="https://i.imgur.com/LQ7Qw8k.png")
    embed.set_footer(text="habbo[FR]", icon_url="https://i.imgur.com/6ePWlHz.png")
    await ctx.send(embed=embed)

#Termina el codigo de habbo.fr
######
#comienza el codigo de habbo.fi

@bot.command()
async def HabboFI(ctx, *, Habboinfo):
  async with ctx.typing():
    await asyncio.sleep(0)
    
    response = requests.get(f'https://www.habbo.fi/api/public/users?name={Habboinfo}')
    Habboinfo = response.json()['uniqueId']
   
    url= f'https://www.habbo.fi/api/public/users/{Habboinfo}/badges'
    

    
    
    r= requests.get(url)
   
    habbo = r.json()
    placas = len(habbo)

    url= f'https://www.habbo.fi/api/public/users/{Habboinfo}/friends'
    r= requests.get(url)
    habbo1 = r.text
    habbo1 = r.json()
    amigos = len(habbo1)

    url = f'https://www.habbo.fi/extradata/public/users/{Habboinfo}/photos'
    r= requests.get(url)
    habbo2 = r.text
    habbo2 = r.json()
    fotos = len(habbo2)

    url = f'https://www.habbo.fi/api/public/users/{Habboinfo}/rooms'
    r= requests.get(url)
    habbo3 = r.text
    habbo3 = r.json()
    salas = len(habbo3)

    url = f'https://www.habbo.fi/api/public/users/{Habboinfo}/groups'
    r= requests.get(url)
    habbo4 = r.text
    habbo4 = r.json()
    grupos = len(habbo4)



    Habbokeko = response.json()['name']
    

    mision = response.json()['motto']
    
    
    #####
    

   
    ####

    MiembroDesde = response.json()['memberSince']
    registrado = MiembroDesde
    miembro = registrado.split("T")[0].split("-")
    fecha = "/".join(reversed(miembro))
    MiembroDesde = MiembroDesde.replace("."," ")
    MiembroDesde = MiembroDesde.replace("000+0000","")
    
    
    registradodesde = MiembroDesde
    miembro1 = registradodesde.split("T")[1].split(" ")
    hora = " ".join(reversed(miembro1))

    

    
  



    NivelActual = response.json()['currentLevel']
    TotalXP = response.json()['totalExperience']
    GemasHabbo = response.json()['starGemCount']
    siguientenivel = response.json()['currentLevelCompletePercent']
    embed = discord.Embed(title="\n\n\nEstá es la info de 🡺 " + Habbokeko, description="•ID🡺 " + Habboinfo + "\n\n•Missión🡺 " + mision   + "\n\n•Miembro Desde🡺 " + " Fecha: " + fecha + " Hora: " + hora + "\n\n•Nivel actual🡺 " + (str(NivelActual) + "\n\n•Total placas🡺 " +('{:,}'.format(placas)).replace(",",".") + "\n\n•Total Amigos🡺 " + ('{:,}'.format(amigos)).replace(",",".") + "\n\n•Fotos Totales🡺 "  +(str(fotos))+ "\n\n•Gemas Obtenidas (Estrellas)🡺 " + ('{:,}'.format(GemasHabbo)).replace(",",".") +"\n\n•Total XP🡺 ")  + ('{:,}'.format(TotalXP)).replace(",",".") + "\n\n•Siguiente nivel🡺 " +(str(siguientenivel)) + "\n\n•Salas totales🡺 " + (str(salas)) + "\n\n•Grupos totales🡺 " + (str(grupos)) + "\n\n[Visita el perfil de " + Habbokeko + "](https://habbo.fi/profile/"+ Habbokeko + ")" "\n\n[twitter oficial](https://twitter.com/HabboFi) | " "[facebook oficial](https://www.facebook.com/Habbo) | " "[instagram oficial](https://www.instagram.com/habboofficial)"

, timestamp=datetime.datetime.utcnow(), color=discord.Colour.random())
    embed.set_thumbnail(url="https://www.habbo.fi/habbo-imaging/avatarimage?user=" + Habbokeko + "&&headonly=1&size=b&gesture=sml&head_direction=4&action=std")
    embed.set_author(name="Habbo [FI]", icon_url="https://i.imgur.com/PFuio6P.png")
    embed.set_footer(text="habbo[FI]", icon_url="https://i.imgur.com/6ePWlHz.png")
    await ctx.send(embed=embed)


#Termina el codigo habbo.fi
######### 
#Comienza el codigo de habbo.it
@bot.command()
async def HabboIT(ctx, *, Habboinfo):
  async with ctx.typing():
    await asyncio.sleep(0)
    
    response = requests.get(f'https://www.habbo.it/api/public/users?name={Habboinfo}')
    Habboinfo = response.json()['uniqueId']
   
    url= f'https://www.habbo.it/api/public/users/{Habboinfo}/badges'
    

    
    
    r= requests.get(url)
   
    habbo = r.json()
    placas = len(habbo)

    url= f'https://www.habbo.it/api/public/users/{Habboinfo}/friends'
    r= requests.get(url)
    habbo1 = r.text
    habbo1 = r.json()
    amigos = len(habbo1)

    url = f'https://www.habbo.it/extradata/public/users/{Habboinfo}/photos'
    r= requests.get(url)
    habbo2 = r.text
    habbo2 = r.json()
    fotos = len(habbo2)

    url = f'https://www.habbo.it/api/public/users/{Habboinfo}/rooms'
    r= requests.get(url)
    habbo3 = r.text
    habbo3 = r.json()
    salas = len(habbo3)

    url = f'https://www.habbo.it/api/public/users/{Habboinfo}/groups'
    r= requests.get(url)
    habbo4 = r.text
    habbo4 = r.json()
    grupos = len(habbo4)



    Habbokeko = response.json()['name']
    

    mision = response.json()['motto']
    
    
    #####
    

   
    ####

    MiembroDesde = response.json()['memberSince']
    registrado = MiembroDesde
    miembro = registrado.split("T")[0].split("-")
    fecha = "/".join(reversed(miembro))
    MiembroDesde = MiembroDesde.replace("."," ")
    MiembroDesde = MiembroDesde.replace("000+0000","")
    
    
    registradodesde = MiembroDesde
    miembro1 = registradodesde.split("T")[1].split(" ")
    hora = " ".join(reversed(miembro1))

    

    
  



    NivelActual = response.json()['currentLevel']
    TotalXP = response.json()['totalExperience']
    GemasHabbo = response.json()['starGemCount']
    siguientenivel = response.json()['currentLevelCompletePercent']
    embed = discord.Embed(title="\n\n\nEstá es la info de 🡺 " + Habbokeko, description="•ID🡺 " + Habboinfo + "\n\n•Missión🡺 " + mision   + "\n\n•Miembro Desde🡺 " + " Fecha: " + fecha + " Hora: " + hora + "\n\n•Nivel actual🡺 " + (str(NivelActual) + "\n\n•Total placas🡺 " +('{:,}'.format(placas)).replace(",",".") + "\n\n•Total Amigos🡺 " + ('{:,}'.format(amigos)).replace(",",".") + "\n\n•Fotos Totales🡺 "  +(str(fotos))+ "\n\n•Gemas Obtenidas (Estrellas)🡺 " + ('{:,}'.format(GemasHabbo)).replace(",",".") +"\n\n•Total XP🡺 ")  + ('{:,}'.format(TotalXP)).replace(",",".") + "\n\n•Siguiente nivel🡺 " +(str(siguientenivel)) + "\n\n•Salas totales🡺 " + (str(salas)) + "\n\n•Grupos totales🡺 " + (str(grupos)) + "\n\n[Visita el perfil de " + Habbokeko + "](https://habbo.it/profile/"+ Habbokeko + ")" "\n\n[twitter oficial](https://twitter.com/HabboItalia) | " "[facebook oficial](https://www.facebook.com/Habbo) | " "[instagram oficial](https://www.instagram.com/habboofficial)", timestamp=datetime.datetime.utcnow(), color=discord.Colour.random())
    embed.set_thumbnail(url="https://www.habbo.it/habbo-imaging/avatarimage?user=" + Habbokeko + "&&headonly=1&size=b&gesture=sml&head_direction=4&action=std")
    embed.set_author(name="Habbo [IT]", icon_url="https://i.imgur.com/UCcDULh.png")
    embed.set_footer(text="habbo[IT]", icon_url="https://i.imgur.com/6ePWlHz.png")
    await ctx.send(embed=embed)



#Termina el codigo de habbo.it





#Comienza el codigo habbo.com.tr

@bot.command()
async def HabboTR(ctx, *, Habboinfo):
  async with ctx.typing():
    await asyncio.sleep(0)
    
    response = requests.get(f'https://www.habbo.com.tr/api/public/users?name={Habboinfo}')
    Habboinfo = response.json()['uniqueId']
   
    url= f'https://www.habbo.com.tr/api/public/users/{Habboinfo}/badges'
    

    
    
    r= requests.get(url)
   
    habbo = r.json()
    placas = len(habbo)

    url= f'https://www.habbo.com.tr/api/public/users/{Habboinfo}/friends'
    r= requests.get(url)
    habbo1 = r.text
    habbo1 = r.json()
    amigos = len(habbo1)

    url = f'https://www.habbo.com.tr/extradata/public/users/{Habboinfo}/photos'
    r= requests.get(url)
    habbo2 = r.text
    habbo2 = r.json()
    fotos = len(habbo2)

    url = f'https://www.habbo.com.tr/api/public/users/{Habboinfo}/rooms'
    r= requests.get(url)
    habbo3 = r.text
    habbo3 = r.json()
    salas = len(habbo3)

    url = f'https://www.habbo.com.tr/api/public/users/{Habboinfo}/groups'
    r= requests.get(url)
    habbo4 = r.text
    habbo4 = r.json()
    grupos = len(habbo4)



    Habbokeko = response.json()['name']
    

    mision = response.json()['motto']
    
    
    #####
    

   
    ####

    MiembroDesde = response.json()['memberSince']
    registrado = MiembroDesde
    miembro = registrado.split("T")[0].split("-")
    fecha = "/".join(reversed(miembro))
    MiembroDesde = MiembroDesde.replace("."," ")
    MiembroDesde = MiembroDesde.replace("000+0000","")
    
    
    registradodesde = MiembroDesde
    miembro1 = registradodesde.split("T")[1].split(" ")
    hora = " ".join(reversed(miembro1))

    

    
  



    NivelActual = response.json()['currentLevel']
    TotalXP = response.json()['totalExperience']
    GemasHabbo = response.json()['starGemCount']
    siguientenivel = response.json()['currentLevelCompletePercent']
    embed = discord.Embed(title="\n\n\nEstá es la info de 🡺 " + Habbokeko, description="•ID🡺 " + Habboinfo + "\n\n•Missión🡺 " + mision   + "\n\n•Miembro Desde🡺 " + " Fecha: " + fecha + " Hora: " + hora + "\n\n•Nivel actual🡺 " + (str(NivelActual) + "\n\n•Total placas🡺 " +('{:,}'.format(placas)).replace(",",".") + "\n\n•Total Amigos🡺 " + ('{:,}'.format(amigos)).replace(",",".") + "\n\n•Fotos Totales🡺 "  +(str(fotos))+ "\n\n•Gemas Obtenidas (Estrellas)🡺 " + ('{:,}'.format(GemasHabbo)).replace(",",".") +"\n\n•Total XP🡺 ")  + ('{:,}'.format(TotalXP)).replace(",",".") + "\n\n•Siguiente nivel🡺 " +(str(siguientenivel)) + "\n\n•Salas totales🡺 " + (str(salas)) + "\n\n•Grupos totales🡺 " + (str(grupos)) + "\n\n[Visita el perfil de " + Habbokeko + "](https://habbo.com.tr/profile/"+ Habbokeko + ")" "\n\n[twitter oficial](https://twitter.com/habbo_tr) | " "[facebook oficial](https://www.facebook.com/Habbo) | " "[instagram oficial](https://www.instagram.com/habboofficial)", timestamp=datetime.datetime.utcnow(), color=discord.Colour.random())
    embed.set_thumbnail(url="https://www.habbo.com.tr/habbo-imaging/avatarimage?user=" + Habbokeko + "&&headonly=1&size=b&gesture=sml&head_direction=4&action=std")
    embed.set_author(name="Habbo [TR]", icon_url="https://i.imgur.com/EyfhMkE.png")
    embed.set_footer(text="habbo[TR]", icon_url="https://i.imgur.com/6ePWlHz.png")
    await ctx.send(embed=embed)

#termina el codigo de habbo.com.tr

#comienza el codigo de habbo.nl

@bot.command()
async def HabboNL(ctx, *, Habboinfo):
  async with ctx.typing():
    await asyncio.sleep(0)
    
    response = requests.get(f'https://www.habbo.nl/api/public/users?name={Habboinfo}')
    Habboinfo = response.json()['uniqueId']
   
    url= f'https://www.habbo.nl/api/public/users/{Habboinfo}/badges'
    

    
    
    r= requests.get(url)
   
    habbo = r.json()
    placas = len(habbo)

    url= f'https://www.habbo.nl/api/public/users/{Habboinfo}/friends'
    r= requests.get(url)
    habbo1 = r.text
    habbo1 = r.json()
    amigos = len(habbo1)

    url = f'https://www.habbo.nl/extradata/public/users/{Habboinfo}/photos'
    r= requests.get(url)
    habbo2 = r.text
    habbo2 = r.json()
    fotos = len(habbo2)

    url = f'https://www.habbo.nl/api/public/users/{Habboinfo}/rooms'
    r= requests.get(url)
    habbo3 = r.text
    habbo3 = r.json()
    salas = len(habbo3)

    url = 'https://www.habbo.nl/api/public/users/{Habboinfo}/groups'
    r= requests.get(url)
    habbo4 = r.text
    habbo4 = r.json()
    grupos = len(habbo4)



    Habbokeko = response.json()['name']
    

    mision = response.json()['motto']
    
    
    #####
    

   
    ####

    MiembroDesde = response.json()['memberSince']
    registrado = MiembroDesde
    miembro = registrado.split("T")[0].split("-")
    fecha = "/".join(reversed(miembro))
    MiembroDesde = MiembroDesde.replace("."," ")
    MiembroDesde = MiembroDesde.replace("000+0000","")
    
    
    registradodesde = MiembroDesde
    miembro1 = registradodesde.split("T")[1].split(" ")
    hora = " ".join(reversed(miembro1))

    

    
  



    NivelActual = response.json()['currentLevel']
    TotalXP = response.json()['totalExperience']
    GemasHabbo = response.json()['starGemCount']
    siguientenivel = response.json()['currentLevelCompletePercent']
    embed = discord.Embed(title="\n\n\nEstá es la info de 🡺 " + Habbokeko, description="•ID🡺 " + Habboinfo + "\n\n•Missión🡺 " + mision   + "\n\n•Miembro Desde🡺 " + " Fecha: " + fecha + " Hora: " + hora + "\n\n•Nivel actual🡺 " + (str(NivelActual) + "\n\n•Total placas🡺 " +('{:,}'.format(placas)).replace(",",".") + "\n\n•Total Amigos🡺 " + ('{:,}'.format(amigos)).replace(",",".") + "\n\n•Fotos Totales🡺 "  +(str(fotos))+ "\n\n•Gemas Obtenidas (Estrellas)🡺 " + ('{:,}'.format(GemasHabbo)).replace(",",".") +"\n\n•Total XP🡺 ")  + ('{:,}'.format(TotalXP)).replace(",",".") + "\n\n•Siguiente nivel🡺 " +(str(siguientenivel)) + "\n\n•Salas totales🡺 " + (str(salas)) + "\n\n•Grupos totales🡺 " + (str(grupos)) + "\n\n[Visita el perfil de " + Habbokeko + "](https://habbo.nl/profile/"+ Habbokeko + ")" "\n\n[twitter oficial](https://twitter.com/Habbo_Staff) | " "[facebook oficial](https://www.facebook.com/Habbo) | " "[instagram oficial](https://www.instagram.com/habboofficial)", timestamp=datetime.datetime.utcnow(), color=discord.Colour.random())
    embed.set_thumbnail(url="https://www.habbo.nl/habbo-imaging/avatarimage?user=" + Habbokeko + "&&headonly=1&size=b&gesture=sml&head_direction=4&action=std")
    embed.set_author(name="Habbo [NL]", icon_url="https://i.imgur.com/zGUsMDQ.png")
    embed.set_footer(text="habbo[NL]", icon_url="https://i.imgur.com/6ePWlHz.png")
    await ctx.send(embed=embed)

#termina el codigo de habbo.nl



#comienza el codigo de habbo.com.br
@bot.command()
async def HabboBR(ctx, *, Habboinfo):
  async with ctx.typing():
    await asyncio.sleep(0)
    
    response = requests.get(f'https://www.habbo.com.br/api/public/users?name={Habboinfo}')
    Habboinfo = response.json()['uniqueId']
   
    url= f'https://www.habbo.com.br/api/public/users/{Habboinfo}/badges'
    

    
    
    r= requests.get(url)
   
    habbo = r.json()
    placas = len(habbo)

    url= f'https://www.habbo.com.br/api/public/users/{Habboinfo}/friends'
    r= requests.get(url)
    habbo1 = r.text
    habbo1 = r.json()
    amigos = len(habbo1)

    url = f'https://www.habbo.com.br/extradata/public/users/{Habboinfo}/photos'
    r= requests.get(url)
    habbo2 = r.text
    habbo2 = r.json()
    fotos = len(habbo2)

    url = f'https://www.habbo.com.br/api/public/users/{Habboinfo}/rooms'
    r= requests.get(url)
    habbo3 = r.text
    habbo3 = r.json()
    salas = len(habbo3)

    url = f'https://www.habbo.com.br/api/public/users/{Habboinfo}/groups'
    r= requests.get(url)
    habbo4 = r.text
    habbo4 = r.json()
    grupos = len(habbo4)



    Habbokeko = response.json()['name']
    

    mision = response.json()['motto']
    
    
    #####
    

   
    ####

    MiembroDesde = response.json()['memberSince']
    registrado = MiembroDesde
    miembro = registrado.split("T")[0].split("-")
    fecha = "/".join(reversed(miembro))
    MiembroDesde = MiembroDesde.replace("."," ")
    MiembroDesde = MiembroDesde.replace("000+0000","")
    
    
    registradodesde = MiembroDesde
    miembro1 = registradodesde.split("T")[1].split(" ")
    hora = " ".join(reversed(miembro1))

    

    
  



    NivelActual = response.json()['currentLevel']
    TotalXP = response.json()['totalExperience']
    GemasHabbo = response.json()['starGemCount']
    siguientenivel = response.json()['currentLevelCompletePercent']
    embed = discord.Embed(title="\n\n\nEstá es la info de 🡺 " + Habbokeko, description="•ID🡺 " + Habboinfo + "\n\n•Missión🡺 " + mision   + "\n\n•Miembro Desde🡺 " + " Fecha: " + fecha + " Hora: " + hora + "\n\n•Nivel actual🡺 " + (str(NivelActual) + "\n\n•Total placas🡺 " +('{:,}'.format(placas)).replace(",",".") + "\n\n•Total Amigos🡺 " + ('{:,}'.format(amigos)).replace(",",".") + "\n\n•Fotos Totales🡺 "  +(str(fotos))+ "\n\n•Gemas Obtenidas (Estrellas)🡺 " + ('{:,}'.format(GemasHabbo)).replace(",",".") +"\n\n•Total XP🡺 ")  + ('{:,}'.format(TotalXP)).replace(",",".") + "\n\n•Siguiente nivel🡺 " +(str(siguientenivel)) + "\n\n•Salas totales🡺 " + (str(salas)) + "\n\n•Grupos totales🡺 " + (str(grupos)) + "\n\n[Visita el perfil de " + Habbokeko + "](https://habbo.com.br/profile/"+ Habbokeko + ")" "\n\n[twitter oficial](https://twitter.com/HabboPTBR) | " "[facebook oficial](https://www.facebook.com/Habbo) | " "[instagram oficial](https://www.instagram.com/habboofficial)", timestamp=datetime.datetime.utcnow(), color=discord.Colour.random())
    embed.set_thumbnail(url="https://www.habbo.com.br/habbo-imaging/avatarimage?user=" + Habbokeko + "&&headonly=1&size=b&gesture=sml&head_direction=4&action=std")
    embed.set_author(name="Habbo [BR]", icon_url="https://i.imgur.com/tPg9Hb2.png")
    embed.set_footer(text="habbo[BR]", icon_url="https://i.imgur.com/6ePWlHz.png")
    await ctx.send(embed=embed)

#Termina el codigo de habbo.com.br



@bot.event
async def on_message(message):
    if message.author.id != bot.user.id:
        if message.guild:  
          
            await bot.process_commands(message)  
        else:
                
            
            embed = discord.Embed(
                
                color = discord.Color.random(),
                title ="Mensaje de frank",
                description = "No puedes escribir comandos por mensaje directo/DM/privado"
                
               


            )
            embed.set_thumbnail(url="https://i.imgur.com/kch7Otk.png")
            
            return await message.author.send(embed=embed)
            





  
    
          

@bot.command(aliases=["quit"])
@commands.has_permissions(administrator=True)
async def cerrar(ctx):
    embed = discord.Embed(title=f" ", description="él BOT **" + bot.user.name + "** ahora está desconectado", color=discord.Color.red())
        
    
    embed.set_thumbnail(url="https://i.imgur.com/iozmWWh.gif")
    await ctx.send(embed=embed)

    await bot.close()
    print("él BOT" + bot.user.name + "se cerró")           
       


@bot.event
async def on_ready():
    
    channel = discord.utils.get(bot.get_all_channels(), name='general')
    embed = discord.Embed(title=f" ", description="él BOT **" + bot.user.name + "** ahora está en linea" + "\n\nEscribe !comandos para conocer los comandos de cada hotel", color=discord.Color.green())
        
    
    embed.set_thumbnail(url="https://i.imgur.com/duRuLN6.gif")
    await channel.send(embed=embed)

    print("BOT " f'{bot.user.name}')
    activity = discord.Game(name="Habbo info", type=1)
    await bot.change_presence(status=discord.Status.online, activity=activity)



@bot.command()
async def comandos(ctx):
  embed = discord.Embed(title="COMANDOS", description="Aquí están todos los comandos para poder generar los usuarios de cada hotel\n\n!HabboES ejemplo\n!HabboCOM ejemplo\n!HabboDE ejemplo\n!HabboFR ejemplo\n!HabboFI ejemplo\n!HabboIT ejemplo\n!HabboTR ejemplo\n!HabboNL ejemplo\n!HabboBR ejemplo\n\n\nEscribe !cerrar para poder cerrar el bot")
  embed.set_author(name="información", icon_url="https://i.imgur.com/grmS8RH.png")
  await ctx.send(embed=embed)  
  



    
bot.run(config['token'])



   



    
  

  
