from llama_index.core import PromptTemplate                      #llama_index.core path corrected

#Instruction String ; to tell engine what to do with PANDAS data
instruction_str = """\
    1. Convert the query to executable Python code using Pandas.
    2. The final line of code should be a Python expression that can be called with the `eval()` function.
    3. The code should represent a solution to the query.
    4. PRINT ONLY THE EXPRESSION.
    5. Do not quote the expression."""

# Specify format ; embed data we want within template ; context
new_prompt = PromptTemplate(
    """\
    You are working with a pandas dataframe in Python.
    The name of the dataframe is `df`.
    This is the result of `print(df.head())`:
    {df_str}  

    Follow these instructions:
    {instruction_str}
    Query: {query_str}

    Expression: """
)