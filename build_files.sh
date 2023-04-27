# build_files.sh
#python manage.py collectstatic
#pip list --format=freeze > requirements.txt
#python manage.py check --deploy


#poetry install
#pip list --format=freeze > requirements.txt
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate