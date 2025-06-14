from InternalAPI.users import userProfile
from flask import *
app = Flask(__name__)

app.add_url_rule("/users/<path:subpath>", methods=['GET', 'POST', 'OPTIONS'], view_func=userProfile)
