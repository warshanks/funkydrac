from os import name, system
if name == "posix":
    system("rsync ./funkydrac.zsh-theme ~/.oh-my-zsh/themes")
    system("rsync ./funkydrac2.zsh-theme ~/.oh-my-zsh/themes")
else:
    print("Not for Windows, yo.")
