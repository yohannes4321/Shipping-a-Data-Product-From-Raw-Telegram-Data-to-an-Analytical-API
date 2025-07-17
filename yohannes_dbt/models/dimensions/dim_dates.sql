select
    distinct
        CAST (message_date AS date) as message_date,
        extract(year from message_date)as year,
        extract(month from message_date)as month,
        TO_CHAR(message_date,'Month') as month_name,
        extract(day from message_date)as day,
        TO_CHAR(message_date,'Day') as day_of_week

    
from {{ref('telegram_messages')}}