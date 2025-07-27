SELECT
    log_id,
    brigade_id,
    date,
    shift_start_time,
    shift_end_time,
    start_depth,
    end_depth,
    weather_condition,
    logistic_issues,
    (end_depth - start_depth) AS drilled_depth,
    (EXTRACT(EPOCH FROM (shift_end_time - shift_start_time)) / 3600) AS shift_duration_hours
FROM
    drilling_logs;

