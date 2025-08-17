from typing import Dict

from InterfaceUsuario import InterfaceUsuario
from MotorInferencia import MotorInferencia
from OpcaoCarreira import OpcaoCarreira
from PerguntaLoader import PerguntaLoader
from SistemaEspecialista import SistemaEspecialista


def inicializar_opcoes() -> Dict[str, OpcaoCarreira]:
    return {
        "especialista": OpcaoCarreira("Especialista Técnico", "Aprofundar-se tecnicamente."),
        "gestao": OpcaoCarreira("Gestão/Liderança", "Liderança de pessoas e processos."),
        "mudanca_area": OpcaoCarreira("Mudança de Área", "Migrar para nova função."),
        "empreendedorismo": OpcaoCarreira("Empreendedorismo", "Criar negócio próprio."),
        "academia": OpcaoCarreira("Pesquisa/Academia", "Seguir mestrado/doutorado."),
        "consultoria": OpcaoCarreira("Consultoria/Freelancer", "Atuar por projetos."),
        "promocao_interna": OpcaoCarreira("Plano Interno (Promoção)", "Crescer na empresa atual."),
        "inicio_carreira": OpcaoCarreira("Estágio/Trainee/Entry-level", "Porta de entrada para iniciantes."),
        "requalificacao": OpcaoCarreira("Requalificação/Upskilling", "Certificações e novos estudos."),
        "pausa": OpcaoCarreira("Pausa Estratégica", "Pausa para saúde/vida pessoal."),
    }


# ======================
# EXECUÇÃO PRINCIPAL
# ======================

if __name__ == "__main__":
    opcoes = inicializar_opcoes()
    perguntas = PerguntaLoader.carregar_arquivo("perguntas.json")  # ← lê do arquivo
    motor = MotorInferencia(opcoes, perguntas)
    interface = InterfaceUsuario()
    sistema = SistemaEspecialista(interface, motor)
    sistema.executar()