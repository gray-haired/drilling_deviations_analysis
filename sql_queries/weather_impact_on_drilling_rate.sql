SELECT
    weather_condition,
    AVG((end_depth - start_depth) / (EXTRACT(EPOCH FROM (shift_end_time - shift_start_time)) / 3600)) AS average_drilling_rate_m_per_h
FROM
    drilling_logs
WHERE
    (EXTRACT(EPOCH FROM (shift_end_time - shift_start_time)) / 3600) > 0 -- Избегаем деления на ноль
GROUP BY
    weather_condition
ORDER BY
    average_drilling_rate_m_per_h DESC;

