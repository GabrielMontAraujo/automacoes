import os

# Estrutura completa baseada no enunciado
estrutura = {
    "Programa_Especializacao_DevOps": {
        "Modulo_A_Fundamentos_Nuvem": {
            "1_Estrategia_e_Economia": {
                "Cliente_1": [
                    "Relatorio_Estrategia.docx",
                    "Apresentacao_Estrategia.pptx",
                    "Resultados_Financeiros.xlsx"
                ],
                "Cliente_2": [
                    "Relatorio_Estrategia.docx",
                    "Apresentacao_Estrategia.pptx",
                    "Resultados_Financeiros.xlsx"
                ]
            },
            "2_Planejamento": {
                "Cliente_1": [
                    "Plano_Adocao.docx",
                    "Backlog_Azure_DevOps.xlsx",
                    "Plano_Capacitacao.docx"
                ],
                "Cliente_2": [
                    "Plano_Adocao.docx",
                    "Backlog_Azure_DevOps.xlsx",
                    "Plano_Capacitacao.docx"
                ]
            },
            "3_Prontidao_e_Landing_Zone": {
                "Scripts": [
                    "identity_config.bicep",
                    "network_topology.bicep",
                    "resource_naming_tagging.json"
                ],
                "Evidencias": {
                    "Cliente_1": [
                        "Capturas_Tela.pdf",
                        "Descricao_Config.docx"
                    ],
                    "Cliente_2": [
                        "Capturas_Tela.pdf",
                        "Descricao_Config.docx"
                    ]
                }
            },
            "4_Governanca": {
                "Cliente_1": [
                    "Politicas_Azure_Policy.json",
                    "Documentacao_Governanca.docx"
                ],
                "Cliente_2": [
                    "Politicas_Azure_Policy.json",
                    "Documentacao_Governanca.docx"
                ]
            },
            "5_Gerenciamento": {
                "Cliente_1": [
                    "Configuracao_Azure_Monitor.docx",
                    "Scripts_Azure_Automation.ps1",
                    "Configuracao_Backup.docx"
                ],
                "Cliente_2": [
                    "Configuracao_Azure_Monitor.docx",
                    "Scripts_Azure_Automation.ps1",
                    "Configuracao_Backup.docx"
                ]
            }
        },
        "Modulo_B_DevOps_GitHub_Azure": {
            "1_Praticas_Consultoria": [
                "Pagina_Publica.md",
                "Carta_Praticas.docx",
                "Roteiro_DevOps.docx"
            ],
            "Opcionais": [
                "Documentacao_Arquitetura.docx",
                "Questionarios_Avaliacao.docx",
                "Processo_Controle_Changes.docx"
            ],
            "2_Avaliacao": {
                "Cliente_1": [
                    "Avaliacao_Ambiente.docx",
                    "Pipeline_Documentacao.pdf"
                ],
                "Cliente_2": [
                    "Avaliacao_Ambiente.docx",
                    "Pipeline_Documentacao.pdf"
                ],
                "Cliente_3_GitHub": [
                    "Avaliacao_Ambiente.docx",
                    "Pipeline_Documentacao.pdf"
                ]
            },
            "3_Design": {
                "Infraestrutura_Codigo": [
                    "Terraform_Config.tf",
                    "Segurança_Workflow.yaml",
                    "Diagramas_Arquitetura.drawio"
                ],
                "Well_Architected_Review": [
                    "Cliente_1_Review.pdf"
                ]
            },
            "4_Entrega": {
                "Repositorios_Git": {
                    "Cliente_1": ["Scripts_CI_CD.yaml"],
                    "Cliente_2": ["Scripts_CI_CD.yaml"]
                },
                "SOWs": [
                    "Declaração_Projeto_Cliente_1.docx",
                    "Declaração_Projeto_Cliente_2.docx",
                    "Declaração_Projeto_Cliente_3.docx"
                ]
            },
            "5_Revisao_Operacoes": {
                "Validacoes": {
                    "Cliente_1": [
                        "Testes_Validacao.docx",
                        "Feedback_Cliente.pdf"
                    ],
                    "Cliente_2": [
                        "Testes_Validacao.docx",
                        "Feedback_Cliente.pdf"
                    ],
                    "Cliente_3": [
                        "Testes_Validacao.docx",
                        "Feedback_Cliente.pdf"
                    ]
                },
                "KPIs": [
                    "Relatorio_KPIs.docx",
                    "Graficos_Analise.xlsx"
                ]
            }
        },
        "Certificacoes": {
            "Certificados_GitHub_Actions.pdf": [],
            "Certificados_GitHub_Admin.pdf": [],
            "Outros": [
                "Certificado_MS_Learn.pdf",
                "Certificado_Azure.pdf"
            ]
        }
    }
}

# Função para criar diretórios e arquivos
def criar_estrutura(base_path, estrutura):
    for nome, conteudo in estrutura.items():
        caminho = os.path.join(base_path, nome)
        try:
            os.makedirs(caminho, exist_ok=True)  # Criação de diretórios
        except OSError as e:
            print(f"Erro ao criar diretório {caminho}: {e}")
            continue

        if isinstance(conteudo, dict):  # Caso o conteúdo seja um dicionário, crie subpastas
            criar_estrutura(caminho, conteudo)
        elif isinstance(conteudo, list):  # Caso o conteúdo seja uma lista, crie os arquivos
            for arquivo in conteudo:
                try:
                    caminho_arquivo = os.path.join(caminho, arquivo)
                    with open(caminho_arquivo, 'w') as f:
                        pass  # Cria um arquivo vazio
                except OSError as e:
                    print(f"Erro ao criar arquivo {caminho_arquivo}: {e}")
                    continue

# Caminho base para criação
base_path = os.path.expanduser("~/Documentos/Estrutura_DevOps")

# Executa a criação da estrutura
try:
    criar_estrutura(base_path, estrutura)
    print(f"Estrutura criada com sucesso em: {base_path}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
