## Initialize
1. `cp .env.example .env`
2. `docker-compose up -d`
3. `docker-compose run --rm web sh`
4. `python manage.py migrate`
5. `python manage.py populate_cities 'city.csv'`
