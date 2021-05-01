# intl-space-jam
Get most popular songs in country under current ISS location.

![readme screenshot](https://user-images.githubusercontent.com/25571355/110048637-395fc280-7d1e-11eb-8997-b003d2b41b33.png)

ISS location updates every 5 seconds (sourced from http://api.open-notify.org/).

Set-up

1. Virtual environment
```
python3 -m venv env
source env/bin/activate

```
2. Create secrets.sh and add your personal spotify keys (see [Spotify Developer](https://developer.spotify.com/documentation/general/guides/authorization-guide/)). The file should look like:

```
export spotify_client_id='<your client id>'

export spotify_client_secret='<your client secret>'

export flask_session_key='ABCD'
```

3. Export your secrets
```
source secrets.sh
```

4. Run app:

```
python3 server.py
```
