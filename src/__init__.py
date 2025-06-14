from InternalAPI.users import userProfile
from flask import *
from InternalAPI.API_Helper.limiter import limiter

app = Flask(__name__)
limiter.init_app(app)

app.add_url_rule("/users/<path:subpath>", methods=['GET', 'POST', 'OPTIONS'], view_func=userProfile)
