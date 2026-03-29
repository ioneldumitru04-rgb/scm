#!/usr/bin/env bash

function correct_ssh_key() {
    ssh-add ~/.ssh/id_rsa_univ    
}

export -f correct_ssh_key