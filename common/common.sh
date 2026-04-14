#!/usr/bin/env bash

# Bold
Black='\033[1;30m'       # Black
Red='\033[1;31m'         # Red
Green='\033[1;32m'       # Green
Yellow='\033[1;33m'      # Yellow
Blue='\033[1;34m'        # Blue
Purple='\033[1;35m'      # Purple
Cyan='\033[1;36m'        # Cyan
White='\033[1;37m'       # White

# Reset
Color_Off='\033[0m'       # Text Reset


function error() {
    echo -e "${Red}[ERROR] $1${Color_Off}"
}

function warn() {
    echo -e "${Yellow}[WARNING] $1${Color_Off}"
}

function success() {
    echo -e "${Green}[SUCCESS] $1${Color_Off}"
}

function git_push_snapshot() {
    local branch="$1"
    git config --global user.email "ionel.dumitru04@e-uvt.ro"
    git config --global user.name "ionelDumitru"
    git add .
    git commit -m "SS: Added new snapshot"
    git push origin ${branch}
}