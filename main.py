import os
import shutil

PATH = "/enter/your/path/here"
Documnet = "/enter/your/path/here"
Pictures = "/enter/your/path/here"
Music = "/enter/your/path/here"
App = "/enter/your/path/here"
Zips = "/enter/your/path/here"
Disc = "/enter/your/path/here"
Exe = "/enter/your/path/here"
Font = "/enter/your/path/here"
Internet = "/enter/your/path/here"
Programming = "/enter/your/path/here"
Video = "/enter/your/path/here"

if os.path.isdir(Documnet):
    pass
else:
    print(f"Invalid path {Documnet}")
    exit()

if os.path.isdir(Video):
    pass
else:
    print(f"Invalid path {Video}")
    exit()

if os.path.isdir(Internet):
    pass
else:
    print(f"Invalid path {Internet}")
    exit()

if os.path.isdir(Programming):
    pass
else:
    print(f"Invalid path {Programming}")
    exit()

if os.path.isdir(Font):
    pass
else:
    print(f"Invalid path {Font}")
    exit()

if os.path.isdir(Exe):
    pass
else:
    print(f"Invalid path {Exe}")
    exit()

if os.path.isdir(Disc):
    pass
else:
    print(f"Invalid path {Disc}")
    exit()

if os.path.isdir(Zips):
    pass
else:
    print(f"Invalid path {Zips}")
    exit()

if os.path.isdir(App):
    pass
else:
    print(f"Invalid path {App}")
    exit()

if os.path.isdir(Music):
    pass
else:
    print(f"Invalid path {Music}")
    exit()

if os.path.isdir(Pictures):
    pass
else:
    print(f"Invalid path {Pictures}")
    exit()

