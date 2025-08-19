from typing import Dict, Any, List

from sistema_especialista.knowledge_base import CAREERS
from sistema_especialista.models import WorkingMemory, Rule


class InferenceEngine:
    def __init__(self, rules: List[Rule]):
        self.rules = rules

    def run(self, fatos: Dict[str, Any]) -> WorkingMemory:
        wm = WorkingMemory(fatos=fatos)
        for c in CAREERS:
            wm.scores[c] = 0.0
            wm.reasons[c] = []

        for r in self.rules:

            print(f"DEBUG: Avaliando regra '{r.nome}'. Condição é: {r.cond(fatos)}")
            try:
                if r.cond(fatos):
                    r.effect(wm)
            except Exception as e:
                wm.reasons.setdefault("__erros__", []).append(f"Regra {r.nome} falhou: {e}")


        return wm