import pytest

from main import PostManager


@pytest.fixture
def posts():
    return [
        {'id': 1, 'text': 'post1', 'tags': ['foo', 'bar', 'baz']},
        {'id': 2, 'text': 'post2', 'tags': ['dich', 'sha']},
        {'id': 3, 'text': 'post3', 'tags': ['bar', 'baz', 'dich']},
        {'id': 4, 'text': 'post4', 'tags': ['bar', 'sha', 'dich']}, 
]


@pytest.fixture
def post_manager(posts):
    return PostManager(posts)



class TestPosts:

    def test_get_post_by_ids(self, post_manager):
        post = post_manager.get_post_by_id(2)
        assert post['id'] == 2
    
    @pytest.mark.parametrize('post_id, result', [
        (1, [3, 4]),
        (3, [1, 2, 4]),
        (4, [1, 2, 3]),
    ])
    def test_find_relevant_posts(self, post_manager, post_id, result):
        sorted_posts = post_manager.find_relevant_post_ids(post_id)
        assert sorted_posts == result