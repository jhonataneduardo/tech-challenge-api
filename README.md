# Arquitetura Hexagonal com Python

FoodAPI é um projeto de estudo, desenvolvido com Python e Flask e baseado na Arquitetura Hexagonal.

## Sumário

- [Instalação](#instalação)
- [Uso](#uso)
- [Documentação](#documentação)
- [Melhorias Previstas](#melhorias-previstas)

## Instalação

### Requisitos

- Docker
- Docker Compose

### Passos

1. Clone este repositório:
    ```sh
    git clone https://github.com/jhonataneduardo/tech-challenge-api
    cd tech-challenge-api
    ```

2. Execute o Docker Compose:
    ```sh
    docker-compose up --build
    ```

## Uso

Após iniciar a aplicação, você pode acessar a API em `http://localhost:5000`.

## Documentação

A documentação Swagger da API está disponível em `http://localhost:5000/apidocs`.

## Melhorias Previstas

| Melhoria             | Descrição                                      |
|----------------------|------------------------------------------------|
| Validação de Campos  | Implementar validação de dados recebidos pela API para garantir a integridade dos dados. |
| Tratamento de Erros  | Adicionar tratamento de erros robusto para fornecer respostas adequadas e informativas em caso de falhas. |
| Testes Unitários     | Escrever testes unitários para garantir que cada parte da aplicação funcione corretamente. |
| Testes de Integração | Desenvolver testes de integração para verificar se os diferentes módulos da aplicação funcionam bem em conjunto. |
