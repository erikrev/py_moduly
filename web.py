import webbrowser
#
# webbrowser.open("https://www.python.org/", new=2)
# webbrowser.open_new("https://www.python.org/")
# help(webbrowser)

chrome = webbrowser.get(using="chromium")
chrome.open_new("https://www.python.org/")