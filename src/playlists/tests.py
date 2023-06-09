from django.test import TestCase
from django.utils import timezone
from django.utils.text import slugify

from djangoflix.db.models import PublishStateOption
from videos.models import Video
from .models import Playlist


class PlaylistModelTestCase(TestCase):

    def create_show_with_seasons(self):
        the_office = Playlist.objects.create(title="The Offirce Series")
        season_1 = Playlist.objects.create(title="The Office Series Season 1", 
        parent=the_office, order=1)
        season_2 = Playlist.objects.create(title="The Office Series Season 2",
        parent=the_office, order=2)
        season_3 = Playlist.objects.create(title="The Office Series Season 3",
        parent=the_office, order=3)
        self.show = the_office


    def create_videos(self):
        video_a = Video.objects.create(title='My title',
        video_id='abs123')
        video_b = Video.objects.create(title='My title',
        video_id='absasda123')
        video_c = Video.objects.create(title='My title',
        video_id='absasd123')
        self.video_a = video_a
        self.video_b = video_b
        self.video_c = video_c
        self.video_qs = Video.objects.all()


    def setUp(self):
        self.create_videos()
        self.create_show_with_seasons()
        self.obj_a = Playlist.objects.create(title = 'This is my title', video=self.video_a)
        obj_b = Playlist.objects.create(title = 'This is my title', 
        state = PublishStateOption.PUBLISH, video=self.video_a)
        # obj_b.videos.set([self.video_a, self.video_b, self.video_c])
        obj_b.videos.set(self.video_qs)
        obj_b.save()
        self.obj_b = obj_b

    def test_show_has_seasons(self):
        seasons = self.show.playlist_set.all()
        self.assertEqual(seasons.count(), 3)

    def test_playlist_video(self):
        self.assertEqual(self.obj_a.video, self.video_a)

    def test_playlist_video_items(self):
        count = self.obj_b.videos.all().count()
        self.assertEqual(count, 3)

    def test_playlist_video_through_model(self):
        v_qs = sorted(list(self.video_qs.values_list('id')))
        video_qs = sorted(list(self.obj_b.videos.all().values_list('id')))
        playlist_item_qs = sorted(list(self.obj_b.playlistitem_set.all().values_list('video')))
        self.assertEqual(v_qs, video_qs, playlist_item_qs)
         
    def test_video_playlist_ids_property(self):
        ids = self.obj_a.video.get_playlist_ids()
        actual_ids = list(Playlist.objects.filter(video=self.
        video_a).values_list('id', flat=True))
        self.assertEqual(ids, actual_ids)

    def test_video_playlist(self):
        qs = self.video_a.playlist_featured.all()
        self.assertEqual(qs.count(), 2)

    def test_slug_field(self):
        title = self.obj_a.title
        test_slug = slugify(title)
        self.assertEqual(test_slug, self.obj_a.slug)

    def test_vaild_title(self):
        title = 'This is my title'
        qs = Playlist.objects.filter(title=title)
        self.assertTrue(qs.exists())

    def test_created_count(self):
        title = 'This is my title'
        qs = Playlist.objects.all()
        self.assertEqual(qs.count(), 6)

    def test_draft_case(self):
        qs = Playlist.objects.filter(state=PublishStateOption.DRAFT)
        self.assertEqual(qs.count(), 5)

    def test_publish_case(self):
        qs = Playlist.objects.filter(state=PublishStateOption.PUBLISH)
        now = timezone.now()
        published_qs = Playlist.objects.filter(
            state=PublishStateOption.PUBLISH,
            publish_timestamp__lte= now,
            )
        self.assertTrue(published_qs.exists())

    def test_publish_manager(self):
        published_qs = Playlist.objects.all().published()
        published_qs_2 = Playlist.objects.published()
        self.assertTrue(published_qs.exists())
        self.assertEqual(published_qs.count(), published_qs_2.count())
