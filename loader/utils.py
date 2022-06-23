def save_picture(picture) -> str:   # Функция сохранения изображения
    filename = picture.filename
    path = f'./uploads/images/{filename}'
    picture.save(path)
    return path