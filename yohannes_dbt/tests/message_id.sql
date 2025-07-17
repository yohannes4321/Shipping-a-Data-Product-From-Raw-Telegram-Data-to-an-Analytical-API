SELECT message_id, COUNT(*)
FROM {{ ref('telegram_messages') }}
GROUP BY message_id
HAVING COUNT(*) > 1

