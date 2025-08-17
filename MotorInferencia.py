from typing import Dict, List, Tuple

from OpcaoCarreira import OpcaoCarreira
from Pergunta import Pergunta


class MotorInferencia:
    """Aplica regras de inferência com base nas respostas."""

    def __init__(self, opcoes: Dict[str, OpcaoCarreira], perguntas: List[Pergunta]):
        self.opcoes = opcoes
        self.perguntas = perguntas
        self.respostas: List[Tuple[int, bool]] = []

    def aplicar_resposta(self, idx_pergunta: int, resposta_sim: bool):
        pergunta = self.perguntas[idx_pergunta]
        impactos = pergunta.impactos_sim if resposta_sim else pergunta.impactos_nao
        for chave, delta in impactos.items():
            self.opcoes[chave].score += delta
            if delta > 0:
                sentido = "SIM" if resposta_sim else "NÃO"
                self.opcoes[chave].motivos.append(f"{sentido} → {pergunta.motivo} (+{delta})")

    def rankear(self) -> List[OpcaoCarreira]:
        return sorted(self.opcoes.values(), key=lambda o: (o.score, len(o.motivos)), reverse=True)