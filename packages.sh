#!/bin/bash

# base base-devel btrfs-progs efibootmgr dosfstools grub git intel-ucode linux linux-firmware linux-headers mtools networkmanager os-prober sddm vim xdg-user-dirs

# systemctl enable NetworkManager
# systemctl enable sddm

sudo pacman -S alacritty bat bleachbit brightnessctl btop blueman bluez bluez-utils chromium cups cups-pdf dialog dunst exfatprogs eza github-cli galculator gvfs gvfs-mtp guvcview hplip hyprland hyprpaper hypridle hyprlock libreoffice-fresh intel-media-driver imv less mpv neofetch ntfs-3g nvidia nwg-look pavucontrol pipewire-alsa pipewire-pulse  papirus-icon-theme polkit-gnome qt5-wayland qt5ct reflector sbctl starship system-config-printer thunar thunar-volman transmission-qt tldr ttf-fira-code tumbler unrar ufw unzip vulkan-intel waybar xdg-desktop-portal-hyprland xdg-utils xorg-xhost zathura zathura-pdf-poppler zsh zsh-autosuggestions zsh-completions zsh-syntax-highlighting

# sudo pacman -S alsa-utils clamav engrampa gparted grub-customizer gufw plymouth  qbittorrent thunar-archive-plugin timeshift tlp tlp-rdw waybar zram-generator zsh-theme-powerlevel10k

sudo pacman -S virt-manager virt-viewer qemu vde2 ebtables iptables-nft nftables dnsmasq bridge-utils ovmf freerdp

yay -S auto-cpufreq bibata-cursor-theme catppuccin-gtk-theme-macchiato envycontrol hyprshot rofi-lbonn-wayland-git sddm-sugar-candy-git visual-studio-code-bin 

# yay -S preload wlogout

# sudo systemctl enable auto-cpufreq
# sudo systemctl enable clamav-freshclam-once.timer
# sudo systemctl enable fstrim.timer
# sudo systemctl enable ufw
# sudo systemctl enable preload

# sudo systemctl start bluetooth            modprobe btusb
# sudo systemctl start cups
# sudo systemctl start libvirtd

# libvirt input wheel lp autologin hari power video storage audio

# curl -fsSL https://bun.sh/install | bash
