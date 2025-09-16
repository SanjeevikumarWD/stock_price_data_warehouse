WITH base AS (
    SELECT
        stock_id,
        date,
        AVG(price) as avg_price,
        SUM(volume) as total_volume
    FROM {{ ref('stg_stocks') }}
    GROUP BY stock_id, date
)

SELECT
    stock_id,
    date,
    avg_price,
    total_volume,
    AVG(avg_price) OVER (PARTITION BY stock_id ORDER BY date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS moving_avg_7,
    AVG(avg_price) OVER (PARTITION BY stock_id ORDER BY date ROWS BETWEEN 29 PRECEDING AND CURRENT ROW) AS moving_avg_30,
    CASE 
        WHEN LAG(avg_price) OVER (PARTITION BY stock_id ORDER BY date) IS NULL THEN 0
        WHEN (avg_price - LAG(avg_price) OVER (PARTITION BY stock_id ORDER BY date)) / LAG(avg_price) OVER (PARTITION BY stock_id ORDER BY date) > 0.1 THEN 1
        ELSE 0
    END AS anomaly_flag,
    CURRENT_TIMESTAMP AS created_at
FROM base

