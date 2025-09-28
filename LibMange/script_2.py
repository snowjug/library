# Create a simple batch file for Windows users to compile and run the application
batch_content = '''@echo off
echo ===================================
echo Library Management System - Setup
echo ===================================

REM Check if Java is installed
java -version > nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Java is not installed or not in PATH!
    echo Please install Java JDK 8 or later.
    pause
    exit /b 1
)

echo Java is installed. Proceeding with compilation...

REM Create directories if they don't exist
if not exist "src\\com\\library\\system" mkdir "src\\com\\library\\system"
if not exist "build" mkdir "build"

REM Check if SQLite JDBC JAR exists
if not exist "sqlite-jdbc-*.jar" (
    echo ERROR: SQLite JDBC JAR file not found!
    echo Please download sqlite-jdbc-3.50.3.0.jar and place it in this directory.
    echo Download from: https://repo1.maven.org/maven2/org/xerial/sqlite-jdbc/3.50.3.0/sqlite-jdbc-3.50.3.0.jar
    pause
    exit /b 1
)

REM Compile the Java files
echo Compiling Java files...
javac -cp "sqlite-jdbc-*.jar" -d build src\\com\\library\\system\\*.java

if %errorlevel% neq 0 (
    echo ERROR: Compilation failed!
    pause
    exit /b 1
)

echo Compilation successful!
echo.

REM Run the application
echo Starting Library Management System...
echo.
java -cp "build;sqlite-jdbc-*.jar" com.library.system.LibraryManagement

pause'''

# Create batch file for Windows
with open("run-library-system.bat", "w", encoding="utf-8") as f:
    f.write(batch_content)

# Create shell script for Unix/Linux/Mac
shell_content = '''#!/bin/bash

echo "==================================="
echo "Library Management System - Setup"
echo "==================================="

# Check if Java is installed
if ! command -v java &> /dev/null; then
    echo "ERROR: Java is not installed or not in PATH!"
    echo "Please install Java JDK 8 or later."
    exit 1
fi

echo "Java is installed. Proceeding with compilation..."

# Create directories if they don't exist
mkdir -p src/com/library/system
mkdir -p build

# Check if SQLite JDBC JAR exists
if ! ls sqlite-jdbc-*.jar 1> /dev/null 2>&1; then
    echo "ERROR: SQLite JDBC JAR file not found!"
    echo "Please download sqlite-jdbc-3.50.3.0.jar and place it in this directory."
    echo "Download from: https://repo1.maven.org/maven2/org/xerial/sqlite-jdbc/3.50.3.0/sqlite-jdbc-3.50.3.0.jar"
    exit 1
fi

# Compile the Java files
echo "Compiling Java files..."
javac -cp "sqlite-jdbc-*.jar" -d build src/com/library/system/*.java

if [ $? -ne 0 ]; then
    echo "ERROR: Compilation failed!"
    exit 1
fi

echo "Compilation successful!"
echo ""

# Run the application
echo "Starting Library Management System..."
echo ""
java -cp "build:sqlite-jdbc-*.jar" com.library.system.LibraryManagement'''

# Create shell script for Unix/Linux/Mac
with open("run-library-system.sh", "w", encoding="utf-8") as f:
    f.write(shell_content)

print("Batch and shell scripts created successfully!")
print("- run-library-system.bat (for Windows)")
print("- run-library-system.sh (for Unix/Linux/Mac)")

