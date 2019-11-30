pooo  
#!/bin/bash
#version 1.5
clear

# Variables
b='\033[1m'
u='\033[4m'
bl='\E[30m'
r='\E[31m'
g='\E[32m'
bu='\E[34m'
m='\E[35m'
c='\E[36m'
w='\E[37m'
endc='\E[0m'
enda='\033[0m'
blue='\e[1;34m'
cyan='\e[1;36m'
red='\e[1;31m'

echo "Kamu Akan Masuk Dalam 5 Detik Lagi Mohon Bersabar Oke" | lolcat
sleep 1
figlet 5 | lolcat
sleep 1
figlet 4 | lolcat
sleep 1
figlet 3 | lolcat
sleep 1
figlet 2 | lolcat
sleep 1
figlet 1 | lolcat
sleep 1
clear
echo "WELLCOME HACKER INDONESIA" | lolcat

figlet ToolsCyber_Team" | lolcat

echo -e  "_____________________________________________________________"
echo -e  "Tools    : ToolsCyberteam $white         " |lolcat
echo -e  "Creadby  : WawanSeloww $white   " |lolcat
echo -e  "Contact  : Wawanseloww0491@gmail.com $white " |lolcat
echo -e "VersiTools : v1.6 $white " |lolcat
echo -e "WhatsApp : 082392073951 $white " |lolcat
echo -e "GitHub : https://github.com/Cyberteam91 $white " |lolcat
echo -e "Copyright By Termux 2019 $white " |lolcat
echo -e "KALAU SCRIPT BERMASALAH HUB CREATOR OKE! $white " |lolcat
echo -e "Bagi Kalian Yang Masih Pemula Kalian Bisa Install Terlebih Dahulu Piliha Nomor 17 Dijamin Termux Kalian Bakalan Bisa Langsung Makek"
echo -e "Jangan Rename Script Ini Kalau Rename Dosa! $white " |lolcat
echo -e  "_____________________________________________________________"

###################################################
# CTRL + C
###################################################
trap ctrl_c INT
ctrl_c() {
clear
echo -e $red"[#]> (Ctrl + C ) Detected, Trying To Exit ... "
sleep 1
echo ""
echo -e $green"[#]> Terima kasih sudah make tools saya semoga bermanfaat ... "
sleep 1
echo ""
echo -e $white"[#]> WawanSeloww Here ... "
sleep 1
echo ""
echo -e $white "[#]> Silahkan Tekan Enter Untuk Melanjutkan! "
sleep 1
read enter
exit
}

lagi=1
while [ $lagi -lt 15 ];
do
echo ""
echo -e $b"1.  Nmap${enda}";
echo -e "============================" | lolcat
echo -e $b"2.  Admin-finder${endc}";
echo -e "============================" | lolcat
echo -e $b"3.  RED_HAWK${endc}";
echo -e "============================" | lolcat
echo -e $b"4   Lazymux${endc}";
echo -e "============================" | lolcat
echo -e $b"5.  Tools-X${endc}";
echo -e "============================" | lolcat
echo -e $b"6.  Tema-Termux${endc}";
echo -e "============================" | lolcat
echo -e $b"7.  Spam-Call${endc}";
echo -e "============================" | lolcat
echo -e $b"8.  Ngrok${endc}";
echo -e "============================" | lolcat
echo -e $b"9.  Hammer${endc}";
echo -e "============================" | lolcat
echo -e $b"10. TuanBadut${endc}";
echo -e "============================" | lolcat
echo -e $b"11.  Webdav${endc}";
echo -e "============================" | lolcat
echo -e $b"12.  Upgrade-Pip${endc}";
echo -e "============================" | lolcat
echo -e $b"13.  Spam-Callv2${endc}";
echo -e "============================" | lolcat
echo -e $b"14.  Create-Virus${endc}";
echo -e "============================" | lolcat
echo -e $b"15.  ApaSajaYangBaru${endc}";
echo -e "============================" | lolcat
echo -e $b"16.  About${endc}";
echo -e "============================" | lolcat
echo -e $b"17.  Pertama-Install${endc}";
echo -e "============================" | lolcat
echo -e $b"18. Exit${endc}";
echo ""
echo -e "╭─0day" |lolcat
read -p "╰─#" pil;

# Nmap

