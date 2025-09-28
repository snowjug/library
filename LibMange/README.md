# Library Management System
### A Complete Java Application using JDBC and Swing in Eclipse IDE

---

## 📋 Project Overview

This project is a **comprehensive Library Management System** built with Java using:
- **Eclipse IDE** for development
- **Java Swing** for GUI components  
- **JDBC** for database connectivity
- **SQLite** as the embedded database

### 🎯 Key Features
- ✅ **Book Management**: Add, view, search, and delete books
- ✅ **Borrower Management**: Manage library member information  
- ✅ **Checkout System**: Track book borrowing and returns
- ✅ **Search Functionality**: Find books by title or author
- ✅ **Data Persistence**: SQLite database with automatic table creation
- ✅ **User-friendly Interface**: Intuitive tabbed GUI design

---

## 🗂️ Project Structure

```
LibraryManagementSystem/
│
├── 📁 src/com/library/system/
│   ├── 📄 Database.java           # Database operations and JDBC connectivity
│   └── 📄 LibraryManagement.java  # Main GUI application with Swing components
│
├── 📁 Referenced Libraries/
│   └── 📦 sqlite-jdbc-3.50.3.0.jar
│
├── 🗃️ library.db                  # SQLite database (auto-created)
├── 📄 setup-guide.md              # Detailed setup instructions
├── 📄 sample_data.sql             # Test data for the database
├── ⚡ run-library-system.bat     # Windows execution script
├── ⚡ run-library-system.sh      # Unix/Linux/Mac execution script
└── 📄 README.md                   # This file
```

---

## 🚀 Quick Start Guide

### Prerequisites
- ☑️ Java JDK 8 or later installed
- ☑️ Eclipse IDE (any recent version)
- ☑️ Internet connection (to download SQLite JDBC driver)

### Step 1: Setup Eclipse Project
1. Open **Eclipse IDE**
2. Create **New Java Project**: `LibraryManagementSystem`
3. Create **Package**: `com.library.system`

### Step 2: Download Dependencies
1. Download **SQLite JDBC Driver**: 
   - Visit: https://mvnrepository.com/artifact/org.xerial/sqlite-jdbc
   - Download latest version (e.g., `sqlite-jdbc-3.50.3.0.jar`)

### Step 3: Configure Build Path
1. Right-click project → **Properties** → **Java Build Path** → **Libraries**
2. Click **Add External JARs** → Select downloaded SQLite JAR
3. Click **Apply and Close**

### Step 4: Add Source Files
1. Copy `Database.java` and `LibraryManagement.java` to your package
2. Ensure proper package declaration: `package com.library.system;`

### Step 5: Run Application
1. Right-click `LibraryManagement.java` → **Run As** → **Java Application**
2. The GUI window should appear with three tabs: Books, Borrowers, Checkouts

---

## 🔧 Application Components

### 1. Database.java
**Core database operations using JDBC:**
```java
// Key methods include:
- createDatabase()     // Creates SQLite database and tables
- addBook()           // Insert new book records
- addBorrower()       // Insert new borrower records  
- addCheckout()       // Track book borrowings
- delete()            // Remove records by ID
- refreshTables()     // Update GUI tables with fresh data
- searchBooks()       // Find books by title/author
```

### 2. LibraryManagement.java
**Swing GUI application with:**
```java
// Main components:
- JTabbedPane         // Three tabs for different functions
- JTable              // Display data in tabular format
- JTextField          // Input fields for data entry
- JButton             // Action buttons for operations
- Event Listeners     // Handle user interactions
```

### 3. Database Schema
**Three main tables:**

#### 📚 Books Table
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER PRIMARY KEY | Unique book identifier |
| title | TEXT NOT NULL | Book title |
| author | TEXT NOT NULL | Book author |
| genre | TEXT | Book category |
| publication_date | TEXT | Publication date |
| isbn | TEXT | ISBN number |
| available | INTEGER | Availability status (1=Yes, 0=No) |

#### 👥 Borrowers Table  
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER PRIMARY KEY | Unique borrower identifier |
| name | TEXT NOT NULL | Borrower's full name |
| email | TEXT UNIQUE NOT NULL | Contact email |
| phone | TEXT | Phone number |
| address | TEXT | Physical address |

#### 📋 Checkouts Table
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER PRIMARY KEY | Unique checkout identifier |
| book_id | INTEGER | Reference to Books table |
| borrower_id | INTEGER | Reference to Borrowers table |
| checkout_date | TEXT | Date book was borrowed |
| due_date | TEXT | Return deadline |
| return_date | TEXT | Actual return date (NULL if ongoing) |

---

## 🎮 How to Use

### Books Management
1. **Add Books**: Fill form fields → Click "Add Book"
2. **Search Books**: Enter title/author → Click "Search Books"  
3. **View All Books**: Click "Refresh All Books"
4. **Delete Books**: Enter Book ID → Click "Remove Book"

