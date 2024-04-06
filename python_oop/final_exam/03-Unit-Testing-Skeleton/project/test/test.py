from unittest import TestCase, main
from project.social_media import SocialMedia


class TestSocialMedia(TestCase):
    def setUp(self):
        self.media = SocialMedia("Peter", "Instagram", 200, "Music")

    def test_correct_init(self):
        self.assertEqual("Peter", self.media._username)
        self.assertEqual("Instagram", self.media._platform)
        self.assertEqual(200, self.media._followers)
        self.assertEqual("Music", self.media._content_type)
        self.assertEqual([], self.media._posts)

    def test_platform_property(self):
        self.media.platform = "YouTube"
        self.assertEqual("YouTube", self.media.platform)

        with self.assertRaises(ValueError):
            self.media.platform = "InvalidPlatform"

    def test_followers_property(self):
        self.media.followers = 300
        self.assertEqual(300, self.media.followers)

        with self.assertRaises(ValueError):
            self.media.followers = -100

    def test_create_post(self):
        post_content = "This is a test post."
        self.assertEqual("New Music post created by Peter on Instagram.", self.media.create_post(post_content))
        self.assertEqual(1, len(self.media._posts))
        self.assertEqual(post_content, self.media._posts[0]['content'])

    def test_like_post(self):
        self.media.create_post("Test post 1")
        self.assertEqual("Post liked by Peter.", self.media.like_post(0))

        # Test maximum likes
        for _ in range(10):
            self.media.like_post(0)
        self.assertEqual("Post has reached the maximum number of likes.", self.media.like_post(0))

    def test_comment_on_post(self):
        self.media.create_post("Test post 1")
        self.assertEqual("Comment added by Peter on the post.", self.media.comment_on_post(0, "Nice post!"))
        self.assertEqual(1, len(self.media._posts[0]['comments']))

        self.assertEqual("Comment should be more than 10 characters.", self.media.comment_on_post(0, "Short"))
        self.assertEqual(1, len(self.media._posts[0]['comments']))


if __name__ == "__main__":
    main()
