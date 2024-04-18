export LC_ALL=en_US.UTF-8

bindkey -v '^[[H' beginning-of-line
bindkey  "^[[F"   end-of-line
bindkey  "^[[3~"  delete-char

alias cls="clear"
alias cat="bat"
alias ls="eza --icons --group-directories-first"
alias man="tldr"
alias i="yay -S "
alias r="sudo pacman -Rns "
alias s="pacman -Ss "
alias f="sudo pacman -Fy"
alias u="yay -Syyu "

eval "$(starship init zsh)"

source ~/Arch/zsh/sudo.plugin.zsh
source ~/Arch/zsh/extract.plugin.zsh

source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh

HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000

zstyle :compinstall filename '~/.zshrc'

autoload -Uz compinit
compinit
export LC_ALL=en_US.UTF-8