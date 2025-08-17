# knowledge_base.py
from typing import Dict, List, Any
from .models import Career, Rule, WorkingMemory

# --- Base de Conhecimento (Dados) ---
CAREERS: Dict[str, Career] = {
    "Desenvolvedor de Software": Career(
        nome="Desenvolvedor de Software",
        dominios=["tech"],
        educacao_min="graduacao",
        ambiente=["remoto", "hibrido", "presencial"],
        core_skills=["programacao", "logica", "estruturas_dados"],
        soft_skills=["resolucao_problemas", "trabalho_equipa"],
        salario="alto",
        demanda="em_alta",
    ),
    "Cientista de Dados": Career(
        nome="Cientista de Dados",
        dominios=["tech", "dados"],
        educacao_min="graduacao",
        ambiente=["remoto", "hibrido"],
        core_skills=["estatistica", "python", "machine_learning"],
        soft_skills=["storytelling", "pensamento_critico"],
        salario="alto",
        demanda="em_alta",
    ),
    "Analista de Marketing Digital": Career(
        nome="Analista de Marketing Digital",
        dominios=["negocios", "marketing"],
        educacao_min="graduacao",
        ambiente=["remoto", "hibrido", "presencial"],
        core_skills=["seo", "midias_sociais", "analytics"],
        soft_skills=["comunicacao", "criatividade"],
        salario="medio",
        demanda="em_alta",
    ),
    "Designer UX/UI": Career(
        nome="Designer UX/UI",
        dominios=["design", "tech"],
        educacao_min="graduacao",
        ambiente=["remoto", "hibrido"],
        core_skills=["ux", "ui", "prototipacao"],
        soft_skills=["empatia", "comunicacao"],
        salario="alto",
        demanda="em_alta",
    ),
    "Técnico de Suporte de TI": Career(
        nome="Técnico de Suporte de TI",
        dominios=["tech"],
        educacao_min="tecnico",
        ambiente=["presencial", "hibrido"],
        core_skills=["redes", "sistemas", "atendimento"],
        soft_skills=["paciência", "comunicacao"],
        salario="medio",
        demanda="estavel",
    ),
    "Engenheiro de Produção": Career(
        nome="Engenheiro de Produção",
        dominios=["industria", "operacoes"],
        educacao_min="graduacao",
        ambiente=["presencial", "hibrido"],
        core_skills=["processos", "lean", "dados"],
        soft_skills=["analitico", "lideranca"],
        salario="alto",
        demanda="estavel",
    ),
    "Enfermeiro": Career(
        nome="Enfermeiro",
        dominios=["saude"],
        educacao_min="graduacao",
        ambiente=["presencial"],
        core_skills=["assistencia", "protocolos", "urgencia"],
        soft_skills=["empatia", "comunicacao"],
        salario="medio",
        demanda="em_alta",
    ),
    "Vendedor Técnico (B2B)": Career(
        nome="Vendedor Técnico (B2B)",
        dominios=["negocios", "vendas"],
        educacao_min="nenhuma",
        ambiente=["campo", "presencial", "hibrido"],
        core_skills=["negociacao", "produto", "relacionamento"],
        soft_skills=["comunicacao", "persuasao"],
        salario="alto",
        demanda="estavel",
    ),
}

# --- Motor de Regras ---
W = {
    "forte": 6.0,
    "medio": 3.0,
    "fraco": 1.0,
    "hard_match": 5.0,
    "soft_match": 2.5,
    "demanda_alta": 2.0,
    "salario_alto": 1.5,
}

def has(f: Dict[str, Any], key: str, value: Any) -> bool:
    v = f.get(key)
    if isinstance(v, list):
        return value in v
    return v == value

def any_match(f: Dict[str, Any], key: str, values: List[str]) -> bool:
    v = f.get(key, [])
    return any(x in v for x in values)

# --- Lista de Regras (Lógica) ---
RULES: List[Rule] = []

# Interesses principais mapeados para domínios
RULES.append(Rule(
    nome="Interesse em Tech",
    cond=lambda f: any_match(f, "interesses", ["tech"]),
    effect=lambda wm: wm.boost_domain("tech", W["forte"], "Interesse declarado em tecnologia"),
    explain="Se o usuário gosta de Tech, carreiras do domínio de tecnologia recebem pontos.",
))
# Adicione todas as outras regras aqui, como estavam no código original.
# Certifique-se de que a lista `RULES` contém todas elas.
RULES.append(Rule(
    nome="Interesse em Dados",
    cond=lambda f: any_match(f, "interesses", ["dados", "analise_dados"]),
    effect=lambda wm: wm.boost_domain("dados", W["forte"], "Interesse declarado em dados"),
    explain="Preferência por trabalhar com dados impulsiona carreiras desse domínio.",
))
# ... (todas as outras regras)
RULES.append(Rule(
    nome="Demanda em Alta",
    cond=lambda f: True,
    effect=lambda wm: [
        wm.boost_career(c.nome, W["demanda_alta"], "Demanda de mercado em alta")
        for c in CAREERS.values() if c.demanda == "em_alta"
    ],
    explain="Áreas quentes recebem bônus base.",
))