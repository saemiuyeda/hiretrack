# Arquitetura do Sistema

## Visão Geral

O HireTrack será desenvolvido como uma aplicação web utilizando uma arquitetura em camadas.

A aplicação será composta por três componentes principais:

- Frontend
- Backend
- Banco de dados

O backend será organizado internamente em camadas, com responsabilidades específicas para cada parte do sistema. Essa separação busca facilitar a manutenção, evolução e organização do software.

Fluxo geral:

- Frontend
- Backend
    - Router
    - Schema
    - Service
    - Model
    - Database
- Banco de dados

### Frontend

Responsável pela interação com o usuário.

Responsabilidades:

- Apresentar as informações do sistema;
- Permitir a entrada de dados;
- Enviar solicitações ao backend;
- Exibir respostas ao usuário.

### Backend

Responsável pelo processamento das solicitações e pela aplicação das regras de negócio.

O backend será organizado em camadas, com responsabilidades separadas para evitar que diferentes partes da aplicação dependam diretamente umas das outras.

Responsabilidades gerais:

- Receber solicitações do frontend;
- Validar os dados recebidos;
- Aplicar regras de negócio;
- Processar as solicitações;
- Realizar a comunicação com o banco de dados;
- Retornar respostas ao frontend.

As responsabilidades internas serão organizadas entre:

- **Router:** recebe e encaminha as requisições HTTP;
- **Schema:** define e valida os dados de entrada e saída da API;
- **Service:** concentra a lógica de negócio e o processamento das operações;
- **Model:** representa as entidades persistidas no banco de dados;
- **Database:** gerencia a conexão e a interação com o banco de dados.

### Banco de dados

O banco de dados será responsável pela persistência das informações.

Responsabilidades:

- Armazenar candidaturas;
- Recuperar dados;
- Atualizar dados;
- Remover dados;
- Garantir a persistência das informações.