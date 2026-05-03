# Docker ile Çalıştırma

## Gereksinimler

- [Docker](https://docs.docker.com/engine/install/)
- [docker-compose](https://docs.docker.com/compose/install/linux/)

---

## Adımlar

### 1. `.env` dosyasını oluştur

```bash
cp .env.example .env
```

### 2. `kampyazilim.conf` dosyasını oluştur

```bash
cp kampyazilim.conf.example kampyazilim.conf
```

> **Önemli:** Docker içinde veritabanı host'u `postgresql` olmalı (`localhost` çalışmaz).
> WhatsApp bridge ayrı çalışıyorsa `[WHATSAPP]` bölümündeki `url`'i o sunucunun adresiyle doldur.

### 3. Başlat

```bash
docker-compose -f docker-compose.yaml up
```

Uygulama `http://localhost:8080` adresinde çalışır.

---

## Yardımcı Komutlar

```bash
# Durdur
docker-compose -f docker-compose.yaml down

# Logları izle
docker-compose -f docker-compose.yaml logs -f

# Django yönetim komutu çalıştır
docker-compose -f docker-compose.yaml exec mudur entrypoint.sh managepy <komut>

# Volume listele / sil (dikkatli! veri silinir)
docker volume ls
docker volume rm kamp-yazilimi_postgres_data
```
