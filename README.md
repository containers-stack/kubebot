# kubechat
kubechat is a POC tool that runs kubectl commands based on the description of the need from the user

kubechat uses OpenAI and Completion to generate the kubectl commands

https://user-images.githubusercontent.com/27952544/207239553-5a21a370-40f6-44a1-9617-0430df21bc2d.mp4

## Installation

clone this repo

```bash
git clone https://github.com/containers-stack/kubebot.git
```

create a openai-config.json file with this content:
```json
{
    "api_key": "<REPLACE WITH openai KEY"
}
```

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
