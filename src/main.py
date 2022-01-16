# importing the module
from colorama import Fore,Back,Style
from functions import *

os.system("clear") 

while True:
    print(Back.BLACK,"\n")
    print(Back.BLACK ,Fore.RED , "Download videos and audio by console")
    print(Fore.LIGHTBLUE_EX , "1. download video or audio")
    print(Fore.LIGHTBLUE_EX , "2. setting  ")
    print(Fore.LIGHTBLUE_EX , "3. Exit  ")


    print(Fore.WHITE , "Selected Option : " , end="")
    option = input(Fore.WHITE );


    try:
        option = int(option);
    except Exception:
        print("Selected option is not a number")

    if(option == 1):
        os.system("clear")
        print(Fore.CYAN,"Enter url:",end=" ")
        url = input()
        dowload_video(url)
    if(option == 2):
        print(Fore.LIGHTYELLOW_EX,"setting ")
        os.system("clear")
        Configure()
    if(option == 3):
        exit()

    



