# How to test
#### Текущее состояние - ДЗ #5 ####
Для имитации нескольких серверов в upstream nginx, топорно поднимем 2 gunicorn с одного и того же wsgi application на разных портах 8081 и 8082 (не знаю, насколько это этично, но захотелось посмотреть на Nginx-овый Round-robin с весами в действии).
```bash
cd ask_gabolaev
gunicorn -c guni_serv1_conf.py ask_gabolaev.wsgi:application
gunicorn -c guni_serv2_conf.py ask_gabolaev.wsgi:application
sudo nginx
```
Для проверки работы wsgi парсера get/post поднимать `ask_gabolaev/getpostparser.py` приложение.
Для проверки этого же через Django поднимать `ask_gabolaev/wsgi.py` приложение.
Для печати текста поднимать `ask_gabolaev/helloworld.py` приложение.

Результаты нагрузочного тестирования лежат в `ab_tests/`.
Параметры нагрузки:
```bash 
ab -c100 -n1000 localhost/blahblah > fileName.txt
```

Конфиги Gunicorn и Nginx в `config/`.
В `/etc/nginx/nginx.conf` добавлено:
`proxy_cache_path ...ask_gabolaev/cache keys_zone=one:10m;`
