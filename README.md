# ai-code-camp

* As of 2025 this camp is optimized for python3.12

## Introduction

This repository supports the AI Code Camp developed by Dr. Cody Dodd.

The code camp covers AI as a practice, including an introduction to AI, Python, accessing AI packages, working with data, and related issues with risk and ethics. 

Participants will gain a solid understand of AI concepts, but more importantly, will leave the camp able to set up development environments, run code and work with AI packages. 

Participants will also develop skills to address data-related challenges when using AI, with a focus on human-centricity.

This is not really a programming course. If you already know how to program, you will gain insights around new AI tools and packages. If you do not know how to program, this course will leave you with a good understanding of the technology behind AI.

## Modules

### Module 1

Core tools of the craft. In some ways this is the hardest module as we have to successfully install VSCode, as well as set up virtual evnironments. 

Hint: Every machine is different and this can take some time. But it is very worth it! When done, you can begin building your own AI tools without risk of making your computer messy with files and packages. 

### Module 2

Python. We'll learn about basic code (variables and functions), packages, and how to import and use third party packages.

### Module 3

Intro to AI. A look at natural language processing, how it works and how it can perpetuate bias and other risks.

### Module 4

More advanced AI packages. From deep learning to image recognition to speech to text and beyond, we will make use of the concepts we learned in module 3.

### Module 5

Optional material highlighting interfaces, and a chance for the teams to present their AI projects.

## AI project

Individuals and teams are encouraged to present 5 to 10 minutes on AI at the end of the code-camp. This can involve building your own solutions, or critically reflecting on your experience with AI. 3 winners will be scored based on:

1. Mindfullness
2. Practicality.
3. Interesting.

## Common commands to remember

Making a virtual environment.

`python3.12 -m venv hello_world_env`

Remember to turn your virtual environment on!

`source hello_world_env/bin/activate`

How to tell if it is on.

You will see something like this in the terminal:

`(hello_world_env_12) codydodd@LAPTOP-RLSD5OPF:~/lse-code-camp$`  Where the beginning of the line shows your virtual environment in brackets ().

Check which version of python you are using. 

`python --version`

Installing packages - The recommended way:

First, add your packages to a file called requirements.txt, then run in the terminal `pip install -r requirements.txt`

Installing packages - the less optimal way:

Without a requirements.txt you can install packages directly using `pip install <package name>`, but this makes it hard to remember what packages you have and even harder if you want to share your project.



