# Docker compose run 

## Prerequisities

- Docker should be installed and ready. Check your distro  https://docs.docker.com/engine/install/
- docker-compose should be installed.  https://docs.docker.com/compose/install/linux/
- You should be familiar with bash shell 
After this: 

### Steps to run this babe

Needless to say, you should be in the same directory where you cloned this git repo.
1.  ```cp .env.example .env```
change values 

### Example .env file

MUDUR_CONFIG=/app/kampyazilim.conf
MUDUR_DEBUG=True
MUDUR_HTTPS=True

POSTGRES_PASSWORD=mudur
POSTGRES_USER=mudur
POSTGRES_DB=mudur

2. ``` cp kampyazilim.conf.example kampyazilim.conf```

### Example kampyazilim.conf
[DB]
host: 192.168.1.15 # localhost or 127.0.0.1 not works. Run ```ip -br a``` ans use the taken ip.
port: 5433
database: mudur
dbuser: mudur
pass: mudur

[DJANGO]
secret_key:HOLA_LKD_coRrECTBATteRyhoRSesTAple💩🍆💦🦴🍒🍑 ¶¼ËßñĆ

[EMAIL]
from:<from address>
host:<smtp server>
port:<smtp port>
username:<smtp username>
password:<smtp password>

[SMS]
url: <api url>
usercode: <usercode>
password: <password>
msgheader: <msgheader>

3. And then the last step. In the same directory with docker-compose.yaml
```docker-compose -f docker-compose.yaml up```

If all goes well you should see mudur is running at 8080 

## Helper docker commands

Terminate containers
```docker-compose -f docker-compose.yaml down``` 

Sometimes postgresql container keeps running. Check with 
```docker ps``` 
 
See the pg container id and 
```docker kill container_id ``` and ``` deocker rm container_id```

If you need to delete volumes check with this
``` docker volume ls```

You can delete anything starts with kamp-yazilimi_
``` docker volume rm kamp-yazilimi_*```

Good luck.


