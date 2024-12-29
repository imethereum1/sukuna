#!/bin/bash
CYAN='\e[0;36m'
RED='\e[0;31m'
GREEN='\e[0;32m'
YELLOW='\e[1;33m'
BLUE='\e[0;34m'
NC='\e[0m'
clear
echo -e "${RED}________________________________WARNING________________________________${NC}"
echo -e "${RED}________________________________WARNING________________________________${NC}"
echo -e "${RED}________________________________WARNING________________________________${NC}"
echo -e "${RED}________________________________WARNING________________________________${NC}"
echo -e "${RED}________________________________WARNING________________________________${NC}"
echo -e "${RED}________________________________WARNING________________________________${NC}"
echo -e "${RED}________________________________WARNING________________________________${NC}"
echo -e "${CYAN}PLEASE ALLOW STORAGE PERMISION IN TERMUX${NC}"
echo -e "${CYAN}PLEASE ALLOW STORAGE PERMISION IN TERMUX${NC}"
termux-setup-storage
read -p "$(echo -e ${CYAN}PERMISION COMPLETE? Y/N:${NC})" st
if [ $st -eq "y","" ];then
	clear
else
	echo "PLEASE ALLOW TERMUX"
fi
clear
echo -e "${BLUE}MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM${NC}"
echo -e "${BLUE}MMMMMMMMMMM                MMMMMMMMMM${NC}"
echo -e "${BLUE}MMMN\$                           vMMMM${NC}"
echo -e "${BLUE}MMMNl  ${NC}MMMMM             MMMMM  ${BLUE}JMMMM${NC}"
echo -e "${BLUE}MMMNl  ${NC}MMMMMMMN       NMMMMMMM  ${BLUE}JMMMM${NC}"
echo -e "${BLUE}MMMNl  ${NC}MMMMMMMMMNmmmNMMMMMMMMM  ${BLUE}JMMMM${NC}"
echo -e "${BLUE}MMMNI  ${NC}MMMMMMMMMMMMMMMMMMMMMMM  ${BLUE}jMMMM${NC}"
echo -e "${BLUE}MMMNI  ${NC}MMMMMMMMMMMMMMMMMMMMMMM  ${BLUE}jMMMM${NC}"
echo -e "${BLUE}MMMNI  ${NC}MMMMM   MMMMMMM   MMMMM  ${BLUE}jMMMM${NC}"
echo -e "${BLUE}MMMNI  ${NC}MMMMM   MMMMMMM   MMMMM  ${BLUE}jMMMM${NC}"
echo -e "${BLUE}MMMNI  ${NC}MMMNM   MMMMMMM   MMMMM  ${BLUE}jMMMM${NC}"
echo -e "${BLUE}MMMNI  ${NC}WMMMM   MMMMMMM   MMMM#  ${BLUE}JMMMM${NC}"
echo -e "${BLUE}MMMMR  ${NC}?MMNM             MMMMM ${BLUE}.dMMMM${NC}"
echo -e "${BLUE}MMMMNm ${NC}\`?MMM             MMMM\` ${BLUE}dMMMMM${NC}"
echo -e "${BLUE}MMMMMMN  ${NC}?MM             MM?  ${BLUE}NMMMMMN${NC}"
echo -e "${BLUE}MMMMMMMMNe                 JMMMMMNMMM${NC}"
echo -e "${BLUE}MMMMMMMMMMNm,            eMMMMMNMMNMM${NC}"
echo -e "${BLUE}MMMMNNMNMMMMMNx        MMMMMMNMMNMMNM${NC}"
echo -e "${BLUE}MMMMMMMMNMMNMMMMm+..+MMNMMNMNMMNMMNMM${NC}"
echo -e "${GREEN}Metasploit Framework - An open-source penetration testing platform.${NC}"
echo ""
echo ""
echo -e "${RED}THIS IS A POWERFULL TOOL${NC}"
echo -e "${CYAN}YOUR TERMUX ARE SETUPING.${NC}"
apt update
yes | apt upgrade
pkg update
yes | pkg upgrade
pkg install git
pkg install python
pkg install python2
pkg install python3
pkg install php
pkg install wget
pkg install curl
pip2 install mechanize
pip2 install requests
pip2 install bs4
pip install bs4
clear
echo -e "${YELLO}WAIT THE ADVANCE PKG ARE INSTALLING${NC}"
pip install six
pip install requests
pip install pycryptodome
pip install psutil
pip install --upgrade urllib3 requests
clear
echo -e "${RED}TERMUX SETUP COMPLETE${NC}"
echo -e "${CYAN}THE TOOL IS RUNNING${NC}"
sleep 0.5
python3 sukuna.py
