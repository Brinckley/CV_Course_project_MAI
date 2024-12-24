# Курсовая работа
## Савин Александр М80-214М-23
Задача : Cегментации изображений  
Перечень объектов : Люди  
# Описание
Проект реализует API для сегментации изображений и видео с помощью предварительно обученной модели DeepLabV3 на базе MobileNetV2. DeepLabV3 — модель для сегментации изображений, разработанная Google. Обычно используется для получения высоких показателей на задачах сегментации. В отличие от обычных моделей классификации, которые дают один класс для каждого изображения, модели сегментации делят изображение на несколько областей и присваивают каждый пиксель соответствующему классу (в данном случае, классу "человек").  
Сегментация позволяет выделить людей на изображениях и в видео. Для сервера используется FastAPI, PyTorch для обработки моделей и OpenCV для работы с видео.  
Компоненты упакованы в Docker-контейнер.

# Запуск
Для запуска выполняем команду в корневой папке проекта: 
```
docker-compose up --build
```
Ендпоинты для отправки изображение и видео: 
```
http://localhost:8000/segment_image/
http://localhost:8000/segment_video/
```
Скины использования из postman.  
![alt text](https://github.com/Brinckley/CV_Course_project_MAI/blob/main/postman/segment_image.jpg)
![alt text](https://github.com/Brinckley/CV_Course_project_MAI/blob/main/postman/segment_video.jpg)

# Пример результатов для изображений
Простое изображение человека:  
![alt text](https://github.com/Brinckley/CV_Course_project_MAI/blob/main/results/result2.jpg)  
Несколько человек:  
![alt text](https://github.com/Brinckley/CV_Course_project_MAI/blob/main/results/result1.jpg)  
  
![alt text](https://github.com/Brinckley/CV_Course_project_MAI/blob/main/results/result4.jpg)  
Фото с эффектами:  
![alt text](https://github.com/Brinckley/CV_Course_project_MAI/blob/main/results/result3.jpg)  

# Пример результатов для видеозаписей
Ноутбук справлялся с задачей относительно медленно, поэтому пришлось снизить до 12fps.
Начальное 4х секундное [видео](https://github.com/Brinckley/CV_Course_project_MAI/blob/main/examples/test_video_2.mp4)
Результат [видео](https://github.com/Brinckley/CV_Course_project_MAI/blob/main/results/video_response_2.mp4)
