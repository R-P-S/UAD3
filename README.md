![picture](Docs/UAD_Logo.png) 
# Undead Assault 3: Dasdan 
This repository contains a open source version of UAD for StarCraft II.

## Requirements
1. StarCraft II account (Starter Edition has editor limitations)

## Installation
1. Clone or download zip to "Mods\UAD3" in StarCraft II install folder (e. g. "C:\Program Files (x86)\StarCraft II\Mods\UAD3"). Create "Mods" folder if necessary. If you need a GUI frontend for Git, I would suggest SourceTree: https://www.sourcetreeapp.com/
3. Launch "Mods\UAD3\Development\Undead Assault 3 Dasdan.SC2Map\ComponentList.SC2Components" to open map in editor. File associations may not work for first run, so be sure to open it with SC2Edit.

## Docs
* Various documents for SC2Edit & game mechanics

## Tools
* Art - .psd templates for buttons & model skins
* BlizWiz - directory for data wizards. File -> Preferences -> Wizards to setup additional directory
* M3 Utility - finds textures associated with M3 models
* Regions - converts terrain region file to UserType xml format
* Replay Utility - dumps player banks from SC2Replay file
* Run Build Script.cmd - creates new build and ouputs to "UAD3\Bin" folder

## Tips
1. When making pull requests please leave a detailed description of what the commit contains.  All pull requests will be reviewed before being accepted.
2. To make map load faster, change Editor startup settings to load triggers module instead of terrain in File -> Preferences -> Startup
3. Editor bank files are located in Documents\StarCraft II\Banks [UAD|UAD3]
4. While in test mode additional Editor cheats can be used for convenience. For full reference see [Docs/Editor/SC2 Editor Cheats.txt](Docs/Editor/SC2 Editor Cheats.txt)

For any further questions you can find us on UAD Discord channel: https://discord.gg/Vr99pGD
