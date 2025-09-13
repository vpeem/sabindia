import streamlit as st
from langchain_openai import ChatOpenAI

# Create dynamic prompts with variables.
from langchain_core.prompts import ChatPromptTemplate

# Parse and process the output from the language model.
from langchain_core.output_parsers import StrOutputParser

# Set the openai API key for authentication with OpenAI.
OPENAI_API_KEY = ""

# Initialize the LLM chat model. Here, we can declare other chat 
# models also like Anthropic, Azure, Google Geminin, AWS, Groq, etc.
llm = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-4o")

# Process or parse the output returned clean, usable string format by a language model
parser = StrOutputParser()

# Chain 1: Summarize prompt
our_prompt = ChatPromptTemplate.from_template("Create a list of all major {event} events with short description of each event that occured in {year}. Do not add any staring or ending statement other than the required list.")

# connects different components (like prompts, language models, 
# and output parsers) into a single pipeline.
our_chain = our_prompt | llm | parser

# Streamlit UI user input
st.title("Eventer⚽")
event = st.text_input("Enter an event:")
year1 = st.text_input("Enter a year:")


if st.button("Search"):
    with st.spinner("Generating Requested List"):
        # Step 1: Get response
        content = our_chain.invoke({"event": event, "year": year1})
        
    # Print output as JSON
    st.subheader("Event List")
    st.write(content)
