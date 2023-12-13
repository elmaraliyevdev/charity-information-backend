from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import access_google_sheet, create_gpt_prompt, get_gpt_summary

app = Flask(__name__)

CORS(app)


@app.route('/search', methods=['POST'])
def search_charity_by_ein():
    data = request.json
    ein_input = data['ein']
    try:
        ein_input = int(ein_input)
    except ValueError:
        return jsonify({"error": "Invalid EIN format"}), 400

    sheet = access_google_sheet()
    all_records = sheet.get_all_records()

    charity_data = None
    for record in all_records:
        ein_sheet = record.get('ein')
        if ein_sheet == ein_input:
            charity_data = record
            break

    if charity_data:
        prompt = create_gpt_prompt(charity_data)
        summary = get_gpt_summary(prompt)
        return jsonify({"summary": summary})
    else:
        return jsonify({"error": "Charity not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
