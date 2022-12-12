import requests
import json
import subprocess
import os

os.system('clear')

config = open('config.json')

data = json.load(config)

url = "https://chat.openai.com/backend-api/conversation"

while(True):
    user_input = input("How we can help: ")

    payload = json.dumps({
        "action": "next",
        "messages": [
            {
                "id": "001bb819-ee7f-4cf1-9fa1-89120f4fd4a2",
                "role": "user",
                "content": {
                    "content_type": "text",
                    "parts": [
                        "kubectl command to " + user_input
                    ]
                }
            }
        ],
        "parent_message_id": "b7f73781-304b-4c88-b35c-e7111630780e",
        "model": "text-davinci-002-render"
    })
    headers = {
        'authority': 'chat.openai.com',
        'accept': 'event-stream',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,he;q=0.8',
        'authorization': data["authorization"],
        'content-type': 'application/json',
        'cookie': data["cookie"],
        'origin': 'https://chat.openai.com',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }

    try:
        response = requests.request("POST", url, headers=headers, data=payload)

        if response.status_code != 200:
            print("Reponse Status:" + str(response.status_code))

        response = response.text.split('data:')[-2]

        response_json = json.loads(response)

        msg = response_json["message"]["content"]["parts"][0]

        msg = msg.split("```\n")[1]

        msg = msg.split("\n")[0]

        print(msg)

        p = subprocess.Popen(msg, stdout=subprocess.PIPE, shell=True)

        print(p.communicate())

    except Exception as ex:
        print(str(ex))
        print(msg)