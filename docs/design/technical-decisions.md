# Decisões Técnicas

Este documento registra as principais decisões técnicas adotadas no desenvolvimento do HireTrack e os motivos que justificam cada escolha.

---

## DT001 - FastAPI

**Decisão:** Utilizar FastAPI como framework para desenvolvimento do backend.

**Justificativa:**

O HireTrack será desenvolvido como uma aplicação web baseada em API REST. O FastAPI é adequado a esse contexto por permitir a construção de APIs utilizando Python, linguagem já conhecida no desenvolvimento do projeto.

Além disso, o framework oferece recursos importantes para o desenvolvimento e teste da API, como integração com Pydantic e geração automática da documentação baseada em OpenAPI e Swagger UI.

A escolha também permite aprofundar a compreensão dos conceitos de desenvolvimento de APIs e aplicações web sem introduzir uma mudança de linguagem durante essa etapa do projeto.

---

## DT002 - PostgreSQL

**Decisão:** Utilizar PostgreSQL como banco de dados relacional do HireTrack.

**Justificativa:**

Os dados são parte central do HireTrack. O objetivo do sistema não se limita ao gerenciamento das candidaturas, pois os dados armazenados deverão futuramente ser utilizados para identificar padrões e gerar insights que auxiliem o usuário na tomada de decisões.

Por esse motivo, a persistência precisa oferecer recursos adequados para manter a integridade dos dados e permitir a evolução do sistema.

O PostgreSQL foi escolhido por ser um banco de dados relacional robusto, adequado a sistemas que dependem de integridade dos dados, relacionamentos, consultas estruturadas e evolução da quantidade e complexidade dos dados.

A escolha também mantém o sistema preparado para futuras necessidades de análise dos dados coletados.

---

## DT003 - SQLAlchemy

**Decisão:** Utilizar SQLAlchemy como biblioteca de acesso e persistência de dados.

**Justificativa:**

O SQLAlchemy fornece uma camada de abstração para a interação entre a aplicação Python e o banco de dados PostgreSQL.

Sua utilização facilita a integração entre a aplicação e a camada de persistência, permitindo trabalhar com os recursos do banco por meio das ferramentas fornecidas pela biblioteca.

A escolha também possibilita utilizar ORM, mantendo uma separação clara entre a representação das entidades na aplicação e sua persistência no banco de dados.

---

## DT004 - ORM

**Decisão:** Utilizar o modelo de mapeamento objeto-relacional (ORM) para representar as entidades persistidas no banco.

**Justificativa:**

A aplicação trabalha principalmente com objetos e entidades Python, enquanto o banco de dados relacional trabalha com tabelas, linhas e colunas.

O ORM estabelece o mapeamento entre essas duas representações:

**Objeto Python ↔ ORM ↔ Tabela relacional**

No HireTrack, por exemplo, a entidade `Application` será representada por um modelo ORM que será mapeado para sua respectiva tabela no PostgreSQL.

Essa abordagem permite que a aplicação trabalhe com as entidades do domínio de forma integrada à camada de persistência, reduzindo a necessidade de manipulação direta de SQL em todas as operações.

---

## DT005 - Arquitetura em camadas

**Decisão:** Organizar o backend utilizando uma arquitetura em camadas.

**Justificativa:**

O HireTrack deverá evoluir além de sua primeira versão e poderá receber novas funcionalidades e regras de negócio ao longo do desenvolvimento.

A arquitetura em camadas foi escolhida para organizar o sistema de acordo com responsabilidades distintas, evitando concentrar toda a lógica em uma única parte da aplicação.

A estrutura permite separar responsabilidades relacionadas à comunicação HTTP, regras de negócio e persistência, contribuindo para uma manutenção e evolução mais controladas.

A arquitetura adotada inicialmente será composta por:

- **Router:** comunicação com a API e tratamento das requisições HTTP;
- **Schema:** representação e validação dos dados de entrada e saída;
- **Service:** regras e operações relacionadas ao domínio da aplicação;
- **Model:** representação das entidades persistidas;
- **Database:** configuração e acesso à infraestrutura de persistência;
- **Main:** inicialização e composição da aplicação.

---

## DT006 - Separação de responsabilidades

**Decisão:** Manter responsabilidades distintas entre as camadas da aplicação.

**Justificativa:**

A separação de responsabilidades reduz o acoplamento entre as diferentes partes do sistema.

Cada camada deve possuir uma responsabilidade claramente definida, evitando que uma camada assuma funções pertencentes a outra.

Por exemplo, o `router` não deve concentrar simultaneamente tratamento HTTP, regras de negócio e operações diretamente no banco de dados.

Essa separação facilita a compreensão do código e reduz o impacto de alterações, contribuindo para a manutenção, evolução e testabilidade do sistema.

---

## DT007 - Funcionalidades fora do escopo inicial

**Decisão:** Adiar funcionalidades e preocupações que não são necessárias para o núcleo do MVP.

**Itens adiados inicialmente:**

- autenticação;
- Docker;
- deploy;
- funcionalidades avançadas de análise;
- otimizações prematuras.

**Justificativa:**

Esses recursos poderão ser necessários em etapas futuras, mas não são essenciais para validar e consolidar o núcleo inicial do HireTrack.

Mantê-los fora da primeira implementação permite preservar o escopo do MVP e concentrar o desenvolvimento nas funcionalidades fundamentais de gerenciamento das candidaturas e na consolidação da arquitetura do sistema.

O adiamento é uma decisão consciente de escopo e não significa que essas funcionalidades foram consideradas desnecessárias para a evolução futura do projeto.

---

## Resumo das decisões

| ID | Decisão | Motivo principal |
| --- | --- | --- |
| DT001 | FastAPI | Construção da API REST utilizando Python e documentação automática |
| DT002 | PostgreSQL | Integridade, evolução e futura utilização analítica dos dados |
| DT003 | SQLAlchemy | Abstração e integração entre aplicação e persistência |
| DT004 | ORM | Mapeamento entre objetos Python e estruturas relacionais |
| DT005 | Arquitetura em camadas | Organização das responsabilidades e evolução do sistema |
| DT006 | Separação de responsabilidades | Redução de acoplamento e facilitação da manutenção |
| DT007 | Adiar funcionalidades não essenciais | Preservação do escopo e foco no MVP |