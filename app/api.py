from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from segmentation import Segmenter
from io import BytesIO
from PIL import Image
from pathlib import Path

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

segmenter = Segmenter()

# локальные папки для данных
input_dir = Path("data/input")
output_dir = Path("data/output")
input_dir.mkdir(parents=True, exist_ok=True)
output_dir.mkdir(parents=True, exist_ok=True)

@app.post("/segment_image/")
async def segment_image(file: UploadFile = File(...)):
    file_path = input_dir / file.filename
    
    with open(file_path, "wb") as f: # сохранение файла локально
        f.write(await file.read())
    image = Image.open(file_path)

    segmentation = segmenter.segment_image(image) # сегментация изображения
    segmented_image = segmenter.save_segmented_image(image, segmentation, None)

    segmented_image_pil = Image.fromarray(segmented_image) # массив -> изображение

    img_byte_arr = BytesIO()
    segmented_image_pil.save(img_byte_arr, format="PNG")

    return StreamingResponse(img_byte_arr, media_type="image/png") # обратная отправка изображения

@app.post("/segment_video/")
async def segment_video(file: UploadFile = File(...)):
    video_path = input_dir / file.filename # сохранение внутри контейнера
    output_video_path = output_dir / f"segmented_{file.filename}"

    with open(video_path, "wb") as f:
        f.write(await file.read())

    output_video = segmenter.segment_video(str(video_path), str(output_video_path))

    return StreamingResponse(open(output_video, "rb"), media_type="video/mp4") # отправка результата