select 
m.message_id,
m.class_name,
m.confidence



from {{source('yohannes_schema','yolo_images')}} as m
LEFT JOIN  {{ ref('fct_message')}} as f
ON f.message_id=m.message_id
