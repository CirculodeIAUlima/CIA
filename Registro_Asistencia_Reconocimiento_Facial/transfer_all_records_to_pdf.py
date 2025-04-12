import os
import datetime
import mysql.connector
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

# pip install mysql-connector-python
# pip install reportlab

def get_data_from_mysql():
    # Connect to the MySQL database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="attendance_db"
    )
    cursor = connection.cursor()

    # Get all the data from the "registration" table sorted by date
    query = "SELECT id, date, name, time FROM registration ORDER BY date"
    cursor.execute(query)
    data = cursor.fetchall()

    # Close the connection
    cursor.close()
    connection.close()

    # Organize the data by date
    organized_data = {}
    for row in data:
        date = row[1]
        if date not in organized_data:
            organized_data[date] = []
        organized_data[date].append(row)

    return organized_data


def create_pdf(organized_data):
    # Create the PDF file named "Assistance_list.pdf"
    filename = "Assistance_list.pdf"
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []

    styles = getSampleStyleSheet()

    for date, data in organized_data.items():
        # Add the date title at the top of the document as a 'Flowable' object
        title = f"Attendance list for the day ({date})"
        title_style = styles['Title']
        title_paragraph = Paragraph(title, title_style)
        elements.append(title_paragraph)

        # Convert the data for that date into a list for the table
        data_table = [['ID', 'Date', 'Name', 'Time']] + data

        # Create the table for that date
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

        # Add a space after the table
        elements.append(Spacer(1, 12))

    # Build the document
    doc.build(elements)

if __name__ == "__main__":
    # Get the data organized by date from MySQL
    organized_data = get_data_from_mysql()

    # Create the PDF with the data from the table organized by date
    create_pdf(organized_data)
