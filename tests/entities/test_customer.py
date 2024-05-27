from app.domain.entities.customer_entity import Customer
from app.domain.value_objects import CPF, Email


def test_simple_customer_creation():
    cpf = CPF("23772094082")
    email = Email("cliente@teste.com")
    customer = Customer(name="João Almeida Silva", cpf=cpf, email=email)

    assert customer.as_dict()["name"] == "João Almeida Silva"
    assert customer.as_dict()["email"] == email.value
    assert customer.as_dict()["cpf"] == cpf.value
