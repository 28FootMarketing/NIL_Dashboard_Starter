# content_templates.py
def generate_template(template_type, name):
    if template_type == "Brand Outreach Email":
        return f"Hi {{Brand Name}},\n\nMy name is {name} and I’m a student-athlete interested in NIL opportunities..."
    elif template_type == "Contract Template":
        return f"CONTRACT AGREEMENT\n\nThis agreement is made between {name} and {{Brand Name}} for NIL services..."
    elif template_type == "Social Media Post":
        return f"Big thanks to {{Brand Name}} for supporting my journey! Proud to partner with them. #NIL #Ad"
    elif template_type == "Thank You Note":
        return f"Dear {{Brand Name}},\n\nThank you for the opportunity to collaborate through NIL. I appreciate your support."
    return "Template not found."
