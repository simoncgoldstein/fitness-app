# **Fitness Manager App**

## Overview

The **Fitness Manager App** is a web application built using **Django** that allows fitness enthusiasts and trainers to manage their clients, workouts, and fitness plans. The app provides two types of user accounts: **Common Users** and **PMA Administrators**. Each user type has unique permissions and views, enabling administrators to manage the system efficiently, while users can interact with their fitness schedules and trainers.

### Key Features
- **Google OAuth** login for secure user authentication.
- **Common Users** can log in and view their assigned fitness plans.
- **PMA Administrators** have full control over user management, including adding/removing users, linking clients to coaches, and more.
- Separate views and permissions for different user types (**Common Users** and **Admins**).

---

## **Installation Instructions**

To set up and run the project locally, follow these steps:

### Prerequisites
- **Python 3.x**
- **Django** (specified in `requirements.txt`)
- A virtual environment for managing dependencies

### Step-by-Step Installation:

1. **Clone the repository:**

2. **Create and activate a virtual environment:**

   - On Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

   - On macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install dependencies from `requirements.txt`:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the app:**

   Open your browser and go to `http://locahost:8000/` to view the app.

---

## **Team Roles**

- **Youssef Cherrat** (jja3em): Scrum Master
- **Simon**: DevOps Manager
- **Raja**: Testing Manager

---

## **How It Works**

### Common Users:
Users with a Google account can log in, view their fitness schedule, and interact with their assigned coach. The app ensures that users without admin permissions can only access their own data and workout plans.

### PMA Administrators:
Admins have additional controls such as adding/removing users and managing the assignment of clients to coaches. When logged in as an admin, the app provides different views to easily manage the backend of the system.

Upon login, both user types will see their names and account types printed on the screen, verifying their credentials and access level.