### Borrowers Management  
1. **Add Borrowers**: Fill borrower details → Click "Add Borrower"
2. **View All Borrowers**: Click "Refresh All"
3. **Delete Borrowers**: Enter Borrower ID → Click "Remove Borrower"

### Checkouts Management
1. **Issue Books**: Enter Book ID, Borrower ID, dates → Click "Add Checkout"
2. **Return Books**: Add return date when creating checkout record
3. **View Transactions**: All checkouts displayed in table
4. **Delete Records**: Enter Checkout ID → Click "Remove Checkout"

---

## 📊 Sample Data

Use the provided `sample_data.sql` file to populate your database with test data:

**Sample Books:**
- "The Java Programming Language" by Ken Arnold
- "Clean Code" by Robert C. Martin  
- "Design Patterns" by Gang of Four

**Sample Borrowers:**
- John Doe (john.doe@email.com)
- Jane Smith (jane.smith@email.com)
- Alice Johnson (alice.johnson@email.com)

---

## 🔍 Technical Details

### JDBC Connection
```java
private final static String DB_URL = "jdbc:sqlite:library.db";
Connection conn = DriverManager.getConnection(DB_URL);
```

### Swing Components Used
- `JFrame` - Main application window
- `JTabbedPane` - Tabbed interface
- `JTable` - Data display
- `JTextField` - Input fields  
- `JButton` - Action buttons
- `JCheckBox` - Boolean inputs
- `DefaultTableModel` - Table data management

### Database Operations
- **CREATE**: Automatic table creation on first run
- **INSERT**: Add new records via prepared statements
- **SELECT**: Retrieve and display data  
- **UPDATE**: Modify existing records
- **DELETE**: Remove records by ID
- **SEARCH**: Find records with LIKE queries

---

## 🛠️ Troubleshooting

### Common Issues & Solutions

**❌ ClassNotFoundException: org.sqlite.JDBC**
- ✅ Ensure SQLite JDBC JAR is in build path
- ✅ Verify JAR appears in "Referenced Libraries"

**❌ GUI doesn't appear**  
- ✅ Check you're running `LibraryManagement.java` (has main method)
- ✅ Look for errors in Eclipse Console

**❌ Database connection failed**
- ✅ Check project directory write permissions
- ✅ Database file created automatically in project root

**❌ Compilation errors**
- ✅ Verify package declarations match folder structure
- ✅ Ensure all imports are correct

---

## 🚀 Future Enhancements

### Possible Improvements:
1. **📅 Date Picker Integration**: Replace text fields with calendar widgets
2. **📊 Reporting System**: Generate PDF reports of library statistics
3. **🔐 User Authentication**: Add login system for librarians
4. **📖 Book Categories**: Advanced filtering and categorization
5. **📱 Responsive Design**: Better UI/UX with modern look
6. **🌐 Web Interface**: Convert to web-based application
7. **📧 Email Notifications**: Overdue book reminders
8. **📈 Analytics Dashboard**: Usage statistics and trends

---

## 📚 Learning Objectives

By completing this project, you will learn:
- ✅ **JDBC Programming**: Database connectivity in Java
- ✅ **Swing GUI Development**: Creating desktop applications  
- ✅ **SQLite Database**: Working with embedded databases
- ✅ **Eclipse IDE**: Professional Java development environment
- ✅ **Event-Driven Programming**: Handling user interactions
- ✅ **Database Design**: Normalized relational database structure
- ✅ **Software Architecture**: Separating concerns (GUI vs Database)

---

## 📝 Code Quality Features

### Best Practices Implemented:
- ✅ **Exception Handling**: Try-catch blocks for database operations
- ✅ **Resource Management**: Proper closing of database connections
- ✅ **Input Validation**: Checks for empty/invalid inputs
- ✅ **User Feedback**: Success/error message dialogs
- ✅ **Code Organization**: Separate classes for different responsibilities
- ✅ **Prepared Statements**: SQL injection prevention
- ✅ **Clean UI Design**: Intuitive and user-friendly interface

---

## 📞 Support & Resources

### Helpful Links:
- 🔗 **SQLite JDBC Driver**: https://github.com/xerial/sqlite-jdbc
- 🔗 **Java Swing Tutorial**: https://docs.oracle.com/javase/tutorial/uiswing/
- 🔗 **JDBC Documentation**: https://docs.oracle.com/javase/tutorial/jdbc/
- 🔗 **Eclipse IDE**: https://www.eclipse.org/ide/

### Getting Help:
1. Check Eclipse **Error Log**: Window → Show View → Error Log
2. Verify **Build Path**: Project Properties → Java Build Path
3. Review **Console Output**: For runtime errors and messages
4. Test **Database File**: Use SQLite browser tools to inspect data

---

## 📄 License

This project is created for educational purposes. Feel free to modify and enhance according to your learning needs.

---

**Happy Coding! 🎉**

*This Library Management System serves as an excellent introduction to Java desktop application development with database integration.*