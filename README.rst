# 📧 Email Exchange Module for Odoo

A custom Odoo module that allows users to send and receive emails using their own email credentials. It also supports adding signatures and attachments to emails directly from within the Odoo environment.

🎥 **Demo Video:** [bit.ly/emailexchange](https://bit.ly/emailexchange)

---

## ✨ Features

- Authenticate users with their email accounts
- Send and receive emails within Odoo
- Add HTML-formatted signatures
- Upload and send file attachments
- Dockerized for easy setup and deployment

---

## 🛠️ Technologies Used

- Python (Odoo backend)
- XML (Odoo views/config)
- Docker
- Odoo ERP Framework

---

## 🚀 Installation & Usage

1. Clone the repository inside your Odoo `addons` directory:
   ```bash
   git clone https://github.com/esraarozika/Email-exchange.git

* First you should install these python packages:
1- email
2- python-imap
3- regex
4- bs4
5- mistletoe
6- html2text
___________________________________________________

* Second you should restsart the server 
___________________________________________________

* Third update your Apps List then install email exchange module
___________________________________________________

* Fourth go to Settingd -> general settings -> External Email Servers => Make it True
___________________________________________________

* Fifth put email in email field all records in res.partner (\* Contacts Module)
___________________________________________________

* Sixth fill in credential fields in your logged in user
