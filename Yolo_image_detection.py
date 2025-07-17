from ultralytics import YOLO
import glob
import json
import pandas as pd
import os

model = YOLO('yolov8n.pt')

all_result = []

datas = glob.glob('C:/Users/Hp/Documents/tenx/Shipping-a-Data-Product-From-Raw-Telegram-Data-to-an-Analytical-API/data/raw/telegram_messages/2025-07-17*/*.json')

for data in datas:
    with open(data, 'r', encoding='utf-8') as file:
        for line in file:
            line = json.loads(line)
            message_id = line.get('message_id')
           
            photo_path = line.get('photo_path')
            if photo_path:
          
                colab_photo_path = os.path.join('/content/drive/MyDrive', photo_path)


                try:
        
                    result = model.predict(colab_photo_path)
                    boxes = result[0].boxes      

                    for box in boxes:
                        class_number = int(box.cls[0])
                        class_name = result[0].names[class_number]
                        confidence = float(box.conf[0])

                        all_result.append({
                            "message_id": message_id,
                            "class_name": class_name,
                            "confidence": confidence,
                            "photo_path": photo_path  
                        })

                except Exception as e:
                    print(f'Error in {colab_photo_path}: {e}')


df = pd.DataFrame(all_result)
 
output_folder = 'C:/Users/Hp/Documents/tenx/Shipping-a-Data-Product-From-Raw-Telegram-Data-to-an-Analytical-API/data/raw/telegram_messages/2025-07-16/yolo_detected_images.json'
os.makedirs(output_folder, exist_ok=True)
output_file = os.path.join(output_folder, 'yolo_detected_images.json')
df.to_json(output_file, orient='records', lines=True)

print(f'Yolo detected images saved to: {output_file}')