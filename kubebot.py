import json
import subprocess
import os
import colorama
import sys
import itertools
import threading
import time
import openai
from colorama import Fore
import inquirer

os.system('clear')

colorama.init()

YELLOW = "\x1b[1;33;40m" 

config = open('openai-config.json')

openai.api_key = json.load(config)["api_key"]

def manage_context():
    contexts = []
    get_contexts_command = subprocess.Popen("kubectl config get-contexts", stdout=subprocess.PIPE, shell=True, universal_newlines=True)

    for line in get_contexts_command.stdout:
        contexts.append(line.split()[0])

    contexts.pop(0)

    contexts.pop(len(contexts)-1)

    questions = [
    inquirer.List('Context set to: ',
                    message="Select Cluster Context ?",
                    choices=contexts,
                ),
    ]
    answers = inquirer.prompt(questions)

    selected_contexts = answers.get("Context set to: ")

    set_contexts_command = subprocess.Popen("kubectl config use-context " + selected_contexts, stdout=subprocess.PIPE, shell=True, universal_newlines=True)

    for line in set_contexts_command.stdout:
        sys.stdout.write(f"{Fore.MAGENTA}{line}")

#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\r' + c)
        sys.stdout.flush()
        time.sleep(0.1)

manage_context()

while(True):
    print(f"\n{Fore.GREEN}How we can help? ", end='')
    user_input = input()
    if user_input == "!conext":
        manage_context()
        user_input = ""

    os.system('clear')
    Fore.WHITE
    done = False  
    
    t = threading.Thread(target=animate)
    t.start()

    try:
        response = openai.Completion.create(
        model="code-davinci-002",
        prompt="kubectl command to " + user_input,
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        done = True

        print(response._previous["choices"][0]["text"].splitlines()[1].replace("+", ""))
        
        tmp_command = list(filter(None, response._previous["choices"][0]["text"].splitlines())) 
        tmp_command = list(filter(lambda k: "kubectl" in k, tmp_command))
        
        command = tmp_command[0].replace("+", "")
        
        print(f"RUN: {command}\n")
        
        print(f"{Fore.YELLOW}Execute this command?[type y to execute] " , end='')
        is_approve = input()

        if  is_approve == "y":        
            p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
            for line in p.stdout:
                sys.stdout.write(f"{Fore.MAGENTA}{line}")
                sys.stdout.flush()

    except Exception as ex:
        print(str(ex))
        print(command)
        done = True
