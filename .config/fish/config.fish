if status is-interactive
    # Commands to run in interactive sessions can go here
end

starship init fish | source
thefuck --alias | source
fzf --fish | source
zoxide init fish | source

# Created by `pipx` on 2025-05-05 22:10:22
set PATH $PATH /home/zapdos/.local/bin

fish_add_path /home/zapdos/.spicetify
fish_add_path /home/zapdos/go/bin/
alias ls=lsd
alias fetch=fastfetch
alias v=nvim
alias cd=z
cat ~/.cache/wal/sequences
