from flask import jsonify
import requests
import importlib.util
import sys
import os

module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'API Helper', 'limiter.py'))
spec = importlib.util.spec_from_file_location("limiter", module_path)
limiter = importlib.util.module_from_spec(spec)
sys.modules["limiter"] = limiter
spec.loader.exec_module(limiter)

@limiter.limit("10 per minute")
def userProfile(username):
  res = requests.get(f'https://api.scratch.mit.edu/users/{username}').json()
  profile = res["profile"]
  return jsonify({ "username": res["username"], "bio": profile["bio"], "status": profile["status"] }) 