# Create a sample data file
sample_data = '''-- Sample Data for Library Management System
-- You can use these INSERT statements to populate your database with test data

-- Note: The database tables are created automatically when you run the application
-- You can execute these SQL statements using any SQLite browser/tool after the database is created

-- Sample Books Data
INSERT OR IGNORE INTO books (title, author, genre, publication_date, isbn, available) VALUES 
('The Java Programming Language', 'Ken Arnold', 'Technology', '2020-01-15', '978-0134685991', 1),
('Clean Code', 'Robert C. Martin', 'Technology', '2008-08-01', '978-0132350884', 1),
('Design Patterns', 'Gang of Four', 'Technology', '1994-10-31', '978-0201633610', 1),
('The Great Gatsby', 'F. Scott Fitzgerald', 'Fiction', '1925-04-10', '978-0743273565', 1),
('To Kill a Mockingbird', 'Harper Lee', 'Fiction', '1960-07-11', '978-0061120084', 0),
('1984', 'George Orwell', 'Fiction', '1949-06-08', '978-0451524935', 1),
('Database System Concepts', 'Abraham Silberschatz', 'Technology', '2019-02-14', '978-0078022159', 1),
('Introduction to Algorithms', 'Thomas H. Cormen', 'Technology', '2009-07-31', '978-0262033848', 1);

-- Sample Borrowers Data
INSERT OR IGNORE INTO borrowers (name, email, phone, address) VALUES 
('John Doe', 'john.doe@email.com', '+1-555-123-4567', '123 Main Street, Bengaluru, Karnataka'),
('Jane Smith', 'jane.smith@email.com', '+1-555-987-6543', '456 Oak Avenue, Mumbai, Maharashtra'),
('Alice Johnson', 'alice.johnson@email.com', '+91-9876543210', '789 Pine Road, Delhi, India'),
('Bob Brown', 'bob.brown@email.com', '+91-8765432109', '321 Elm Street, Chennai, Tamil Nadu'),
('Carol White', 'carol.white@email.com', '+1-555-555-5555', '654 Maple Lane, Hyderabad, Telangana');

-- Sample Checkout Data
INSERT OR IGNORE INTO checkouts (book_id, borrower_id, checkout_date, due_date, return_date) VALUES 
(1, 1, '2024-01-15', '2024-02-15', NULL),
(2, 2, '2024-01-20', '2024-02-20', '2024-02-18'),
(3, 3, '2024-01-25', '2024-02-25', NULL),
(5, 4, '2024-01-10', '2024-02-10', NULL),
(4, 5, '2024-01-05', '2024-02-05', '2024-02-03');

-- Additional INSERT statements for more test data
INSERT OR IGNORE INTO books (title, author, genre, publication_date, isbn, available) VALUES 
('Head First Java', 'Kathy Sierra', 'Technology', '2005-02-01', '978-0596009205', 1),
('Effective Java', 'Joshua Bloch', 'Technology', '2017-12-27', '978-0134685991', 1),
('Pride and Prejudice', 'Jane Austen', 'Fiction', '1813-01-28', '978-0141439518', 1),
('The Catcher in the Rye', 'J.D. Salinger', 'Fiction', '1951-07-16', '978-0316769174', 1);'''

# Save sample data
with open("sample_data.sql", "w", encoding="utf-8") as f:
    f.write(sample_data)

print("Sample data file created: sample_data.sql")

# Create project directory structure instructions
project_structure = '''Library Management System - Project Directory Structure

After setting up your Eclipse project, your directory structure should look like this:

LibraryManagementSystem/
│
├── src/
│   └── com/
│       └── library/
│           └── system/
│               ├── Database.java
│               └── LibraryManagement.java
│
├── build/ (created automatically)
│   └── com/
│       └── library/
│           └── system/
│               ├── Database.class
│               └── LibraryManagement.class
│
├── Referenced Libraries/ (in Eclipse)
│   └── sqlite-jdbc-3.50.3.0.jar
│
├── sqlite-jdbc-3.50.3.0.jar (downloaded separately)
├── library.db (created automatically when you first run the app)
├── run-library-system.bat (Windows script)
├── run-library-system.sh (Unix/Linux/Mac script)
├── sample_data.sql (sample data for testing)
├── setup-guide.md (comprehensive setup guide)
└── README.md (project documentation)

Quick Start Steps:
1. Create Eclipse project named "LibraryManagementSystem"
2. Create package "com.library.system"
3. Download SQLite JDBC JAR file
4. Add JAR to project build path
5. Copy Database.java and LibraryManagement.java to the package
6. Run LibraryManagement.java as Java Application

Database Location:
- The SQLite database file (library.db) will be created in the root directory of your Eclipse project
- You can view/edit this database using SQLite browser tools like DB Browser for SQLite

For detailed setup instructions, see setup-guide.md'''

with open("project-structure.txt", "w", encoding="utf-8") as f:
    f.write(project_structure)

print("Project structure guide created: project-structure.txt")
print("\\nAll files have been created successfully!")
print("\\nFiles created:")
print("1. Database.java - Database operations class")
print("2. LibraryManagement.java - Main GUI application")  
print("3. setup-guide.md - Comprehensive setup instructions")
print("4. run-library-system.bat - Windows batch script")
print("5. run-library-system.sh - Unix/Linux/Mac shell script")
print("6. sample_data.sql - Sample data for testing")
print("7. project-structure.txt - Project organization guide")