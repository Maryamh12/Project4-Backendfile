python manage.py dumpdata albums --output albums/seeds.json --indent=2;
python manage.py dumpdata artists --output artists/seeds.json --indent=2;
python manage.py dumpdata genres --output genres/seeds.json --indent=2;
python manage.py dumpdata comments --output comments/seeds.json --indent=2;
python manage.py dumpdata songs --output songs/seeds.json --indent=2;
python manage.py dumpdata jwt_auth --output jwt_auth/seeds.json --indent=2;