from googlesearch import search
# import beautifulsoup4

spotify_country_playist_ids = {
"Asia" : { "Japan" : {}, "Israel": {}, "Hong Kong": {}, "Indonesia": {}, "Malaysia": {}, "Philippines": {}, "Singapore": {}, "Taiwan": {}, "Thailand": {}, "Vietnam": {}, "India": {}},
"Europe" :  {"Andorra": {}, "Austria": {}, "Belgium": {}, "Bulgaria": {}, "Cyprus": {}, "Czech Republic": {}, "Denmark": {}, "Estonia": {}, "Finland": {}, "France": {}, "Germany": {}, "Greece": {}, "Hungary": {}, "Iceland": {}, "Ireland": {}, "Italy": {}, "Latvia": {}, "Liechtenstein": {}, "Lithuania": {}, "Luxembourg": {}, "Malta": {}, "Monaco": {}, "Netherlands": {}, "Norway": {}, "Poland": {}, "Portugal": {}, "Romania": {}, "Slovakia": {}, "Spain": {}, "Sweden": {}, "Switzerland": {}, "Turkey": {}, "United Kingdom}": {}},
"Latin America and  Caribbean ": { "Argentina": {}, "Bolivia": {}, "Brazil": {}, "Chile": {}, "Colombia": {}, "Costa Rica": {}, "Dominican Republic": {}, "Ecuador": {}, "El Salvador": {}, "Guatemala": {}, "Honduras": {}, "Mexico": {}, "Nicaragua": {}, "Panama": {}, "Paraguay": {}, "Peru": {}, "Uruguay": {}},
"North America":  {"Canada": {}, "United States" : "37i9dQZEVXbMDoHDwVN2tF"},
"Africa" : {"Algeria": {}, "Egypt": {}, "Morocco": {}, "South Africa": {}, "Tunisia": {}},
"Oceania" : {"Australia": {}, "New Zealand": {}},
"Middle East" : {"Bahrain": {}, "Jordan": {}, "Kuwait": {}, "Lebanon": {}, "Oman": {}, "Palestine": {}, "Qatar": {}, "Saudi Arabia": {}, "United Arab Emirates": {}}
}






def get_country_playlist_url(country):
    """given name of country, return playlist id from url"""

    query = f"site:open.spotify.com Top 50 on Spotify {country}"
  
    # use google.com to get one result 
    # the result is a generator object, so we need to loop through it
    for url in search(query, tld="com", num=1, stop=1, pause=2): 

        print(url)

        url_pieces = url.split("/")

        playlist_id = url_pieces[-1]

        print(country, ":", playlist_id)

        


get_country_playlist_url("Japan")


