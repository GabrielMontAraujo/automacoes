
# Exemplo de Criação de Estrutura de Pastas e Arquivos

Este repositório contém um exemplo de como criar estruturas organizadas de pastas e arquivos utilizando Python. Este script é útil para automatizar a criação de diretórios e arquivos em projetos que seguem padrões específicos, como programas de especialização, consultorias, ou quaisquer outras iniciativas com grande volume de organização.

## Fórmula de Criação da Estrutura

A estrutura é definida em um dicionário Python, seguindo esta lógica:

- **Chaves**: Representam o nome das pastas.  
- **Valores**:
  - Outro dicionário (`dict`) -> Representa subpastas dentro da pasta.
  - Lista (`list`) -> Representa os arquivos a serem criados dentro da pasta.

### Exemplo de Estrutura:

```python
estrutura = {
    "Pasta_Principal": {
        "Subpasta_1": [
            "arquivo1.txt",
            "arquivo2.docx"
        ],
        "Subpasta_2": {
            "SubSubpasta": [
                "script.py",
                "config.json"
            ]
        }
    }
}
```

### O Script

O script percorre essa estrutura recursivamente e utiliza as funções `os.makedirs()` para criar diretórios e `open()` para criar arquivos vazios. Você pode personalizar o dicionário para atender às necessidades do seu projeto.

### Estrutura Criada por Este Exemplo

A estrutura gerada pelo script para este exemplo é a seguinte:

```
Programa_Especializacao_DevOps/
├── Modulo_A_Fundamentos_Nuvem/
│   ├── 1_Estrategia_e_Economia/
│   │   ├── Cliente_1/
│   │   │   ├── Relatorio_Estrategia.docx
│   │   │   ├── Apresentacao_Estrategia.pptx
│   │   │   └── Resultados_Financeiros.xlsx
│   │   └── Cliente_2/
│   │       ├── Relatorio_Estrategia.docx
│   │       ├── Apresentacao_Estrategia.pptx
│   │       └── Resultados_Financeiros.xlsx
│   ├── 2_Planejamento/
│   │   ├── Cliente_1/
│   │   └── Cliente_2/
│   └── ...
├── Modulo_B_DevOps_GitHub_Azure/
│   ├── 1_Praticas_Consultoria/
│   │   ├── Pagina_Publica.md
│   │   └── Carta_Praticas.docx
│   ├── 2_Avaliacao/
│   │   ├── Cliente_1/
│   │   └── Cliente_3_GitHub/
│   └── ...
└── Certificacoes/
    ├── Certificados_GitHub_Actions.pdf
    ├── Certificados_GitHub_Admin.pdf
    └── Outros/
        ├── Certificado_MS_Learn.pdf
        └── Certificado_Azure.pdf
```

## Como Usar

1. Clone este repositório ou copie o script `estrutura_devops.py`.
2. Personalize o dicionário `estrutura` no script para refletir as necessidades do seu projeto.
3. Execute o script para criar as pastas e arquivos automaticamente.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests com melhorias no script ou neste README.

---

Com este script, você pode economizar tempo e manter a organização em projetos complexos. 🚀
