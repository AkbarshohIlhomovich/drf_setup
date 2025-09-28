# DRF Project - Modern Django REST Framework Setup

Bu loyiha zamonaviy Django REST Framework (DRF) asosida yaratilgan bo'lib, PostgreSQL database, Django Unfold admin interface va Swagger API hujjatlari bilan jihozlangan professional web API loyihasi.

## 🚀 Xususiyatlar

✅ **Simple Custom User Model** - sodda va samarali foydalanuvchi modeli
✅ **PostgreSQL Database** - professional database bilan
✅ **Django Unfold Admin** - zamonaviy Tailwind CSS admin interface
✅ **Swagger API Documentation** - avtomatik API hujjatlari
✅ **Environment Variables** - xavfsiz konfiguratsiya
✅ **CORS Support** - frontend bilan ishlash uchun
✅ **Django REST Framework** - to'liq API development
✅ **Filtering & Search** - API'da qidirish va filtrlash
✅ **Docker Support** - container bilan deploy
✅ **Nginx Configuration** - production ready
✅ **Professional Structure** - production uchun tayyor

## 🐳 Docker bilan ishga tushirish (Tavsiya etiladi)

### Tez boshlash
```bash
git clone https://github.com/AkbarshohIlhomovich/drf_setup.git
cd drf_setup
docker-compose up --build
```

### Manzillar
- **Web application**: http://localhost
- **Django admin**: http://localhost/admin (admin/admin123)
- **API Documentation**: http://localhost/swagger/

Batafsil ma'lumot uchun [DOCKER.md](DOCKER.md) ni o'qing.

## 📦 O'rnatish

### 1. Repository'ni clone qiling
```bash
git clone https://github.com/AkbarshohIlhomovich/drf_setup.git
cd drf_setup
```

### 2. Virtual environment yaratish
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# yoki
venv\Scripts\activate  # Windows
```

### 3. Dependencies o'rnatish
```bash
pip install -r requirements.txt
```

### 4. PostgreSQL o'rnatish va sozlash
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install postgresql postgresql-contrib

# PostgreSQL'ga kirish
sudo -i -u postgres
psql

# Database va user yaratish
CREATE DATABASE drf_project;
CREATE USER drf_user WITH PASSWORD 'your_password' SUPERUSER CREATEDB;
GRANT ALL PRIVILEGES ON DATABASE drf_project TO drf_user;
\q
exit
```

### 5. Environment variables sozlash
`.env.example` faylini `.env` ga nusxalang va o'z qiymatlaringizni kiriting:
```bash
cp .env.example .env
```

`.env` faylini tahrirlang:
```bash
SECRET_KEY=your-secret-key-here
DEBUG=True
DB_PASSWORD=your_actual_password
```

### 6. Database migration
```bash
python manage.py migrate
```

### 7. Superuser yaratish
```bash
python manage.py createsuperuser
```

### 8. Development server ishga tushirish
```bash
python manage.py runserver
```

## 🌐 Manzillar

- **Admin Panel**: http://127.0.0.1:8000/admin/ (Django Unfold interface)
- **API Documentation (Swagger)**: http://127.0.0.1:8000/swagger/
- **API Documentation (ReDoc)**: http://127.0.0.1:8000/redoc/
- **API Endpoints**: http://127.0.0.1:8000/api/v1/accounts/

## 📋 API Endpoints

### Users
- `GET /api/v1/accounts/users/` - Barcha foydalanuvchilar ro'yxati
- `POST /api/v1/accounts/users/` - Yangi foydalanuvchi yaratish
- `GET /api/v1/accounts/users/{id}/` - Foydalanuvchi ma'lumotlari
- `PUT /api/v1/accounts/users/{id}/` - Foydalanuvchi ma'lumotlarini yangilash
- `DELETE /api/v1/accounts/users/{id}/` - Foydalanuvchini o'chirish
- `GET /api/v1/accounts/users/me/` - Joriy foydalanuvchi ma'lumotlari

### Authentication
- API TokenAuthentication va SessionAuthentication qo'llab-quvvatlanadi
- Swagger UI orqali API'ni test qilish mumkin

## 👤 User Model Fields

Sodda va samarali User modeli:

### Django standart maydonlari:
- `username` - Foydalanuvchi nomi
- `email` - Email manzil
- `password` - Parol
- `first_name` - Ism
- `last_name` - Familiya
- `is_active` - Faol holat
- `is_staff` - Admin huquqi
- `is_superuser` - Super admin huquqi
- `date_joined` - Ro'yxatdan o'tgan sana
- `last_login` - Oxirgi kirish

### Qo'shimcha maydonlar:
- `phone_number` - Telefon raqami
- `profile_photo` - Profil rasmi

## 📦 Technology Stack

### Backend
- **Django 5.1.1** - Modern web framework
- **Django REST Framework 3.15.2** - Powerful API toolkit
- **PostgreSQL 16.10** - Professional database
- **psycopg2-binary 2.9.9** - PostgreSQL adapter

### API & Documentation
- **drf-yasg 1.21.7** - Swagger/OpenAPI 3.0 documentation
- **django-cors-headers 4.4.0** - CORS support
- **django-filter 24.3** - Advanced filtering

### Admin Interface
- **django-unfold 0.66.0** - Modern Tailwind CSS admin
- **Pillow 10.4.0** - Image processing

### Development Tools
- **django-extensions 3.2.3** - Django utilities
- **python-decouple 3.8** - Environment variables management

### Environment
- **Python 3.12+** - Latest Python version
- **Virtual Environment** - Isolated dependencies

## 🔧 Development

### Code Style
```bash
# Django extensions commands
python manage.py shell_plus
python manage.py show_urls
python manage.py runserver_plus
```

### API Testing
- Swagger UI: http://127.0.0.1:8000/swagger/
- Postman yoki curl bilan API test qiling
- DRF Browsable API: http://127.0.0.1:8000/api/v1/accounts/users/

### Database Management
```bash
# Migration yaratish
python manage.py makemigrations

# Migration qo'llash
python manage.py migrate

# Database shell
python manage.py dbshell
```

## 🚀 Production

### Environment Variables
```bash
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
SECRET_KEY=your-super-secure-secret-key
DB_PASSWORD=strong-database-password
```

### Static Files
```bash
python manage.py collectstatic --noinput
```

### Deployment
1. **Gunicorn** WSGI server bilan
2. **Nginx** reverse proxy sifatida
3. **PostgreSQL** production database
4. **Redis** (ixtiyoriy) caching uchun

## 📁 Project Structure

```
drf_setup/
├── accounts/           # User management app
├── config/             # Main project settings
├── static/             # Static files
├── media/              # Media files
├── venv/               # Virtual environment
├── .env                # Environment variables
├── .env.example        # Environment template
├── .gitignore          # Git ignore rules
├── requirements.txt    # Dependencies
├── Dockerfile          # Docker configuration
├── docker-compose.yml  # Docker services
├── nginx.conf          # Nginx configuration
├── entrypoint.sh       # Docker entrypoint
├── DOCKER.md           # Docker documentation
└── README.md           # This file
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Support

Agar savollar bo'lsa:
- GitHub Issues orqali murojaat qiling: https://github.com/AkbarshohIlhomovich/drf_setup/issues
- Email: akbarshoh.ilhomovich@gmail.com