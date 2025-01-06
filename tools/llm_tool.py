import os
from typing import Annotated, Optional
from typing_extensions import TypedDict
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

with open(r'C:\local_workspace\x2bee_github_push\plateer_dataloader\api_key\API_KEY.txt', 'r') as api:
    os.environ["OPENAI_API_KEY"] = api.read()

class structured_output(TypedDict):
    korean: Annotated[str, ..., "한국어로 번역된 문장"]

# Model
model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
model = model.with_structured_output(structured_output)

def eng_to_kor(sentence:str):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", """
                당신은 최고 수준의 번역 전문가입니다.
                당신은 주어진 영어 문장을 한국어로 번역합니다.
                
                원본 문장에서 제시되는 단어의 의미를 최대한 유지하세요.
                임의로 문장의 의미를 해석하는 것은 허용되지 않습니다.
                최대한 사무적인 어조로 답변을 작성하세요.
                """),
            ("human", "Sentence: {sentence}")
        ]
    )
    
    chain = prompt | model
    result = chain.invoke({"sentence": sentence})

    return result['korean']