### Описание проекта

Проект представляет собой интерфейс API и является частью проекта **Yatube**.
Интерфейс позволяет работать с сервисом блогов с помощью CRUD-модели взаимодействия.

### Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Alexshifter/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
Перейти в директорию проекта и выполнить миграции:
```
cd yatube_api
```
```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
### Возможности API

- Для неавторизованного пользователя:
   - Получение списка постов. Опциональные параметры ```limit``` ```offset```; 
   - Получения поста по его id;
   - Получение списка комментариев к посту;
   - Получение комментария к посту по его id;
   - Получение списка сообществ;
   - Получение сообщества по его id;
   - Получение/Обновление/Проверка JWT токена;
     
- Для авторизованного пользователя:
   - Получение списка подписок пользователя. Опциональный параметр: ```search```;
   - Добавление пользователя в список своих подписок;
   - Создание, обновление, частичное обновление поста автором;
   - Создание, обновление, частичное обновление комментария автором;

### Основные эндпоинты

```/posts/```
```/posts/{post_id}/```
```/posts/{post_id}/comments/```
```/posts/{id}/comments/{comment_id}/```
```/groups/```
```/groups/{group_id}/```
```/follow/```
```/jwt/create/```
```/jwt/verify/```
```/jwt/refresh/```


### Примеры запросов

- **Получение списка всех постов:**
  
  ![изображение](https://github.com/Alexshifter/api_final_yatube/assets/146896696/651c614f-8ac0-4e69-9968-804e2fe041e0)
  
- **Получение всех комментариев к посту:**

  ![изображение](https://github.com/Alexshifter/api_final_yatube/assets/146896696/0a6c0710-2107-40fe-9410-2a1e37f4757a)

- **Получение подписок пользователя**:

  ![изображение](https://github.com/Alexshifter/api_final_yatube/assets/146896696/65544ed1-7251-436d-9f33-7c28582fa1ff)
  
- **Создание поста**:

  ![изображение](https://github.com/Alexshifter/api_final_yatube/assets/146896696/9eabf249-0358-4598-8867-0384415c99b9)

- **Созданиме комментария**:
 
  ![изображение](https://github.com/Alexshifter/api_final_yatube/assets/146896696/16972d79-0454-4936-8bb7-73128694b4da)
  
- **Обновление поста**:
  
  ![изображение](https://github.com/Alexshifter/api_final_yatube/assets/146896696/cd7a7cb6-dd7d-4291-b787-e989956f8dd6)
  
- **Подписка на пользователя**:
  
  ![изображение](https://github.com/Alexshifter/api_final_yatube/assets/146896696/0e7c8b93-28f0-4415-916d-8840c665ae1c)


  
  





