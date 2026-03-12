from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

def create_pdf(query, result):

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("AI Research Report", styles['Title']))
    elements.append(Spacer(1,20))

    elements.append(Paragraph("User Query", styles['Heading2']))
    elements.append(Paragraph(query, styles['BodyText']))

    elements.append(Spacer(1,20))

    elements.append(Paragraph("Generated Result", styles['Heading2']))
    elements.append(Paragraph(result, styles['BodyText']))

    doc.build(elements)

    buffer.seek(0)
    return buffer