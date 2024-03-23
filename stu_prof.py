import os 
from autogen import ConversableAgent

import colorama
colorama.init()


student_agent = ConversableAgent(
    name="Student_agent",
    system_message = "You are a student willing to learn",
    llm_config={"config_list": [{"model": "gpt-4", "api_key": os.environ["OPENAI_API_KEY"]}]},
)

teacher_agent = ConversableAgent(
    name="Reacher_agent",
    system_message = "You are a math teacher.",
    llm_config={"config_list": [{"model": "gpt-4", "api_key": os.environ["OPENAI_API_KEY"]}]},
)

# chat_result = student_agent.initiate_chat(teacher_agent,message="What is triangle inequality?",summary_method="reflection_with_llm",max_turns=2)
chat_result = student_agent.initiate_chat(teacher_agent,message="What is the triangle inequality?",summary_method="reflection_with_llm",max_turns=2)


print("chat result: ")
print(chat_result)