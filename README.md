# Charity Information Backend

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Features

- Look up charities by their EIN (Employer Identification Number).
- Generate AI-powered summaries of charity information.
- Front-end built with React for a responsive user interface.
- Back-end built with Flask, integrating with Google Sheets and OpenAI.

## Installation

### Prerequisites

- Python 3.8 or higher
- Google Sheets API credentials
- OpenAI API

### Backend Setup

1. Clone the repository and navigate into the project directory.

   ```bash
   git clone <repository-url>
   cd <repository-directory>

2. Install required packages

   ```bash
   pip install -r requirements.txt
   
3. Set up the environment
  
   ```bash
   # OpenAI settings
   OPENAI_API_KEY=your_openai_api_key_here
   OPENAI_ORG_KEY=your_openai_org_key_here
   
   # Google Sheets settings
   GOOGLE_SHEET_ID=your_google_sheet_id_here

4. Run the server

   ```bash
   flask run
   
## Important Note

Before running the application, you **must** place your `credentials.json` file in the root directory. This file contains your Google service account keys necessary for accessing the Google Sheets API.

**`credentials.json` structure:**

```json
{
  "type": "service_account",
  "project_id": "your-project-id",
  "private_key_id": "your-private-key-id",
  ...
}