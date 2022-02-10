import os

PATH = input("Enter folder path: ")
dir = os.listdir(PATH)



def txt_file():
    pass


def mp3_file():
    pass


def mp4_file():
    pass


def jpg_file():
    pass


def app():
    for file in dir:
        if file.endswith(".txt"):
            txt_file()
            print("txt")
        elif file.endswith(".mp3"):
            mp3_file()
            print("mp3")
        elif file.endswith(".mp4"):
            mp4_file()
            print("mp4")
        elif file.endswith(".jpg"):
            jpg_file()
            print("jpg")

app()
