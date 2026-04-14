# 🚀 CSCI2040 Lab Repo

A full-stack stock trading application with a React frontend and Flask backend.

---

# 📦 Prerequisites

Choose **ONE** setup method:

### 🟢 Option 1 (Recommended): Docker

* Install Docker Desktop

### 🟡 Option 2: Manual Setup

* Install:

  * Node.js
  * Python (3.x)

---

# 🐳 Run with Docker (Easiest)

### 1. Navigate to project

```
cd myapp
```

### 2. Start the app

```
docker-compose up --build
```

### 3. Open in browser

```
http://localhost:5173
```

### 4. Stop the app

```
CTRL + C
```

---

# 💻 Run Manually (Development Mode)

## 1. Navigate to project

```
cd myapp
```

---

## 2. Setup Frontend

```
npm install
```

---

## 3. Setup Backend

### Windows:

```
npm run setup-backend
```

### Mac/Linux:

```
npm run setup-backend-mac
```

---

## 4. Run the App

### Start Frontend

```
npm run dev
```

### Start Backend

#### Windows:

```
npm run start-backend
```

#### Mac/Linux:

```
npm run start-backend-unix
```

---

# 🧹 Cleanup (Windows Only)

```
npm run clean
```

---

# 🛠 Troubleshooting

### 🔁 Rebuild Docker

```
docker-compose down
docker-compose up --build
```

---

### ❌ API not working?

* Ensure backend is running
* If using Docker, verify API URL is:

```
http://backend:5000
```

---

### ❌ Port already in use?

Close other apps using:

* `5000` (backend)
* `5173` (frontend)

---

# 📁 Project Structure

```
myapp/
  backend/        # Flask API
  src/            # React frontend
  docker-compose.yml
```

---

# 💡 Notes

* Docker setup is recommended for easiest use
* Manual setup is better for development/debugging
* Environment variables may be required for API configuration

---

# 👨‍💻 Authors

PYMAB Team
