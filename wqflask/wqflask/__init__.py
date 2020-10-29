import sys
import time
import jinja2

from flask import g
from flask import Flask
from utility import formatting

import logging
logger = logging.getLogger(__name__ )
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# See http://flask.pocoo.org/docs/config/#configuring-from-files
# Note no longer use the badly named WQFLASK_OVERRIDES (nyi)
app.config.from_envvar('GN2_SETTINGS')
app.jinja_env.globals.update(
    undefined=jinja2.StrictUndefined,
    numify=formatting.numify)


@app.before_request
def before_request():
   g.request_start_time = time.time()
   g.request_time = lambda: "%.5fs" % (time.time() - g.request_start_time)


from wqflask.api import router
from wqflask import group_manager
from wqflask import resource_manager
from wqflask import search_results
from wqflask import export_traits
from wqflask import gsearch
from wqflask import update_search_results
from wqflask import docs
from wqflask import news
from wqflask import db_info
from wqflask import user_login
from wqflask import user_session

import wqflask.views
