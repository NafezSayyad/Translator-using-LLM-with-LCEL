import getpass
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv, find_dotenv

# Load environment variables
load_dotenv(find_dotenv())

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "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"
os.environ["OPENAI_API_KEY"] = "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"

# Initialize the model
model = ChatOpenAI(model="gpt-4o-mini")

# Define the messages
# messages = [
#     SystemMessage(content="Translate the following from English into Italian"),
#     HumanMessage(content="hi!"),
# ]

system_template = "Translate the following into {language}:"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)
parser = StrOutputParser()
chain = prompt_template | model | parser
result = chain.invoke({"language": "italian", "text": "hi"})
# Invoke the model
# parser = StrOutputParser()
# chain = model | parser
# response=chain.invoke(messages)
print(result)
