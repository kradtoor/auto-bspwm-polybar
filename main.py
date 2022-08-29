import os, time
from sys import stdout

def red():
    RED = "\033[1;31m"
    stdout.write(RED)

def green():
    GREEN = "\033[0;32m"
    stdout.write(GREEN)

def blue():
    BLUE = "\033[1;34m"
    stdout.write(BLUE)

def yellow():
    YELLOW = "\033[1;33m"
    stdout.write(YELLOW)

def purple():
    PURPLE = "\033[1;35m"
    stdout.write(PURPLE)

def white():
    WHITE = "\033[1;37m"
    stdout.write(WHITE)

banner = """
 ██████╗ ███████╗██████╗ ██╗    ██╗███╗   ███╗
██╔══██╗██╔════╝██╔══██╗██║    ██║████╗ ████║  
██████╔╝███████╗██████╔╝██║ █╗ ██║██╔████╔██║  
██╔══██╗╚════██║██╔═══╝ ██║███╗██║██║╚██╔╝██║  (by Yorkox / KradToor)
██████╔╝███████║██║     ╚███╔███╔╝██║ ╚═╝ ██║
═════╝ ╚══════╝╚═╝      ╚══╝╚══╝ ╚═╝     ╚═╝
"""

def menu():
    red()
    print(banner)
    blue()
    time.sleep(1)
    print("Desea instalar Bspwm, Polybar, Picom, Rofi, Kitty y Scripts?")

    option = input("\n [y/n] >: ")

    if option.casefold() == "y":
        req()
        bspwm()
        polybar()
    if option.casefold() == "n":
        exit()

def req():
    green()
    print("[+] Instalando requerimientos...\n")

    # Instalando Requerimientos
    os.system("sudo apt-get update -y")
    os.system("sudo apt install net-tools libuv1-dev build-essential git vim xcb libxcb-util0-dev libxcb-ewmh-dev libxcb-randr0-dev libxcb-icccm4-dev libxcb-keysyms1-dev libxcb-xinerama0-dev libasound2-dev libxcb-xtest0-dev libxcb-shape0-dev -y")
    os.system("sudo apt install cmake cmake-data pkg-config python3-sphinx libcairo2-dev libxcb1-dev libxcb-util0-dev libxcb-randr0-dev libxcb-composite0-dev python3-xcbgen xcb-proto libxcb-image0-dev libxcb-ewmh-dev libxcb-icccm4-dev libxcb-xkb-dev libxcb-xrm-dev libxcb-cursor-dev libasound2-dev libpulse-dev libjsoncpp-dev libmpdclient-dev libnl-genl-3-dev -y")
    os.system("sudo apt install meson libxext-dev libxcb1-dev libxcb-damage0-dev libxcb-xfixes0-dev libxcb-shape0-dev libxcb-render-util0-dev libxcb-render0-dev libxcb-randr0-dev libxcb-composite0-dev libxcb-image0-dev libxcb-present-dev libxcb-xinerama0-dev libpixman-1-dev libdbus-1-dev libconfig-dev libgl1-mesa-dev libpcre2-dev libevdev-dev uthash-dev libev-dev libx11-xcb-dev libxcb-glx0-dev xte -y")
    os.system("sudo apt install bspwm rofi caja feh kitty imagemagick scrot neovim xclip tmux acpi scrub bat fzf wmname -y")

    time.sleep(2)
    print("[+] Requerimientos instalados correctamente.")

def bspwm():
    green()

    # Create folders for bspwm and sxhkd inside of ~/.config
    os.system("mkdir ~/.config/bspwm")
    os.system("mkdir ~/.config/bspwm/scripts")
    os.system("mkdir ~/.config/sxhkd")
    os.system("mkdir ~/.config/bin")

    # Install bspwm
    os.system("git clone https://github.com/baskerville/bspwm")
    os.chdir("bspwm/")
    os.system("make")
    os.system("sudo make install")
    os.system("cp examples/bspwmrc ~/.config/bspwm/")
    os.system("cp examples/sxhkdrc ~/.config/sxhkd/")
    os.system("chmod +x ~/.config/bspwm/bspwmrc")
    os.chdir("..")
    os.system("sudo rm -rf bspwm/")
    os.system("chmod +x tools/bspwm_resize")
    os.system("cp tools/bspwm_resize ~/.config/bspwm/scripts/")

    # Install sxhkd
    os.system("git clone https://github.com/baskerville/sxhkd")
    os.chdir("sxhkd/")
    os.system("make")
    os.system("sudo make install")
    os.chdir("..")
    os.system("sudo rm -rf sxhkd/")
    os.system("cp tools/sxhkdrc ~/.config/sxhkd")

    time.sleep(2)
    print("\n[+] Bspwm instalado correctamente")

