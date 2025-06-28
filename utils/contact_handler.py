# contact_handler.py
import pandas as pd

def record_to_sheet(name, email, school):
    df = pd.DataFrame([[name, email, school]], columns=["Name", "Email", "School"])
    df.to_csv("contacts_log.csv", mode="a", index=False, header=False)

def send_email(name, email, score):
    body = get_email_body(name, score)
    print(f"Sending email to {email} with score: {score}")
    return True, body

def get_email_body(name, score):
    return f"Hi {name},\nThanks for using the NIL Moneymaker Agent. Your score: {score}/100.\nStay ready and keep building!"
