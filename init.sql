-- TABELAS
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    email VARCHAR(80) NOT NULL,
    cpf VARCHAR(11) UNIQUE NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP
);

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(80) UNIQUE NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(80) NOT NULL,
    description TEXT NOT NULL,
    price DECIMAL NOT NULL,
    category_id INTEGER NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories (id)
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    status SMALLINT NOT NULL,
    total DECIMAL NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers (id)
);

CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,
    product_id INTEGER NOT NULL,
    order_id INTEGER NOT NULL,
    price DECIMAL NOT NULL,
    quantity DECIMAL NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products (id),
    FOREIGN KEY (order_id) REFERENCES orders (id)
);

-- CATEGORIAS
INSERT INTO categories (id, name, created_at, updated_at)
VALUES (1, 'Lanche', NOW(), NULL);

INSERT INTO categories (id, name, created_at, updated_at)
VALUES (2, 'Acompanhamento', NOW(), NULL);

INSERT INTO categories (id, name, created_at, updated_at)
VALUES (3, 'Bebida', NOW(), NULL);

INSERT INTO categories (id, name, created_at, updated_at)
VALUES (4, 'Sobremesa', NOW(), NULL);

-- PRODUTOS - LANCHE
INSERT INTO products (id, name, description, price, category_id, created_at, updated_at)
VALUES (1, 'X-Tudo', 'Pão crocante, queijo derretido, suculento hambúrguer, bacon, presunto, alface, tomate, cebola e molho especial.', 18.90, 1, NOW(), NULL);
INSERT INTO products (id, name, description, price, category_id, created_at, updated_at)
VALUES (2, 'Beirute de Carne Seca', 'Pão sírio recheado com carne seca desfiada, queijo catupiry, cebola roxa e vinagrete. ', 16.50, 1, NOW(), NULL);

-- PRODUTOS - ACOMPANHAMENTO
INSERT INTO products (id, name, description, price, category_id, created_at, updated_at)
VALUES (3, 'Batata Frita', 'Fritas crocantes temperadas com sal e páprica doce.', 8.0, 2, NOW(), NULL);
INSERT INTO products (id, name, description, price, category_id, created_at, updated_at)
VALUES (4, 'Arroz Branco', 'Arroz branco soltinho e temperado com sal a gosto.', 5.0, 2, NOW(), NULL);

-- PRODUTOS - BEBIDA
INSERT INTO products (id, name, description, price, category_id, created_at, updated_at)
VALUES (5, 'Refrigerante Lata', 'Refrigerante de sua escolha em lata de 350ml.', 5.50, 3, NOW(), NULL);
INSERT INTO products (id, name, description, price, category_id, created_at, updated_at)
VALUES (6, 'Suco de Laranja Natural', 'Suco de laranja fresco feito na hora com 500ml.', 7.80, 3, NOW(), NULL);

-- PRODUTOS - SOBREMESA
INSERT INTO products (id, name, description, price, category_id, created_at, updated_at)
VALUES (7, 'Mousse de Chocolate', 'Deliciosa mousse de chocolate cremosa com calda de chocolate.', 12.00, 4, NOW(), NULL);
INSERT INTO products (id, name, description, price, category_id, created_at, updated_at)
VALUES (8, 'Brigadeiro', 'Brigadeiro tradicional feito com leite condensado, chocolate em pó e manteiga.', 3.50, 4, NOW(), NULL);

-- CLIENTES
INSERT INTO customers (id, name, email, cpf, created_at, updated_at)
VALUES (1, 'Ana Silva', 'ana@example.com', '00000000000', NOW(), NULL);
INSERT INTO customers (id, name, email, cpf, created_at, updated_at)
VALUES (2, 'João Oliveira', 'ana@example.com', '11111111111', NOW(), NULL);

-- ORDERS
INSERT INTO orders (id, customer_id, status, total, created_at, updated_at)
VALUES (1, 1, 1, 10.00, NOW(), NULL);
INSERT INTO orders (id, customer_id, status, total, created_at, updated_at)
VALUES (2, 2, 1, 10.00, NOW(), NULL);

INSERT INTO order_items (id, product_id, order_id, price, quantity)
VALUES (1, 1, 1, 18.90, 1.0);
INSERT INTO order_items (id, product_id, order_id, price, quantity)
VALUES (2, 2, 1, 16.50, 1.0);
