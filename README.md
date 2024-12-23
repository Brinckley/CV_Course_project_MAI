# Курсовая работа
## Савин Александр М80-214М-23

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

