
-- ========================================
-- Query 1: Top 5 Customers by Total Purchases (Past 12 Months)
-- ========================================

SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    SUM(o.total_amount) AS total_spent,
    COUNT(o.order_id) AS total_orders
FROM 
    customers c
JOIN 
    orders o ON c.customer_id = o.customer_id
WHERE 
    o.order_date >= DATE_SUB(CURDATE(), INTERVAL 12 MONTH)
GROUP BY 
    c.customer_id, c.first_name, c.last_name
ORDER BY 
    total_spent DESC
LIMIT 5;


-- ========================================
-- Query 2: Monthly Sales Summary (Current Year)
-- ========================================

SELECT 
    DATE_FORMAT(o.order_date, '%Y-%m') AS month,
    COUNT(o.order_id) AS total_orders,
    SUM(o.total_amount) AS total_revenue,
    AVG(o.total_amount) AS average_order_value
FROM 
    orders o
WHERE 
    YEAR(o.order_date) = YEAR(CURDATE())
GROUP BY 
    month
ORDER BY 
    month ASC;


-- ========================================
-- Query 3: Repeat Customers (Placed More Than 3 Orders)
-- ========================================

SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    COUNT(o.order_id) AS total_orders
FROM 
    customers c
JOIN 
    orders o ON c.customer_id = o.customer_id
GROUP BY 
    c.customer_id, c.first_name, c.last_name
HAVING 
    total_orders > 3
ORDER BY 
    total_orders DESC;


-- ========================================
-- Query 4 : Rank Customers Based on Total Spend (Last 6 Months)
-- ========================================

SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    SUM(o.total_amount) AS total_spent,
    RANK() OVER (ORDER BY SUM(o.total_amount) DESC) AS spend_rank
FROM 
    customers c
JOIN 
    orders o ON c.customer_id = o.customer_id
WHERE 
    o.order_date >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
GROUP BY 
    c.customer_id, c.first_name, c.last_name
ORDER BY 
    spend_rank ASC;


