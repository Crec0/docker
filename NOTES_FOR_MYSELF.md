# Notes for myself

### Authelia

#### Password hashing thing
- `docker run authelia/authelia:latest authelia crypto hash generate argon2 --password 'PASSWORD_HERE'`
- `docker exec -it authelia authelia crypto hash generate pbkdf2 --variant sha512 --random --random.length 72 --random.charset rfc3986`

### Pterodactyl

Command to make panel user
- `docker compose run --rm panel php artisan p:user:make`

### Wings

- Remember to change the url in config.yml to https instead of http

### JQ query to extract the certificate and keys from acme json

- `jq -cj '.letsencrypt.Certificates[] | select(.domain.main == "<DOMAIN HERE>") | .certificate' acme.json | base64 -d`
- `jq -cj '.letsencrypt.Certificates[] | select(.domain.main == "<DOMAIN HERE>") | .key' acme.json | base64 -d`

### Wireguard

Peer info

- `docker exec -it wireguard cat /config/peer_home/peer_home.conf`

### PGADMIN

Otherwise you get weird spooky permission issues
- `sudo chown -R 5050:5050 ./data/pgadmin`

### Taskfile

taskfile.dev

### .gitattributes

Put this in .git/config with YOUR_DOMAIN.COM being your domain to replace, for stuff.
```diff 
+ [filter "yeet-domain"]
+	clean = sed s/YOUR_DOMAIN.COM/domain.com/ %f
```