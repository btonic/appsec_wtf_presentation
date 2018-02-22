"""
TODO: DOC
"""
import redis
import os

def configure(app):
    """
    TODO: DOC
    """
    redis_host =os.environ.get("REDIS_HOST", "localhost")
    redis_port =os.environ.get("REDIS_PORT", 6379)
    redis_db = os.environ.get("REDIS_DB", 0)

    app.config.update(
        redis=redis.StrictRedis(
            host=redis_host,
            port=redis_port,
            db=redis_db
        )
    )
