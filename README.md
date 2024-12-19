# **Fitness Manager App**

## **Overview**

The **Fitness Manager App** is a web application built using **Django** that allows fitness enthusiasts and trainers to manage their clients, workouts, and fitness plans. The app provides two types of user accounts: **Common Users** and **PMA Administrators**. Each user type has unique permissions and views, enabling administrators to manage the system efficiently, while users can interact with their fitness schedules and trainers.

### **Key Features**
- **Google OAuth** login for secure user authentication.
- **Common Users** can log in and view their assigned fitness plans.
- **PMA Administrators** have full control over user management, including adding/removing users, linking clients to coaches, and more.
- Separate views and permissions for different user types (**Common Users** and **Admins**).

---

## **Installation Instructions**

To set up and run the project locally, follow these steps:

### **Prerequisites**
- **Python 3.x**
- **Django** (specified in `requirements.txt`)
- A virtual environment for managing dependencies

### **Step-by-Step Installation**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/simoncgoldstein/fitness-app.git
   cd fitness-app
   ```

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
   Open your browser and go to `http://localhost:8000/` to view the app.

---

## **Team Roles**

- **Youssef Cherrat** (jja3em): Scrum Master
- **Simon Goldstein**: DevOps Manager  
  - Set up the project deployment pipeline using **GitHub Actions** and **Heroku** for automated deployment.
  - Configured the project to use **PostgreSQL** and **Amazon S3** for database and file storage.
  - Implemented role-based access control to define permissions for admins and users.
  - Created an **admin dashboard** for managing users, coaches, and fitness plans efficiently.
  - Handled static and media file management for the application.
- **Raja**: Testing Manager  

---

## **How It Works**

### **Common Users**
Users with a Google account can log in, view their fitness schedule, and interact with their assigned coach. The app ensures that users without admin permissions can only access their own data and workout plans.

### **PMA Administrators**
Admins have additional controls such as adding/removing users, managing client-coach assignments, and overseeing fitness plan uploads. When logged in as an admin, the app provides enhanced views for seamless management of the backend.

Upon login, both user types will see their names and account types displayed, verifying their credentials and access levels.

---

## **Your Role in the Project**
As the **DevOps Manager**, I took on key responsibilities to ensure smooth development and deployment of the Fitness Manager App. This included configuring a robust CI/CD pipeline, integrating third-party services, and optimizing the app's infrastructure for scalability and reliability. My contributions focused on making the development process efficient and the application user-friendly for both admins and end-users.
