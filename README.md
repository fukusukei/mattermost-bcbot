# mattermost-bcbot

## USAGE

### Container start

```
docker-compose build
docker-compose up -d
```

### run 

```
docker exec -it mattermost-bcbot_app_1 python workspace/announce.py
```

### cron
```
36 14   23   4   *    docker exec -i mattermost-bcbot_app_1 python workspace/announce.py
```