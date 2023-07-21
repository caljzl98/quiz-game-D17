import requests
import html
url = "https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean"
data = requests.get(url).json()

question_data = []
for result in data["results"]:
    # raw JSON data returns string with HTML entities
    # html.unescape decodes them to their corresponding Unicode characters.
    result["question"] = html.unescape(result["question"])
    question_data.append(result)