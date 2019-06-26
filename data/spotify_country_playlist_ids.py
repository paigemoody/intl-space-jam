from googlesearch import search





def get_country_playlist_url(country):
    """given name of country, return playlist id from url"""

    query = f"site:open.spotify.com Top 50 on Spotify {country}"
  
    # use google.com to get one result 
    # the result is a generator object, so we need to loop through it
    for url in search(query, tld="com", num=1, stop=1, pause=4): 

        print(url)

        url_pieces = url.split("/")

        playlist_id = url_pieces[-1]

        return {'url': url, 'playlist_id' : playlist_id}
        


def build_url_playlist_id_to_dict():
    """ Add url and playlist id for each country to spotify countries dict"""
    spotify_country_playist_ids = {
        # "Asia" : { "Japan" : {}, "Israel": {}, "Hong Kong": {}, "Indonesia": {}, "Malaysia": {}, "Philippines": {}, "Singapore": {}, "Taiwan": {}, "Thailand": {}, "Vietnam": {}, "India": {}},
        # "Europe" :  {"Andorra": {}, "Austria": {}, "Belgium": {}, "Bulgaria": {}, "Cyprus": {}, "Czech Republic": {}, "Denmark": {}, "Estonia": {}, "Finland": {}, "France": {}, "Germany": {}, "Greece": {}, "Hungary": {}, "Iceland": {}, "Ireland": {}, "Italy": {}, "Latvia": {}, "Liechtenstein": {}, "Lithuania": {}, "Luxembourg": {}, "Malta": {}, "Monaco": {}, "Netherlands": {}, "Norway": {}, "Poland": {}, "Portugal": {}, "Romania": {}, "Slovakia": {}, "Spain": {}, "Sweden": {}, "Switzerland": {}, "Turkey": {}, "United Kingdom}": {}},
        "Latin America and Caribbean ": { "Argentina": {}, "Bolivia": {}, "Brazil": {}, "Chile": {}, "Colombia": {}, "Costa Rica": {}, "Dominican Republic": {}, "Ecuador": {}, "El Salvador": {}, "Guatemala": {}, "Honduras": {}, "Mexico": {}, "Nicaragua": {}, "Panama": {}, "Paraguay": {}, "Peru": {}, "Uruguay": {}},
        "North America":  {"Canada": {}, "United States" : "37i9dQZEVXbMDoHDwVN2tF"},
        "Africa" : {"Algeria": {}, "Egypt": {}, "Morocco": {}, "South Africa": {}, "Tunisia": {}},
        "Oceania" : {"Australia": {}, "New Zealand": {}},
        "Middle East" : {"Bahrain": {}, "Jordan": {}, "Kuwait": {}, "Lebanon": {}, "Oman": {}, "Palestine": {}, "Qatar": {}, "Saudi Arabia": {}, "United Arab Emirates": {}}
    }
    
    # loop over regions 

    # loop over countries 

    for region in spotify_country_playist_ids:
        print(region)

        for country in spotify_country_playist_ids[region]:
            
            print(country)
            
            country_data = get_country_playlist_url(country)

            spotify_country_playist_ids[region][country]['url'] = country_data['url']

            spotify_country_playist_ids[region][country]['playlist_id'] = country_data['playlist_id']

            print(f" {country} : 'url' : {country_data['url']} , 'playlist_id': {country_data['playlist_id']} ")

            print("\n\n\n")

    return spotify_country_playist_ids


print(build_url_playlist_id_to_dict())



Asia
Japan
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbKXQ4mDTEBXq
 Japan : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbKXQ4mDTEBXq , 'playlist_id': 37i9dQZEVXbKXQ4mDTEBXq 




Israel
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbJ6IpvItkve3
 Israel : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbJ6IpvItkve3 , 'playlist_id': 37i9dQZEVXbJ6IpvItkve3 




Hong Kong
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbLwpL8TjsxOG
 Hong Kong : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbLwpL8TjsxOG , 'playlist_id': 37i9dQZEVXbLwpL8TjsxOG 




Indonesia
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbObFQZ3JLcXt
 Indonesia : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbObFQZ3JLcXt , 'playlist_id': 37i9dQZEVXbObFQZ3JLcXt 




