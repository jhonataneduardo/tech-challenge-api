from dataclasses import dataclass


@dataclass(frozen=True)
class CPF:
    value: str


@dataclass(frozen=True)
class Email:
    value: str
