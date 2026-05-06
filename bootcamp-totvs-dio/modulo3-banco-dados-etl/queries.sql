-- =============================================================================
-- ARQUIVO DE CONSULTAS SQL - Módulo 3
-- Bootcamp TOTVS - Fundamentos de Engenharia de Dados e Machine Learning
-- =============================================================================
-- RACIOCÍNIO:
-- Este arquivo contém as principais queries SQL para consultar e analisar
-- os dados carregados pelo pipeline ETL no banco vendas.db
-- Execute no DB Browser for SQLite ou via Python com sqlite3
-- =============================================================================


-- -----------------------------------------------------------------------------
-- 1. CONSULTAS BÁSICAS (SELECT, WHERE, ORDER BY)
-- -----------------------------------------------------------------------------

-- Todos os pedidos
SELECT * FROM pedidos;

-- Apenas pedidos concluídos
SELECT * FROM pedidos
WHERE status = 'concluido';

-- Pedidos ordenados por receita (maior primeiro)
SELECT id_pedido, cliente, produto, receita_total
FROM pedidos
ORDER BY receita_total DESC;

-- Pedidos acima de R$ 5.000
SELECT id_pedido, cliente, produto, receita_total
FROM pedidos
WHERE receita_total > 5000
ORDER BY receita_total DESC;


-- -----------------------------------------------------------------------------
-- 2. FUNÇÕES DE AGREGAÇÃO (COUNT, SUM, AVG, MAX, MIN)
-- -----------------------------------------------------------------------------

-- Total de pedidos
SELECT COUNT(*) AS total_pedidos FROM pedidos;

-- Receita total geral
SELECT SUM(receita_total) AS receita_total FROM pedidos;

-- Ticket médio dos pedidos
SELECT ROUND(AVG(receita_total), 2) AS ticket_medio FROM pedidos;

-- Maior e menor pedido
SELECT 
    MAX(receita_total) AS maior_pedido,
    MIN(receita_total) AS menor_pedido
FROM pedidos;


-- -----------------------------------------------------------------------------
-- 3. AGRUPAMENTO (GROUP BY + HAVING)
-- -----------------------------------------------------------------------------

-- Receita e quantidade por produto
SELECT 
    produto,
    COUNT(*) AS total_pedidos,
    SUM(quantidade) AS unidades_vendidas,
    ROUND(SUM(receita_total), 2) AS receita_total
FROM pedidos
GROUP BY produto
ORDER BY receita_total DESC;

-- Receita por status
SELECT 
    status,
    COUNT(*) AS total_pedidos,
    ROUND(SUM(receita_total), 2) AS receita_total
FROM pedidos
GROUP BY status;

-- Clientes com mais de 1 pedido (HAVING filtra após o GROUP BY)
SELECT 
    cliente,
    COUNT(*) AS total_pedidos,
    ROUND(SUM(receita_total), 2) AS receita_total
FROM pedidos
GROUP BY cliente
HAVING COUNT(*) > 1
ORDER BY total_pedidos DESC;

-- Receita por mês
SELECT 
    mes,
    COUNT(*) AS total_pedidos,
    ROUND(SUM(receita_total), 2) AS receita_mensal
FROM pedidos
GROUP BY mes
ORDER BY mes;


-- -----------------------------------------------------------------------------
-- 4. SUBCONSULTAS (SUBQUERIES)
-- -----------------------------------------------------------------------------

-- Pedidos acima da média de receita
SELECT id_pedido, cliente, produto, receita_total
FROM pedidos
WHERE receita_total > (SELECT AVG(receita_total) FROM pedidos)
ORDER BY receita_total DESC;

-- Produto com maior receita total
SELECT produto, ROUND(SUM(receita_total), 2) AS receita_total
FROM pedidos
GROUP BY produto
ORDER BY receita_total DESC
LIMIT 1;


-- -----------------------------------------------------------------------------
-- 5. MANIPULAÇÃO DE DADOS (INSERT, UPDATE, DELETE)
-- -----------------------------------------------------------------------------

-- Inserir novo pedido
INSERT INTO pedidos (id_pedido, cliente, produto, quantidade, preco_unitario, receita_total, data_pedido, status, ano, mes, dia_semana, processado_em)
VALUES (11, 'Roberto Alves', 'Notebook', 1, 3500.00, 3500.00, '2024-01-25', 'concluido', 2024, 1, 'Friday', datetime('now'));

-- Atualizar status de um pedido
UPDATE pedidos
SET status = 'concluido'
WHERE id_pedido = 2;

-- Deletar pedidos cancelados
DELETE FROM pedidos
WHERE status = 'cancelado';

-- Verificar após as alterações
SELECT * FROM pedidos ORDER BY id_pedido;
