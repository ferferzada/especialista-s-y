
import math
from typing import Dict, Any, List
from .knowledge_base import RULES, CAREERS
from .engine import InferenceEngine

class CareerExpert:
    def __init__(self):
        self.engine = InferenceEngine(RULES)

    def recomendar(self, perfil: Dict[str, Any], top_k: int = 5) -> Dict[str, Any]:
        wm = self.engine.run(perfil)

        scores = wm.scores.copy()
        ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        top = [(n, s) for n, s in ranked if not math.isclose(s, 0.0, abs_tol=1e-6)][:top_k]

        explicacoes: Dict[str, List[str]] = {k: wm.reasons.get(k, []) for k, _ in top}

        # Gera próximos passos
        next_steps = {}
        for nome, _ in top:
            c = CAREERS[nome]
            passos = [
                "Estudar fundamentos do domínio...",
                f"Validar fit com 1 projeto prático curto alinhado a {nome}",
                "Buscar 1 mentor...",
                "Montar um mini-portfólio...",
            ]
            next_steps[nome] = passos

        return {
            "perfil": perfil,
            "recomendacoes": [
                {
                    "carreira": nome,
                    "score": round(score, 2),
                    "dominios": CAREERS[nome].dominios,
                    "educacao_min": CAREERS[nome].educacao_min,
                    "ambiente": CAREERS[nome].ambiente,
                    "explicacoes": explicacoes.get(nome, []),
                    "proximos_passos": next_steps[nome],
                }
                for nome, score in top
            ],
            "todas_pontuacoes": {k: round(v, 2) for k, v in ranked},
        }