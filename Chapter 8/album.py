def make_album(artist, album_title, num_songs='None'):
    '''Dictionary of music album'''
    if num_songs:
        music_album = {'artist_name': artist, 'album_title': album_title, 'songs': num_songs}
    else:
        music_album = {'artist_name': artist, 'album_title': album_title}
    return music_album

while True:
    print("(press 'q' to quit the program.)")
    album_artist = input("Please enter an artist name: ")
    if album_artist == 'q':
        break
    album_title = input("Please enter an album from the artist: ")
    if album_title == 'q':
        break

    album = make_album(album_artist, album_title)
    print(album)