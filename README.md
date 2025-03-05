# TESTE OUTSERA

## Sobre o projeto
Segue abaixo instruções sobre como instalar e executar o projeto do teste outsera seguindo a prosposta enviada

## Instalação
- git clone url
- ter python 3.13+ instalado
- executar pip install -r requirements.txt no diretório do projeto

## Inicializar API
- Executar no diretório do projeto uvicorn app:app --host=127.0.0.1 --port=8000, --host e --port podem ser alterados conforme necessário
- O primeiro arquivo .csv dentro da pasta data do projeto será o arquivo de dados utilizado pela api

## Execução de testes
- se as variáveis --port ou --host foram alteradas alterar o arquivo .env na pasta tests do projeto conforme os novos valores informados
- a api deve estar em execução antes do comando de teste ser executado
- executar no diretório do projeto python -m unittest tests.integration_tests.TestDataIntegrity