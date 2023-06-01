## Playlist of Playlists

```python

from playlists.models import Playlist

the_office = PLaylist.object.create(title='The Office Series')
# featured video / videos /


season_1 = PLaylist.object.create(title='The Office Series Season 1', parent=the_office, order=1)
# featured video / videos /

season_2 = PLaylist.object.create(title='The Office Series Season 2',parent=the_office, order=2)
# featured video / videos /

season_3 = PLaylist.object.create(title='The Office Series Season 3', parent=the_office, order=3)
# featured video / videos /


shows = Playlist.objects.filter(parent__isnull=True)
show = Playlist.object.get(id=1)
# seasons = Playlist.objects.filter(parent=show)
```