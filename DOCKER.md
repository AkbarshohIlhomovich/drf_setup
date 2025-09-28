# Docker Setup - DRF Project

## 🐳 Docker bilan ishga tushirish

### 1. Docker va Docker Compose o'rnatilgan bo'lishi kerak

```bash
# Docker versiyasini tekshirish
docker --version
docker-compose --version
```

### 2. Loyihani Docker bilan ishga tushirish

```bash
# Barcha servislarni ishga tushirish
docker-compose up --build

# Background rejimda ishga tushirish
docker-compose up -d --build
```

### 3. Servislar

- **web**: Django application (port 8000)
- **db**: PostgreSQL database (port 5432)
- **nginx**: Nginx reverse proxy (port 80)

### 4. Manzillar

- **Web application**: http://localhost
- **Django admin**: http://localhost/admin
- **API Documentation**: http://localhost/swagger/
- **Direct Django**: http://localhost:8000 (development)

### 5. Default superuser

Automatic yaratiladi:
- **Username**: admin
- **Password**: admin123
- **Email**: admin@example.com

### 6. Docker buyruqlari

```bash
# Servislarni to'xtatish
docker-compose down

# Volumelar bilan birga o'chirish
docker-compose down -v

# Loglarni ko'rish
docker-compose logs -f

# Specific service loglari
docker-compose logs -f web

# Django shell
docker-compose exec web python manage.py shell

# Migration yaratish
docker-compose exec web python manage.py makemigrations

# Migration qo'llash
docker-compose exec web python manage.py migrate

# Static files yig'ish
docker-compose exec web python manage.py collectstatic --noinput

# Container ichiga kirish
docker-compose exec web bash

# Database backup
docker-compose exec db pg_dump -U drf_user drf_project > backup.sql

# Database restore
docker-compose exec -T db psql -U drf_user drf_project < backup.sql
```

### 7. Production uchun

Production muhiti uchun:

1. `.env` faylini yangilang:
```bash
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
SECRET_KEY=your-super-secure-secret-key
```

2. SSL sertifikat qo'shing
3. Nginx konfiguratsiyasini yangilang
4. `docker-compose.prod.yml` yarating

### 8. Muammolarni hal qilish

**Database connection error:**
```bash
# Database servisini qayta ishga tushirish
docker-compose restart db
```

**Static files yuklanmaydi:**
```bash
# Static files qayta yig'ish
docker-compose exec web python manage.py collectstatic --noinput
```

**Permission errors:**
```bash
# Ownership o'zgartirish
sudo chown -R $USER:$USER .
```

### 9. Development workflow

```bash
# O'zgarishlarni kuzatish uchun
docker-compose up

# Yangi package o'rnatgandan keyin
docker-compose build web
docker-compose up

# Database reset
docker-compose down -v
docker-compose up --build
```