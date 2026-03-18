import logging
import os
import redis

# Set up logging
logger = logging.getLogger(__name__)

def get_redis_config(config_file_path):
    try:
        with open(config_file_path, 'r') as config_file:
            config = config_file.read()
            config_dict = {}
            for line in config.split('\n'):
                if line:
                    key, value = line.split('=')
                    config_dict[key.strip()] = value.strip()
            return config_dict
    except FileNotFoundError:
        logger.error(f"Config file not found at {config_file_path}")
        return None

def create_redis_client(config):
    if config is None:
        logger.error("Redis config is None")
        return None

    try:
        host = config['host']
        port = config['port']
        password = config['password']
        db = config['db']
        redis_client = redis.Redis(host=host, port=port, password=password, db=db)
        return redis_client
    except KeyError as e:
        logger.error(f"Missing config key: {e}")
        return None
    except redis.ConnectionError as e:
        logger.error(f"Failed to connect to Redis: {e}")
        return None

def get_cache_config():
    cache_config_file_path = os.environ.get('CACHE_CONFIG_FILE_PATH')
    if cache_config_file_path is None:
        logger.error("CACHE_CONFIG_FILE_PATH environment variable not set")
        return None

    cache_config = get_redis_config(cache_config_file_path)
    return cache_config

def get_redis_client():
    cache_config = get_cache_config()
    return create_redis_client(cache_config)