import os
import gspread
from openai import OpenAI
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    organization=os.getenv('OPENAI_ORG_KEY'),
    api_key=os.getenv('OPENAI_API_KEY')
)


def access_google_sheet():
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
    ]

    credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

    google_client = gspread.authorize(credentials)

    sheet = google_client.open_by_key(os.getenv('GOOGLE_SHEET_ID')).sheet1

    return sheet


def create_gpt_prompt(charity_data):
    prompt = f"""
    I have gathered some information about a charity and need a concise summary.

    Name: {charity_data.get('name')}
    Type of Charity: {charity_data.get('type of charity')}
    Form Submitted: {charity_data.get('form_type')}
    Contact Person: {charity_data.get('president_name')}
    Title: {charity_data.get('president_title')}
    Salary of the Principal Officer: {charity_data.get('The salary of the Principal Officer')}
    Ruling Year: {charity_data.get('ruling_year')}
    Location: {charity_data.get('address')}
    Website: {charity_data.get('website')}
    Programs: {charity_data.get('Program service')}
    Financial Information for Current Year: {charity_data.get('current year')} with Total Revenue {charity_data.get('crrent total revenue')} and Total Expenses {charity_data.get('crrent total expenses')}
    Financial Information for Previous Year: {charity_data.get('previous year')} with Total Revenue {charity_data.get('previous total revenue')} and Total Expenses {charity_data.get('previous total expenses')}

    Please provide a summary that answers the following:
    1. What is the charity's name and what type of charity are they?
    2. What form did the charity submit?
    3. Who is the contact and what is their title? What is their salary?
    4. What is the ruling year of the charity?
    5. Where is the charity located?
    6. What is the website of the charity?
    7. What are the programs the charity has?
    8. List all financial information and the year the financial information refers to if available.
    """
    return prompt


def get_gpt_summary(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    summary = response.choices[0].message.content.strip()

    return summary
