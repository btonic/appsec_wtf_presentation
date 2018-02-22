"""
Configure the application to be able to use a redis client through
`app.config`. Configuration of Redis endpoint location is done through
environment variables.
"""
import redis
import os

def configure(app):
    """
    Configures the app to have a redis client instance available globally.
    To configure the host, port, and db the app connects to, you must set the
    following environment variables:

        REDIS_HOST="localhost"
        REDIS_PORT=6379
        REDIS_DB=0

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
