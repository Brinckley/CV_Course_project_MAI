import torch
from torchvision import models, transforms
from PIL import Image
import numpy as np
import cv2
from pathlib import Path

class Segmenter:
    def __init__(self):       
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = models.segmentation.deeplabv3_resnet101(pretrained=True).eval()      

        self.transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])

    def segment_image(self, image: Image):
        image_tensor = self.transform(image).unsqueeze(0)
        with torch.no_grad():
            output = self.model(image_tensor)['out'][0]
        output_predictions = torch.argmax(output, dim=0)
        return output_predictions

    def save_segmented_image(self, image: Image, segmentation, output_path: str = None):
        human_mask = 15 # маска для людей в DeepLabV3
        mask = segmentation.cpu().numpy()
        mask_people = np.where(mask == human_mask, 1, 0)
        
        segmented_image = np.array(image) * mask_people[:, :, None]
        segmented_image = np.uint8(segmented_image)

        return segmented_image # сегментированное изображение
     
    def segment_video(self, video_path: str, output_path: str):
        cap = cv2.VideoCapture(video_path) # загрузка видео
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        out = cv2.VideoWriter(output_path, fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

        counter = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame_pil = Image.fromarray(frame) # кадр в PIL Image
            print(counter)
            counter += 1
            segmentation = self.segment_image(frame_pil) # сегментируем кадр как изображение
            segmented_frame = self.save_segmented_image(frame_pil, segmentation) # сохранение кадра

            out.write(segmented_frame) # добавление кадра к финальному видео

        cap.release()
        out.release()
        return output_path # путь до результата