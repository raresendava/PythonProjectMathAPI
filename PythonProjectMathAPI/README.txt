Math Microservice (FastAPI + SQLite + JWT + Docker)
===================================================

This project is a production-ready microservice that exposes a REST API to perform mathematical operations:

- Power function: pow(a, b)
- N-th Fibonacci number: fib(n)
- Factorial of a number: fact(n)

All requests are persisted in a SQLite database and secured with JWT-based authentication. The service includes containerization, Prometheus-compatible monitoring, caching, and simulated Kafka-style logging.

Features
--------

- REST API (FastAPI)
- SQLite request logging
- JWT authentication
- In-memory caching using functools.lru_cache
- Prometheus /metrics endpoint
- Dockerized service
- Structured simulated logging to Kafka (console)
- MVC/MVCS-style modular codebase

Project Structure
-----------------

    math_service_full/
    ├── app/
    │   ├── api/             # API route definitions
    │   ├── db/              # SQLite setup and connection
    │   ├── models/          # SQLAlchemy model for request logs
    │   ├── services/        # Business logic (pow, fib, fact)
    │   ├── utils/           # JWT handling and Kafka logger
    │   └── main.py          # FastAPI app startup
    ├── generate_token.py    # Script to create test JWT tokens
    ├── requirements.txt     # Project dependencies
    ├── Dockerfile           # Docker container definition
    └── test.http            # REST Client tests

Setup Instructions
------------------

### Prerequisites

- Docker (e.g. via Rancher Desktop or Docker Desktop)
- Python 3.11+ (for optional local JWT token generation)
- VS Code (recommended)
- REST Client extension (optional)

Running the Service
-------------------

1. Build the Docker image:

       docker build -t math-service .

2. Run the container:

       docker run -p 8000:8000 math-service

3. Access the API:

- Swagger UI: http://localhost:8000/docs
- Metrics: http://localhost:8000/metrics

JWT Authentication
------------------

All endpoints require a valid JWT token in the Authorization header.

### Generating a Token

Use the provided generate_token.py script:

    python generate_token.py

This will output a token like:

    eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

Use it in requests as:

    Authorization: Bearer <your_token>

The secret and algorithm are configured in app/utils/auth.py.

API Usage
---------

### Endpoints

    /math/fib   - Fibonacci number, requires param: a
    /math/fact  - Factorial, requires param: a
    /math/pow   - Power function, requires params: a, b

### Example Request

    GET http://localhost:8000/math/fib?a=10
    Authorization: Bearer <your_token>

Testing with REST Client (VS Code)
----------------------------------

1. Open test.http
2. Replace YOUR_JWT_TOKEN_HERE with a real token
3. Click "Send Request" to test the endpoints

Logging
-------

Each request is logged in:

- SQLite database (math.db)
- Terminal output using simulated Kafka logger

Example log:

    [Kafka Log] User: player1, Operation: fib, Result: 21

Monitoring
----------

Visit:

    http://localhost:8000/metrics

This returns Prometheus metrics including request counts, latency, and operation breakdowns.

Caching
-------

- Fibonacci and factorial use functools.lru_cache
- Cache size is 128 entries

Extensibility
-------------

- Add new math functions in services/math_service.py
- Expand routes in api/routes.py
- Add real Kafka, Redis, PostgreSQL with Docker Compose

Future Improvements
-------------------

- Redis cache
- Real Kafka streaming
- OAuth2 authentication
- CLI or web frontend

License
-------

MIT License