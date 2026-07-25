
CREATE DATABASE IF NOT EXISTS saas_db;
USE saas_db;


DROP TABLE IF EXISTS telco_churn;

CREATE TABLE telco_churn (
    customer_id VARCHAR(50),
    count INT,
    country VARCHAR(50),
    state VARCHAR(50),
    city VARCHAR(50),
    zip_code VARCHAR(20),
    lat_long VARCHAR(100),
    latitude DECIMAL(10,6),
    longitude DECIMAL(10,6),
    gender VARCHAR(20),
    senior_citizen VARCHAR(10),
    partner VARCHAR(10),
    dependents VARCHAR(10),
    tenure_months INT,
    phone_service VARCHAR(10),
    multiple_lines VARCHAR(30),
    internet_service VARCHAR(30),
    online_security VARCHAR(30),
    online_backup VARCHAR(30),
    device_protection VARCHAR(30),
    tech_support VARCHAR(30),
    streaming_tv VARCHAR(30),
    streaming_movies VARCHAR(30),
    contract VARCHAR(30),
    paperless_billing VARCHAR(10),
    payment_method VARCHAR(50),
    monthly_charges DECIMAL(10,2),
    total_charges DECIMAL(10,2),
    churn_label VARCHAR(10),
    churn_value INT,
    churn_score INT,
    cltv INT,
    churn_reason VARCHAR(255),
    tenure_group VARCHAR(20)
);
SET GLOBAL local_infile = 1;



