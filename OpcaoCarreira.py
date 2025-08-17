from dataclasses import dataclass, field
from typing import List

@dataclass
class OpcaoCarreira:
    """Representa uma opção de plano de carreira com score e motivos."""
    nome: str
    descricao: str
    score: int = 0
    motivos: List[str] = field(default_factory=list)
