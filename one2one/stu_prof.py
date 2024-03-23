import os 
from autogen import ConversableAgent

import pprint

import colorama
colorama.init()

config_list = {
    "config_list":[{"model":"gpt-4", "api_key":os.environ["OPENAI_API_KEY"]}]
}

student_agent = ConversableAgent(
    name="Student_agent",
    system_message = "You are a student willing to learn",
    llm_config=config_list,
)

teacher_agent = ConversableAgent(
    name="Reacher_agent",
    system_message = "You are a math teacher.",
    llm_config={"config_list": [{"model": "gpt-4", "api_key": os.environ["OPENAI_API_KEY"]}]},
)

# chat_result = student_agent.initiate_chat(teacher_agent,message="What is triangle inequality?",summary_method="reflection_with_llm",max_turns=2)
chat_result = student_agent.initiate_chat(teacher_agent,message="What is the triangle inequality?",summary_method="reflection_with_llm",max_turns=2)

print(type(chat_result.chat_history)) # chat_history is a list
print("chat result: ")
pprint.pprint(chat_result.chat_history)