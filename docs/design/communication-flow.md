# Fluxo de Comunicação

## Cadastrar candidatura

1. Usuário preenche os dados da candidatura.
2. O frontend envia uma requisição ao backend.
3. O backend recebe a requisição.
4. O backend valida os dados e aplica as regras de negócio.
5. O backend solicita o armazenamento da candidatura ao banco de dados.
6. O banco de dados confirma o armazenamento.
7. O backend retorna a resposta ao frontend.
8. O frontend apresenta a resposta ao usuário.

---

## Listar candidaturas

1. Usuário solicita a listagem das candidaturas.
2. O frontend envia uma requisição ao backend.
3. O backend recebe a requisição.
4. O backend solicita as candidaturas ao banco de dados.
5. O banco de dados retorna os dados.
6. O backend retorna a resposta ao frontend.
7. O frontend apresenta as candidaturas ao usuário.

---

## Editar candidatura

1. Usuário seleciona a candidatura e informa os novos dados.
2. O frontend envia uma requisição ao backend.
3. O backend recebe a requisição.
4. O backend verifica se a candidatura existe e valida as regras de negócio.
5. O backend solicita a atualização da candidatura ao banco de dados.
6. O banco de dados confirma a atualização.
7. O backend retorna a resposta ao frontend.
8. O frontend apresenta a resposta ao usuário.

---

## Excluir candidatura

1. Usuário solicita a exclusão de uma candidatura.
2. O frontend envia uma requisição ao backend.
3. O backend recebe a requisição.
4. O backend verifica se a candidatura existe.
5. O backend solicita a remoção da candidatura ao banco de dados.
6. O banco de dados confirma a remoção.
7. O backend retorna a resposta ao frontend.
8. O frontend apresenta a resposta ao usuário.