# funkydrac 🧛👻
### Dracula themed oh-my-zsh themes based on [funky](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/funky.zsh-theme) and an [oh-my-posh theme](#aliensdracula-oh-my-posh) based on [aliens](https://github.com/JanDeDobbeleer/oh-my-posh/blob/main/themes/aliens.omp.json).
### These themes use the [Dracula color scheme for Windows Terminal](https://draculatheme.com/windows-terminal).
<br />

## funkydrac 🧛
![funkydrac](./samples/funkydrac.png)
## funkydrac2 👻
![funkydrac2](./samples/funkydrac2.png)

### To automatically install to oh-my-zsh themes directory...
```bash
sh -c "$(wget -O- https://raw.githubusercontent.com/warshanks/funkydrac/main/install.sh)"
```


# aliensdracula (oh-my-posh)
![aliensdracula](./samples/aliensdracula.png)
### To use, open $PROFILE in a text editor...
```powershell
notepad $PROFILE
```
### ... and add
```powershell
oh-my-posh init pwsh --config 'https://raw.githubusercontent.com/warshanks/funkydrac/main/aliensdracula.omp.json' | Invoke-Expression
```
