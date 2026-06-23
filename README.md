# AI Code Camp — Practical Skills for Research Professionals (LSE MISDI 2026)

* As of 2026 this camp is optimized for python3.12

## Introduction

Welcome to the AI Code Camp!

This 3‑day intensive is a hands‑on, modern introduction to AI systems, from classic deterministic models to generative transformers. As well as how to combine them into real, reliable solutions.

This is not a programming course and not a theory course.

You will experiment, break things, debug, and build, while picking up critical skills used in real research and public‑sector AI work.

## What You’ll Learn

By the end of the camp, you will be able to:

- Configure and run AI through Python scripts

- Understand how Python logic translates into agentic workflows

- Explain why Python still matters (grounding, reproducibility, auditability)

- Describe the difference between deterministic AI, machine learning, and generative AI

- Compare deterministic vs generative systems — and know when to use each

- Identify sources of AI risk: bias, privacy leakage, hallucinations, sycophancy, pollution, non‑determinism

- Build and present an AI project scored on interesting, practical, and mindful

## How We’ll Work

You can run everything in:

- GitHub Codespaces (recommended — zero setup)

- or your local machine (if you want to learn environments and pip)

All exercises are in this repo.

Codespaces will install everything automatically from requirements.txt.\

## Setting Up a Python Environment (Linux, macOS, Windows), for those not using Codespace

Most of the course can be done in Codespaces, but if you want to run things locally, here’s the simplest way to set up a clean Python environment and install everything from requirements.txt.

1. Check Your Python Version

You need Python 3.10+.

`python3 --version`

or 

`python --version`

2. Create a Virtual Environment

A virtual environment keeps your project’s packages separate from the rest of your computer.
This prevents version conflicts and keeps things reproducible.

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

When it is activated it should say:

`(.lse_code_camp_environment) yourname@computer:~/project$`

3. Install All Packages from requirements.txt

Once your environment is activated:

`pip install -r requirements.txt`

### Other hints

Windows users may have a better experience adding 'WLS2:ubuntu' to their machine. More information can be found: 

WSL2 gives you:

- A full Linux environment inside Windows

- Much better compatibility with Python, ML libraries, and command‑line tools

- Faster installs and fewer dependency issues

- A clean separation between your system and your AI experiments

- The same environment used in most research and production AI work

Installation guide can be found here: https://learn.microsoft.com/windows/wsl/install



## Running scripts

`python your_script.py`


## Experiments We’ll Run

You’ll run a series of structured experiments designed to reveal the strengths and weaknesses of different AI systems.


1. Computer Vision & Bias

- Try cat‑face detection

- See how CV models succeed or fail

- Discuss bias, fairness, and “black cat vs white cat” issues


2. Deterministic vs Generative — Diabetes Prediction

- Run a deterministic Python model

- Ask Copilot/Claude to predict the same data

- Compare drift, pollution, and reproducibility

- See why LLMs simulate math instead of doing math

3. Drivers Analysis — Random Forest vs LLMs

- Run a Random Forest to find top drivers

- Ask LLMs to do the same

- Observe everyone people → completeley different LLM answers

- Understand hidden sampling parameters and non‑determinism

4. Thematic Analysis — Dictionary vs ML vs LLM

- Run a dictionary‑based classifier

- Run naive ML

- Run weighted ML (learns from human corrections)

- Ask LLMs to tag the same data

- Compare accuracy, cost, drift, and reliability

5. Agents & Orchestration

- See how Claude Agents run tools, code, and workflows

- Compare agentic orchestration vs Python orchestration

- Understand when to use each

- Build hybrid systems

## Final Showcase (Day 4)

You’ll present an AI idea, prototype, or reflection.
Projects are scored on:

- Interesting — creative, novel, insightful

- Practical — could actually work

- Mindful — considers risk, governance, and impact

You can work solo or in groups.
You can use Python, LLMs, agents, or hybrids.