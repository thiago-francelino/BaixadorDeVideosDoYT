from pytube import YouTube
import os
ytlink = input('Cole aqui a url do video do youtube: ')
youtube= YouTube(ytlink)
print(f"Titulo: {youtube.title}")
print('Fazendo download...')
musicas=youtube.streams.get_highest_resolution()
musicas.download()