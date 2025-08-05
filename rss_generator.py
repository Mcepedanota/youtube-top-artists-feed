from datetime import datetime
from xml.etree.ElementTree import Element, SubElement, ElementTree

top_artists = [
    {"rank": 1, "artist": "Drake", "link": "https://www.youtube.com/channel/UCByOQJjav0CUDwxCk-jVNRQ"},
    {"rank": 2, "artist": "Taylor Swift", "link": "https://www.youtube.com/channel/UCqECaJ8Gagnn7YCbPEzWH6g"},
    {"rank": 3, "artist": "Bad Bunny", "link": "https://www.youtube.com/channel/UCmBA_wu8xGg1OfOkfW13Q0Q"},
    {"rank": 4, "artist": "Peso Pluma", "link": "https://www.youtube.com/channel/UCo9aWzTLlaL0z4HINlvRM2A"},
    {"rank": 5, "artist": "Eslabon Armado", "link": "https://www.youtube.com/channel/UCjqjV13v8wN0pTCSQ7l5NXw"},
]

rss = Element("rss", version="2.0")
channel = SubElement(rss, "channel")

SubElement(channel, "title").text = "YouTube Top Artists - US Weekly"
SubElement(channel, "link").text = "https://charts.youtube.com/charts/TopArtists/us/weekly"
SubElement(channel, "description").text = "Weekly Top Artists on YouTube in the US"
SubElement(channel, "language").text = "en-us"
SubElement(channel, "lastBuildDate").text = datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S +0000")

for artist in top_artists:
    item = SubElement(channel, "item")
    SubElement(item, "title").text = f"#{artist['rank']} - {artist['artist']}"
    SubElement(item, "link").text = artist['link']
    SubElement(item, "description").text = f"{artist['artist']} is ranked #{artist['rank']} this week."
    SubElement(item, "pubDate").text = datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S +0000")

tree = ElementTree(rss)
tree.write("youtube_top_artists_us_weekly.xml", encoding="utf-8", xml_declaration=True)
