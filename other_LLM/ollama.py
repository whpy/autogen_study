from autogen import UserProxyAgent, ConversableAgent
import os


# For now we only work on windows platform, the configuration is as follow:
# 1. python 3.11.8
# 2. autogen
# 3. litellm[proxy] (pip install "litellm[proxy]")
# 4. ollama(model == llama2), installed by windows installer

# The process create interface of local llm:
# 1. open an terminal, input "litellm --model ollama/llama2"(if the local is llama2)
# 2. It would show an address like "0.0.0.0:4000"
# 3. we can create multiple terminal to introduce multiple local model
# 4. fill the (modified) address into the llm_config below

local_llm_config={
    "config_list": [
        {
            "model": "llama2", # Loaded with LiteLLM command, only placeholder
            "api_key": "Null", # Not needed
            "base_url": "http://127.0.0.1:4000"  # Your LiteLLM URL, it would show 0.0.0.0:4000 but we should transform it into 127.0.0.1;4000. It should be noted that a terminal is required to maintain the url.
        }
    ],
    "cache_seed": None # Turns off caching, useful for testing different models
}



# Create the agent that uses the LLM.
assistant = ConversableAgent("agent", llm_config=local_llm_config)

# Create the agent that represents the user in the conversation.
user_proxy = UserProxyAgent("user", code_execution_config=False)

# Let the assistant start the conversation.  It will end when the user types exit.
assistant.initiate_chat(user_proxy, message="How can I help you today?")