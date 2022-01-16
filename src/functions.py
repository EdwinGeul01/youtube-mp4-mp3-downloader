from logging import exception
from colorama.ansi import Back, Fore
from pytube import YouTube
from pytube import Playlist
import json 
import os
from moviepy.video.io.VideoFileClip import VideoFileClip


f = open("config.json",'rb')
yt = None
config = json.load(f)


f.close()

def progress_function(stream, chunk, bytes_remaining):
    print("DESCARGANDO....")


def __download_youtube(url):
    try:
        # YouTube(url).streams.filter(file_extension=config['format'],only_audio=True).first().download(config['output'])
        yt = YouTube(url,on_progress_callback=progress_function).streams.filter(file_extension=config['format']).get_highest_resolution()
        print(yt.title)
        yt.download(config['output'])
        return True
    except Exception as e:
        print(Back.RED,Fore.WHITE,"ERROR AL DESCARGAR")
        print(str(e))
        return False


def __download_youtubeList(url):
    try:
        p = Playlist(url)
        for video in p.videos:
            yt = video.streams.filter(file_extension=config['format']).get_highest_resolution()
            yt.download(config['output'])
            print(yt.title)
        return True
    except Exception as e:
        print(Back.RED,Fore.WHITE,"ERROR AL DESCARGAR")
        print(str(e))
        return False





def convert_to_mp3(url):
    try:
        video = VideoFileClip(url + ".mp4")
        video.audio.write_audiofile(url + ".mp3")
        video.close()
        os.remove(url+".mp4")   
        return True
    except Exception as e:
        print(str(e))

def __dowload_AudioList(url):
    try:
        p = Playlist(url)
        for video in p.videos:
            yt = video.streams.filter(file_extension='mp4').get_highest_resolution()
            print(yt.title)
            yt.download(config['output'])
            filedir = config['output'] + yt.default_filename.split(".")[0]
            print(filedir)
            convert_to_mp3(filedir)
        return True
    except Exception as e:
        print(Back.RED,Fore.WHITE,"ERROR AL DESCARGAR")
        print(str(e))
        return False

    



def __dowload_youtubeAudio(url):
    try:
        yt = YouTube(url,on_progress_callback=progress_function).streams.filter(file_extension='mp4').first()
        print(yt.title)
        yt.download(config['output'])
        filedir = config['output'] + yt.default_filename.split(".")[0]
        print(filedir)
        convert_to_mp3(filedir)
        return True
    except Exception as e:
        print(Back.RED,Fore.WHITE,"ERROR AL DESCARGAR")
        print(str(e))
        return False



def Configure():
    try:
        print(Fore.WHITE,"(1)FORMAT -----> " + config['format'])
        print(Fore.WHITE,"(2)TYPE -----> " + config['type'])
        print(Fore.WHITE,"(3)Output -----> " + config['output'])
        print(Fore.WHITE,"(Other)Exit ")
        select = int(input("ingrese la opcion : "))


        if(select == 1):
            print(Fore.CYAN,"1. MP4 \n 2. MP3" )
            print(Fore.CYAN , "select option : " , end="")
            selectopt = int(input())
            if(selectopt == 1):
                config['format'] = "mp4"
            elif(selectopt == 2):
                config['format'] = "MP3"
        elif(select==2):
            print(Fore.CYAN, "1. Single\n 2. List" )
            print(Fore.CYAN , "select option : " , end="")
            selectopt = int(input())
            if(selectopt == 1):
                config["type"] = "single"
            elif(selectopt == 2):
                config["type"] = "list"
        elif(select==3):
            print(Fore.CYAN , "url output : " , end="")
            selectopt = input()
            config["output"] = selectopt


        os.system("clear")
        print(Fore.YELLOW,"configuration: ")
        print(config)
        configstring = json.dumps(config)
        fw = open("./config.json",'w')
        fw.write(configstring)
        fw.close()
    except Exception:
        print(Back.BLACK,Fore.WHITE,end="")



def dowload_video(url):
    if(config['type'] == "single"):
        if(config['format']== "mp4"):
            print(Fore.WHITE,"downloading.....")
            __download_youtube(url)
            print(Back.BLACK,end=" ")
            os.system("clear")

        else:
            print(Fore.WHITE,"downloading.....")
            __dowload_youtubeAudio(url)
            print(Back.BLACK,end=" ")
            os.system("clear")
    
    elif(config['type'] == "list"):
        if(config['format']== "mp4"):
            print(Fore.WHITE,"downloading.....")
            __download_youtubeList(url)
            print(Back.BLACK,end=" ")
            os.system("clear")
        
        else:
            print(Fore.WHITE,"downloading.....")
            __dowload_AudioList(url)
            print(Back.BLACK,end=" ")
            os.system("clear")

