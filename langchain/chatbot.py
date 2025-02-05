import os
from dotenv import load_dotenv
load_dotenv()

os.environ['GROQ_API_KEY']=os.getenv("GROQ_API_KEY")
## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")


from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

# prompt template
from langchain.prompts import ChatPromptTemplate
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Questions:{question}")
    ]
)

#streamlit framework

st.title("Groq Chatbot")
input_text=st.text_input("Search for anything...")

#model
llm = ChatGroq(model="llama3-8b-8192")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser


if input_text:
    st.write(chain.invoke({'question': input_text}))