Malaysia
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbJlfUljuZExa
 Malaysia : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbJlfUljuZExa , 'playlist_id': 37i9dQZEVXbJlfUljuZExa 




Philippines
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbNBz9cRCSFkY
 Philippines : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbNBz9cRCSFkY , 'playlist_id': 37i9dQZEVXbNBz9cRCSFkY 




Singapore
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbK4gjvS1FjPY
 Singapore : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbK4gjvS1FjPY , 'playlist_id': 37i9dQZEVXbK4gjvS1FjPY 




Taiwan
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbMnZEatlMSiu
 Taiwan : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbMnZEatlMSiu , 'playlist_id': 37i9dQZEVXbMnZEatlMSiu 




Thailand
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbMnz8KIWsvf9
 Thailand : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbMnz8KIWsvf9 , 'playlist_id': 37i9dQZEVXbMnz8KIWsvf9 




Vietnam
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbLdGSmz6xilI
 Vietnam : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbLdGSmz6xilI , 'playlist_id': 37i9dQZEVXbLdGSmz6xilI 




India
https://open.spotify.com/user/sopgcbs63fn507qga340tl85f/playlist/24ToMDjkwvwWFhXQzrEydv
 India : 'url' : https://open.spotify.com/user/sopgcbs63fn507qga340tl85f/playlist/24ToMDjkwvwWFhXQzrEydv , 'playlist_id': 24ToMDjkwvwWFhXQzrEydv 




Europe
Andorra
https://open.spotify.com/user/spotify/playlist/0YoK1LOYnnws2wYvmH2gB4
 Andorra : 'url' : https://open.spotify.com/user/spotify/playlist/0YoK1LOYnnws2wYvmH2gB4 , 'playlist_id': 0YoK1LOYnnws2wYvmH2gB4 




Austria
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbKNHh6NIXu36
 Austria : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbKNHh6NIXu36 , 'playlist_id': 37i9dQZEVXbKNHh6NIXu36 




Belgium
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbJNSeeHswcKB
 Belgium : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbJNSeeHswcKB , 'playlist_id': 37i9dQZEVXbJNSeeHswcKB 




Bulgaria
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbNfM2w2mq1B8
 Bulgaria : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbNfM2w2mq1B8 , 'playlist_id': 37i9dQZEVXbNfM2w2mq1B8 




Cyprus
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbNBxnXSWuAcX
 Cyprus : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbNBxnXSWuAcX , 'playlist_id': 37i9dQZEVXbNBxnXSWuAcX 




Czech Republic
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbIP3c3fqVrJY
 Czech Republic : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbIP3c3fqVrJY , 'playlist_id': 37i9dQZEVXbIP3c3fqVrJY 




Denmark
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbL3J0k32lWnN
 Denmark : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbL3J0k32lWnN , 'playlist_id': 37i9dQZEVXbL3J0k32lWnN 




Estonia
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbLesry2Qw2xS
 Estonia : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbLesry2Qw2xS , 'playlist_id': 37i9dQZEVXbLesry2Qw2xS 




Finland
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbMxcczTSoGwZ
 Finland : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbMxcczTSoGwZ , 'playlist_id': 37i9dQZEVXbMxcczTSoGwZ 




France
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbIPWwFssbupI
 France : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbIPWwFssbupI , 'playlist_id': 37i9dQZEVXbIPWwFssbupI 




Germany
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbJiZcmkrIHGU
 Germany : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbJiZcmkrIHGU , 'playlist_id': 37i9dQZEVXbJiZcmkrIHGU 




Greece
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbJqdarpmTJDL
 Greece : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbJqdarpmTJDL , 'playlist_id': 37i9dQZEVXbJqdarpmTJDL 




Hungary
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbNHwMxAkvmF8
 Hungary : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbNHwMxAkvmF8 , 'playlist_id': 37i9dQZEVXbNHwMxAkvmF8 




Iceland
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbKMzVsSGQ49S
 Iceland : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbKMzVsSGQ49S , 'playlist_id': 37i9dQZEVXbKMzVsSGQ49S 




Ireland
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbKM896FDX8L1
 Ireland : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbKM896FDX8L1 , 'playlist_id': 37i9dQZEVXbKM896FDX8L1 




