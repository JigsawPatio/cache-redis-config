# cache-redis-config
======================

A lightweight Redis configuration manager for caching in Node.js applications

## Description
---------------

cache-redis-config is a simple and efficient Redis configuration manager designed for caching in Node.js applications. It provides a convenient API for setting up and managing Redis connections, allowing developers to focus on building robust caching solutions.

## Features
------------

### Key Features

*   **Easy Setup**: Quickly establish Redis connections using a simple configuration object
*   **Flexible Configuration**: Support for custom Redis connection parameters and TTL (time-to-live) settings
*   **Secure**: Automatic SSL/TLS encryption and support for Redis password authentication
*   **Highly Performant**: Optimized for fast data access and caching operations

## Technologies Used
-------------------

### Dependencies

*   **redis**: Official Redis client for Node.js
*   **dotenv**: Load environment variables from a .env file

### Development

*   **TypeScript**: Strict type checking and auto-completion for a more productive development experience
*   **ESLint**: Enforce coding standards and catch potential errors early

## Installation
--------------

### Prerequisites

*   **Node.js**: v14.x or later
*   **npm**: v6.x or later

### Installation Steps

1.  Install the package using npm:
    ```
    npm install cache-redis-config
    ```
2.  Import the module in your project and configure Redis connections as needed

### Example Usage

```javascript
// Import the cache-redis-config module
const cacheRedisConfig = require('cache-redis-config');

// Configure Redis connections using a simple configuration object
const redisConfig = {
  host: 'localhost',
  port: 6379,
  password: 'your_redis_password',
  ssl: true,
  tls: true,
  timeout: 10000,
  ttl: 120,
};

// Establish a Redis connection using the configured settings
const redisClient = cacheRedisConfig.createClient(redisConfig);

// Use the Redis client for caching operations
redisClient.set('my_key', 'my_value', (err, reply) => {
  if (err) {
    console.error(err);
  } else {
    console.log(reply);
  }
});
```

## Contributing
--------------

Contributions and pull requests are welcome! If you'd like to contribute to this project, please follow these guidelines:

1.  Fork the repository
2.  Create a new branch for your feature or bug fix
3.  Commit changes with meaningful commit messages
4.  Open a pull request to the main branch

## License
---------

cache-redis-config is open-sourced under the [MIT License](https://opensource.org/licenses/MIT).