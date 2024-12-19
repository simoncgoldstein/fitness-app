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
