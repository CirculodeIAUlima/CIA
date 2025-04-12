import os
import datetime
import mysql.connector
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

# pip install mysql-connector-python
# pip install reportlab

def get_current_date():
    # Get the current date in "YYYY-MM-DD" format
    return datetime.datetime.now().strftime("%Y-%m-%d")

def get_data_from_mysql():
    # Connect to the MySQL database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="attendance_db"
    )
    cursor = connection.cursor()

    # Get the current date in "YYYY-MM-DD" format
    current_date = get_current_date()

    # Get the data from the "registration" table for the current date
    query = f"SELECT id, date, name, time FROM registration WHERE date = '{current_date}'"
    cursor.execute(query)
    data = cursor.fetchall()

    # Close the connection
    cursor.close()
    connection.close()

    return data

def create_pdf(data):
    # Create the PDF file named "lista_asistencia_fecha.pdf"
    filename = f"Assistance_List_{get_current_date()}.pdf"
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []

    # Add the title at the top of the document as a Flowable object
    title = f"Attendance list for the day ({get_current_date()})"
    title_style = getSampleStyleSheet()['Title']
    title_paragraph = Paragraph(title, title_style)
    elements.append(title_paragraph)

    # Convert the data into a list for the table
    data_table = [['ID', 'Date', 'Name', 'Time']] + data

    # Create the table
    table = Table(data_table)

    # Table style
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
        ('ALIGN',(0,0),(-1,-1),'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND',(0,1),(-1,-1),colors.beige),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
    ])
    table.setStyle(style)

    # Add the table to the document
    elements.append(table)

    # Build the document
    doc.build(elements)

if __name__ == "__main__":
    # Get the data from MySQL
    data = get_data_from_mysql()

    # Create the PDF with the table data
    create_pdf(data)
