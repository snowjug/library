# Library Management System - Eclipse Setup Guide

## Overview
This is a comprehensive guide to create a **Simple Library Management System** using:
- **Java** (Core programming language)
- **JDBC** (Database connectivity)
- **Swing** (GUI framework) 
- **SQLite** (Embedded database)
- **Eclipse IDE** (Development environment)

## Features
✅ **Books Management**: Add, view, search, and delete books  
✅ **Borrowers Management**: Manage library member information  
✅ **Checkout System**: Track book borrowing and returns  
✅ **Search Functionality**: Find books by title or author  
✅ **SQLite Database**: Lightweight, embedded database  
✅ **User-friendly GUI**: Intuitive Swing interface

## Prerequisites
- Java JDK 8 or later
- Eclipse IDE (any recent version)
- Internet connection (to download SQLite JDBC driver)

## Step-by-Step Setup Instructions

### Step 1: Create Eclipse Project

1. **Open Eclipse IDE**
2. Go to **File** → **New** → **Java Project**
3. **Project Name**: `LibraryManagementSystem`
4. **Use default location** or choose your preferred directory
5. **JRE Version**: Use default (JRE 8 or later)
6. Click **Next** → **Finish**
7. If prompted about module-info.java, click **Don't Create**

### Step 2: Create Package Structure

1. **Right-click** on `src` folder in your project
2. Select **New** → **Package**
3. **Package Name**: `com.library.system`
4. Click **Finish**

### Step 3: Download SQLite JDBC Driver

**Option A: Direct Download**
1. Go to https://mvnrepository.com/artifact/org.xerial/sqlite-jdbc
2. Click on the **latest version** (e.g., 3.50.3.0)
3. Download the **JAR file** (e.g., `sqlite-jdbc-3.50.3.0.jar`)
4. Save it to a known location on your computer

**Option B: Download Link**
Direct download: https://repo1.maven.org/maven2/org/xerial/sqlite-jdbc/3.50.3.0/sqlite-jdbc-3.50.3.0.jar

### Step 4: Add SQLite JDBC Driver to Project

1. **Right-click** on your project name (`LibraryManagementSystem`)
2. Select **Properties**
3. In left panel, click **Java Build Path**
4. Go to **Libraries** tab
5. Click **Classpath** (if using older Eclipse) or **Modulepath** (if using newer Eclipse)
6. Click **Add External JARs...**
7. **Browse** to the location where you saved `sqlite-jdbc-3.50.3.0.jar`
8. **Select** the JAR file and click **Open**
9. Click **Apply and Close**

**Verification**: You should now see the SQLite JDBC driver under "Referenced Libraries" in your project explorer.

### Step 5: Add Java Source Files

1. **Right-click** on the package `com.library.system`
2. Select **New** → **Class**
3. Create **Database.java** class
4. Copy and paste the Database.java code
5. Repeat for **LibraryManagement.java**

### Step 6: Project Structure
Your project structure should look like this:
```
LibraryManagementSystem/
├── src/
│   └── com.library.system/
│       ├── Database.java
│       └── LibraryManagement.java
├── Referenced Libraries/
│   └── sqlite-jdbc-3.50.3.0.jar
└── library.db (will be created automatically)
```

## Running the Application

### Method 1: Run from Eclipse
1. **Right-click** on `LibraryManagement.java`
2. Select **Run As** → **Java Application**
3. The GUI window should appear

### Method 2: Run main method directly
1. **Open** `LibraryManagement.java`
2. **Right-click** in the editor
3. Select **Run As** → **Java Application**

## Application Usage

### Books Tab
- **Add Book**: Fill in book details and click "Add Book"
- **Search**: Enter title/author in search field and click "Search Books"
- **Delete**: Enter Book ID and click "Remove Book"
- **Refresh**: Click "Refresh All Books" to show all books

### Borrowers Tab  
- **Add Borrower**: Fill in borrower details and click "Add Borrower"
- **Delete**: Enter Borrower ID and click "Remove Borrower"
- **View All**: Click "Refresh All" to see all borrowers

