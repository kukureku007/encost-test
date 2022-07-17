1. Установка зависимостей из requirements.txt
2. Создать таблицу endpoint_names

```
create table endpoint_names (
	endpoint_id int,
	endpoint_name varchar(250)
);
```
3. Создать файл .env в папке со скриптом, в котором описать параметры подключения к базе (пример .env.template)
4. Запуск python3 main.py 'filename.xls'