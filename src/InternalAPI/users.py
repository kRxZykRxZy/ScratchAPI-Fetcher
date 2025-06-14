from flask import limiter, jsonify
import requests

@limiter.limit("10 per minute")
def userProfile(username):
  res = requests.get(f'https://api.scratch.mit.edu/users/{username}').json()
  profile = res["profile"]
  return jsonify({ "username": res["username"], "bio": profile["bio"], "status": profile["status"] }) 
