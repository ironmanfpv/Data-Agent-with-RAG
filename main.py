# imports
from dotenv import load_dotenv
import os
import pandas as pd
#import sys
#sys.path.append("C:\Users\akita\Data-Agent-with-RAG\ai\Lib\site-packages\llama_index")
from llama_index.core.query_engine import PandasQueryEngine   #With llama_index. query engine call fixed.
from prompts import new_prompt, instruction_str

#load the API keys
load_dotenv() 

population_path = os.path.join("data","population.csv")  # specifies the data path 
population_df = pd.read_csv(population_path)             # population data frame, loading in files with pandas /read in population data

print(population_df.head())                              # state testing

population_query_engine = PandasQueryEngine(
    df=population_df, verbose=True, instruction_str=instruction_str      # allow for thoughts, detail output when using data engine
)
population_query_engine.update_prompts({"pandas_prompt": new_prompt})     # Pass in a python dictionary
population_query_engine.query("What is the population of canada")         # Example query



 