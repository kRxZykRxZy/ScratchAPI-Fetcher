from .users import userProfile

def internal_register_routes(app)
app.add_url_rule("/users/<path:subpath>", methods=['GET', 'POST', 'OPTIONS'], view_func=userProfile)
