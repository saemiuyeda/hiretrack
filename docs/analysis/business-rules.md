# Regras de Negócio

## Objetivo

Este documento descreve as regras de negócio do HireTrack.

As regras de negócio representam restrições, validações e comportamentos do domínio que devem ser respeitados independentemente da tecnologia utilizada.

---

## Convenção

Cada regra recebe um identificador único.

Exemplo:

RN001
RN002
RN003
...

---

## Regras

RN001:  Toda candidatura deve estar associada a uma vaga.

RN002: Toda candidatura deve estar associada a uma empresa.

RN003: Toda candidatura deve possuir uma origem da candidatura (plataforma ou canal).

RN004: Toda candidatura deve possuir uma data de candidatura.

RN005: Nenhuma data de candidatura pode ser futura.

RN006: Toda candidatura deve possuir um status inicial.

RN007: O status de uma candidatura deve pertencer à lista de status permitidos pelo sistema.

RN008: O sistema permite alterar uma candidatura para qualquer status válido. O MVP não estabelece uma sequência obrigatória entre os status.

RN009: Toda candidatura deve possuir um identificador único.

RN010: A data de cadastro deve ser registrada automaticamente no momento em que a candidatura é criada.

Status permitidos:

- Inscrição
- Triagem
- Entrevista RH
- Entrevista Técnica
- Proposta
- Contratada
- Rejeitada
- Cancelada