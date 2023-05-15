from fastapi import FastAPI
import time
from pydantic import BaseModel, BaseSettings


# Settings
class Settings(BaseSettings):
    OPENAI_API_KEY: str
    DB_URL: str = "sqlite:///./database.db"
    INDEX_PATH: str = "./faiss.index"
    MODEL: str = "gpt-3.5-turbo"  # Can also be set to "gpt-4"


settings = Settings()


# Models
class PromptQuery(BaseModel):
    prompt: str


# OpenAI API utilities
from gptcache import cache, adapter, manager, embedding
from gptcache.adapter import openai
from gptcache.similarity_evaluation.distance import SearchDistanceEvaluation


def response_text(openai_resp):
    return openai_resp['choices'][0]['message']['content']


# Cache initialization
print("Cache loading.....")

onnx = embedding.Onnx()

cache.init(
    embedding_func=onnx.to_embeddings,
    data_manager=manager.get_data_manager(manager.CacheBase("sqlite", sql_url=settings.DB_URL),
                                          manager.VectorBase("faiss", dimension=onnx.dimension,
                                                             index_path=settings.INDEX_PATH)),
    similarity_evaluation=SearchDistanceEvaluation(),
)
cache.set_openai_key()


# Main function to get response from OpenAI
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


# FastAPI app
app = FastAPI()


@app.get("/")
def read_root():
    return "Hello World"


@app.get("/query")
def get_prompt(prompt: str):
    return ask(prompt)


@app.post("/query")
def post_prompt(query: PromptQuery):
    return ask(query.prompt)
