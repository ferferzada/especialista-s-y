
from typing import Dict

class Pergunta:
    """Modela uma pergunta do sistema especialista."""
    def __init__(self, texto: str, impactos_sim: Dict[str, int], impactos_nao: Dict[str, int], motivo: str):
        self.texto = texto
        self.impactos_sim = impactos_sim
        self.impactos_nao = impactos_nao
        self.motivo = motivo