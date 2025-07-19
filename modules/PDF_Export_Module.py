from fpdf import FPDF

def export_pdf(session_data, filename="NIL_Session_Log.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for msg in session_data:
        role = msg.get("role", "").upper()
        content = msg.get("content", "")
        pdf.multi_cell(0, 10, f"{role}:\n{content}\n\n")

    pdf.output(filename)
    return filename

