@echo off
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

REM Create build directory if it doesn't exist
if not exist "build" mkdir "build"

REM Check if SQLite JDBC JAR exists
if not exist "sqlite-jdbc-3.50.3.0.jar" (
    echo ERROR: SQLite JDBC JAR file not found!
    echo Please download sqlite-jdbc-3.50.3.0.jar and place it in this directory.
    echo Download from: https://repo1.maven.org/maven2/org/xerial/sqlite-jdbc/3.50.3.0/sqlite-jdbc-3.50.3.0.jar
    pause
    exit /b 1
)

REM Compile all Java files in src\com\library\system
echo Compiling Java files...
javac -cp "sqlite-jdbc-3.50.3.0.jar" -d build src\com\library\system\Database.java src\com\library\system\LibraryManagement.java

if %errorlevel% neq 0 (
    echo ERROR: Compilation failed!
    pause
    exit /b 1
)

echo Compilation successful!
echo.

REM Run the application
echo Starting Library Management System...
java -cp "build;sqlite-jdbc-3.50.3.0.jar" com.library.system.LibraryManagement

pause
exit /b 0
@echo off