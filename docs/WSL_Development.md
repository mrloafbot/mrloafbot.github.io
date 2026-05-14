#  WSL Development 

How to setup Linux in Windows for AI and Web development. 

## Why ? 

Everything is developed with Linux in mind first and the web runs on linux. Running linux in your development setup lets you use all the tools and libraries as they are developed. Microsoft has made running linux in windows not only easy but very powerful.  By default your linux vm will have drivers for your gpu. 

## How

1. [VS Code](#vs-code)
1. [WSL](#wsl) 
1. [Ubuntu](#ubuntu)
1. SSH Keys
1. Github
1. Fork Demo
1. Pull Fork
1. Vscode from Linux
1. Run Sample project

## Next steps

* Hugging face
* Stable Diffusion
* Image to Image Project

## VS Code

Visual Studio Code

[Install Instructions from Microsoft](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-vscode)

Install VS Code from here:

https://code.visualstudio.com/download

When prompted to Select Additional Tasks during installation, be sure to check the Add to PATH option so you can easily open a folder in WSL using the code command.

Install the [Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack) extension pack. This extension pack includes the WSL extension, in addition to the Remote - SSH, and Dev Containers extensions, enabling you to open any folder in a container, on a remote machine, or in WSL. You can install it from the web page link.

## WSL

Windows Subsystem for Linux. 

[Install Instructions from Microsoft](https://learn.microsoft.com/en-us/windows/wsl/install)

Start button
Type Power
Powershell should be the acitve selction
Click "Run as Administator"

A new power shell winodw will pop up. 

Type "wsl --install" and hit enter. 

This will install WSL and an Ubuntu Linux VM on your computer. 

# Ubuntu

Launch Ubuntu from the Start menu, or from Windows Terminal. 

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


```
ssh-keygen
```
This will generate your SSH keys, these are cryptographic keys to encode and decode message from trusted systems. Hit enter for any messages or questions the program prompts you for. They will be created in a ".ssh" folder for your user. 


```
mkdir Projects
```

This will make a new dire

```
cd Projects
```
