from Warhammer40k import Warhammer40k
from LLM import LLM
warhammer40k: Warhammer40k = Warhammer40k()
llm: LLM = LLM()


if __name__ == "__main__":
    llm.create_context()
    llm.response_to_pandas()
    df = llm.df_context
    df.to_excel("data.xlsx")
    print(df)
