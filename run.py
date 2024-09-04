import os
import subprocess
import shutil

CRD_SSH_Code = input("Google CRD SSH Code :")
username = "fsbotz" #@param {type:"string"}
password = "firossha" #@param {type:"string"}
os.system(f"useradd -m {username}")
os.system(f"adduser {username} sudo")
os.system(f"echo '{username}:{password}' | sudo chpasswd")
os.system("sed -i 's/\/bin\/sh/\/bin\/bash/g' /etc/passwd")

Pin = 098765 #@param {type: "integer"}
Autostart = True #@param {type: "boolean"}

class CRDSetup:
    def __init__(self, user):
        os.system("apt update")
        self.installCRD()
        self.installDesktopEnvironment()
        self.changewall()
        self.installGoogleChrome()
        self.installVsCode()
        self.installTelegram()
        self.installQbit()
        self.finish(user)

    @staticmethod
    def installCRD():
        subprocess.run(['wget', 'https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb'])
        subprocess.run(['dpkg', '--install', 'chrome-remote-desktop_current_amd64.deb'])
        subprocess.run(['apt', 'install', '--assume-yes', '--fix-broken'])
        print("Chrome Remoted Desktop Installed !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    @staticmethod
    def installDesktopEnvironment():
        os.system("export DEBIAN_FRONTEND=noninteractive")
        os.system("apt install --assume-yes gnome desktop-base gnome-terminal")
        os.system("bash -c 'echo \"exec /etc/X11/Xsession /usr/bin/gnome-session\" > /etc/chrome-remote-desktop-session'")
        os.system("apt remove --assume-yes xfce4-terminal xscreensaver")
        os.system("sudo apt install --reinstall gnome-screensaver")
        os.system("systemctl disable lightdm.service")
        print("Installed GNOME Desktop Environment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


    @staticmethod
    def installGoogleChrome():
        subprocess.run(["wget", "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"])
        subprocess.run(["dpkg", "--install", "google-chrome-stable_current_amd64.deb"])
        subprocess.run(['apt', 'install', '--assume-yes', '--fix-broken'])
        print("Google Chrome Installed !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    #wget https://file.io/wjIAicuGnf0K -O code_1.92.2-1723660989_amd64.deb

    @staticmethod
    def installVsCode():
        subprocess.run(["wget", "https://file.io/wjIAicuGnf0K","-O","code_1.92.2-1723660989_amd64.deb"])
        subprocess.run(["dpkg", "--install", "code_1.92.2-1723660989_amd64.deb"])
        subprocess.run(['apt', 'install', '--assume-yes', '--fix-broken'])
        print("VsCode Installed !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    @staticmethod
    def installTelegram():
        subprocess.run(["apt", "install", "--assume-yes", "telegram-desktop"])
        print("Telegram Installed !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    @staticmethod
    def changewall():
        os.system(f"curl -s -L -k -o xfce-verticals.png https://gitlab.com/chamod12/changewallpaper-win10/-/raw/main/CachedImage_1024_768_POS4.jpg")
        current_directory = os.getcwd()
        custom_wallpaper_path = os.path.join(current_directory, "xfce-verticals.png")
        destination_path = '/usr/share/backgrounds/xfce/'
        shutil.copy(custom_wallpaper_path, destination_path)
        print("Wallpaper Changed !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
   
    @staticmethod
    def installQbit():
        subprocess.run(["sudo", "apt", "update"])
        subprocess.run(["sudo", "apt", "install", "-y", "qbittorrent"])
        print("Qbittorrent Installed !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    @staticmethod
    def finish(user):
        if Autostart:
            os.makedirs(f"/home/{user}/.config/autostart", exist_ok=True)
            link = "https://awful-harley-tgbotzbyfsbotz-3d10a02b.koyeb.app/"
            colab_autostart = """[Desktop Entry]
            print("Finalizing !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

Type=Application
Name=Colab
Exec=sh -c "sensible-browser {}"
Icon=
Comment=Open a predefined notebook at session signin.
X-GNOME-Autostart-enabled=true""".format(link)
            with open(f"/home/{user}/.config/autostart/colab.desktop", "w") as f:
                f.write(colab_autostart)
            os.system(f"chmod +x /home/{user}/.config/autostart/colab.desktop")
            os.system(f"chown {user}:{user} /home/{user}/.config")
            
        os.system(f"adduser {user} chrome-remote-desktop")
        command = f"{CRD_SSH_Code} --pin={Pin}"
        os.system(f"su - {user} -c '{command}'")
        os.system("service chrome-remote-desktop start")
        
        print("..........................................................") 
        print(".....Brought By The Disala................................") 
        print("..........................................................") 
        print("......#####...######...####....####...##.......####.......") 
        print("......##..##....##....##......##..##..##......##..##......")  
        print("......##..##....##.....####...######..##......######......") 
        print("......##..##....##........##..##..##..##......##..##......") 
        print("......#####...######...####...##..##..######..##..##......") 
        print("..........................................................") 
        print("..Youtube Video Tutorial - https://youtu.be/xqpCQCJXKxU ..") 
        print("..........................................................") 
        print("Log in PIN : 098765") 
        print("User Name : fsbotz") 
        print("User Pass : firossha") 
        while True:
            pass

try:
    if CRD_SSH_Code == "":
        print("Please enter authcode from the given link")
    elif len(str(Pin)) < 6:
        print("Enter a pin more or equal to 6 digits")
    else:
        CRDSetup(username)
except NameError as e:
    print("'username' variable not found, Create a user first")