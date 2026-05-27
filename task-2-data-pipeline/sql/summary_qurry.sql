

SELECT
    trend,
    COUNT(*) AS total_coins,
    AVG(price_change_24h) AS average_price_change
FROM
    `YOUR_PROJECT_ID.crypto_pipeline.crypto_market_data`
GROUP BY
    trend
ORDER BY
    average_price_change DESC;