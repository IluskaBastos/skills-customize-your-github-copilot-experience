"""Starter code para a assignment de testes com pytest.

Objetivo: escrever testes de unidade para validar comportamentos esperados,
casos de borda e tratamento de erros.
"""


def is_even(number: int) -> bool:
    """Retorna True quando o numero for par."""
    return number % 2 == 0


def format_full_name(first_name: str, last_name: str) -> str:
    """Formata nome completo com iniciais maiusculas."""
    return f"{first_name.strip().title()} {last_name.strip().title()}"


def clamp_score(score: int) -> int:
    """Limita a nota no intervalo de 0 a 100."""
    if score < 0:
        return 0
    if score > 100:
        return 100
    return score


def safe_divide(a: float, b: float) -> float:
    """Divide dois numeros e levanta ZeroDivisionError quando b == 0."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