def polybar():
    green()

    # Install polybar
    os.system("git clone --recursive https://github.com/polybar/polybar")
    os.chdir("polybar/")
    os.system("cmake .")
    os.system("make -j$(nproc)")
    os.system("sudo make install")
    os.chdir("..")
    os.system("sudo rm -rf polybar/")

    # Install picom
    os.system("git clone https://github.com/ibhagwan/picom")
    os.chdir("picom/")
    os.system("git submodule update --init --recursive")
    os.system("meson --buildtype=release . build")
    os.system("ninja -C build")
    os.system("sudo ninja -C build install")
    os.chdir("..")
    os.system("sudo rm -rf picom/")

    # Añade el wallpaper
    os.system("mkdir ~/.wallpapers")
    os.system("cp tools/wallpaper.jpg ~/.wallpapers")
    os.system("echo 'feh --bg-fill ~/.wallpapers/wallpaper.jpg' >> ~/.config/bspwm/bspwmrc")
    os.system("echo 'xsetroot -cursor_name left_ptr &' >> ~/.config/bspwm/bspwmrc")
    os.system("echo 'wmname LG3D &' >> ~/.config/bspwm/bspwmrc")

    # Configure polybar into ~/.config
    os.system("sudo rm -rf ~/.config/polybar/")
    os.system("unzip tools/polybar.zip")
    os.system("sudo mv polybar/ ~/.config/")
    os.system("echo '~/.config/polybar/./launch.sh' >> ~/.config/bspwm/bspwmrc")
    os.system("sudo cp ~/.config/polybar/fonts/* /usr/share/fonts")

    # Configure picom
    os.system("mkdir ~/.config/picom")
    os.system("echo 'bspc config focus_follows_pointer false' >> ~/.config/bspwm/bspwmrc")

    expback = input("\nDesea usear los experimental-backends en picom? Si no se activa se puede detectar lentitud en el equipo al no disponer de una buena GPU. [y/n] -> ")

    if expback.casefold() == "y":
        os.system("cp tools/picom.conf ~/.config/picom")

    if expback.casefold() == "n":
        os.system("cp tools/picom-blur.conf ~/.config/picom/picom.conf")

    os.system("echo 'bspc config border_width 0' >> ~/.config/bspwm/bspwmrc")
    os.system("echo 'picom --experimental-backends &' >> ~/.config/bspwm/bspwmrc")

    # Config for battery.sh ethernet_status.sh hackthebox.sh target_to_hack.sh inside of ~/.config/bin
    os.chdir("tools")
    os.system("chmod +x *.sh")
    os.system("cp battery.sh ethernet_status.sh hackthebox.sh target_to_hack.sh ~/.config/bin")
    os.system("echo '' > ~/.config/bin/target")
    os.chdir("..")

     # Configure rofi
    os.system("rm -rf ~/.config/rofi")
    os.system("mkdir ~/.config/rofi")
    os.system("mkdir ~/.config/rofi/themes")
    os.system("cp tools/nord.rasi ~/.config/rofi/themes")
    os.system("echo 'rofi.theme: .config/rofi/themes/nord.rasi' > ~/.config/rofi/config")

    # Config for target
    os.system("sudo cp tools/settarget tools/cleartarget /bin")
    os.system("sudo chmod +x /bin/settarget")
    os.system("sudo chmod +x /bin/cleartarget")

    # Config for kitty
    os.system("rm -rf ~/.config/kitty")
    os.system("mkdir ~/.config/kitty")
    os.system("wget https://raw.githubusercontent.com/jcalvopinam/config-files/master/kitty/kitty.conf -O ~/.config/kitty/kitty.conf")
    os.system("wget https://raw.githubusercontent.com/jcalvopinam/config-files/master/kitty/color.ini -O ~/.config/kitty/color.ini")

    # Install Hack Nerd Fonts
    os.system("unzip tools/Hack.zip")
    os.system("sudo mv *.ttf /usr/share/fonts")

    # Config nvim
    os.system("rm -rf ~/.config/nvim/")
    os.system("mkdir ~/.config/nvim")
    os.system("mkdir ~/.config/nvim/colors")
    os.system("wget https://raw.githubusercontent.com/jcalvopinam/config-files/master/nvim/init.vim -O ~/.config/nvim/init.vim")
    os.system("wget https://raw.githubusercontent.com/jcalvopinam/config-files/master/nvim/lotus.vim -O ~/.config/nvim/lotus.vim")
    os.system("wget https://raw.githubusercontent.com/jcalvopinam/config-files/master/nvim/lotusbar.vim -O ~/.config/nvim/lotusbar.vim")
    os.system("wget https://raw.githubusercontent.com/jcalvopinam/config-files/master/nvim/colors/nord.vim -O ~/.config/nvim/colors/nord.vim")

    # alias & functions
    os.system("cp tools/alias ~/.alias")
    os.system("cp tools/functions ~/.functions")

    # Install scripts extractPort and whichSystem
    os.system("sudo cp tools/extractPort.sh tools/whichSystem.py /bin")

    # Install lsd
    os.system("sudo dpkg -i tools/lsd.deb")

    # Install oh-my-zsh
    os.system("rm -rf ~/.zshrc")
    os.system("sudo apt install zsh -y")
    os.system("sh -c \"$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)\" \"\" --unattended")
    os.system("git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions")
    os.system("git clone https://github.com/zsh-users/zsh-completions ${ZSH_CUSTOM:-${ZSH:-~/.oh-my-zsh}/custom}/plugins/zsh-completions")
    os.system("git clone https://github.com/zsh-users/zsh-syntax-highlighting ${ZSH_CUSTOM:-${ZSH:-~/.oh-my-zsh}/custom}/plugins/zsh-syntax-highlighting")
    os.system("cp tools/zshrc ~/.zshrc")

    time.sleep(2)
    print("\n[+] Polybar instalado correctamente.")
    print("\n\n[+] [+] Seleccione el nuevo entorno BSPWM en las opciones del login e inicie sesión.")
    print("Presione cualquier tecla para cerrar la sesión.")

    input()
    os.system("sudo kill -9 -1")

if __name__ == '__main__':
    id = os.getuid()
    
    if id == 0:
        red()
        print()
        print("[!] No se deber configurar sobre el usuario root")
        print()
    else:
        menu()
