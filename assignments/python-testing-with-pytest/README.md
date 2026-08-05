# 📘 Assignment: Python Testing with Pytest

## 🎯 Objective

Aprender os fundamentos de testes automatizados com `pytest`, escrevendo testes claros para validar comportamentos esperados, casos de borda e erros comuns.

## 📝 Tasks

### 🛠️ Write Your First Unit Tests

#### Descrição
Use o arquivo `starter-code.py` para criar seu primeiro arquivo de testes com `pytest`.

#### Requisitos
O programa concluído deve:

- Criar um arquivo de testes (ex.: `test_starter_code.py`) com pelo menos 3 testes.
- Testar as funções `is_even()` e `format_full_name()` com entradas válidas.
- Usar `assert` para comparar resultados esperados e retornados.


### 🛠️ Cover Edge Cases and Invalid Inputs

#### Descrição
Expanda sua suíte para cobrir cenários menos óbvios e entradas inválidas.

#### Requisitos
O programa concluído deve:

- Adicionar testes para casos de borda em `clamp_score()` (abaixo de 0 e acima de 100).
- Escrever um teste para confirmar que `safe_divide()` lança erro ao dividir por zero.
- Usar `pytest.raises(...)` no teste de exceção.


### 🛠️ Run Tests and Improve Code Quality

#### Descrição
Execute os testes, interprete os resultados e ajuste o código quando necessário.

#### Requisitos
O programa concluído deve:

- Rodar `pytest -q` e verificar o resumo de testes passados/falhos.
- Corrigir no `starter-code.py` qualquer comportamento que faça testes falharem.
- Entregar com todos os testes passando.
