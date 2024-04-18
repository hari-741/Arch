#!/bin/sh

killall dunst
dunst &
shyprctl reload
notify-send "Ark" "Reloaded"