### Checkouts Tab
- **Create Checkout**: Enter Book ID, Borrower ID, dates and click "Add Checkout"
- **Return Book**: You can add return date when creating checkout
- **Delete Record**: Enter Checkout ID and click "Remove Checkout"

## Database Schema

The SQLite database (`library.db`) contains three tables:

### Books Table
- `id` (INTEGER PRIMARY KEY)
- `title` (TEXT NOT NULL)
- `author` (TEXT NOT NULL)  
- `genre` (TEXT)
- `publication_date` (TEXT)
- `isbn` (TEXT)
- `available` (INTEGER DEFAULT 1)

### Borrowers Table
- `id` (INTEGER PRIMARY KEY)
- `name` (TEXT NOT NULL)
- `email` (TEXT UNIQUE NOT NULL)
- `phone` (TEXT)
- `address` (TEXT)

### Checkouts Table
- `id` (INTEGER PRIMARY KEY)
- `book_id` (INTEGER - Foreign Key)
- `borrower_id` (INTEGER - Foreign Key)
- `checkout_date` (TEXT NOT NULL)
- `due_date` (TEXT NOT NULL)
- `return_date` (TEXT)

## Troubleshooting

### Common Issues

**1. ClassNotFoundException: org.sqlite.JDBC**
- **Solution**: Make sure SQLite JDBC JAR is properly added to build path
- Verify the JAR appears under "Referenced Libraries"

**2. Database connection errors**
- **Solution**: Database file will be created automatically in project root
- Check if you have write permissions in the project directory

**3. GUI doesn't appear**
- **Solution**: Make sure you're running `LibraryManagement.java` with main method
- Check Eclipse console for error messages

**4. Build path errors**
- **Solution**: Right-click project → Properties → Java Build Path → Libraries
- Remove and re-add the SQLite JDBC JAR if necessary

### IDE-Specific Tips

**Eclipse WindowBuilder (Optional)**
- Install WindowBuilder plugin for visual GUI design
- Help → Eclipse Marketplace → Search "WindowBuilder"
- Install and restart Eclipse

**Code Formatting**
- **Ctrl+Shift+F**: Format code automatically
- **Ctrl+Shift+O**: Organize imports

## Sample Data for Testing

### Sample Books
```
Title: "The Java Programming Language"
Author: "Ken Arnold"
Genre: "Technology"
Publication Date: "2020-01-15"
ISBN: "978-0134685991"
Available: Yes
```

### Sample Borrower
```
Name: "John Doe"
Email: "john.doe@email.com"
Phone: "+1-555-123-4567"
Address: "123 Main Street, City, State"
```

### Sample Checkout
```
Book ID: 1
Borrower ID: 1
Checkout Date: 2024-01-15
Due Date: 2024-02-15
Return Date: (leave empty for ongoing checkout)
```

## Advanced Features (Optional Enhancements)

### 1. Add Date Picker
- Download JXDatePicker library
- Replace text fields with date picker components

### 2. Reports Generation
- Add functionality to generate PDF reports
- Use libraries like iText or Apache PDFBox

### 3. Data Validation
- Add input validation for dates, email formats
- Implement ISBN validation

### 4. Search Filters
- Add genre-based filtering
- Publication year range search

## Database File Location

The SQLite database file (`library.db`) will be created in:
- **Windows**: `C:\path\to\your\workspace\LibraryManagementSystem\library.db`
- **Mac/Linux**: `/path/to/your/workspace/LibraryManagementSystem/library.db`

## Export Project

To share your project:
1. **Right-click** on project → **Export**
2. Select **General** → **Archive File**
3. Choose destination and click **Finish**

## Next Steps

After successfully running the basic system:
1. Add more validation and error handling
2. Implement advanced search features
3. Add user authentication
4. Create reports and analytics
5. Deploy as executable JAR file

## Support

If you encounter any issues:
1. Check Eclipse Error Log (Window → Show View → Error Log)
2. Verify all JAR files are properly added
3. Ensure proper package declarations in Java files
4. Check database file permissions

This guide provides everything needed to create a fully functional Library Management System in Eclipse using JDBC and Swing!