# kubechat
kubechat is a POC tool that runs kubectl commands based on the description of the need from the user

kubechat uses OpenAI and ChatGPT to generate the kubectl commands

## Installation

clone this repo

```bash
git clone https://github.com/containers-stack/kubebot.git
```

create a openai-config.json file with this content:
```json
{
    "authorization": "Bearer <NEED_TO_GET_THE_TOKEN_FROM https://chat.openai.com/chat>",
    "cookie": "<NEED_TO_GET_THE_COOKIE_FROM https://chat.openai.com/chat>" 
}
```

## To get the  acccess_tokne and cookie 
    1. Go to https://chat.openai.com/chat
    2. Open the developer console
    3. Go to Networking Tab
    4. Search for request with 'conversation' name 
    5. copy the authorization & cookie header from the requst header ans sace them into openai-config.json 

## Usage

```bash
cd ./kubebot
pip install -r requirement.txt 
python ./kubebot.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
