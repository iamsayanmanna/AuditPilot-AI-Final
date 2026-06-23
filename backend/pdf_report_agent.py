from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet
import os


def generate_pdf_report(report_data):

    pdf_file = os.path.join(
        os.path.dirname(__file__),
        "audit_report.pdf"
    )

    doc = SimpleDocTemplate(pdf_file)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "AuditPilot AI Executive Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 20))

    for key, value in report_data.items():

        content.append(
            Paragraph(
                f"<b>{key}</b>: {value}",
                styles["BodyText"]
            )
        )

        content.append(Spacer(1, 10))

    doc.build(content)

    return pdf_file