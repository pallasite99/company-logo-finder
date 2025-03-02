# Company Logo Retrieval System

## Overview
This project is a **Company Logo Retrieval System** that allows users to input a list of company names and retrieve their corresponding logos. The system uses a combination of **Clearbit's API** and a **pre-populated SQLite database** containing **50,000+ company logos**.

## Features
- **Automated Logo Retrieval:** Fetches logos dynamically via **Clearbit API**.
- **Massive Company Dataset:** Preloads logos for **50,000+ global companies**.
- **Search Interface:** Users can enter company names and retrieve logos via an easy-to-use **frontend UI**.
- **Database Caching:** Stores logos locally in an **SQLite database** for fast retrieval.
- **REST API:** Provides a simple API endpoint to fetch logos programmatically.

## Technologies Used
- **Backend:** Python, Flask, Flask-CORS, SQLite, Requests
- **Frontend:** HTML, JavaScript (Fetch API), CSS
- **Database:** SQLite (Local Storage)

## Installation & Setup
### Prerequisites
- Python 3.6+
- pip (Python Package Manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/pallasite99/company-logo-finder.git
cd company-logo-retrieval
```

### Step 2: Install Dependencies
```bash
pip install flask flask-cors requests
```

### Step 3: Run the Backend Server
```bash
python index.py  # Ensure script filename is correct
```

### Step 4: Run the Frontend
Simply open `index.html` in a browser.

## API Usage
### Endpoint: `/get_logos`
- **Method:** `POST`
- **Request Body:**
```json
{
  "companies": ["Google", "Amazon", "Microsoft"]
}
```
- **Response:**
```json
{
  "Google": "https://logo.clearbit.com/google.com",
  "Amazon": "https://logo.clearbit.com/amazon.com",
  "Microsoft": "https://logo.clearbit.com/microsoft.com"
}
```

## Sample UI output (can be made prettier)

![image](https://github.com/user-attachments/assets/36762b8a-a94f-41e5-8276-3171dbe4994d)

## Deployment Options
- Deploy the **backend** to **Heroku, AWS, or DigitalOcean**.
- Host the **frontend** on **Netlify or Vercel**.

## Future Enhancements
- Expand company dataset beyond 50,000 entries.
- Add alternative API sources for improved coverage.
- Implement **caching mechanisms** for optimized performance.

## Contact
For questions or support, please reach out at **salil.apte99@gmail.com**.

