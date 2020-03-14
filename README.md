# intl-space-jam
Get most popular songs in country under current ISS location.

![readme screenshot](https://user-images.githubusercontent.com/25571355/76674095-ef0f8f80-6568-11ea-971c-6d6d7ce233fa.png)

ISS location updates every 5 seconds - sourced from http://api.open-notify.org/.

Set-up

1. Virtual environment
```
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
$ source secrets.sh
```

4. Run app:

```
python3 server.py
```