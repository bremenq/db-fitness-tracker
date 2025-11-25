#!/bin/bash
# Security II Deployment Script

PASSWORD='****'

echo "=== Deploying Security II to ClamV Server ==="

# Upload authentication files
echo "1. Uploading authentication files..."
sshpass -p "$PASSWORD" scp auth_utils.py login.html login.py logout.py maintenance.html \
    azinovev@clamv.constructor.university:~/public_html/

# Upload all updated CGI scripts
echo "2. Uploading updated CGI scripts..."
sshpass -p "$PASSWORD" scp add_*.py \
    azinovev@clamv.constructor.university:~/public_html/

# Set permissions
echo "3. Setting file permissions..."
sshpass -p "$PASSWORD" ssh azinovev@clamv.constructor.university \
    "chmod 755 ~/public_html/*.py && chmod 644 ~/public_html/login.html ~/public_html/maintenance.html"

# Create database table
echo "4. Creating admin_user table..."
sshpass -p "$PASSWORD" ssh azinovev@clamv.constructor.university \
    "mysql -u your_username -p'****' db_your_username -e \"
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

INSERT IGNORE INTO admin_user (username, password_hash, full_name, email) 
VALUES ('admin', SHA2('fittrack2025', 256), 'System Administrator', 'admin@fittrack.local');

SELECT 'Deployment complete!' AS status;
\""

echo "=== Deployment Complete! ==="
echo "Login URL: https://clamv.constructor.university/~azinovev/login.html"
echo "Username: admin"
echo "Password: fittrack2025"
