# 데이터 모델이 필요한 경우 정의
# FastAPI와 Pydantic을 사용한 모델 예시

from pydantic import BaseModel

class SearchQuery(BaseModel):
    query: str