# 📘 Atividade: Building REST APIs com FastAPI

## 🎯 Objetivo

Construir uma API REST simples com FastAPI, aplicando criação de rotas, validação com Pydantic e operações CRUD em memória com respostas HTTP apropriadas.

## 📝 Tarefas

### 🛠️ Criar a Base da API

#### Descrição
Configure uma aplicação FastAPI funcional e implemente endpoints iniciais para validar que o servidor está rodando corretamente.

#### Requisitos
O programa completo deve:

- Criar uma instância FastAPI em `app = FastAPI()`.
- Implementar `GET /` retornando uma mensagem de boas-vindas em JSON.
- Implementar `GET /health` retornando status `ok` e código HTTP `200`.


### 🛠️ Implementar CRUD de Tarefas

#### Descrição
Implemente um recurso de tarefas (`tasks`) com armazenamento em memória, permitindo criar, listar, buscar por ID e remover tarefas.

#### Requisitos
O programa completo deve:

- Criar um modelo `TaskCreate` com campos `title` (obrigatório) e `done` (padrão `False`).
- Criar um modelo `Task` com `id`, `title` e `done`.
- Implementar `POST /tasks` para criar uma nova tarefa.
- Implementar `GET /tasks` para listar todas as tarefas.
- Implementar `GET /tasks/{task_id}` para buscar uma tarefa por ID.
- Implementar `DELETE /tasks/{task_id}` para remover uma tarefa por ID.


### 🛠️ Melhorar Validação e Respostas HTTP

#### Descrição
Melhore a robustez da API com validações e códigos de status consistentes para cenários de erro e sucesso.

#### Requisitos
O programa completo deve:

- Retornar `404` com detalhe claro quando uma tarefa não existir.
- Garantir que o `title` não seja vazio.
- Retornar `201` ao criar uma tarefa com sucesso.
- Manter respostas em formato JSON em todos os endpoints.
