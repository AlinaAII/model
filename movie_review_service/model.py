import joblib
import os
from pathlib import Path

def load_model():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    MODEL_PATH = os.path.join(BASE_DIR, 'sentiment_model.joblib')
    full_path = os.path.abspath(MODEL_PATH)
    print(f"Используем путь к модели: {full_path}")

    try:
        model = joblib.load(full_path)
        print("Модель загружена успешно.")
        return model
    except FileNotFoundError:
        print(f"Файл модели не найден: {full_path}")
        raise
    except Exception as e:
        print(f"Произошла ошибка при загрузке модели: {str(e)}")
        raise


try:
    BASE_DIR = Path(__file__).resolve().parent.parent
    MODEL_PATH = os.path.join(BASE_DIR, 'sentiment_model.joblib')
    full_path = os.path.abspath(MODEL_PATH)
    joblib.dump(model, MODEL_PATH)
    print("Модель успешно сохранена.")
except Exception as e:
    print(f"Ошибка при сохранении модели: {str(e)}")
    raise

