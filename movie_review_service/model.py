def load_model():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    MODEL_PATH = os.path.join(BASE_DIR, 'model.pkl')
    full_path = os.path.abspath(MODEL_PATH)
    print(f"Используем путь к модели: {full_path}")

    try:
        with open(full_path, 'rb') as f:
            model = pickle.load(f)
        print("Модель загружена успешно.")
        return model
    except FileNotFoundError:
        print(f"Файл модели не найден: {full_path}")
        raise
    except Exception as e:
        print(f"Произошла ошибка при загрузке модели: {str(e)}")
        raise
