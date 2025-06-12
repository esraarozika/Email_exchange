# 📧 Email Exchange Module for Odoo

A custom Odoo module that allows users to send and receive emails using their own email credentials. It also supports adding signatures and attachments to emails directly from within the Odoo environment.

🎥 **Demo Video:** [View on Google Drive](https://drive.google.com/file/d/1Qs8BWefdDQX5GFaVYJr0I8jpzIqZzBi6/view?usp=sharing)

----

## ✨ Features

- Authenticate users with their email accounts
- Send and receive emails within Odoo
- Add HTML-formatted signatures
- Upload and send file attachments
- Dockerized for easy setup and deployment

----

## 🛠️ Technologies Used

- Python (Odoo backend)
- XML (Odoo views/config)
- Docker
- Odoo ERP Framework

----

## 🚀 Installation & Usage

1. Clone the repository inside your Odoo `addons` directory:
   ```bash
   
   git clone https://github.com/esraarozika/Email-exchange.git


2.docker-compose up

3.install these python packages:

   1- email

   2- python-imap

   3- regex

   4- bs4

   5- mistletoe

   6- html2text
   
   *  you should restsart the server 

4.Install the module from the Odoo Apps interface.

5.go to Settingd -> general settings -> External Email Servers => Make it True

6.Go to Email Exchange in the Odoo dashboard:
   *Add your email credentials
   *Compose and send emails
   *Add signatures and attachments

=>all records in res.partner (\* Contacts Module)

----

📂 Folder Structure:

Email-exchange/

├── controllers/
|
├── models/
|
├── views/
|
├── __manifest__.py
|
├── __init__.py
|
├── README.md


