import json
import webbrowser

webbrowser.register('firefox', None, "C:\Program Files\Mozilla Firefox/firefox.exe")

f = open("data.json")
data = json.load(f)
f.close()

json_data = {}

for row in data:
    webbrowser.get("firefox").open_new_tab(row + " hex color code")