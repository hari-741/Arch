#!/bin/bash

# base base-devel btrfs-progs efibootmgr dosfstools grub git intel-ucode linux linux-firmware linux-headers mtools networkmanager os-prober sddm vim xdg-user-dirs

# systemctl enable NetworkManager
# systemctl enable sddm

sudo pacman -S alacritty bat bleachbit brightnessctl btop blueman bluez bluez-utils dialog dunst exfatprogs eza github-cli galculator gvfs gvfs-mtp guvcview hyprland hyprpaper hypridle hyprlock libreoffice-fresh intel-media-driver imv less mpv fastfetch ntfs-3g nwg-look pavucontrol pipewire-alsa pipewire-pulse papirus-icon-theme polkit-gnome qt5-wayland qt5ct reflector starship thunar thunar-volman transmission-qt tldr ttf-fira-code tumbler unrar ufw unzip vulkan-intel waybar xdg-desktop-portal-hyprland xdg-utils xorg-xhost zathura zathura-pdf-poppler zsh zsh-autosuggestions zsh-completions zsh-syntax-highlighting

# sudo pacman -S alsa-utils clamav cups cups-pdf engrampa gparted grub-customizer gufw hplip nvidia plymouth qbittorrent sbctl system-config-printer thunar-archive-plugin timeshift tlp tlp-rdw zram-generator zsh-theme-powerlevel10k

# sudo pacman -S virt-manager virt-viewer qemu vde2 ebtables iptables-nft nftables dnsmasq bridge-utils ovmf freerdp

yay -S auto-cpufreq bibata-cursor-theme brave-bin catppuccin-gtk-theme-macchiato hyprshot rofi-lbonn-wayland-git visual-studio-code-bin 

# yay -S envycontrol preload sddm-sugar-candy-git wlogout

# sudo systemctl enable auto-cpufreq
# sudo systemctl enable clamav-freshclam-once.timer
# sudo systemctl enable fstrim.timer
# sudo systemctl enable ufw
# sudo systemctl enable preload

# sudo systemctl start bluetooth            modprobe btusb
# sudo systemctl start cups
# sudo systemctl start libvirtd

# libvirt input wheel lp autologin hari power video storage audio