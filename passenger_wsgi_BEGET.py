# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/home/g/gaidys2d/novokosulino-2/Novokosulino')
sys.path.insert(1, '/home/g/gaidys2d/.local/lib/python3.10/site-packages')
# sys.path.insert(1, '/home/g/gaidys2d/novokosulino/venv/lib/python3.10/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'Novokosulino.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

