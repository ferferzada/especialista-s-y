from typing import List

from OpcaoCarreira import OpcaoCarreira


class InterfaceUsuario:
    """Responsável por interagir com o usuário (entrada e saída)."""

    @staticmethod
    def ask_yes_no(prompt: str) -> bool:
        while True:
            resp = input(f"{prompt} (s/n): ").strip().lower()
            if resp in {"s", "sim", "y", "yes"}:
                return True
            if resp in {"n", "nao", "não", "no"}:
                return False
            print("Por favor, responda apenas com 's' para SIM ou 'n' para NÃO.")

    @staticmethod
    def imprimir_recomendacoes(top: List[OpcaoCarreira], limite: int = 3):
        print("\n📌 Recomendações de Plano de Carreira (Top {}):".format(limite))
        for i, opc in enumerate(top[:limite], start=1):
            print(f"\n{i}. {opc.nome}  —  Pontos: {opc.score}")
            print(f"   {opc.descricao}")
            if opc.motivos:
                print("   Razões detectadas:")
                for m in opc.motivos[:5]:
                    print(f"    • {m}")
            else:
                print("   (sem razões registradas)")
    @staticmethod
    def imprimir_sugestoes_acao(opcao: OpcaoCarreira):
        print("\n🎯 Próximos passos sugeridos para:", opcao.nome)
        if opcao.nome == "Especialista Técnico":
            print("   • Foque em uma stack e construa projetos reais.")
        elif opcao.nome == "Gestão/Liderança":
            print("   • Estude gestão de equipes e pratique liderança informal.")
        elif opcao.nome == "Mudança de Área":
            print("   • Monte plano de transição e faça networking.")
        elif opcao.nome == "Empreendedorismo":
            print("   • Valide ideias de negócio com clientes reais.")
        elif opcao.nome == "Consultoria/Freelancer":
            print("   • Estruture portfólio e defina nicho de atuação.")
        elif opcao.nome == "Pesquisa/Academia":
            print("   • Considere mestrado/doutorado e artigos acadêmicos.")
        else:
            print("   • Defina metas claras e revise mensalmente.")
