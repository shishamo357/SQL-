/*

* CREATE table customer(id integer, name varchar(255));

* CREATE table item(id integer, name varchar(255), price integer);

* CREATE table customer_item(id integer, customer_id integer, item_id integer);

*/

SELECT
    ci.customer_id,
    SUM(i.price) AS total_amount
FROM customer_item ci
JOIN item i
    ON ci.item_id = i.id
GROUP BY ci.customer_id
ORDER BY ci.customer_id ASC;
