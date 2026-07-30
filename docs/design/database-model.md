# Modelo de Banco de Dados

## Tabela: applications

Armazena as candidaturas cadastradas no HireTrack.

| Campo | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| id | UUID | Sim | Identificador único gerado pelo sistema |
| registration_date | TIMESTAMP | Sim | Data e horário em que a candidatura foi cadastrada no sistema |
| position | TEXT | Sim | Nome da vaga |
| company_name | TEXT | Sim | Nome da empresa |
| status | ENUM | Sim | Status pré-definido da candidatura |
| source | TEXT | Não | Origem da vaga/candidatura |
| applied_date | DATE | Sim | Data em que a candidatura foi realizada |

## Restrições

- `id` deve ser único e funcionar como chave primária.
- `status` deve aceitar somente os valores definidos pelo domínio do MVP.
- `source` pode ser nula.
- `registration_date` é gerada pelo sistema.
- Os demais campos obrigatórios não podem ser nulos.

## Observações

O modelo representa somente os dados necessários para o MVP. Funcionalidades e informações futuras não fazem parte deste modelo.