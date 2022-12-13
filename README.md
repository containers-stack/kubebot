# kubechat
kubechat is a POC tool that runs kubectl commands based on the description of the need from the user

kubechat uses OpenAI and ChatGPT to generate the kubectl commands

https://user-images.githubusercontent.com/27952544/207239553-5a21a370-40f6-44a1-9617-0430df21bc2d.mp4

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

https://user-images.githubusercontent.com/27952544/207239273-92f815fe-9ac6-4cf4-9699-a11f937bc6d6.mp4


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
