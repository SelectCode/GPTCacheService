from fastapi import FastAPI

app = FastAPI()

import time

from pydantic import BaseModel

from pydantic import BaseSettings


class Settings(BaseSettings):
    OPENAI_API_KEY: str
    DB_URL: str = "sqlite:///./database.db"
    INDEX_PATH: str = "./faiss.index"
    MODEL: str = "gpt-3.5-turbo"


settings = Settings()


class PromptQuery(BaseModel):
    prompt: str


def response_text(openai_resp):
    return openai_resp['choices'][0]['message']['content']


print("Cache loading.....")

# To use GPTCache, that's all you need
# -------------------------------------------------
from gptcache import cache
from gptcache.adapter import openai
from gptcache.manager import get_data_manager, CacheBase, VectorBase
from gptcache.embedding import Onnx

from gptcache.similarity_evaluation.distance import SearchDistanceEvaluation

onnx = Onnx()

cache.init(
    embedding_func=onnx.to_embeddings,
    data_manager=get_data_manager(CacheBase("sqlite", sql_url=settings.DB_URL),
                                  VectorBase("faiss", dimension=onnx.dimension,
                                             index_path=settings.INDEX_PATH)),
    similarity_evaluation=SearchDistanceEvaluation(),
)
cache.set_openai_key()


def ask(prompt: str):
    start_time = time.time()

    response = openai.ChatCompletion.create(
        model=settings.MODEL,
        messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ],
    )
    print("Time consuming: {:.2f}s".format(time.time() - start_time))
    return response_text(response)


@app.get("/")
def read_root():
    return "Hello World"


@app.get("/query")
def get_prompt(prompt: str):
    return ask(prompt)


@app.post("/query")
def post_prompt(query: PromptQuery):
    return ask(query.prompt)
