#!/bin/bash

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
java -cp "build:sqlite-jdbc-*.jar" com.library.system.LibraryManagement