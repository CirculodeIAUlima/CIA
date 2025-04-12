# Attendance with Face Recognition

Welcome to the **Attendance with Face Recognition** repository! This repository is designed to facilitate attendance tracking through facial recognition and seamless database registration.

- The `Attendance` directory houses the core code responsible for executing the facial recognition process and registering attendance in the database.
- The `Images` directory is designated for storing the photographs of individuals, which the system will use for recognition purposes. Every photo will be identified and registrated by the file name.

## Requirements

Before getting started, please ensure you have the following prerequisites ready:

- MySQL installed, with a database named `attendance_db` created within it (you have to create it).
- `pip` installed and properly configured in your system's PATH.
- `virtualenv` installed to manage the project's Python environment (see `requirements.txt` for dependencies).
- Store images in the `Images` directory, ensuring they are in either **"jpg"** or **"png"** format.

## Installation and Setup

Follow these steps to set up the project on your local machine:

1. Install `virtualenv` using the command: `pip install virtualenv`.
2.  Navigate to the `Attendance-with-Face-Recognition` directory and create a virtual environment with the command: 
    `virtualenv assistance_venv`.
3. Activate the virtual environment:
   - For Windows: `.\assistance_venv\Scripts\activate`
   - For Unix or MacOS: `source assistance_venv/bin/activate`
4. Navigate to the `Attendance-with-Face-Recognition/` directory and install the required Python packages with: 
    `pip install -r requirements.txt`

## To run It

1. Make sure the Virtual Environment is activated
2. Go to inside the 'Attendance' folder and run py .\detect_face_and_register_in_db.py
3. Export the database records of the day running py .\transfer_today_records_to_pdf.py
4. Export all the database records running py .\transfer_all_records_to_pdf.py

## Visual Guide

For your convenience, here are some visual aids to help you with the expected outcomes:

- Example of Attendance Taking & Records
  
  ![Example of Attendance Taking & Records](https://i.ibb.co/PYNx0JF/att.png)

This project was developed for the Artificial Intelligence circle at the University of Lima and aims to provide a straightforward, efficient method for attendance tracking through the innovative use of facial recognition technology.
