from InterfaceUsuario import InterfaceUsuario
from MotorInferencia import MotorInferencia


class SistemaEspecialista:
    """Orquestra todo o sistema especialista."""

    def __init__(self, interface: InterfaceUsuario, motor: MotorInferencia):
        self.interface = interface
        self.motor = motor

    def executar(self):
        print("=== Sistema Especialista de Plano de Carreira (SIM/NÃO) ===")
        print("Responda às perguntas para receber recomendações personalizadas.\n")

        for i, pergunta in enumerate(self.motor.perguntas):
            resposta = self.interface.ask_yes_no(pergunta.texto)
            self.motor.respostas.append((i, resposta))
            self.motor.aplicar_resposta(i, resposta)

        ordenadas = self.motor.rankear()
        self.interface.imprimir_recomendacoes(ordenadas, limite=3)

        if ordenadas:
            self.interface.imprimir_sugestoes_acao(ordenadas[0])

        print("\n📊 Pontuações finais:")
        for opc in ordenadas:
            print(f" - {opc.nome}: {opc.score}")
        print("\nObrigado por usar o sistema! 🚀")
