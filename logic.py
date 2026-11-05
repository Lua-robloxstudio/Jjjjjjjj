import requests
from urllib.parse import quote
from config import api_key


def generate_image(prompt: str) -> str:
    """
    Создание картинки по запросу
    """
    # Заголовки запроса
    headers = {
        "authorization": "Bearer %s" % api_key
    }

    # URL для генерации: промпт передаётся прямо в адресе
    url = "https://gen.pollinations.ai/image/%s" % quote(prompt)

    # Параметры генерации
    params = {
        "width": 512,     # ширина изображения
        "height": 512,    # высота изображения
        "model": "flux"   # модель
    }

    # Отправляем GET-запрос: сервер сразу возвращает готовую картинку
    response = requests.get(url, params=params, headers=headers, timeout=120)
    if response.status_code == 200:
        print("Картинка получена")
        with open("cat.jpg", "wb") as f:
            f.write(response.content)
            print("Картинка сохранена")
        return "cat.jpg"
    else:
        return "Не удалось сгенерировать картинку"

    
if __name__ == "__main__":
    prompt = "cat with green eyes"
    result = generate_image(prompt)
    print(result)
