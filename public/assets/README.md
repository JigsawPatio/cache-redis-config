# -*- coding: utf-8 -*-

"""
cache-redis-config
==================

A lightweight Python library for generating cache configuration files for Redis.

Usage
-----

```python
import cache_redis_config as crc

# Create a new configuration object
config = crc.Config()

# Set cache expiration time in seconds
config.expiration_time = 3600  # 1 hour

# Set cache key prefix
config.key_prefix = 'my_app'

# Generate the Redis configuration file
crc.generate_config(config, 'redis_config.conf')
```

Configuration Object
-------------------

```python
class Config:
    def __init__(self):
        self.expiration_time = 0
        self.key_prefix = ''
        self.database = 0
        self.max_memory = 0
        self.max_connections = 0

    @property
    def expiration_time(self):
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, value):
        if value < 0:
            raise ValueError('Expiration time must be a non-negative integer')
        self._expiration_time = value

    @property
    def key_prefix(self):
        return self._key_prefix

    @key_prefix.setter
    def key_prefix(self, value: str):
        if not isinstance(value, str):
            raise TypeError('Key prefix must be a string')
        self._key_prefix = value

    @property
    def database(self):
        return self._database

    @database.setter
    def database(self, value: int):
        if not isinstance(value, int):
            raise TypeError('Database must be an integer')
        self._database = value

    @property
    def max_memory(self):
        return self._max_memory

    @max_memory.setter
    def max_memory(self, value: int):
        if not isinstance(value, int):
            raise TypeError('Max memory must be an integer')
        self._max_memory = value

    @property
    def max_connections(self):
        return self._max_connections

    @max_connections.setter
    def max_connections(self, value: int):
        if not isinstance(value, int):
            raise TypeError('Max connections must be an integer')
        self._max_connections = value
```

Functions
---------

```python
def generate_config(config: Config, filename: str):
    with open(filename, 'w') as f:
        f.write('maxmemory ' + str(config.max_memory) + '\n')
        f.write('maxmemory-policy volatile-lru\n')
        f.write('maxconnections ' + str(config.max_connections) + '\n')
        f.write('db ' + str(config.database) + '\n')
        f.write('keyprefix ' + config.key_prefix + '\n')
```