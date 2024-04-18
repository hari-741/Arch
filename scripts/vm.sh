#!/bin/sh

user="Lycan"
pass="748521"
ip="192.168.122.33"

pkexec systemctl start libvirtd
virsh --connect qemu:///system start win10
dunstify "Win 10" "starting soon..." -i "folder-wine"
sleep 10
wlfreerdp -grab-keyboard /v:$ip /u:$user /p:$pass /f /cert-ignore /d: /dynamic-resolution /gfx-h264:avc444 +gfx-progressive &