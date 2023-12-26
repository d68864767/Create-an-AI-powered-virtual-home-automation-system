```sql
-- SQL Database for AI-powered virtual home automation system

CREATE DATABASE HomeAutomation;

USE HomeAutomation;

-- Table for devices
CREATE TABLE Devices (
    id INT AUTO_INCREMENT,
    device_name VARCHAR(255) NOT NULL,
    status VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

-- Table for users
CREATE TABLE Users (
    id INT AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

-- Table for device control logs
CREATE TABLE DeviceControlLogs (
    id INT AUTO_INCREMENT,
    user_id INT,
    device_id INT,
    status VARCHAR(255),
    control_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (device_id) REFERENCES Devices(id)
);
```
