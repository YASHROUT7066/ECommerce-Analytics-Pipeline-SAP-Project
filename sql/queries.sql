-- Total sales
SELECT SUM(amount) FROM sales;

-- Sales by product
SELECT product, SUM(amount) FROM sales GROUP BY product;

-- Top customers
SELECT customer, SUM(amount) AS total
FROM sales
GROUP BY customer
ORDER BY total DESC;
