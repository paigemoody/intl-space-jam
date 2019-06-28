from googlesearch import search
from random import choice


def get_country_playlist_url(country):
    """given name of country, return playlist id from url"""

    query = f"site:open.spotify.com Top 50 on Spotify {country}"
  
    # use google.com to get one result 
    # the result is a generator object, so we need to loop through it

    pause_len = choice([4,5,6])
    for url in search(query, tld="com", num=1, stop=1, pause=pause_len): 

        url_pieces = url.split("/")

        playlist_id = url_pieces[-1]

        return {'url': url, 'playlist_id' : playlist_id}
        


def build_url_playlist_id_to_dict():
    """ Add url and playlist id for each country to spotify countries dict"""
    spotify_country_playist_ids = {
        # "Asia" : { "Japan" : {}, "Israel": {}, "Hong Kong": {}, "Indonesia": {}, "Malaysia": {}, "Philippines": {}, "Singapore": {}, "Taiwan": {}, "Thailand": {}, "Vietnam": {}, "India": {}},
        # "Europe" :  {
        # "Andorra": {}, "Austria": {}, "Belgium": {}, "Bulgaria": {}, "Cyprus": {}, "Czech Republic": {}, "Denmark": {}, "Estonia": {}, "Finland": {}, "France": {}, "Germany": {}, "Greece": {}, "Hungary": {}, "Iceland": {}, "Ireland": {}, 
        # "Italy": {}, "Latvia": {}, "Liechtenstein": {}, "Lithuania": {}, "Luxembourg": {}, "Malta": {}, "Monaco": {}, "Netherlands": {}, "Norway": {}, "Poland": {}, "Portugal": {}, "Romania": {}, "Slovakia": {}, "Spain": {}, "Sweden": {}, "Switzerland": {}, "Turkey": {}, "United Kingdom}": {}},
        # "Latin America and Caribbean ": { "Argentina": {}, "Bolivia": {}, "Brazil": {}, "Chile": {}, "Colombia": {}, "Costa Rica": {}, "Dominican Republic": {}, "Ecuador": {}, "El Salvador": {}, "Guatemala": {}, "Honduras": {}, "Mexico": {}, "Nicaragua": {}, "Panama": {}, "Paraguay": {}, "Peru": {}, "Uruguay": {}},
        "North America":  { 
        # "Canada": {}, 
        "United States" : ""},
        "Africa" : {"Algeria": {}, "Egypt": {}, "Morocco": {}, "South Africa": {}, "Tunisia": {}},
        "Oceania" : {"Australia": {}, "New Zealand": {}},
        "Middle East" : {"Bahrain": {}, "Jordan": {}, "Kuwait": {}, "Lebanon": {}, "Oman": {}, "Palestine": {}, "Qatar": {}, "Saudi Arabia": {}, "United Arab Emirates": {}}
    }
    
    # loop over regions 

    # loop over countries 

    for region in spotify_country_playist_ids:
        print("'"+ region + "'" + " {")

        for country in spotify_country_playist_ids[region]:
                        
            country_data = get_country_playlist_url(country)

            spotify_country_playist_ids[region][country]['url'] = country_data['url']

            spotify_country_playist_ids[region][country]['playlist_id'] = country_data['playlist_id']

            left_curl = "{"
            right_curl = "}"

            print(f" {left_curl} '{country}' : {left_curl} 'url' : '{country_data['url']}' , 'playlist_id': '{country_data['playlist_id']}' {right_curl}{right_curl},")

            print("\n")

        print(region + " }")

    return spotify_country_playist_ids


print(build_url_playlist_id_to_dict())



