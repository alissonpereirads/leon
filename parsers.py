from pydantic import BaseModel, Field
from typing import List


class ResumoResposta(BaseModel):
    resumo: str = Field(..., description="Texto resumido gerado pelo modelo")
    topicos: List[str] = Field(
        ..., description="Lista de tópicos importantes extraídos do texto"
    )
