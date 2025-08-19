from dataclasses import dataclass, field
from typing import List, Dict, Callable, Any

@dataclass
class Career:
    nome: str
    dominios: List[str]
    educacao_min: str
    ambiente: List[str]
    core_skills: List[str]
    soft_skills: List[str]
    salario: str
    demanda: str

@dataclass
class Rule:
    nome: str
    cond: Callable[[Dict[str, Any]], bool]
    effect: Callable[["WorkingMemory"], None]
    explain: str

@dataclass
class WorkingMemory:
    fatos: Dict[str, Any]
    scores: Dict[str, float] = field(default_factory=dict)
    reasons: Dict[str, List[str]] = field(default_factory=dict)


    def boost_domain(self, domain: str, pts: float, reason: str):
        for c in CAREERS.values():
            if domain in c.dominios:
                self.scores[c.nome] = self.scores.get(c.nome, 0.0) + pts
                self.reasons.setdefault(c.nome, []).append(f"(+{pts:.1f}) {reason}")

    def boost_career(self, career: str, pts: float, reason: str):
        self.scores[career] = self.scores.get(career, 0.0) + pts
        self.reasons.setdefault(career, []).append(f"(+{pts:.1f}) {reason}")

    def penalize_career(self, career: str, pts: float, reason: str):
        self.scores[career] = self.scores.get(career, 0.0) - pts
        self.reasons.setdefault(career, []).append(f"(-{pts:.1f}) {reason}")