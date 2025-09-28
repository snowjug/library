-- Sample Data for Library Management System
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
('The Catcher in the Rye', 'J.D. Salinger', 'Fiction', '1951-07-16', '978-0316769174', 1);