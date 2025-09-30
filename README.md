# DevOps FastAPI Project

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-green.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)

A production-ready FastAPI application designed for experimenting with modern DevOps tools and practices. This project serves as a comprehensive learning and testing platform for DevOps methodologies in a Python environment, featuring authentication, database integration, API versioning, and containerization.

## 📺 Demo Video

**Project 4 Tutorial:** [Watch on YouTube](https://www.youtube.com/watch?v=03fnj4TSAwI)

## 🎯 Project Goals

* **DevOps Foundation**: Establish a robust base for testing and implementing DevOps practices
* **Tool Integration**: Seamlessly integrate various DevOps tools (Docker, Terraform, CI/CD)
* **Learning Platform**: Foster hands-on learning for DevOps within a Python/FastAPI environment
* **Best Practices**: Demonstrate modern software development and deployment patterns

## ✨ Features

### Core Functionality
- **RESTful API**: Built with FastAPI for high performance and automatic OpenAPI documentation
- **JWT Authentication**: Secure OAuth2 with JWT tokens for user authentication
- **CRUD Operations**: Complete Create, Read, Update operations for items resource
- **API Versioning**: Structured v1 API endpoints for backward compatibility
- **Database Integration**: PostgreSQL database with SQLAlchemy ORM
- **CORS Support**: Configured Cross-Origin Resource Sharing for frontend integration

### DevOps Features
- **Containerization**: Docker and Docker Compose configurations
- **Infrastructure as Code**: Terraform configuration for cloud deployment
- **Testing Suite**: Comprehensive pytest-based test coverage
- **Code Quality**: Integrated linting (flake8, pylint) and formatting (autopep8)
- **Environment Configuration**: Environment variable based configuration management

### API Endpoints

#### Authentication
- `POST /token` - Login with username/password to receive JWT access token
- `GET /users/me/` - Get current authenticated user profile

#### Items (Protected - Requires Authentication)
- `GET /items/` - List items with pagination (skip, limit parameters)
- `POST /items/` - Create a new item
- `PATCH /items/{id}` - Update an existing item

#### Documentation
- `GET /docs` - Interactive Swagger UI API documentation (auto-generated)
- `GET /redoc` - ReDoc API documentation (auto-generated)

## 🏗️ Project Structure

```
api-python-project-devops-fast-api21/
├── app/
│   ├── config/          # Configuration files (database, settings)
│   ├── models/          # Database models and Pydantic schemas
│   ├── repositories/    # Data access layer (repository pattern)
│   ├── routers/         # API route handlers
│   │   └── v1/          # Version 1 API endpoints
│   ├── security/        # Security utilities
│   └── services/        # Business logic layer
├── tests/               # Test suite
│   ├── test_auth.py     # Authentication tests
│   └── test_items.py    # Items endpoint tests
├── main.py              # Application entry point
├── call_db.py           # Database connection utilities
├── Dockerfile           # Docker image configuration
├── docker-compose.yml   # Multi-container Docker setup
├── main.tf              # Terraform infrastructure configuration
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

## 🛠️ Technology Stack

### Core Framework
- **FastAPI** (0.109.0) - Modern, fast web framework for building APIs
- **Uvicorn** (0.25.0) - ASGI server for running FastAPI
- **Pydantic** (2.5.3) - Data validation using Python type annotations

### Database
- **SQLAlchemy** (2.0.25) - SQL toolkit and ORM
- **PostgreSQL** - Primary database (via psycopg2-binary)

### Authentication & Security
- **python-jose** (3.3.0) - JWT token creation and validation
- **passlib** (1.7.4) & **bcrypt** (4.1.2) - Password hashing
- **cryptography** (41.0.7) - Cryptographic recipes

### Development & Testing
- **pytest** (7.4.4) - Testing framework
- **pytest-html** (4.1.1) - HTML test reports
- **flake8** (7.0.0) - Code linting
- **pylint** (3.0.3) - Code analysis
- **autopep8** (2.0.4) - Code formatting

### DevOps Tools
- **Docker** & **Docker Compose** - Containerization
- **Terraform** - Infrastructure as Code
- **Gunicorn** (20.1.0) - WSGI HTTP server for production

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed:
- **Python 3.x** (3.9 or higher recommended)
- **pip** (Python package manager)
- **Docker** and **Docker Compose** (for containerized deployment)
- **PostgreSQL** (if running locally without Docker)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/maxiplux/api-python-project-devops-fast-api.git
   cd api-python-project-devops-fast-api21
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   
   Create a `.env` file or export the following variables:
   ```bash
   DB_USERNAME=postgres
   DB_PASSWORD=postgres
   DB_HOST=localhost
   DB_NAME=postgres
   SECRET_KEY=your-secret-key-here
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

### Running the Application

#### Option 1: Local Development

Run the FastAPI application with hot-reload:
```bash
uvicorn main:app --reload
```

The API will be available at:
- **API**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc

#### Option 2: Docker (Single Container)

Build and run the Docker container:
```bash
docker build -t fastapi-devops .
docker run -p 8000:8000 \
  -e DB_USERNAME=your_username \
  -e DB_PASSWORD=your_password \
  -e DB_HOST=your_host \
  -e DB_NAME=your_db_name \
  fastapi-devops
```

#### Option 3: Docker Compose (Recommended)

Run the complete stack with PostgreSQL database:
```bash
docker-compose up -d
```

The application will be available at:
- **API**: http://localhost:8080
- **PostgreSQL**: localhost:5432

To stop the services:
```bash
docker-compose down
```

## 🧪 Testing

Run the test suite using pytest:

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=app

# Run with HTML report
pytest --html=report.html

# Run specific test file
pytest tests/test_auth.py
```

## 🔐 Authentication Usage

1. **Obtain an access token:**
   ```bash
   curl -X POST "http://localhost:8000/token" \
     -H "Content-Type: application/json" \
     -d '{"username":"testuser","password":"testpass"}'
   ```

2. **Use the token for authenticated requests:**
   ```bash
   curl -X GET "http://localhost:8000/items/" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
   ```

## 🔧 Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `DB_USERNAME` | PostgreSQL username | postgres | Yes |
| `DB_PASSWORD` | PostgreSQL password | postgres | Yes |
| `DB_HOST` | Database host | localhost | Yes |
| `DB_NAME` | Database name | postgres | Yes |
| `SECRET_KEY` | JWT secret key | - | Yes |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token expiration time | 30 | No |

## 🐛 Troubleshooting

### Database Connection Issues
- Verify PostgreSQL is running: `docker-compose ps`
- Check environment variables are correctly set
- Ensure the database exists and user has proper permissions

### Port Already in Use
```bash
# Check what's using port 8000
netstat -ano | findstr :8000  # Windows
lsof -i :8000                  # Linux/Mac

# Kill the process or use a different port
uvicorn main:app --reload --port 8001
```

### Import Errors
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guidelines
- Write tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR

## 📝 License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.

## 📧 Contact

**Maintainer**: maxiplux  
**Email**: maxiplux@gmail.com  
**GitHub**: [@maxiplux](https://github.com/maxiplux)

---

**⭐ If you find this project helpful, please consider giving it a star!**
