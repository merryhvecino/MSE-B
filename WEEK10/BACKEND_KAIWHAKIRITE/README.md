# Kaiwhakarite Rawa Māori – Inventory Management System Backend

This is the backend server for the Kaiwhakarite Rawa Māori inventory management system, designed specifically for Māori small businesses.

## Features

- User Authentication (Rangatira/Kaimahi roles)
- Product Management with barcode support
- Stock Transaction tracking
- Supplier Directory
- Low stock alerts
- Bilingual support
- RESTful API endpoints

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- SQLite (included with Python)

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd BACKEND_KAIWHAKIRITE
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
- Windows:
```bash
.\venv\Scripts\activate
```
- Unix/MacOS:
```bash
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Create a `.env` file in the root directory with the following content:
```
SECRET_KEY=your-super-secret-key-here
FLASK_ENV=development
DATABASE_URL=sqlite:///kaiwhakarite.db
```

6. Initialize the database:
```bash
python run.py
```

## Running the Server

To start the development server:
```bash
python run.py
```

The server will start at `http://localhost:5000`

## API Endpoints

### Authentication
- POST /api/auth/register - Register new user
- POST /api/auth/login - User login
- GET /api/auth/me - Get current user

### Products
- GET /api/products - List all products
- POST /api/products - Create new product
- PUT /api/products/:id - Update product
- DELETE /api/products/:id - Delete product
- POST /api/products/:id/restore - Restore deleted product
- GET /api/products/barcode/:barcode - Get product by barcode

### Suppliers
- GET /api/suppliers - List all suppliers
- POST /api/suppliers - Create new supplier
- PUT /api/suppliers/:id - Update supplier
- DELETE /api/suppliers/:id - Delete supplier

### Stock Transactions
- GET /api/transactions - List transactions
- POST /api/transactions - Create transaction
- GET /api/transactions/low-stock - Get low stock alerts

## Security

- JWT-based authentication
- Password hashing using bcrypt
- Role-based access control
- CORS protection

## Deployment

The application can be deployed to any hosting platform that supports Python applications. Some recommended options:

- Render
- Railway
- Heroku
- DigitalOcean

## License

[MIT License](LICENSE)
