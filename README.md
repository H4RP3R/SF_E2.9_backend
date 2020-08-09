## Как запустить  

```
git clone https://github.com/H4RP3R/SF_E2.9_backend.git
cd SF_E2.9_backend
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
export EMAIL_HOST_PASSWORD=<your-yandex-password>
export EMAIL_HOST_USER=<your-yandex-email-address>
export SECRET_KEY=<django-secret-key>
python manage.py migrate
python manage.py runserver
```
Фронт-енд [тут](https://github.com/H4RP3R/SF_E2.9_frontend)
