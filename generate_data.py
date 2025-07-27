import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

np.random.seed(44)
random.seed(44)

n_brigades = 10
brigade_ids = [f'BRIGADE_{i:02d}' for i in range(1, n_brigades + 1)]

# Генерируем синтетические данные журналов бурения
drilling_logs = []
start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 7, 25)

current_date = start_date
while current_date <= end_date:
    for brigade_id in brigade_ids:
        n_shifts = random.randint(1, 3) # от 1 до 3 смен в день на бригаду
        for _ in range(n_shifts):
            shift_start_time = current_date + timedelta(hours=random.randint(0, 23), minutes=random.randint(0, 59))
            shift_duration_hours = random.uniform(6, 12)
            shift_end_time = shift_start_time + timedelta(hours=shift_duration_hours)
            
            # Симулируем прогресс бурения
            start_depth = random.uniform(0, 500)
            drilled_depth = random.uniform(10, 100)
            end_depth = start_depth + drilled_depth
            
            # Симулируем влияние погоды и логистики
            weather_conditions = random.choice(['Sunny', 'Rainy', 'Snowy', 'Windy', 'Cloudy'])
            logistics_issues = np.random.choice([True, False], p=[0.1, 0.9])
            
            drilling_logs.append({
                'log_id': len(drilling_logs) + 1,
                'brigade_id': brigade_id,
                'log_date': current_date,
                'shift_start_time': shift_start_time,
                'shift_end_time': shift_end_time,
                'start_depth_m': round(start_depth, 2),
                'end_depth_m': round(end_depth, 2),
                'drilled_depth_m': round(drilled_depth, 2),
                'weather': weather_conditions,
                'logistics_issue': logistics_issues
            })
    current_date += timedelta(days=1)

drilling_logs_df = pd.DataFrame(drilling_logs)
drilling_logs_df.to_csv('drilling_logs.csv', index=False)

print('Синтетические данные журналов бурения успешно сгенерированы!')
print(f'Всего записей бурения: {len(drilling_logs_df)}')


