import json
from typing import List
from Pergunta import Pergunta


class PerguntaLoader:
    """Carrega perguntas de um arquivo externo (JSON)."""

    @staticmethod
    def carregar_arquivo(caminho: str) -> List['Pergunta']:
        with open(caminho, "r", encoding="utf-8") as f:
            data = json.load(f)

        perguntas = []
        for item in data:
            perguntas.append(Pergunta(
                texto=item["texto"],
                impactos_sim=item.get("impactos_sim", {}),
                impactos_nao=item.get("impactos_nao", {}),
                motivo=item.get("motivo", "")
            ))
        return perguntas
