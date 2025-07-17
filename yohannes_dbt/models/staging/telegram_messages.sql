WITH source AS (
    SELECT * FROM {{ source('yohannes_schema', 'tellegram_data') }}
),
renamed AS (
    SELECT
        message_id,
        CAST(date AS date) AS message_date,
        channel_name AS channel,
        channel_id,
        text AS description,
        
        photo_path AS image_path,
        product,
        price
    FROM source
),
filtered AS (
    SELECT
        message_id,
        product,
        price,
        message_date,
        channel,
        channel_id,
        REPLACE(
            REPLACE(description, E'\n', ' '),    
            E'\\/', '/'                         
        ) AS description,
   
        image_path
    FROM renamed
    WHERE description IS NOT NULL
      AND image_path IS NOT NULL
      AND channel IS NOT NULL
        AND product is not NULL
         
      AND message_id IS NOT NULL
)
SELECT * FROM filtered
