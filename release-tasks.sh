python3 manage.py reset_db --noinput -c
python3 manage.py migrate
python3 manage.py collectstatic --noinput
python3 manage.py load_dummy_data
