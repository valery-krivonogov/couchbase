#  Выполнение домашнего задания:

## Развернуть кластер Couchbase

Развертывается 4 ноды:
- couchbase1
- couchbase2
- couchbase3
- couchbasemain 

docker-compose.yml:
```
version: '3.9'
services:
  couchbase1:
    image: couchbase/server
    container_name: couchbase1
    volumes:
      - ./node1:/opt/couchbase/var
    ports:
      - 8101:8091
  couchbase2:
    image: couchbase/server
    container_name: couchbase2
    volumes:
      - ./node2:/opt/couchbase/var
    ports:
      - 8102:8091
  couchbase3:
    image: couchbase/server
    container_name: couchbase3
    volumes:
      - ./node3:/opt/couchbase/var
    ports:
      - 8103:8091
  couchbasemain:
    image: couchbase/server
    container_name: couchbasemain
    volumes:
      - ./nodeMain:/opt/couchbase/var
    ports:
      - 8201:8091
      - 8202:8092
      - 8203:8093
      - 8204:8094
      - 11210:11210

```

Команда запуска:
docker-compose -f docker-compose.yml up
```
[+] Running 5/5
 ✔ Network couchbase_default  Created                                                                                                                      0.1s 
 ✔ Container couchbase3       Started                                                                                                                      1.5s 
 ✔ Container couchbase1       Started                                                                                                                      1.5s 
 ✔ Container couchbasemain    Started                                                                                                                      1.6s 
 ✔ Container couchbase2       Started  
```

Настройка кластера осуществляется в wi

Настроенный кластер:<br>
![Кластер](/images/cluster.jpg)

### Создать БД, наполнить небольшими тестовыми данными

Создана база данных, загружены тестовые данные<br>
![Database](/images/testDB.jpg)

Выполнение запроса данных:<br>
![Select](/images/select_beer.jpg)

### Проверить отказоустойчивость

Отключение ноды с данными (couchbase3)<br>
Сбой обнаружен:<br><br>
![fail](/images/nodeStop.jpg)

Восстановление работоспособности ноды<br>
Нода couchbase3 подключена к кластеру:<br><br>
![restore](/images/nodeStart.jpg)
