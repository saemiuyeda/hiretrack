# Caso de Uso

# Nome

Cadastrar candidatura.

## Ator

Usuário.

## Pré-condição

Não se aplica.

## Fluxo básico

1. O usuário acessa a página de cadastro de candidatura.
2. O sistema apresenta o formulário de cadastro contendo os seguintes campos:
    1. Vaga
    2. Empresa
    3. Status
    4. Plataforma/Canal
    5. Data de candidatura
3. O usuário preenche as informações solicitadas.
4. O usuário envia o formulário de cadastro.
5. O sistema valida as informações fornecidas.
6. O sistema registra a candidatura.
7. O sistema exibe uma mensagem informando que o cadastro foi realizado com sucesso.
8. O fluxo é encerrado.

## Fluxo alternativo

### FA001 - Dados obrigatórios não preenchidos

Relacionado ao passo 5.

Fluxo:

1. O sistema identifica que existem campos obrigatórios não preenchidos.
2. O sistema informa ao usuário quais campos devem ser preenchidos.
3. O usuário preenche as informações obrigatórias.
4. O fluxo retorna ao passo 4 do fluxo básico.

---

### FA002 - Status informado é inválido

Relacionado ao passo 5.

Fluxo:

1. O sistema identifica que o status informado é inválido.
2. O sistema informa os status permitidos.
3. O usuário informa um novo status.
4. O fluxo retorna ao passo 4 do fluxo básico.

---

### FA003 - Data de candidatura inválida

Relacionado ao passo 5.

Fluxo:

1. O sistema identifica que a data informada é inválida.
2. O sistema informa o formato esperado.
3. O usuário informa uma nova data.
4. O fluxo retorna ao passo 4 do fluxo básico.

## Pós-condição

Uma nova candidatura é registrada e armazenada pelo sistema.

---

# Nome

Listar candidaturas.

## Ator

Usuário.

## Pré-condição

Não se aplica.

## Fluxo básico

1. O usuário acessa a página de candidaturas.
2. O sistema recupera as candidaturas cadastradas.
3. O sistema exibe a lista de candidaturas.
4. O fluxo é encerrado.

## Fluxo alternativo

### FA001 - Não existem candidaturas cadastradas

Relacionado ao passo 2.

Fluxo:

1. O sistema identifica que não existem candidaturas cadastradas.
2. O sistema informa ao usuário que nenhuma candidatura foi encontrada.
3. O fluxo é encerrado.

## Pós-condição

Não se aplica.

---

# Nome

Editar candidatura.

## Ator

Usuário.

## Pré-condição

Deve existir ao menos uma candidatura cadastrada.

## Fluxo básico

1. O usuário acessa a página de candidaturas.
2. O sistema exibe as candidaturas cadastradas.
3. O usuário seleciona a candidatura que deseja editar.
4. O sistema apresenta as informações da candidatura selecionada.
5. O usuário altera os campos desejados.
6. O usuário envia as alterações.
7. O sistema valida os novos dados informados.
8. O sistema atualiza a candidatura.
9. O sistema informa que a edição foi realizada com sucesso.
10. O fluxo é encerrado.

## Fluxo alternativo

### FA001 - Candidatura não encontrada

Relacionado ao passo 4.

Fluxo:

1. O sistema identifica que a candidatura selecionada não foi encontrada.
2. O sistema informa ao usuário que a candidatura não existe.
3. O fluxo é encerrado.

---

### FA002 - Novo valor inválido

Relacionado ao passo 7.

Fluxo:

1. O sistema identifica que um ou mais valores informados são inválidos.
2. O sistema informa o motivo da invalidação.
3. O usuário corrige as informações.
4. O fluxo retorna ao passo 6 do fluxo básico.

## Pós-condição

A candidatura é atualizada e a alteração é armazenada pelo sistema.

---

# Nome

Excluir candidatura.

## Ator

Usuário.

## Pré-condição

Deve existir ao menos uma candidatura cadastrada.

## Fluxo básico

1. O usuário acessa a página de candidaturas.
2. O sistema exibe a lista de candidaturas cadastradas.
3. O usuário seleciona a candidatura que deseja excluir.
4. O sistema solicita a confirmação da exclusão.
5. O usuário confirma a exclusão.
6. O sistema remove a candidatura.
7. O sistema informa que a exclusão foi realizada com sucesso.
8. O fluxo é encerrado.

## Fluxo alternativo

### FA001 - Candidatura não encontrada

Relacionado ao passo 3.

Fluxo:

1. O sistema identifica que a candidatura selecionada não foi encontrada.
2. O sistema informa ao usuário que a candidatura não existe.
3. O fluxo é encerrado.

---

### FA002 - Exclusão cancelada pelo usuário

Relacionado ao passo 4.

Fluxo:

1. O usuário cancela a exclusão.
2. O sistema cancela a operação.
3. O fluxo é encerrado.

## Pós-condição

A candidatura é removida do sistema e a exclusão é persistida.