case $pil in
1) echo "Otw Install Nmap Dalam"
echo "3"
sleep 1
echo "2"
sleep 1
echo "1"
sleep 1
pkg install nmap
echo -e  "${y} {1} Masukkan Web${endc}:"
read web
nmap $web
echo
echo "Nmap Selesai Di Install"

;;

# admin-finder

2) echo "Otw Install admin-finder Dalam"
echo "3"
sleep 1
echo "2"
sleep 1
echo "1"
sleep 1
git clone  https://github.com/the-c0d3r/admin-finder.git
echo -e "${y} cara menggunakan admin finder"
echo -e "${y} cd admin-finder"
echo -e "${y} python admin-finder.py"
cd /data/data/com.termux/files/home/admin-finder/
python2 /data/data/com.termux/files/home/admin-finder/admin-finder.py
echo
echo "Admin Finder Selesai Di Install"

;;

#RED_HAWK

3) echo "Otw Install RED_HAWK Dalam"
echo "3"
sleep 1
echo "2"
sleep 1
echo "1"
sleep 1
git clone https://github.com/Tuhinshubhra/RED_HAWK
echo -e "${y} Installer RED_HAWK..."
echo -e "${y} cd RED_HAWK"
echo -e "${y} php RED_HAWK.php"
cd /data/data/com.termux/files/home/RED_HAWK/
php /data/data/com.termux/files/home/RED_HAWK/ RED_HAWK.php
echo "Red Hawk Selesai Di Install"

;;

#Lazymux

4) echo "Otw Install Lazymux Dalam"
echo "3"
sleep 1
echo "2"
sleep 1
echo "1"Dr


sleep 1
git clone https://github.com/Gameye98/Lazymux
echo -e "${y} Installer Lazymux..."
echo -e "${y} cd Lazymux"
echo -e "${y} python lazymux.py"
cd /data/data/com.termux/files/home/Lazymux/
python2 /data/data/com.termux/files/home/Lazymux/ lazymux.py
echo "Lazymux Selesai Di Install"

;;

#Tools-X

5) echo "Otw Install Tools-X Dalam"
echo "3"
sleep 1
echo "2"
sleep 1
echo "1"
sleep 1
git clone https://github.com/Rajkumrdusad/Tool-X
echo -e "${y} Installer Tool-X..."
echo -e "${y} cd Tool-X"
echo -e "${y} sh install.aex"
cd /data/data/com.termux/files/home/Tool-X
bash /data/data/com.termux/files/home/Tool-X/sh install.aex
echo "Tools-X Selesai Di Install"
;;

#thema-termux

6) echo "Otw Install Thema-Termux Dalam"
echo "3"
sleep 1
echo "2"
sleep 1
echo "1"
sleep 1
apt-get update && apt-get upgrade
sh -c "$(curl -fsSL https://github.com/Cabbagec/termux-ohmyzsh/raw/master/install.sh)"
~/.termux/colors.sh
echo $red" ganti color ? ketik ~/.termux/colors.sh "
echo "Thema Termux Selesai"

;;

#Spam-Call

7) echo "Otw Install SpamCall Dalam"
echo "3"
sleep 1
echo "2"
sleep 1
echo "1"
sleep 1
apt-get update && apt-get upgrade
apt-get install git
apt-get install unzip
apt-get install php
git clone https://github.com/mrcakil/spam
cd spam
unzip toko-pedia.zip
echo "SpamCall Selesai Di Install"

;;

#Ngrok

8) echo "Otw Install Ngrok Dalam"
echo "3"
sleep 1
echo "2"
sleep 1
echo "1"
sleep 1
apt install wget
mkdir ngrok
cd ~/ngrok
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip
unzip ngrok-stable-linux-arm.zip
cd ~/
echo "Ngrok Selesai Di Install"

;;

#Hammer

9) echo "Otw Install Hammer Dalam"
echo "3"
sleep 1
echo "2"
sleep 1
echo "1"
sleep 1
pkg update
pkg upgrade
pkg install python
pkg install git
git clone https://github.com/cyweb/hammer
cd ~/
echo "Hammer Selesai Di Install"

;;

#TuanBadut

10) echo "Otw Install TuanBadut Dalam"
echo "3"
sleep 1
echo "2"
sleep 1
echo "1"
sleep 1
apt update && apt upgrade -y
apt install git
apt install php
apt install curl
apt install ruby
apt install figlet
apt install python2
gem install lolcat 
git clone https://github.com/TUANB4DUT/TOOLSINSTALLERv3 
cd TOOLSINSTALLERv3 
chmod +x TUANB4DUT.sh
echo "TuanBadut Selesai Di Install"

