def audio_features_to_grab(track_uri, list_of_audio_features):
    audio_features_to_return = {}
    all_audio_features = sp.audio_features(track_uri)[0]

    for feature in list_of_audio_features:
        audio_features_to_return[feature] = all_audio_features[feature]

    return audio_features_to_return


def get_playlist_track_info(playlist_uri, list_of_audio_features=['danceability','energy','key','loudness','mode','speechiness','acousticness','instrumentalness','liveness','valence','tempo','time_signature']):
    d = {}
    playlist_items = sp.playlist_items(playlist_uri)['items']
    
    for track in playlist_items:
        track_info = track['track']
        track_uri = track_info['uri']
        track_name = track_info['name']
        track_duration = track_info['duration_ms']
        track_popularity = track_info['popularity']
        track_is_explicit = track_info['explicit']
        
        first_artist_info = track_info['artists'][0]
        first_artist_info_name = first_artist_info['name']

        d['uri'] = track_info['uri']
        d['first_artist_name'] = first_artist_info['name']
        d['track_name'] = track_info['name']
        d['track_duration_ms'] = track_info['duration_ms']
        d['track_popularity'] = track_info['popularity']
        d['is_track_explicit'] = track_info['explicit']
    

        track_audio_features = audio_features_to_grab(track_uri=track_uri, list_of_audio_features=list_of_audio_features)

        d.update(track_audio_features)
        
        return d


def get_track_info(track_dict:dict, list_of_audio_features=['danceability','energy','key','loudness','mode','speechiness','acousticness','instrumentalness','liveness','valence','tempo','time_signature']):
    d = {}
    
    track_info = track['track']
    track_uri = track_info['uri']
    track_name = track_info['name']
    track_duration = track_info['duration_ms']
    track_popularity = track_info['popularity']
    track_is_explicit = track_info['explicit']
    
    first_artist_info = track_info['artists'][0]
    first_artist_info_name = first_artist_info['name']

    d['uri'] = track_info['uri']
    d['first_artist_name'] = first_artist_info['name']
    d['track_name'] = track_info['name']
    d['track_duration_ms'] = track_info['duration_ms']
    d['track_popularity'] = track_info['popularity']
    d['is_track_explicit'] = track_info['explicit']


    track_audio_features = audio_features_to_grab(track_uri=track_uri, list_of_audio_features=list_of_audio_features)
    
    d.update(track_audio_features)

    return d