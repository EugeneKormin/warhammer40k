import pandas as pd

from Warhammer40k import Warhammer40k
from Prompts import Prompt
import requests

prompt: Prompt = Prompt()
warhammer40k: Warhammer40k = Warhammer40k()


class LLM(object):
    def __init__(self):
        self.__data_for_embedding: pd.DataFrame = pd.DataFrame({})

        self.__page_list = []
        self.__context_list = []
        self.__book_list = []
        self.__text_list = []

    def create_context(self) -> None:
        self.__ask_agent()
        self.response_to_pandas()

    def __ask_agent(self) -> None:
        for PAGE_NUM in range(16, 18):
            print(PAGE_NUM)
            if PAGE_NUM > 16:
                PREV_CONTEXT: str = warhammer40k.get_page_by_num(PAGE_NUM=PAGE_NUM-1)
                CONTEXT: str = warhammer40k.get_page_by_num(PAGE_NUM=PAGE_NUM)
                CONTEXT: str = f"{PREV_CONTEXT}\n{CONTEXT}"
            else:
                CONTEXT: str = warhammer40k.get_page_by_num(PAGE_NUM=PAGE_NUM)
            print(CONTEXT)
            tokens = requests.get(f"http://127.0.0.1:8082/invoke/tokens?text={CONTEXT}").text
            embedding = requests.get(f"http://127.0.0.1:8082/invoke/embeddings?text={CONTEXT}").text
            print(tokens)
            print(embedding)
            print(len(embedding)/len(tokens))
            break

    def response_to_pandas(self) -> None:
        self.__data_for_embedding: pd.DataFrame = pd.DataFrame({
            "page": self.__page_list,
            "book": self.__book_list,
            "text": self.__text_list,
        })

    @property
    def df_context(self) -> pd.DataFrame:
        return self.__data_for_embedding
