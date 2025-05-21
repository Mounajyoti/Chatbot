from huggingface_hub import InferenceClient
from utils.file_reader import read_file
import os
from utils.get_config import get_config

class Chatbot:
    """
    Chatbot class to handle interactions with the LLM.
    """

    def __init__(self):

        # Load configuration
        config = get_config()

        # LLM settings
        self.api_token = config['LLM']['api_token']
        self.model_name = config['LLM']['model_name']
        
        # Paths
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.info_path = os.path.join(base_dir, config['PATHS']['information_path'])
        self.prompt_path = os.path.join(base_dir, config['PATHS']['prompt_path'])
        
        # Chat settings
        self.max_new_tokens = int(config['SETTINGS']['max_new_tokens'])
        self.temperature = float(config['SETTINGS']['temperature'])
        self.history_limit = int(config['SETTINGS']['history_limit'])

        # Initialize client and load content
        self.client = InferenceClient(
            model=self.model_name,
            token=self.api_token
        )
        self.info_content = read_file(self.info_path)
        self.base_prompt = read_file(self.prompt_path)
        self.history = []

    def format_prompt(self, user_input):
        prompt = f"{self.base_prompt}\n\ninformation Content:\n{self.info_content}\n\n"
        prompt += '\nChat History:\n'
        for user_msg, bot_msg in self.history:
            prompt += f"User: {user_msg}\nAssistant: {bot_msg}\n"
        prompt += f"Based on the informations above, answer this : {user_input}"
        return prompt

    def get_response(self, user_input):
        prompt = self.format_prompt(user_input)
        response = self.client.text_generation(
            prompt=prompt,
            max_new_tokens=self.max_new_tokens,
            temperature=self.temperature,
            do_sample=True,
            stop=["User:", "Assistant:"],
            top_p=0.9,
            top_k=50
        )
        bot_reply = response.strip()
        self.history.append((user_input, bot_reply))
        # Keep history to configured limit
        if len(self.history) > self.history_limit:
            self.history = self.history[-self.history_limit:]
        return bot_reply

if __name__ == "__main__":
    chatbot = Chatbot()
    # print(chatbot.format_prompt("Hello!"))
    # print(chatbot.get_response('hi'))
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = chatbot.get_response(user_input)
        print(f"Assistant: {response}")