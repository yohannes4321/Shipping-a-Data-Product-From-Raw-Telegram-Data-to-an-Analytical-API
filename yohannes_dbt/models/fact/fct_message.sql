SELECT
    
    m.message_id,
    m.channel ,
    m.channel_id, 
    m.message_date,
    m.description,
    CASE 
        WHEN m.image_path IS NOT NULL THEN TRUE
        ELSE FALSE
    END AS has_image,
    d.year,
    d.month,
    d.day,
    d.month_name,
    d.day_of_week,
    m.product,
    m.price

FROM {{ ref('telegram_messages') }} m   
LEFT JOIN {{ ref('dim_dates') }} d 
    ON CAST(m.message_date AS date) = d.message_date
LEFT JOIN {{ ref('dim_channels') }} c
    ON m.channel = c.channel_id
