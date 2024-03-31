from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# XML content
xml_content = """
<document>
    <header align="center">
        <para fontSize="14">Sample Report Header</para>
    </header>

    <body>
        <para fontSize="12">This is a sample report generated using XML with ReportLab.</para>
    </body>

    <footer align="center">
        <para fontSize="10">Page # <pageNumber /></para>
    </footer>
</document>
"""

# Create a PDF document
doc = SimpleDocTemplate("report.pdf", pagesize=letter)

# Apply styles
styles = getSampleStyleSheet()

# Parse XML content
content = []
for line in xml_content.split('\n'):
    if line.strip():
        content.append(Paragraph(line.strip(), styles["Normal"]))

# Build PDF document
doc.build(content)

print("PDF report generated successfully.")
