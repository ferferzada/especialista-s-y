# cli.py
import json
from typing import Dict, Any
from .career_expert import CareerExpert


def run_cli():
    """Lida com a interação com o usuário via terminal."""
    expert = CareerExpert()

    print("\n=== Orientador de Carreira (Sistema Especialista) ===\n")
    print("Responda de forma simples. Exemplos: tech, dados, design, marketing...")

    perfil: Dict[str, Any] = {}
    perfil["interesses"] = input("Principais interesses (lista separada por vírgula): ").strip().lower().replace(" ",
                                                                                                                 "").split(
        ",")
    perfil["forcas"] = input(
        "Suas forças/habilidades (ex: programacao, comunicacao, estatistica): ").strip().lower().replace(" ", "").split(
        ",")
    perfil["valores"] = input(
        "O que você valoriza? (ex: salario, estabilidade, impacto, flexibilidade): ").strip().lower().replace(" ",
                                                                                                              "").split(
        ",")
    perfil["preferencia_trabalho"] = input(
        "Preferência de trabalho (remoto/presencial/hibrido/campo): ").strip().lower()
    perfil["educacao"] = input("Nível educacional (nenhuma/tecnico/graduacao/pos): ").strip().lower()
    try:
        perfil["xp_programacao_anos"] = float(
            input("Anos de experiência em programação (número, 0 se nenhuma): ").strip())
    except Exception:
        perfil["xp_programacao_anos"] = 0.0
    perfil["perfil"] = input("Seu perfil (introvertido/extrovertido/analitico): ").strip().lower()

    resultado = expert.recomendar(perfil)

    print("\n=== Recomendações ===")

    # Este 'if' e 'else' tratam do caso em que não há recomendações
    if not resultado["recomendacoes"]:
        print("\nNenhuma recomendação foi gerada com base no seu perfil. Tente responder de forma diferente.")
    else:
        # Este laço 'for' mostra as recomendações no console
        for rec in resultado["recomendacoes"]:
            print(f"\n- {rec['carreira']} (score {rec['score']})")
            print(f"  Domínios: {', '.join(rec['dominios'])}")
            print(f"  Ambiente: {', '.join(rec['ambiente'])}")
            print("  Explicações:")
            for r in rec["explicacoes"]:
                print(f"    • {r}")
            print("  Próximos passos:")
            for p in rec["proximos_passos"]:
                print(f"    • {p}")


if __name__ == "__main__":
    run_cli()