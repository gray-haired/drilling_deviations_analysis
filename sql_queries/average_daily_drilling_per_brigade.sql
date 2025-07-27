WITH DailyDrilling AS (
    SELECT
        date,
        brigade_id,
        SUM(end_depth - start_depth) AS daily_drilled_depth
    FROM
        drilling_logs
    GROUP BY
        date,
        brigade_id
)
SELECT
    brigade_id,
    AVG(daily_drilled_depth) AS average_daily_drilled_depth
FROM
    DailyDrilling
GROUP BY
    brigade_id
ORDER BY
    average_daily_drilled_depth DESC;

