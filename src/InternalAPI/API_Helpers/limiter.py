from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import redis

redis_connection = redis.Redis(host='bc_redis', port=6379)
# Create a global limiter instance
limiter = Limiter(
    get_remote_address,
    default_limits=[],
    storage_uri="redis://bc_redis:6379",
)
