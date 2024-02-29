#Для запуска - docker-compose up --bild

#В корне должен лежать .env типа:

DB_USER= admin \
DB_PASS=admin \
DB_HOST=localhost \
DB_PORT=5432 \
DB_NAME=ta_fastapi \

#Без .env не запустится. Из него парсятся переменные на всех уровнях