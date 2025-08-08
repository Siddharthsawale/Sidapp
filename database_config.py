import pymssql
from datetime import datetime

# Database Configuration
DB_CONFIG = {
    'server': 'nexiqon-dbserver.database.windows.net',
    'database': 'nexiqon25',
    'user': 'nexiqon2025',
    'password': '@dmin2025',
    'port': 1433
}

def get_db_connection():
    """Create and return a database connection"""
    try:
        connection = pymssql.connect(**DB_CONFIG)
        return connection
    except Exception as e:
        print(f"Error connecting to SQL Server Database: {e}")
        return None

def test_connection():
    """Test the database connection"""
    try:
        connection = get_db_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT @@VERSION")
            version = cursor.fetchone()
            cursor.close()
            connection.close()
            print(f"Database connection successful. SQL Server version: {version[0]}")
            return True
        return False
    except Exception as e:
        print(f"Database connection failed: {e}")
        return False

def create_tables():
    """Create all necessary database tables"""
    try:
        connection = get_db_connection()
        if not connection:
            return False
    
        cursor = connection.cursor()
        
        # Users table
        cursor.execute("""
            IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[users]') AND type in (N'U'))
            BEGIN
                CREATE TABLE users (
                    id INT IDENTITY(1,1) PRIMARY KEY,
                    email NVARCHAR(255) UNIQUE NOT NULL,
                    password NVARCHAR(255) NOT NULL,
                    role NVARCHAR(100) DEFAULT 'employee',
                    created_at DATETIME DEFAULT GETDATE()
                )
            END
        """)
        
        # Employees table
        cursor.execute("""
            IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[employees]') AND type in (N'U'))
            BEGIN
                CREATE TABLE employees (
                    id INT IDENTITY(1,1) PRIMARY KEY,
                    user_id INT,
                    full_name NVARCHAR(255) NOT NULL,
                    email NVARCHAR(255) UNIQUE NOT NULL,
                    phone NVARCHAR(20),
                    department NVARCHAR(100),
                    position NVARCHAR(100),
                    hire_date DATE,
                    manager NVARCHAR(255),
                    location NVARCHAR(100),
                    salary_band NVARCHAR(50),
                    employment_type NVARCHAR(50),
                    created_at DATETIME DEFAULT GETDATE()
                )
            END
        """)
        
        # Tickets table
        cursor.execute("""
            IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[tickets]') AND type in (N'U'))
            BEGIN
                CREATE TABLE tickets (
                    id INT IDENTITY(1,1) PRIMARY KEY,
                    title NVARCHAR(255) NOT NULL,
                    description NVARCHAR(MAX),
                    priority NVARCHAR(50) DEFAULT 'medium',
                    status NVARCHAR(50) DEFAULT 'open',
                    user_email NVARCHAR(255) NOT NULL,
                    assigned_to NVARCHAR(255),
                    created_at DATETIME DEFAULT GETDATE(),
                    updated_at DATETIME DEFAULT GETDATE()
                )
            END
        """)
        
        # Ticket Comments table
        cursor.execute("""
            IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[ticket_comments]') AND type in (N'U'))
            BEGIN
                CREATE TABLE ticket_comments (
                    id INT IDENTITY(1,1) PRIMARY KEY,
                    ticket_id INT,
                    comment NVARCHAR(MAX),
                    admin_name NVARCHAR(255),
                    created_at DATETIME DEFAULT GETDATE()
                )
            END
        """)
        
        # Timeoff Requests table
        cursor.execute("""
            IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[timeoff_requests]') AND type in (N'U'))
            BEGIN
                CREATE TABLE timeoff_requests (
                    id INT IDENTITY(1,1) PRIMARY KEY,
                    employee_name NVARCHAR(255) NOT NULL,
                    start_date DATE NOT NULL,
                    end_date DATE NOT NULL,
                    reason NVARCHAR(MAX),
                    status NVARCHAR(50) DEFAULT 'pending',
                    submitted_at DATETIME DEFAULT GETDATE()
                )
            END
        """)
        
        # Leave Requests table
        cursor.execute("""
            IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[leave_requests]') AND type in (N'U'))
            BEGIN
                CREATE TABLE leave_requests (
                    id INT IDENTITY(1,1) PRIMARY KEY,
                    employee_id INT,
                    employee_name NVARCHAR(255) NOT NULL,
                    leave_type NVARCHAR(100),
                    start_date DATE NOT NULL,
                    end_date DATE NOT NULL,
                    reason NVARCHAR(MAX),
                    status NVARCHAR(50) DEFAULT 'pending',
                    approved_by NVARCHAR(255),
                    approved_at DATETIME,
                    submitted_at DATETIME DEFAULT GETDATE()
                )
            END
        """)
        
        # Feedback table
        cursor.execute("""
            IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[feedback]') AND type in (N'U'))
            BEGIN
                CREATE TABLE feedback (
                    id INT IDENTITY(1,1) PRIMARY KEY,
                    type NVARCHAR(100),
                    text NVARCHAR(MAX),
                    department NVARCHAR(100),
                    priority NVARCHAR(50),
                    status NVARCHAR(50) DEFAULT 'pending',
                    submitted_at DATETIME DEFAULT GETDATE()
                )
            END
        """)
        
        # Feedback Comments table
        cursor.execute("""
            IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[feedback_comments]') AND type in (N'U'))
            BEGIN
                CREATE TABLE feedback_comments (
                    id INT IDENTITY(1,1) PRIMARY KEY,
                    feedback_id INT,
                    comment NVARCHAR(MAX),
                    admin_name NVARCHAR(255),
                    created_at DATETIME DEFAULT GETDATE()
                )
            END
        """)
        
        # Service Requests table
        cursor.execute("""
            IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[service_requests]') AND type in (N'U'))
            BEGIN
                CREATE TABLE service_requests (
                    id INT IDENTITY(1,1) PRIMARY KEY,
                    user_email NVARCHAR(255) NOT NULL,
                    request_type NVARCHAR(100) NOT NULL,
                    subject NVARCHAR(255),
                    description NVARCHAR(MAX),
                    priority NVARCHAR(50) DEFAULT 'medium',
                    status NVARCHAR(50) DEFAULT 'pending',
                    assigned_to NVARCHAR(255),
                    created_at DATETIME DEFAULT GETDATE(),
                    updated_at DATETIME DEFAULT GETDATE()
                )
            END
        """)
        
        # Service Request Comments table
        cursor.execute("""
            IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[service_request_comments]') AND type in (N'U'))
            BEGIN
                CREATE TABLE service_request_comments (
                    id INT IDENTITY(1,1) PRIMARY KEY,
                    request_id INT,
                    comment NVARCHAR(MAX),
                    admin_name NVARCHAR(255),
                    created_at DATETIME DEFAULT GETDATE()
                )
            END
        """)
        
        # Jobs table
        cursor.execute("""
            IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[jobs]') AND type in (N'U'))
            BEGIN
                CREATE TABLE jobs (
                    id INT IDENTITY(1,1) PRIMARY KEY,
                    title NVARCHAR(255) NOT NULL,
                    department NVARCHAR(100),
                    location NVARCHAR(100),
                    description NVARCHAR(MAX),
                    requirements NVARCHAR(MAX),
                    salary_range NVARCHAR(100),
                    status NVARCHAR(50) DEFAULT 'open',
                    created_at DATETIME DEFAULT GETDATE(),
                    updated_at DATETIME DEFAULT GETDATE()
                )
            END
        """)
        
        # Job Applications table
        cursor.execute("""
            IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[job_applications]') AND type in (N'U'))
            BEGIN
                CREATE TABLE job_applications (
                    id INT IDENTITY(1,1) PRIMARY KEY,
                    job_id INT,
                    user_email NVARCHAR(255) NOT NULL,
                    applicant_name NVARCHAR(255),
                    applicant_email NVARCHAR(255),
                    resume_path NVARCHAR(MAX),
                    cover_letter NVARCHAR(MAX),
                    status NVARCHAR(50) DEFAULT 'submitted',
                    reviewed_by NVARCHAR(255),
                    reviewed_at DATETIME,
                    applied_at DATETIME DEFAULT GETDATE()
                )
            END
        """)
        
        # Internal Jobs table
        cursor.execute("""
            IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[internal_jobs]') AND type in (N'U'))
            BEGIN
                CREATE TABLE internal_jobs (
                    id INT IDENTITY(1,1) PRIMARY KEY,
                    title NVARCHAR(255) NOT NULL,
                    department NVARCHAR(100),
                    location NVARCHAR(100),
                    job_type NVARCHAR(100),
                    description NVARCHAR(MAX),
                    requirements NVARCHAR(MAX),
                    salary_range NVARCHAR(100),
                    posted_date DATE,
                    deadline_date DATE,
                    status NVARCHAR(50) DEFAULT 'active',
                    created_at DATETIME DEFAULT GETDATE()
                )
            END
        """)
        
        # Internal Job Applications table
        cursor.execute("""
            IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[internal_job_applications]') AND type in (N'U'))
            BEGIN
                CREATE TABLE internal_job_applications (
                    id INT IDENTITY(1,1) PRIMARY KEY,
                    job_id INT,
                    user_email NVARCHAR(255) NOT NULL,
                    resume_path NVARCHAR(MAX),
                    cover_letter NVARCHAR(MAX),
                    status NVARCHAR(50) DEFAULT 'pending',
                    applied_date DATETIME DEFAULT GETDATE()
                )
            END
        """)
        
        # Timesheets table
        cursor.execute("""
            IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[timesheets]') AND type in (N'U'))
            BEGIN
                CREATE TABLE timesheets (
                    id INT IDENTITY(1,1) PRIMARY KEY,
                    user_id INT,
                    date DATE NOT NULL,
                    start_time TIME,
                    end_time TIME,
                    hours_worked DECIMAL(5,2),
                    description NVARCHAR(MAX),
                    status NVARCHAR(50) DEFAULT 'pending',
                    approved_by NVARCHAR(255),
                    approved_at DATETIME,
                    created_at DATETIME DEFAULT GETDATE()
                )
            END
        """)
        
        # Timesheet Comments table
        cursor.execute("""
            IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[timesheet_comments]') AND type in (N'U'))
            BEGIN
                CREATE TABLE timesheet_comments (
                    id INT IDENTITY(1,1) PRIMARY KEY,
                    timesheet_id INT,
                    comment NVARCHAR(MAX),
                    admin_name NVARCHAR(255),
                    created_at DATETIME DEFAULT GETDATE()
                )
            END
        """)
        
        # Badges table
        cursor.execute("""
            IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[badges]') AND type in (N'U'))
            BEGIN
                CREATE TABLE badges (
                    id INT IDENTITY(1,1) PRIMARY KEY,
                    name NVARCHAR(255) NOT NULL,
                    description NVARCHAR(MAX),
                    icon NVARCHAR(255),
                    category NVARCHAR(100),
                    created_at DATETIME DEFAULT GETDATE()
                )
            END
        """)
        
        # User Badges table
        cursor.execute("""
            IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[user_badges]') AND type in (N'U'))
            BEGIN
                CREATE TABLE user_badges (
                    id INT IDENTITY(1,1) PRIMARY KEY,
                    user_id INT,
                    badge_id INT,
                    awarded_by NVARCHAR(255),
                    reason NVARCHAR(MAX),
                    awarded_at DATETIME DEFAULT GETDATE()
                )
            END
        """)
        
        # Skills Assessments table
        cursor.execute("""
            IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[skills_assessments]') AND type in (N'U'))
            BEGIN
                CREATE TABLE skills_assessments (
                    id INT IDENTITY(1,1) PRIMARY KEY,
                    user_email NVARCHAR(255) NOT NULL,
                    test_type NVARCHAR(100),
                    score INT,
                    total_questions INT,
                    answers NVARCHAR(MAX),
                    completed_at DATETIME DEFAULT GETDATE()
                )
            END
        """)
        
        # Learning Roadmaps table
        cursor.execute("""
            IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[learning_roadmaps]') AND type in (N'U'))
            BEGIN
                CREATE TABLE learning_roadmaps (
                    id INT IDENTITY(1,1) PRIMARY KEY,
                    user_email NVARCHAR(255) NOT NULL,
                    assessment_id INT,
                    improvement_areas NVARCHAR(MAX),
                    recommended_path NVARCHAR(MAX),
                    created_at DATETIME DEFAULT GETDATE()
                )
            END
        """)
        
        # Courses table
        cursor.execute("""
            IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[courses]') AND type in (N'U'))
            BEGIN
                CREATE TABLE courses (
                    id INT IDENTITY(1,1) PRIMARY KEY,
                    title NVARCHAR(255) NOT NULL,
                    description NVARCHAR(MAX),
                    content NVARCHAR(MAX),
                    questions NVARCHAR(MAX),
                    passing_score INT DEFAULT 70,
                    badge NVARCHAR(255),
                    category NVARCHAR(100),
                    duration INT,
                    created_at DATETIME DEFAULT GETDATE()
                )
            END
        """)
        
        # User Courses table
        cursor.execute("""
            IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[user_courses]') AND type in (N'U'))
            BEGIN
                CREATE TABLE user_courses (
                    id INT IDENTITY(1,1) PRIMARY KEY,
                    user_email NVARCHAR(255) NOT NULL,
                    course_id INT,
                    progress INT DEFAULT 0,
                    status NVARCHAR(50) DEFAULT 'enrolled',
                    created_at DATETIME DEFAULT GETDATE(),
                    completed_at DATETIME
                )
            END
        """)
        
        # Quiz Results table
        cursor.execute("""
            IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[quiz_results]') AND type in (N'U'))
            BEGIN
                CREATE TABLE quiz_results (
                    id INT IDENTITY(1,1) PRIMARY KEY,
                    user_email NVARCHAR(255) NOT NULL,
                    course_id INT,
                    score INT,
                    total_questions INT,
                    percentage DECIMAL(5,2),
                    passed BIT,
                    completed_at DATETIME DEFAULT GETDATE()
                )
            END
        """)
        
        # Notifications table
        cursor.execute("""
            IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[notifications]') AND type in (N'U'))
            BEGIN
                CREATE TABLE notifications (
                    id INT IDENTITY(1,1) PRIMARY KEY,
                    user_email NVARCHAR(255) NOT NULL,
                    title NVARCHAR(255) NOT NULL,
                    message NVARCHAR(MAX),
                    type NVARCHAR(50),
                    read_status BIT DEFAULT 0,
                    created_at DATETIME DEFAULT GETDATE()
                )
            END
        """)
        
        connection.commit()
        cursor.close()
        connection.close()
        return True
        
    except Exception as e:
        print(f"Error creating tables: {e}")
        return False

if __name__ == "__main__":
    # Test the connection
    if test_connection():
        print("Successfully connected to the database")
        # Create tables
        if create_tables():
            print("Successfully created/verified all tables")
        else:
            print("Error creating tables")
    else:
        print("Failed to connect to the database") 