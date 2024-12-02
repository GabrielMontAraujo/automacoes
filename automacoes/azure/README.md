# **Automação de Levantamento de Inventário no Azure**

Este projeto é uma automação em Python para coletar informações sobre recursos no Azure, incluindo inventário, configurações de rede e conformidade. A ferramenta utiliza o **Azure SDK for Python** para se autenticar e interagir com a API do Azure, fornecendo dados consolidados em um formato estruturado.

---

## **Funcionalidades**

- Listar todos os recursos no Azure (nome, tipo, grupo de recursos, região, etc.).
- Detalhar configurações de rede, incluindo VNets, sub-redes e endereços IP.
- Verificar políticas de conformidade e governança ativas nos recursos.
- Exportar os dados para um arquivo Excel para análise ou documentação.

---

## **Pré-requisitos**

1. **Python 3.7+**
   - Certifique-se de que o Python esteja instalado em sua máquina.
2. **Pacotes Necessários**
   - Instale as dependências com o comando:
     ```bash
     pip install azure-mgmt-resource azure-mgmt-network azure-identity pandas openpyxl
     ```
3. **Autenticação no Azure**
   - Configure o acesso ao Azure usando o **Azure CLI**:
     ```bash
     az login
     ```
   - Ou use uma identidade gerenciada ou variáveis de ambiente compatíveis com o `DefaultAzureCredential`.

---

## **Como Usar**

1. Clone este repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_REPOSITORIO>
2. Configure a assinatura do Azure no arquivo .env ou diretamente no código:

export AZURE_SUBSCRIPTION_ID="SUA_ASSINATURA"

3. Execute o script principal:

    python main.py

4. Os resultados serão exibidos no console e exportados para um arquivo Inventario_Azure.xlsx.

## **Arquitetura do Projeto**

.
├── find-resource.py                  # Script principal
├── README.md                # Documentação
├── requirements.txt         # Dependências do projeto
├── output/
│   └── Inventario_Azure.xlsx # Arquivo gerado com o inventário
└── .env                     # Variáveis de ambiente

## **Exemplo de Saída**

| Recurso          | Subscrição    | Tipo           | Grupo de Recursos | Região         |
|-------------------|---------------|----------------|--------------------|----------------|
| VM01             | Subscrição A  | VirtualMachine | ResourceGroup01    | East US        |
| StorageAccount01 | Subscrição A  | StorageAccount | ResourceGroup02    | West Europe    |
| Database01       | Subscrição B  | SQLDatabase    | ResourceGroup03    | Central US     |
| Firewall01       | Subscrição C  | Firewall       | ResourceGroup04    | Southeast Asia |

## **Contribuindo**

   1. Faça um fork do repositório.
   2. Crie uma branch para suas alterações:
    ```bash
   git checkout -b minha-feature
``
   3. Envie um pull request com uma descrição das alterações.

Licença

Este projeto está sob a licença MIT.


Se precisar de ajustes, posso ajudar! 🚀