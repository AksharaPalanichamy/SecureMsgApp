# SecureMsgApp
1.CREATE DATABASE secure_message_service_db


2.
CREATE USER 'application_user'@'localhost' IDENTIFIED BY 'Akshara123!';
GRANT ALL PRIVILEGES ON secure_message_service_db.* TO 'application_user'@'localhost';
FLUSH PRIVILEGES;

3.
ALTER DATABASE secure_message_service_db CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

tables we might need
user
user_verification
messages -sender,reciever,encrypted messages,timestamp


YTD
online status
OTP?? if time permits