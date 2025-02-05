from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv
load_dotenv()

os.environ['GROQ_API_KEY']=os.getenv("GROQ_API_KEY")
## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

app=FastAPI(
    title="LangChain GroQ Chatbot",
    description="A chatbot using LangChain and GroQ",
    version="1.0"
)

add_routes(
    app,
    ChatGroq(),
    path="/Groq",
    )

model=ChatGroq()

prompt1=ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2=ChatPromptTemplate.from_template("Write me an poem about {topic} for a 5 years child with 100 words")

add_routes(
    app,
    prompt1|model,
    path="/essay"


)

add_routes(
    app,
    prompt2|model,
    path="/poem"


)


if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)
