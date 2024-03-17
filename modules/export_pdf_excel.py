from datetime import datetime
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle


def create_pdf(filename: str, info_data: list[str], path: str):

    data = [
        ["Id Turno", "DNI", "Hora Entrada", "Hora Salida", "Total"],]
    for entry in info_data:
        total = datetime.strptime(
            entry[3], "%d/%m/%Y %H:%M:%S") - datetime.strptime(entry[2], "%d/%m/%Y %H:%M:%S")

        info_table = [n for n in entry]
        info_table.append(total)
        data.append(list(info_table))
    name_pdf = path + "/" + filename + ".pdf"
    doc = SimpleDocTemplate(name_pdf, pagesize=letter)
    table = Table(data)

    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),

                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    table.setStyle(style)
    elements = []
    # elements.append(Paragraph("Reporte de Turnos Trabajados en Cronos\n\n\n"))
    elements.append(table)
    elements.append(Paragraph(
        f"Informe realizado el: {datetime.now()}"))
    doc.build(elements)
