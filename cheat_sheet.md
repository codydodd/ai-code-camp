# Cheat sheet for code and commands

## Getting the repo
The repo:
https://github.com/codydodd/ai-code-camp

Cloning the repo to your computer
1) Create a folder to hold your code
2) In VSCode, 'open' this folder. 
3) Terminal: git clone https://github.com/codydodd/ai-code-camp.git

## Changing directory:
You may have to move from the folder you created, to the folder you downloaded. To do that:

`cd ai-code-camp`

If you are too deep in a folder, you can go 'up' by typing: `cd ..`

## Creating an environment

Linux/Mac
```
python3 -m venv .lse_code_camp_environment
source .lse_code_camp_environment/bin/activate
```

Windows (powershell)
```
python -m venv .venv
.\.venv\Scripts\activate
```

## Activating your environment:
`source <name of environment>/bin/activate`

## Activate code:
python subfolder/script_name.py