SELECT
    stock_id,
    date,
    AVG(price) as avg_price,
    SUM(volume) as total_volume
FROM {{ ref('stg_stocks') }}
GROUP BY stock_id, date
