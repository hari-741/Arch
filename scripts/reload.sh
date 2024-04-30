#!/bin/sh

killall dunst
dunst &
hyprctl reload
notify-send "Ark" "Reloaded"