while True:
    for file in os.listdir(PATH):
        # Audio file
        if file.endswith(".aif"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Music, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Music)
                print(f"{filename} moved to {Music}")
        elif file.endswith(".cda"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Music, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Music)
                print(f"{filename} moved to {Music}")
        elif file.endswith(".mid"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Music, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Music)
                print(f"{filename} moved to {Music}")
        elif file.endswith(".midi"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Music, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Music)
                print(f"{filename} moved to {Music}")
        elif file.endswith(".mp3"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Music, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Music)
                print(f"{filename} moved to {Music}")
        elif file.endswith(".mpa"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Music, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Music)
                print(f"{filename} moved to {Music}")
        elif file.endswith(".ogg"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Music, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Music)
                print(f"{filename} moved to {Music}")
        elif file.endswith(".wav"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Music, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Music)
                print(f"{filename} moved to {Music}")
        elif file.endswith(".wma"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Music, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Music)
                print(f"{filename} moved to {Music}")
        elif file.endswith(".wpl"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Music, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Music)
                print(f"{filename} moved to {Music}")
        # Compressed file
        elif file.endswith(".7z"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Zips, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Zips)
                print(f"{filename} moved to {Zips}")
        elif file.endswith(".arj"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Zips, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Zips)
                print(f"{filename} moved to {Zips}")
        elif file.endswith(".deb"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Zips, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Zips)
                print(f"{filename} moved to {Zips}")
        elif file.endswith(".pkg"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Zips, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Zips)
                print(f"{filename} moved to {Zips}")
        elif file.endswith(".rar"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Zips, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Zips)
                print(f"{filename} moved to {Zips}")
        elif file.endswith(".rpm"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Zips, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Zips)
                print(f"{filename} moved to {Zips}")
        elif file.endswith(".tar.gz"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Zips, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Zips)
                print(f"{filename} moved to {Zips}")
        elif file.endswith(".z"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Zips, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Zips)
                print(f"{filename} moved to {Zips}")
        elif file.endswith(".zip"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Zips, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Zips)
                print(f"{filename} moved to {Zips}")
        # Disc and media file
        elif file.endswith(".csv"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Disc, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Disc)
                print(f"{filename} moved to {Disc}")
        elif file.endswith(".db"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Disc, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Disc)
                print(f"{filename} moved to {Disc}")
        elif file.endswith(".dbf"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Disc, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Disc)
                print(f"{filename} moved to {Disc}")
        elif file.endswith(".log"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Disc, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Disc)
                print(f"{filename} moved to {Disc}")
        elif file.endswith(".mdb"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Disc, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Disc)
                print(f"{filename} moved to {Disc}")
        elif file.endswith(".sav"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Disc, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Disc)
                print(f"{filename} moved to {Disc}")
        elif file.endswith(".sql"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Disc, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Disc)
                print(f"{filename} moved to {Disc}")
        elif file.endswith(".tar"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Disc, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Disc)
                print(f"{filename} moved to {Disc}")
        elif file.endswith(".xml"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Disc, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Disc)
                print(f"{filename} moved to {Disc}")
        # Executable file
        elif file.endswith(".apk"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Exe, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Exe)
                print(f"{filename} moved to {Exe}")
        elif file.endswith(".bat"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Exe, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Exe)
                print(f"{filename} moved to {Exe}")
        elif file.endswith(".bin"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Exe, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Exe)
                print(f"{filename} moved to {Exe}")
        elif file.endswith(".cgi"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Exe, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Exe)
                print(f"{filename} moved to {Exe}")
        elif file.endswith(".pl"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Exe, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Exe)
                print(f"{filename} moved to {Exe}")
        elif file.endswith(".exe"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Exe, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Exe)
                print(f"{filename} moved to {Exe}")
        elif file.endswith(".gadget"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Exe, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Exe)
                print(f"{filename} moved to {Exe}")
        elif file.endswith(".jar"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Exe, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Exe)
                print(f"{filename} moved to {Exe}")
        elif file.endswith(".msi"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Exe, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Exe)
                print(f"{filename} moved to {Exe}")
        elif file.endswith(".py"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Exe, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Exe)
                print(f"{filename} moved to {Exe}")
        elif file.endswith(".wsf"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            exist = os.path.exists(joined_path)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Exe)
                print(f"{filename} moved to {Exe}")
        # Font file
        elif file.endswith(".fnt"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Font, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Font)
                print(f"{filename} moved to {Font}")
        elif file.endswith(".fon"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Font, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Font)
                print(f"{filename} moved to {Font}")
        elif file.endswith(".ttf"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Font, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Font)
                print(f"{filename} moved to {Font}")
        elif file.endswith(".otf"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Font, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Font)
                print(f"{filename} moved to {Font}")
        # Image file
        elif file.endswith(".ai"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Pictures, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Pictures)
                print(f"{filename} moved to {Pictures}")
        elif file.endswith(".bmp"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Pictures, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Pictures)
                print(f"{filename} moved to {Pictures}")
        elif file.endswith(".gif"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Pictures, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Pictures)
                print(f"{filename} moved to {Pictures}")
        elif file.endswith(".ico"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Pictures, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Pictures)
                print(f"{filename} moved to {Pictures}")
        elif file.endswith(".jpeg"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Pictures, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Pictures)
                print(f"{filename} moved to {Pictures}")
        elif file.endswith(".jpg"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Pictures, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Pictures)
                print(f"{filename} moved to {Pictures}")
        elif file.endswith(".png"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Pictures, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Pictures)
                print(f"{filename} moved to {Pictures}")
        elif file.endswith(".ps"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Pictures, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Pictures)
                print(f"{filename} moved to {Pictures}")
        elif file.endswith(".psd"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Pictures, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Pictures)
                print(f"{filename} moved to {Pictures}")
        elif file.endswith(".svg"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Pictures, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Pictures)
                print(f"{filename} moved to {Pictures}")
        elif file.endswith(".svg"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Pictures, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Pictures)
                print(f"{filename} moved to {Pictures}")
        elif file.endswith(".tif"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Pictures, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Pictures)
                print(f"{filename} moved to {Pictures}")
        elif file.endswith(".tiff"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Pictures, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Pictures)
                print(f"{filename} moved to {Pictures}")
        # Internet file
        elif file.endswith(".asp"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Internet, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Internet)
                print(f"{filename} moved to {Internet}")
        elif file.endswith(".aspx"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Internet, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Internet)
                print(f"{filename} moved to {Internet}")
        elif file.endswith(".cer"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Internet, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Internet)
                print(f"{filename} moved to {Internet}")
        elif file.endswith(".cfm"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Internet, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Internet)
                print(f"{filename} moved to {Internet}")
        elif file.endswith(".cgi"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Internet, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Internet)
                print(f"{filename} moved to {Internet}")
        elif file.endswith(".pl"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Internet, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Internet)
                print(f"{filename} moved to {Internet}")
        elif file.endswith(".css"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Internet, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Internet)
                print(f"{filename} moved to {Internet}")
        elif file.endswith(".htm"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Internet, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Internet)
                print(f"{filename} moved to {Internet}")
        elif file.endswith(".html"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Internet, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Internet)
                print(f"{filename} moved to {Internet}")
        elif file.endswith(".js"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Internet, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Internet)
                print(f"{filename} moved to {Internet}")
        elif file.endswith(".jsp"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Internet, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Internet)
                print(f"{filename} moved to {Internet}")
        elif file.endswith(".part"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Internet, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Internet)
                print(f"{filename} moved to {Internet}")
        elif file.endswith(".php"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Internet, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Internet)
                print(f"{filename} moved to {Internet}")
        elif file.endswith(".rss"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Internet, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Internet)
                print(f"{filename} moved to {Internet}")
        elif file.endswith(".xhtml"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Internet, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Internet)
                print(f"{filename} moved to {Internet}")
        # Presentation file
        elif file.endswith(".key"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Documnet, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Documnet)
                print(f"{filename} moved to {Documnet}")
        elif file.endswith(".odp"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Documnet, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Documnet)
                print(f"{filename} moved to {Documnet}")
        elif file.endswith(".ppt"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Documnet, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Documnet)
                print(f"{filename} moved to {Documnet}")
        elif file.endswith(".pptx"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Documnet, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Documnet)
                print(f"{filename} moved to {Documnet}")
        # Programming file
        elif file.endswith(".c"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Programming, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Programming)
                print(f"{filename} moved to {Programming}")
        elif file.endswith(".cgi"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Programming, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Programming)
                print(f"{filename} moved to {Programming}")
        elif file.endswith(".pl"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Programming, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Programming)
                print(f"{filename} moved to {Programming}")
        elif file.endswith(".class"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Programming, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Programming)
                print(f"{filename} moved to {Programming}")
        elif file.endswith(".cs"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Programming, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Programming)
                print(f"{filename} moved to {Programming}")
        elif file.endswith(".h"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Programming, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Programming)
                print(f"{filename} moved to {Programming}")
        elif file.endswith(".java"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Programming, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Programming)
                print(f"{filename} moved to {Programming}")
        elif file.endswith(".php"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Programming, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Programming)
                print(f"{filename} moved to {Programming}")
        elif file.endswith(".py"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Programming, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Programming)
                print(f"{filename} moved to {Programming}")
        elif file.endswith(".sh"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Programming, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Programming)
                print(f"{filename} moved to {Programming}")
        elif file.endswith(".swift"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Programming, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Programming)
                print(f"{filename} moved to {Programming}")
        elif file.endswith(".vb"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Programming, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Programming)
                print(f"{filename} moved to {Programming}")
        # Spreadsheet file
        elif file.endswith(".ods"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Documnet, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Documnet)
                print(f"{filename} moved to {Documnet}")
        elif file.endswith(".xlsm"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Documnet, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Documnet)
                print(f"{filename} moved to {Documnet}")
        elif file.endswith(".xls"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Documnet, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Documnet)
                print(f"{filename} moved to {Documnet}")
        elif file.endswith(".xlsx"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Documnet, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Documnet)
                print(f"{filename} moved to {Documnet}")
        # Video file
        elif file.endswith(".3g2"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Video, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Video)
                print(f"{filename} moved to {Video}")
        elif file.endswith(".3gp"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Video, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Video)
                print(f"{filename} moved to {Video}")
        elif file.endswith(".avi"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Video, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Video)
                print(f"{filename} moved to {Video}")
        elif file.endswith(".flv"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Video, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Video)
                print(f"{filename} moved to {Video}")
        elif file.endswith(".h264"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Video, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Video)
                print(f"{filename} moved to {Video}")
        elif file.endswith(".m4v"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Video, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Video)
                print(f"{filename} moved to {Video}")
        elif file.endswith(".mkv"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Video, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Video)
                print(f"{filename} moved to {Video}")
        elif file.endswith(".mov"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Video, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Video)
                print(f"{filename} moved to {Video}")
        elif file.endswith(".mp4"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Video, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Video)
                print(f"{filename} moved to {Video}")
        elif file.endswith(".mpg"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Video, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Video)
                print(f"{filename} moved to {Video}")
        elif file.endswith(".mpeg"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Video, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Video)
                print(f"{filename} moved to {Video}")
        elif file.endswith(".rm"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            exist = os.path.exists(joined_path)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Video)
                print(f"{filename} moved to {Video}")
        elif file.endswith(".swf"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Video, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Video)
                print(f"{filename} moved to {Video}")
        elif file.endswith(".vob"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Video, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Video)
                print(f"{filename} moved to {Video}")
        elif file.endswith(".wmv"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Video, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Video)
                print(f"{filename} moved to {Video}")
        # Text file
        elif file.endswith(".doc"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Documnet, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Documnet)
                print(f"{filename} moved to {Documnet}")
        elif file.endswith(".docx"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Documnet, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Documnet)
                print(f"{filename} moved to {Documnet}")
        elif file.endswith(".odt"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Documnet, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Documnet)
                print(f"{filename} moved to {Documnet}")
        elif file.endswith(".pdf"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Documnet, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Documnet)
                print(f"{filename} moved to {Documnet}")
        elif file.endswith(".rtf"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Documnet, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Documnet)
                print(f"{filename} moved to {Documnet}")
        elif file.endswith(".tex"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Documnet, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Documnet)
                print(f"{filename} moved to {Documnet}")
        elif file.endswith(".txt"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Documnet, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Documnet)
                print(f"{filename} moved to {Documnet}")
        elif file.endswith(".wpd"):
            filename = os.path.basename(file)
            file_path = os.path.abspath(file)
            joined_path = os.path.join(PATH, filename)
            test = os.path.join(Documnet, filename)
            exist = os.path.exists(test)
            if exist is True:
                pass
            else:
                shutil.move(joined_path, Documnet)
                print(f"{filename} moved to {Documnet}")
