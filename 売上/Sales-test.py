/*

* CREATE table sales(id integer, shop_id integer, amount integer, month integer);

* CREATE table shop(id integer, name varchar(255), city_id integer);

* CREATE table city(id integer, name varchar(255));

*/

--返ってきて
WITH tmp AS (
  SELECT 
    sh.name,
    SUM(s.amount) AS total
  FROM shop sh
  JOIN city c ON sh.city_id = c.id
  JOIN sales s ON sh.id = s.shop_id
  WHERE c.name = 'Tokyo'
    AND s.month = 3
  GROUP BY sh.name
)

SELECT
  --最小の売上
  (SELECT MIN(total) FROM tmp) AS min_sales,

  -- 小店舗
  (
    SELECT STRING_AGG(name, ',')
    FROM tmp
    WHERE total = (SELECT MIN(total) FROM tmp)
  ) AS min_sales_shop_name,

  -- 最大の売上
  (SELECT MAX(total) FROM tmp) AS max_sales,

  -- 大店舗
  (
    SELECT STRING_AGG(name, ',')
    FROM tmp
    WHERE total = (SELECT MAX(total) FROM tmp)
  ) AS max_sales_shop_name
;