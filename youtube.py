import urllib.request
import re


def youtube(query):
    search_keyword = urllib.parse.quote(query)
    html = urllib.request.urlopen(
        "https://www.youtube.com/results?search_query=" + search_keyword
    )
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    return "https://www.youtube.com/watch?v=" + video_ids[0]
