import pandas as pd
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

# Autenticação
credential = DefaultAzureCredential()
subscription_id = "SEU_ID_DE_ASSINATURA"
resource_client = ResourceManagementClient(credential, subscription_id)

# Coleta de dados do Azure
resource_data = []
for resource in resource_client.resources.list():
    resource_data.append({
        "Nome": resource.name,
        "Tipo": resource.type,
        "Grupo de Recursos": resource.resource_group,
        "Localização": resource.location
    })

# Criar DataFrame e salvar como Excel
df = pd.DataFrame(resource_data)
output_file = "output/Inventario_Azure.xlsx"
df.to_excel(output_file, index=False)

print(f"Inventário exportado com sucesso para {output_file}")