# build_files.sh
#python manage.py collectstatic
#pip list --format=freeze > requirements.txt

#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install
pip list --format=freeze > requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate