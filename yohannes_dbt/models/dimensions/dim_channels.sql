select
    distinct
    channel_id,
    channel

from {{ref ('telegram_messages')}}