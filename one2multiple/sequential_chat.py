import os 
from autogen import ConversableAgent

import pprint

import colorama
colorama.init()

config_list = {
    "config_list":[
        {"model":"gpt-4", 
        "api_key":os.environ["OPENAI_API_KEY"]
        }
        ]
}

host_agent = ConversableAgent(
    name="host_agent",
    system_message="You are a host of the whole calculation, just repeat the number you receive.",
    llm_config = config_list,
    human_input_mode="NEVER"
)

number_agent = ConversableAgent(
    name="number_agent",
    system_message="You generate 4 integral number randomly, one number each line",
    llm_config = config_list,
    human_input_mode="NEVER"
)

adder_agent = ConversableAgent(
    name="adder_agent",
    system_message="You add 1 to each number I give you and return me the new number, one number each line.",
    llm_config = config_list,
    human_input_mode="NEVER"
)

multiplier_agent = ConversableAgent(
    name="multiplier_agent",
    system_message="You multiply each number I give you by 2 and return me the new number, one number each line.",
    llm_config = config_list,
    human_input_mode="NEVER"
)

chat_results = host_agent.initiate_chats(
    [
        {
            "recipient": number_agent,
            "message":" please generate the numbers",
            "max_turns": 1,
            "summary_method": "last_msg",
        },

        {
            "recipient": adder_agent,
            "message":" These are my numbers",
            "max_turns": 2,
            "summary_method": "last_msg",
        },
        {
            "recipient": multiplier_agent,
            "message":"These are my numbers",
            "max_turns": 2,
            "summary_method": "last_msg",
        },
    ]
)

# print("chat results: ")
# pprint.pprint(chat_results.chat_history)