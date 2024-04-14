# imports
from dotenv import load_dotenv
import os
import pandas as pd
from llama_index.core.query_engine import PandasQueryEngine   # With llama_index.core.query engine call fixed.
from prompts import new_prompt, instruction_str, context
from note_engine import note_engine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms import openai

#load the API keys
load_dotenv() 

population_path = os.path.join("data","population.csv")  # specifies the data path 
population_df = pd.read_csv(population_path)             # population data frame, loading in files with pandas /read in population data

print(population_df.head())                              # state testing

population_query_engine = PandasQueryEngine(
    df=population_df, verbose=True, instruction_str=instruction_str      # allow for thoughts, detail output when using data engine
)
population_query_engine.update_prompts({"pandas_prompt": new_prompt})     # Pass in a python dictionary
#population_query_engine.query("What is the population of canada")        # Example query state testing

tools = [
    note_engine,
    QueryEngineTool(
        query_engine=population_query_engine,
        metadata=ToolMetadata(
        name="population_data",
        description="this gives information at the world population and demographics"
        )
    )
]

llm = openai(model="gpt-3.5-turbo-0613") 
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)

while(prompt:=input("Enter a prompt(q to quit): ")) != "q":
    result = agent.query(prompt)
    print(result)