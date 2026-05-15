#  WSL Development 

How to setup Linux in Windows for AI and Web development. 

## Why ? 

Everything is developed with Linux in mind first and the web runs on linux. Running linux in your development setup lets you use all the tools and libraries as they are developed. Microsoft has made running linux in windows not only easy but very powerful.  By default your linux vm will have drivers for your gpu. 

## How

1. [VS Code Install](#vs-code-install)
1. [WSL Install](#wsl-install) 
1. [Ubuntu Setup](#ubuntu-setup)
1. [SSH Keys](#ssh-keys)
1. [Project Directory](#project-directory)
1. [Github](#github)
1. [Vscode from Linux](#vs-code-from-linux)
1. [Run Sample project](#run-sample-project)
1. [Conclusions](#conclusions)
1. [What's Next](#whats-next)



## VS Code Install

Visual Studio Code

[Install Instructions from Microsoft](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-vscode)

Install VS Code from here:

https://code.visualstudio.com/download

When prompted to Select Additional Tasks during installation, be sure to check the Add to PATH option so you can easily open a folder in WSL using the code command.

Install the [Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack) extension pack. This extension pack includes the WSL extension, in addition to the Remote - SSH, and Dev Containers extensions, enabling you to open any folder in a container, on a remote machine, or in WSL. You can install it from the web page link.

## WSL Install

Windows Subsystem for Linux. 

[Install Instructions from Microsoft](https://learn.microsoft.com/en-us/windows/wsl/install)

Start button
Type Power
Powershell should be the acitve selction
Click "Run as Administator"

A new power shell winodw will pop up. 

Type "wsl --install" and hit enter. 

This will install WSL and an Ubuntu Linux VM on your computer. 

# Ubuntu Setup

Launch Ubuntu from the Start menu, or from Windows Terminal (right click on the shortcut, or the down arrow head in an open windows terminal). 

This will open a terminal runing Ubuntu, type:

```
sudo apt update
```

Enter your password if prompted. Sudo means "Super User DO" meaning you're acting as the administator for the system.  Apt, is a pacakge manager, that can install, remove and update programs for linux. Update means update apt to see if there ia anything to do. Next type: 

```
sudo apt upgrade -y 
```

This now upgrades your packages. The "-y" just says yes to every upgrade so you dont have to confirm each one. 

```
sudo apt install python git vim
```
This will install Python, Git and VIm. Python is a programing language. Git is version control software. Vim is the text editor. We will be using VS Code to edit our code, but it's good to have something in the terminal too. 

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```
This will install UV, a package manger and more for python. [Offical UV link to instructions](https://docs.astral.sh/uv/getting-started/installation/)


## SSH Keys

Still inside the linux terminal type:

```
ssh-keygen
```
This will generate your SSH keys, these are cryptographic keys to encode and decode message from trusted systems. Hit enter for any messages or questions the program prompts you for. They will be created in a ".ssh" folder for your user. 

```
cat ~/.ssh/id_ed25519.pub
```
This will print your public key to the terminal. This is the key will need to share with Github later.  

Select the text with your mouse, and press Cntrl+Shift+V, this will copy the text from the terminal. Cntrl+V will not work, that's something else. 

Never share "~/.ssh/id_ed25519" this is your private key. Public keys can encode messages, that only the private key can decode.  

## Project Directory 

Again in the linux terminal. We need to setup our project directory. Type:

```
mkdir Projects
```

This will make a new directory called "Projects". You will put your code projects here to keep them organized. 

```
cd Projects
```
"cd" stands for Change Directory and this will move our working directory to the projects folder we created. Notice the captial P, in linux Projects and projects can be different folders. This is not the case with windows. 

Do not close this window we will retun to it.

If you've done something not in this tutorial, type:

```
cd ~
```
This will return you to your home directory. Where you started. 

you can also type:

```
cd ..
```

To move up a directory, now you know how to move around in a terminal. 

## Github 

[Github Website](https://github.com/)

Create your own account. I'll wait.

Next, upload your public ssh keys. [Github Instructions](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)

Click on your accout icon in the upper right section of the page, it will open a dropdown, and click on "Settings".

On the left side, find "SSH and GPT keys", and click on that.

You'll see a button in the upper right "New SSH key", click that. 

In the larger text window at the bottom, press Cntrl + P to paste the ssh key value from the termial. You dont need to fill anything else out. Now click "Add SSH Key". 

Perfect, now your linux vm can securly connect to Github and you can push and pull code without having to type passwords. This is the way.

Now pen the Gradio demo project from here: [https://github.com/mrloafbot/Gradio_Hello_World](https://github.com/mrloafbot/Gradio_Hello_World)

In the upper right hand side of the page, click the "Fork" button.  This will make a copy of the demo project in your GitHub account. 

Now we need to clone your fork of the project to your computer to run it locally. 

Click your user Icon, in the upper right corner and find "Repositories" Click that.

Find your copy of "Gradio_Hello_World" and click on it. 

There is a green button called "<> Code" ont the upper right. Click on that. Copy the ssh url from the popup. 

Back in the Linux terminal you should be in your Projects directory. If you are not type:

```
cd ~/Projects
```

This will take you to your Projects directory.

now type:

```
git clone 
```

and then press the spacebar, then cntrl+shift+ to paste the ssh path from github. Press enter.

You just pulled your copy of the repository from your github account. 

## VS Code from Linux 

Still in the linux terminal, from your Projects directory type:

```
cd Gradio_Hello_World
```

This will change your working directory to what you just downloaded. Now Type:

```
code .
```

Now that VSCode is open, we want a terminal there. Terminals are great. From the top bar of VS Code, find "Terminal" and click on "New Terminal". 

## Run Sample Project

Now in the terminal, that is running inside VS Code, type:

```
uv venv
```
This will create python virtual enviorment. It will allow you to install packages without installing them to your main system. Allowing you to try different versions and combinaitons with out breaking anyting. Now type:

```
uv sync
```

This will sync your virtual enviorment with the packages defined in the project. In this case it will be Gradio, which will also pull other packages. Now type:

```
gradio main.py
```
This will run the sample Gradio application on your local computer.  

## Conclusions

Write a summary what what you learned.  

Give some examples of what you can do next, in this project. 

## What's Next

* Hugging face, download Ai models
* Stable Diffusion, locally
* Image to Image Project, with Stable Diffusion, running locally in Gradio. 