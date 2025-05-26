SELECT
    stock_id,
    date,
    price,
    volume
FROM {{ source('raw', 'raw_stocks') }}
WHERE price > 0 AND volume > 0
