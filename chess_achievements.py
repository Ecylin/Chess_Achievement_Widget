import requests
from bs4 import BeautifulSoup


def load_achievements(file_path):
    achievement_data = {}
    try:
        with open(file_path, 'r') as file:
            for line in file.readlines():
                name, display_name = line.strip().split(',')
                achievement_data[name] = display_name
    except FileNotFoundError:
        print("Achievement file not found.")
    return achievement_data


def get_missing(username):
    r = requests.get("https://www.chess.com/awards/" + username + "/achievements")

    # If unable to load url, print error message
    if r.status_code == 404:
        return f"Unable to load achievements for user \"{username}\". Make sure you input your username correctly"

    soup = BeautifulSoup(r.content, 'html.parser')

    def has_data_code(tag):
        return tag.has_attr('data-code')

    s = soup.findAll(has_data_code)

    user_achievements = {}

    for link in s:
        dcode = link.get('data-code', 'No data-code attribute')

        # Account for if the achievement is displayed but still locked
        hidden = link.get('data-is-hidden', 'Data is not hidden!')
        if hidden == "Data is not hidden!":
            user_achievements[dcode] = 0

    missing = [element for element in load_achievements("Achievements.txt") if element not in user_achievements]

    return missing


def get_names(string_list):

    achievements = load_achievements("Achievements.txt")

    output = ""
    for i in string_list:
        output = output + f"{achievements[i]}\n"

    return output
