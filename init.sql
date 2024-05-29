-- Criar sequência para tabela customers
CREATE SEQUENCE customers_id_seq;

-- Criar tabela customers
CREATE TABLE customers (
    id INTEGER PRIMARY KEY DEFAULT nextval('customers_id_seq'),
    name VARCHAR(120) NOT NULL,
    email VARCHAR(80) NOT NULL,
    cpf VARCHAR(11) UNIQUE NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP
);

-- Criar sequência para tabela categories
CREATE SEQUENCE categories_id_seq;

-- Criar tabela categories
CREATE TABLE categories (
    id INTEGER PRIMARY KEY DEFAULT nextval('categories_id_seq'),
    name VARCHAR(80) UNIQUE NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP
);

-- Criar sequência para tabela products
CREATE SEQUENCE products_id_seq;

-- Criar tabela products
CREATE TABLE products (
    id INTEGER PRIMARY KEY DEFAULT nextval('products_id_seq'),
    name VARCHAR(80) NOT NULL,
    description TEXT NOT NULL,
    price DECIMAL NOT NULL,
    category_id INTEGER NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories (id)
);

-- Criar sequência para tabela orders
CREATE SEQUENCE orders_id_seq;

-- Criar tabela orders
CREATE TABLE orders (
    id INTEGER PRIMARY KEY DEFAULT nextval('orders_id_seq'),
    customer_id INTEGER NOT NULL,
    status SMALLINT NOT NULL,
    total DECIMAL NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers (id)
);

-- Criar sequência para tabela order_items
CREATE SEQUENCE order_items_id_seq;

-- Criar tabela order_items
CREATE TABLE order_items (
    id INTEGER PRIMARY KEY DEFAULT nextval('order_items_id_seq'),
    product_id INTEGER NOT NULL,
    order_id INTEGER NOT NULL,
    price DECIMAL NOT NULL,
    quantity DECIMAL NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products (id),
    FOREIGN KEY (order_id) REFERENCES orders (id)
);

INSERT INTO categories (id, name, created_at, updated_at)
VALUES (nextval('categories_id_seq'), 'Lanche', NOW(), NULL);

INSERT INTO categories (id, name, created_at, updated_at)
VALUES (nextval('categories_id_seq'), 'Acompanhamento', NOW(), NULL);

INSERT INTO categories (id, name, created_at, updated_at)
VALUES (nextval('categories_id_seq'), 'Bebida', NOW(), NULL);

INSERT INTO categories (id, name, created_at, updated_at)
VALUES (nextval('categories_id_seq'), 'Sobremesa', NOW(), NULL);

-- Produtos - Lanche
INSERT INTO products (id, name, description, price, category_id, created_at, updated_at)
VALUES (nextval('products_id_seq'), 'X-Tudo', 'Pão crocante, queijo derretido, suculento hambúrguer, bacon, presunto, alface, tomate, cebola e molho especial.', 18.90, 1, NOW(), NULL);

INSERT INTO products (id, name, description, price, category_id, created_at, updated_at)
VALUES (nextval('products_id_seq'), 'Beirute de Carne Seca', 'Pão sírio recheado com carne seca desfiada, queijo catupiry, cebola roxa e vinagrete.', 16.50, 1, NOW(), NULL);

-- Produtos - Acompanhamento
INSERT INTO products (id, name, description, price, category_id, created_at, updated_at)
VALUES (nextval('products_id_seq'), 'Batata Frita', 'Fritas crocantes temperadas com sal e páprica doce.', 8.00, 2, NOW(), NULL);

INSERT INTO products (id, name, description, price, category_id, created_at, updated_at)
VALUES (nextval('products_id_seq'), 'Arroz Branco', 'Arroz branco soltinho e temperado com sal a gosto.', 5.00, 2, NOW(), NULL);

-- Produtos - Bebida
INSERT INTO products (id, name, description, price, category_id, created_at, updated_at)
VALUES (nextval('products_id_seq'), 'Refrigerante Lata', 'Refrigerante de sua escolha em lata de 350ml.', 5.50, 3, NOW(), NULL);

INSERT INTO products (id, name, description, price, category_id, created_at, updated_at)
VALUES (nextval('products_id_seq'), 'Suco de Laranja Natural', 'Suco de laranja fresco feito na hora com 500ml.', 7.80, 3, NOW(), NULL);

-- Produtos - Sobremesa
INSERT INTO products (id, name, description, price, category_id, created_at, updated_at)
VALUES (nextval('products_id_seq'), 'Mousse de Chocolate', 'Deliciosa mousse de chocolate cremosa com calda de chocolate.', 12.00, 4, NOW(), NULL);

INSERT INTO products (id, name, description, price, category_id, created_at, updated_at)
VALUES (nextval('products_id_seq'), 'Brigadeiro', 'Brigadeiro tradicional feito com leite condensado, chocolate em pó e manteiga.', 3.50, 4, NOW(), NULL);

INSERT INTO customers (id, name, email, cpf, created_at, updated_at)
VALUES (nextval('customers_id_seq'), 'Ana Silva', 'ana@example.com', '00000000000', NOW(), NULL);

INSERT INTO customers (id, name, email, cpf, created_at, updated_at)
VALUES (nextval('customers_id_seq'), 'João Oliveira', 'joao@example.com', '11111111111', NOW(), NULL);

INSERT INTO orders (id, customer_id, status, total, created_at, updated_at)
VALUES (nextval('orders_id_seq'), 1, 1, 35.40, NOW(), NULL);

INSERT INTO orders (id, customer_id, status, total, created_at, updated_at)
VALUES (nextval('orders_id_seq'), 2, 1, 10.00, NOW(), NULL);

INSERT INTO order_items (id, product_id, order_id, price, quantity)
VALUES (nextval('order_items_id_seq'), 1, 1, 18.90, 1.0);

INSERT INTO order_items (id, product_id, order_id, price, quantity)
VALUES (nextval('order_items_id_seq'), 2, 1, 16.50, 1.0);

INSERT INTO order_items (id, product_id, order_id, price, quantity)
VALUES (nextval('order_items_id_seq'), 3, 2, 8.00, 1.0);
