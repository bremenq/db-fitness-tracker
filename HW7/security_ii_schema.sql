-- Security II: User Authentication Schema
-- Assignment 7 - Databases Project 2025
-- Creates admin_user table for access control

-- Create admin_user table
CREATE TABLE IF NOT EXISTS admin_user (
    admin_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(100),
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP NULL,
    is_active BOOLEAN DEFAULT TRUE,
    
    CONSTRAINT chk_username_length CHECK (LENGTH(username) >= 3)
);

-- Insert default admin user
-- Username: admin
-- Password: fittrack2025
-- Note: Password is hashed using SHA2-256
INSERT INTO admin_user (username, password_hash, full_name, email) 
VALUES (
    'admin', 
    SHA2('fittrack2025', 256), 
    'System Administrator', 
    'admin@fittrack.local'
);

-- Optional: Create session table for database-backed sessions
CREATE TABLE IF NOT EXISTS user_session (
    session_id VARCHAR(64) PRIMARY KEY,
    admin_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP NOT NULL,
    ip_address VARCHAR(45),
    user_agent TEXT,
    
    FOREIGN KEY (admin_id) REFERENCES admin_user(admin_id) ON DELETE CASCADE,
    INDEX idx_expires (expires_at)
);

-- Verify tables created
SELECT 'Admin user table created successfully' AS status;
SELECT username, full_name, email, created_at FROM admin_user;