Italy
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbIQnj7RRhdSX
 Italy : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbIQnj7RRhdSX , 'playlist_id': 37i9dQZEVXbIQnj7RRhdSX 




Latvia
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbJWuzDrTxbKS
 Latvia : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbJWuzDrTxbKS , 'playlist_id': 37i9dQZEVXbJWuzDrTxbKS 




Liechtenstein
https://open.spotify.com/user/spotify/playlist/27o9Trolqt1osQAZJStHb6
 Liechtenstein : 'url' : https://open.spotify.com/user/spotify/playlist/27o9Trolqt1osQAZJStHb6 , 'playlist_id': 27o9Trolqt1osQAZJStHb6 




Lithuania
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbMx56Rdq5lwc
 Lithuania : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbMx56Rdq5lwc , 'playlist_id': 37i9dQZEVXbMx56Rdq5lwc 




Luxembourg
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbKGcyg6TFGx6
 Luxembourg : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbKGcyg6TFGx6 , 'playlist_id': 37i9dQZEVXbKGcyg6TFGx6 




Malta
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbMD2H5HJqmx9
 Malta : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbMD2H5HJqmx9 , 'playlist_id': 37i9dQZEVXbMD2H5HJqmx9 




Monaco
https://open.spotify.com/user/spotify/playlist/7LXKLIgNj5bQBFGJ5yCkUR
 Monaco : 'url' : https://open.spotify.com/user/spotify/playlist/7LXKLIgNj5bQBFGJ5yCkUR , 'playlist_id': 7LXKLIgNj5bQBFGJ5yCkUR 




Netherlands
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbKCF6dqVpDkS
 Netherlands : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbKCF6dqVpDkS , 'playlist_id': 37i9dQZEVXbKCF6dqVpDkS 




Norway
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbJvfa0Yxg7E7
 Norway : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbJvfa0Yxg7E7 , 'playlist_id': 37i9dQZEVXbJvfa0Yxg7E7 




Poland
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbN6itCcaL3Tt
 Poland : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbN6itCcaL3Tt , 'playlist_id': 37i9dQZEVXbN6itCcaL3Tt 




Portugal
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbKyJS56d1pgi
 Portugal : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbKyJS56d1pgi , 'playlist_id': 37i9dQZEVXbKyJS56d1pgi 




Romania
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbNZbJ6TZelCq
 Romania : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbNZbJ6TZelCq , 'playlist_id': 37i9dQZEVXbNZbJ6TZelCq 




Slovakia
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbKIVTPX9a2Sb
 Slovakia : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbKIVTPX9a2Sb , 'playlist_id': 37i9dQZEVXbKIVTPX9a2Sb 




Spain
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbNFJfN1Vw8d9
 Spain : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbNFJfN1Vw8d9 , 'playlist_id': 37i9dQZEVXbNFJfN1Vw8d9 




Sweden
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbLoATJ81JYXz
 Sweden : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbLoATJ81JYXz , 'playlist_id': 37i9dQZEVXbLoATJ81JYXz 




Switzerland
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbJiyhoAPEfMK
 Switzerland : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbJiyhoAPEfMK , 'playlist_id': 37i9dQZEVXbJiyhoAPEfMK 




Turkey
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbIVYVBNw9D5K
 Turkey : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbIVYVBNw9D5K , 'playlist_id': 37i9dQZEVXbIVYVBNw9D5K 




United Kingdom}
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbLnolsZ8PSNw
 United Kingdom} : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbLnolsZ8PSNw , 'playlist_id': 37i9dQZEVXbLnolsZ8PSNw 




Latin America and Caribbean 
Argentina
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbMMy2roB9myp
 Argentina : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbMMy2roB9myp , 'playlist_id': 37i9dQZEVXbMMy2roB9myp 




Bolivia
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbJqfMFK4d691
 Bolivia : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbJqfMFK4d691 , 'playlist_id': 37i9dQZEVXbJqfMFK4d691 



Brazil
https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbMXbN3EUUhlg
 Brazil : 'url' : https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbMXbN3EUUhlg , 'playlist_id': 37i9dQZEVXbMXbN3EUUhlg 
