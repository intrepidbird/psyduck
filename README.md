# Psyduck 

![image](https://github.com/intrepidbird/psyduck/assets/140008493/8f868741-f1f5-458d-834e-93c2d058a1c5)

💻 Description: Psyduck AI

💻 Code can be found in [`main.py`](https://github.com/intrepidbird/psyduck/blob/main/main.py)

💻 **Wolfram AI** command is `!orz [prompt]`

💻 **OpenAI AI** command is `!ai [prompt]`


## 🚀 Getting started

### Installation Guide

1. Make sure you have python installed on your machine. If you haven't, you can get it from [official download link](https://www.python.org/downloads/).
2. Clone this repo by using git.
3. In the cloned repo, make a virtual environment by using `python -m venv env`.
4. Activate the virtual environment with `source env/bin/activate` on Linux, or `env\Scripts\Activate` on Windows.
5. Install the depedencies using `pip install -r requirements.txt`.

### Setup Guide

Go to `main.py` file. There are token and API keys that you need to fill in.

```python
openai.api_key = 'your-openai-api-key'
wolfram_api_key = 'your-wolfram-alpha-api-key'
bot_token = 'your-bot-token'
```

- To create openAI API key, you can get it from its [official website](https://openai.com/blog/openai-api). Then put the key on `openai.api_key`.
- To create wolfram API key, Go to the WolframAlpha Developer portal [here](https://developer.wolframalpha.com/). Then put the key on `wolfram_api_key`.
- To create discord bot token, follow the official instruction [here](https://discord.com/developers/docs/getting-started). Then put the token in `bot_token` variable. Don't forget to invite your created bot application into your discord server.

### Run the Bot

After all are set, run the bot using `python main.py`. Now you can interact with your bot by triggering the commands.

## 📝 License

[MIT](LICENSE)