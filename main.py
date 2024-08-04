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
os.environ["LANGCHAIN_API_KEY"] = "LANGCHAIN_API_KEY"
os.environ["OPENAI_API_KEY"] = "OPENAI_API_KEY"

# Initialize the model
model = ChatOpenAI(model="gpt-4o-mini")

system_template = "Translate the following into {language}:"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)
parser = StrOutputParser()
chain = prompt_template | model | parser
result = chain.invoke({"language": "italian", "text": "hi"})

print(result)
