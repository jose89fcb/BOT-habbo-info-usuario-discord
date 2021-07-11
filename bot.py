import discord, asyncio
from discord.ext import commands
import requests
import json
import discord
from urllib import parse, request
from requests import get
import datetime
import asyncio
 
 
 
 
bot = commands.Bot(command_prefix='!')
bot.remove_command("help")
 
 
 
 
@bot.command()
async def Habbo(ctx, *, Habboinfo):
  async with ctx.typing():
    await asyncio.sleep(0)
 
    
    
    response = requests.get(f'https://www.habbo.es/api/public/users?name={Habboinfo}')
    Habboinfo = response.json()['uniqueId']
    url= f'https://www.habbo.es/api/public/users/{Habboinfo}/badges'
    r= requests.get(url)
    habbo = r.text
    habbo = r.json()
    length = len(habbo)
    Habbokeko = response.json()['name']
    
 
    mision = response.json()['motto']
    ultimoaccesso = response.json()['lastAccessTime']
    fecha = ultimoaccesso
    partes = fecha.split("T")[0].split("-")
    convertida = "/".join(reversed(partes))
    MiembroDesde = response.json()['memberSince']
    registrado = MiembroDesde
    miembro = registrado.split("T")[0].split("-")
    completa = "/".join(reversed(miembro))import discord, asyncio
from discord.ext import commands
import requests
import json
import discord
from urllib import parse, request
from requests import get
import datetime
import asyncio



#######################
#configuracion:
#######################




bot = commands.Bot(command_prefix="!")
bot.remove_command("help")





@bot.command()
async def Habbo(ctx,  *, Habboinfo):
  async with ctx.typing():
    await asyncio.sleep(0)

    
    
   

     

    
    response = requests.get(f'https://www.habbo.es/api/public/users?name={Habboinfo}')
    Habboinfo = response.json()['uniqueId']
    
    
    url= f'https://www.habbo.es/api/public/users/{Habboinfo}/badges'
    

    
    
    r= requests.get(url)
    habbo = r.text
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
    embed = discord.Embed(title="\n\n\nEstá es la info de 🡺 " + Habbokeko, description="•ID🡺 " + Habboinfo + "\n\n•Missión🡺 " + mision   + "\n\n•Miembro Desde🡺 " + " Fecha: " + fecha + " Hora: " + hora + "\n\n•Nivel actual🡺 " + (str(NivelActual) + "\n\n•Total placas🡺 " +(str(placas)) + "\n\n•Total Amigos🡺 " + (str(amigos)) + "\n\n•Fotos Totales🡺 "  +(str(fotos))+ "\n\n•Gemas Obtenidas (Estrellas)🡺 " + (str(GemasHabbo)) +"\n\n•Total XP🡺 ")  + (str(TotalXP)) + "\n\n•Siguiente nivel🡺 " +(str(siguientenivel)) + "\n\n•Salas totales🡺 " + (str(salas)) + "\n\n•Grupos totales🡺 " + (str(grupos)) + "\n\n[Visita el perfil de " + Habbokeko + "](https://habbo.es/profile/"+ Habbokeko + ")", timestamp=datetime.datetime.utcnow(), color=discord.Colour.random())
    embed.set_thumbnail(url="https://www.habbo.es/habbo-imaging/avatarimage?user=" + Habbokeko + "&&headonly=1&size=b&gesture=sml&head_direction=4&action=std")
    embed.set_author(name="Habbo [ES]", icon_url="https://i.imgur.com/0UDuO3n.png")
    await ctx.send(embed=embed)
    
    

     


@bot.event
async def on_ready():
      print("BOT listo!")
  
  
bot.run("")    
   


    
  
    
  

  

    NivelActual = response.json()['currentLevel']
    TotalXP = response.json()['totalExperience']
    GemasHabbo = response.json()['starGemCount']
    siguientenivel = response.json()['currentLevelCompletePercent']
    embed = discord.Embed(title="Está es la info de 🡺 " + Habbokeko, description="•ID🡺 " + Habboinfo + "\n\n•Missión🡺 " + mision + "\n\n•Último accesso🡺 " + convertida + "\n\n•Miembro Desde🡺 " + completa  + "\n\n•Nivel actual🡺 " + (str(NivelActual) + "\n\n•Total placas🡺 " +(str(length)) + "\n\n•Gemas Obtenidas (Estrellas)🡺 " + (str(GemasHabbo)) +"\n\n•Total XP🡺 ")  + (str(TotalXP)) + "\n\n•Siguiente nivel🡺 " +(str(siguientenivel)), timestamp=datetime.datetime.utcnow(), color=discord.Colour.random())
    embed.set_thumbnail(url="https://www.habbo.es/habbo-imaging/avatarimage?user=" + Habbokeko + "&&headonly=1&size=b&gesture=sml&head_direction=4&action=std")
    
    await ctx.send(embed=embed)
    
    
@bot.event
async def on_ready():
      print("BOT listo!")
  
  
bot.run("")     #Deberas de crear tu propio bot e TOKEN en el siguiente enlace: https://discord.com/developers/applications
