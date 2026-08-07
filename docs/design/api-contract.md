# Recurso principal

O MVP do HireTrack possui como principal recurso a **Application (Candidatura)**.

O recurso representa uma candidatura realizada pelo usuário para uma vaga.

## Estrutura do recurso

```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "position": "Software Engineer Intern",
  "company_name": "Empresa X",
  "status": "Inscrição",
  "source": "LinkedIn",
  "applied_date": "2026-07-23"
}
```

# Endpoints

## Criar candidatura

### POST `/applications`

Responsável por cadastrar uma nova candidatura.

### Request Body

```json
{
  "position": "Software Engineer Intern",
  "company_name": "Empresa X",
  "status": "Inscrição",
  "source": "LinkedIn",
  "applied_date": "2026-07-23"
}
```

### Response — Sucesso

**HTTP 201 Created**

```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "position": "Software Engineer Intern",
  "company_name": "Empresa X",
  "status": "Inscrição",
  "source": "LinkedIn",
  "applied_date": "2026-07-23"
}
```

---

## Listar candidaturas

### GET `/applications`

Responsável por retornar todas as candidaturas cadastradas.

### Request Body

Não possui.

### Response — Sucesso

**HTTP 200 OK**

```json
[
  {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "position": "Software Engineer Intern",
    "company_name": "Empresa X",
    "status": "Entrevista RH",
    "source": "LinkedIn",
    "applied_date": "2026-07-23"
  },
  {
    "id": "b3b6c9d2-8b6b-4b77-9f89-4f6d6f8d5d10",
    "position": "Backend Developer",
    "company_name": "Empresa Y",
    "status": "Triagem",
    "source": "Gupy",
    "applied_date": "2026-07-20"
  }
]
```

---

## Atualizar candidatura

### PATCH `/applications/{application_id}`

Responsável por atualizar parcialmente uma candidatura existente.

### Parâmetro

`id` → identificador único da candidatura.

Exemplo:

```text
PATCH /applications/550e8400-e29b-41d4-a716-446655440000
```

### Request Body

Somente os campos que precisam ser alterados.

Exemplo:

```json
{
  "status": "Entrevista RH"
}
```

### Response — Sucesso

**HTTP 200 OK**

```json
{
  "message": "Candidatura atualizada com sucesso."
}
```

---

## Excluir candidatura

### DELETE `/applications/{id}`

Responsável por remover uma candidatura existente.

### Parâmetro

`id` → identificador único da candidatura.

Exemplo:

```text
DELETE /applications/550e8400-e29b-41d4-a716-446655440000
```

### Request Body

Não possui.

### Response — Sucesso

**HTTP 204 No Content**

Sem corpo de resposta.

---

## Schemas

| Campo | Tipo | Obrigatório | Observação |
| --- | --- | --- | --- |
| id | UUID | sim | identificador único gerado pelo sistema para diferenciar cada candidatura |
| position | str | sim | Nome da vaga aplicada |
| company_name | str | sim | Nome da empresa onde a candidatura foi enviada |
| status | Enum | sim | Estado atual da candidatura  |
| source | str | não | A plataforma/canal em que encontrou a vaga |
| applied_date | date | sim | Data em que a candidatura foi enviada |

---

## Status

| Status | Significado |
| --- | --- |
| Inscrição | O usuário se inscreveu na vaga. |
| Triagem | Etapa do processo seletivo onde o RH filtra os candidatos. |
| Entrevista RH | Etapa em que o RH avalia as soft skills do candidato. |
| Entrevista Técnica | Etapa em que o domínio técnico do candidato é avaliado. |
| Proposta | Etapa em que ocorre a oferta de emprego e a apresentação das condições de contratação. |
| Contratada | Processo seletivo concluído com a contratação do candidato. |
| Rejeitada | Processo seletivo encerrado sem aprovação do candidato. |
| Cancelada | Candidatura cancelada pelo usuário ou pela empresa. |

---

## Respostas e erros da API

| Endpoint | Sucesso | Erros |
| --- | --- | --- |
| POST `/applications` | 201 Created | 422 Unprocessable Content | 409 Conflit | 500 Internal Server Error |
| GET `/applications` | 200 OK | — |
| PATCH `/applications/{id}` | 200 OK | 404 Not Found | 422 Unprocessable Content | 500 Internal Server Error |
| DELETE `/applications/{id}` | 204 No Content | 404 Not Found | 500 Internal Server Error |

---

# Observações do projeto

- O recurso principal do MVP é `Application`.
- Empresa, vaga e plataforma são atributos da candidatura, não recursos independentes neste momento.
- O campo `status` possui valores limitados, representados por um `Enum`.
- O MVP não estabelece uma ordem obrigatória para alteração dos status; o usuário pode alterar uma candidatura para qualquer status válido.
- A API seguirá o padrão REST, utilizando recursos no plural e métodos HTTP conforme a operação realizada.