# Desafio-Neurotech

- Teste pratico para vaga de Engenharia de Software Full Stack Jr na Neurotech. Objetivo é desenvolver uma solução web full stack realizando a integração com o Hubspot, um CRM muito utilizado
no mercado para Marketing e Vendas.

# Configurações

- A versão do python utilizado foi a 3.8.10
- Para instalar as dependências bastar utilizar o comando: pip install -r requirements.txt
- Para alterar a API Key Basta colocar a nova Chave no arquivo config.json, onde também se encontra outras informações do HubSpot
- Para iniciar a aplicação bastar utilizar o comando: python manage.py runserver; e você encontrará o prejoto na url: http://localhost:8000/

# Comentarios

O arquivo hsapi.py foi feito para testar a comunicação com o HubSpot utilizando os seus endpoints, para isso era apenas necessário da API Key.
Depois de conseguir utilizar o OAuth para coletar os dados achei que o hsapi.py não seria mais necessário, mas com authenticated_api_client não consegui atualizar os dados de um contato que já está salvo por não ter o id, para conseguir fazer isso usei uma função do hsapi.py que usa um endpoint que salva um contato ou atualiza se ja estiver salvo. E para isso ele utiliza o email para indentificar o contato.
