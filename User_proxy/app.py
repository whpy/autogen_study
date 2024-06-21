import autogen
import os

import colorama
colorama.init()

config_list=[
    {
        "model":"gpt-4",
        "api_key":os.environ["OPENAI_API_KEY"]
    }
]

llm_config = {
        "seed":42,
        "config_list":config_list,
        "temperature":0
    }


ass0 = autogen.AssistantAgent(
    name="ass0",
    llm_config=llm_config
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x:x.get("content","").rstrip().endswith("TERMINATE"), # the msg is a dict with "content" and "role" key
    llm_config=llm_config,
    system_message="Reply TERMINATE if the task has been solved at full satisfaction. Otherwise, reply CONTINUE or the reason why the task is not solved yet",
    code_execution_config={"work_dir":"coding", "use_docker":False}
)

task = """Write python code to output numbers 1 to 100, do not execute it but store it in a file."""

user_proxy.initiate_chat(
    ass0,
    message=task
)