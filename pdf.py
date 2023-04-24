import pandas as pd
import numpy as np
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

data = pd.read_csv('data.csv')
LocaitonAVG = data.groupby('location')[['price', 'sqft']].mean()
TypeAVG = data.groupby('type')[['bedrooms', 'bathrooms']].mean()
def generate_report(LocaitonAVG, TypeAVG):
    c = canvas.Canvas("report.pdf", pagesize=letter)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(1 * inch, 10 * inch, "Property Values")
    c.setFont("Helvetica", 14)
    c.drawString(1 * inch, 9.5 * inch, "Average Values")
    c.setFont("Helvetica", 12)
    y_offset = 9 * inch
    for location, avg_data in LocaitonAVG.iterrows():
        c.drawString(1 * inch, y_offset, location)
        c.drawString(2 * inch, y_offset, "Price: {:,.2f}".format(avg_data['price']))
        c.drawString(3.5 * inch, y_offset, "Sqft: {:.2f}".format(avg_data['sqft']))
        y_offset -= 0.25 * inch
    c.setFont("Helvetica", 14)
    c.drawString(1 * inch, y_offset - 0.5 * inch, "Average Values")
    c.setFont("Helvetica", 12)
    y_offset -= 0.75 * inch
    for prop_type, avg_data in TypeAVG.iterrows():
        c.drawString(1 * inch, y_offset, prop_type)
        c.drawString(2 * inch, y_offset, "Bedrooms: {:.2f}".format(avg_data['bedrooms']))
        c.drawString(3.5 * inch, y_offset, "Bathrooms: {:.2f}".format(avg_data['bathrooms']))
        y_offset -= 0.25 * inch 
    c.showPage()
    c.save()

if __name__ == "__main__":
    generate_report(LocaitonAVG, TypeAVG)