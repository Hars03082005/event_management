# Event Management System

A robust event management web application built with FastAPI, featuring user authentication, event registration, and comprehensive performance testing with Locust.

## 📋 Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Performance Testing](#performance-testing)
- [API Endpoints](#api-endpoints)
- [Database Schema](#database-schema)

## ✨ Features

- **User Authentication**: Secure user registration and login system
- **Event Management**: Browse available events with fees and details
- **Event Registration**: Users can register for multiple events
- **My Events**: View all registered events for a user
- **Checkout System**: Integrated checkout functionality
- **Error Handling**: Global exception handler with user-friendly error pages
- **Performance Testing**: Comprehensive Locust test suites for load testing

## 🛠 Tech Stack

- **Backend Framework**: FastAPI
- **Template Engine**: Jinja2
- **Database**: SQLite3
- **Server**: Uvicorn
- **Load Testing**: Locust
- **Language**: Python 3.x

## 📁 Project Structure

```
CC_Lab-2/
├── main.py                     # Main FastAPI application
├── database.py                 # Database connection handler
├── insert_events.py            # Script to populate events
├── requirements.txt            # Python dependencies
├── templates/                  # HTML templates
│   ├── base.html
│   ├── checkout.html
│   ├── error.html
│   ├── events.html
│   ├── login.html
│   ├── my_events.html
│   └── register.html
├── checkout/                   # Checkout module
│   └── __init__.py
└── locust/                     # Load testing scripts
    ├── checkout_locustfile.py
    ├── events_locustfile.py
    ├── myevents_locustfile.py
    └── journey_locustfile.py
```

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/Hars03082005/event_management.git
cd event_management
```

2. **Create a virtual environment** (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

## 🚀 Usage

### Running the Application

1. **Start the FastAPI server**
```bash
python -m uvicorn main:app --reload
```

2. **Access the application**
   - Open your browser and navigate to: `http://localhost:8000`
   - API documentation (Swagger UI): `http://localhost:8000/docs`

### Initial Setup

1. **Populate events** (if needed)
```bash
python insert_events.py
```

2. **Register a new user**
   - Navigate to `/register`
   - Create your account

3. **Login**
   - Use your credentials at `/login`

4. **Browse and register for events**
   - View available events
   - Register for events of your choice
   - Check your registrations in "My Events"

## 🧪 Performance Testing

The project includes comprehensive Locust test suites for load testing:

### Run Individual Tests

1. **Events Page Test**
```bash
locust -f locust/events_locustfile.py
```

2. **My Events Page Test**
```bash
locust -f locust/myevents_locustfile.py
```

3. **Checkout Test**
```bash
locust -f locust/checkout_locustfile.py
```

4. **Full User Journey Test**
```bash
locust -f locust/journey_locustfile.py
```

### Access Locust Web UI
After starting Locust, open your browser to `http://localhost:8089` to:
- Configure number of users
- Set spawn rate
- Monitor real-time performance metrics
- View response time graphs

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/register` | Display registration page |
| POST | `/register` | Create new user account |
| GET | `/login` | Display login page |
| POST | `/login` | Authenticate user |
| GET | `/events?user={username}` | View all available events |
| GET | `/register_event/{event_id}?user={username}` | Register for an event |
| GET | `/my-events?user={username}` | View user's registered events |
| GET | `/checkout` | Display checkout page |

## 🗄 Database Schema

### Users Table
```sql
CREATE TABLE users (
    username TEXT PRIMARY KEY,
    password TEXT
)
```

### Events Table
```sql
CREATE TABLE events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    fee INTEGER
)
```

### Registrations Table
```sql
CREATE TABLE registrations (
    username TEXT,
    event_id INTEGER
)
```

## 🔧 Configuration

- **SRN**: PES1UG23CS237 (configured in main.py)
- **Database**: SQLite (`fest.db`)
- **Templates Directory**: `templates/`

## 🎯 Performance Considerations

The application includes intentional computational tasks in certain endpoints:
- `/events`: Includes computation loop (3M iterations)
- `/my-events`: Includes computation loop (1.5M iterations)

These are designed for performance testing and can be removed for production use.

## 🛡 Error Handling

- Global exception handler catches all unhandled errors
- User-friendly error pages maintain UI consistency
- Preserves user context during error states

## 📝 Development Notes

- Database is automatically initialized on application startup
- Tables are created if they don't exist
- Uses SQLite Row factory for dictionary-like access to results

## 👤 Author

**Harshavardhana**
- SRN: PES1UG23CS237
- GitHub: [@Hars03082005](https://github.com/Hars03082005)

## 📄 License

This project is developed for educational purposes.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

---
**Note**: This application uses SQLite for simplicity. For production environments, consider using PostgreSQL or MySQL with proper security measures including password hashing and session management.
