# build_files.sh
pip list --format=freeze > requirements.txt
python manage.py collectstatic