;;

#Webdav

11) echo "Otw Install Webdav Dalam"
echo "3"
sleep 1
echo "2"
sleep 1
echo "1"
sleep 1
apt update && apt upgrade
apt install python2
pip2 install urllib3 chardet certifi idna requests
apt install openssl curl
pkg install libcurl
mkdir webdav
cd ~/webdav
wget https://pastebin.com/raw/HnVyQPtR -O webdav.py
chmod 777 webdav.py
cd ~/
echo "Webdav Selesai Di Install"

;;

#Upgrade-Pip

12) pip install --upgrade pip

;;

#Spam-Callv2

13) echo "Otw Install SpamCall Dalam"
echo "3"
sleep 1
echo "2"
sleep 1
echo "1"
sleep 1
pkg update && pkg upgrade
pkg install php
pkg install git
git clone https://github.com/GebangKiidiw/SpamCall
echo "Spam-Callv2 Selesai Di Install"

;;

#Create-Virus

14) echo "Otw Install Create-Virus Dalam"
echo "3"
sleep 1
echo "2"
sleep 1
echo "1"
sleep 1
git clone https://github.com/ashishb/android-malware
echo -e "${y} Cara membuat virus mematikan"
echo -e "${y} cd android-malware"
echo -e "${y} ls"
echo -e "${y} Nah kalian tinggal masuk ke dictiory virusnya"
echo -e "${y} Contoh = cd xbot"
echo -e "${y} ls"
echo -e "${y} Nah kalian tinggal pindahin virus itu ke sdcard"

;;

#ApaSajaYangBaru

15) echo -e "Pembaruan Tools"
echo -e "Bagian Masuk Tools Di Adakan 5 Detik"
echo -e "Di Exit Menambah Tulisan"
echo -e "Di Tambahkan Pembaruan Tools Ini"
echo -e "Pembaruan (29/11/2019 ~ 02:00)"
echo -e "Tekan Enter Untuk Kembali"
read enter

;;

#About

16) echo -e "Author : Wawan Setiawan Cyber Team'"
echo -e "Name : ToolsCyberTeam"
echo -e "CodeName : WawanSelow"
echo -e "version : v1.6"
echo -e "Date : (29/11/2019)~(02:00)"
echo -e "Team : DevilBlack Cyber Team"
echo -e "Email : Wawanseloww0491@gmail.com"
echo -e "WhatsApp : 082392073951"
echo -e "Teken Enter Untuk Kembali"
read enter

;;
    
#Pertama-Install

17) echo "Ini Membutuhkan Waktu 10 Menit Lebih Jadi Mohon Sabar Oke"
echo "Jadi Tunggu Jangan Di Ctrl + C Oke"
sleep 3
apt-get update && upgrade
pkg update && pkg upgrade
apt-get install python2
pkg install python
apt-get install toilet
apt-get install php
apt-get install figlet
pip2 install requests
pip2 install mechanize
pkg install ruby
gem install lolcat
pkg install cowsay
pkg install nano
pkg install curl
pkg install sl
pkg install wget
pkg install neofetch
pkg install openssh
echo "instalasi selesai gan !! semua sudah bisa di pakai"
echo "Disini Di Install (python2 python toilet figlet cowsay ruby lolcat nano curl sl neofetch)"
echo "Dan Masih Banyak Lagi Semua Sudah Download Jadi Kalian Tinggal Memakai Nya Saja"

;;

18) echo "Created By : WawanSeloww" | lolcat
echo "Terimakasih Karena Sudah Menggunakan Tools Dari Saya " | lolcat
echo "semoga Tools Singkat Ini Bermanfaat" | lolcat
echo "Dan Berbagilah Apa Yang Telah Kalian Ketahui Yang Belom Di Ketahui Orang Lain " | lolcat
echo "__BERBAGI ITU INDAH TETAPI BERBAGILAH UNTUK HAL-HAL YANG POSITIF__" | lolcat
echo " Bye... Gays... SeeYouNextNewTools.." | lolcat
echo "____$____$____$____$____$____$____$____$____$____"
sleep 3
exit
;;

*) echo "Kata Kata Yang Anda Masukan Salah"
esac
done
✔
