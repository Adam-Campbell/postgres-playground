from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

db = create_engine("postgresql:///chinook")
base = declarative_base()


class Artist(base):
    __tablename__ = "Artist"

    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)

    albums = relationship("Album", back_populates="artist")

    def __str__(self):
        return f"Artist: {self.Name} | ID: {self.ArtistId}"



class Album(base):
    __tablename__ = "Album"

    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))

    artist = relationship("Artist", back_populates="albums")
    tracks = relationship("Track", back_populates="album")

    def __str__(self):
        return f"Album: {self.Title} | ID: {self.AlbumId} | Artist: {self.artist.Name}"



class Track(base):
    __tablename__ = "Track"

    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)

    album = relationship("Album", back_populates="tracks")

    def __str__(self):
        return f"Track: {self.Name} | ID: {self.TrackId} | Album: {self.album.Title} | Composer: {self.Composer}"



Session = sessionmaker(db)
session = Session()
base.metadata.create_all(db)


artists = session.query(Artist).filter_by(Name="Queen")

#for artist in artists:
#    print(f"Artist: {artist.Name} | ID: {artist.ArtistId}")

albums = session.query(Album).filter_by(ArtistId=artists[0].ArtistId)

#for album in albums:
    #print(f"Album: {album.Title} | ID: {album.AlbumId}")
    #print(album.artist.Name)

queen = session.query(Artist).filter_by(Name="Queen").first()

#for album in queen.albums:
#    print(f"Album: {album.Title} | ID: {album.AlbumId}")
#    if len(album.tracks) > 0:
#        print(f"Tracks:")
#        for track in album.tracks:
#            print(f"  {track.Name}")


tracks_by_queen = session.query(Track).filter_by(Composer="Queen")

for track in tracks_by_queen:
    print(track)








