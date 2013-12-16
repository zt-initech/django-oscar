#!/usr/bin/env bash

cd /var/www/oscar/builds/latest
git pull --ff-only 2> /dev/null
[ $? -gt 0 ] && echo "Git pull failed" >&2 && exit 1

# Update any dependencies
source ../../virtualenvs/latest/bin/activate
python setup.py develop
pip install -r requirements.txt

cd sites/sandbox
./manage.py syncdb --noinput
./manage.py migrate
./manage.py collectstatic --noinput
./manage.py loaddata ../_fixtures/promotions.json
./manage.py thumbnail clear
./manage.py rebuild_index --noinput

# Re-compile python code
touch deploy/wsgi/latest

# Copy down server config files
cp deploy/nginx/latest.conf /etc/nginx/sites-enabled/latest.oscarcommerce.com
/etc/init.d/nginx configtest 2> /dev/null && /etc/init.d/nginx force-reload 2> /dev/null

cp deploy/supervisord/latest.conf /etc/supervisor/conf.d/oscar-latest.conf
supervisorctl reread && supervisorctl reload

# Copy down cronjob file
/etc/init.d/supervisor restart
