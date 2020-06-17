class PostManager:

    def __init__(self, posts):
        self.posts = posts

    def get_posts_by_ids(self, post_ids):
        return list(filter(lambda i: i['id'] in post_ids, self.posts))

    def get_post_by_id(self, post_id):
        return self.get_posts_by_ids([post_id])[0]

    def find_relevant_post_ids(self, post_id):
        compeared_post = self.get_post_by_id(post_id)
        compared_post_tags = set(compeared_post['tags'])
        result = []
        for post in self.posts:
            if post['id'] == compeared_post['id']:
                continue
            post_tags = set(post['tags'])
            match_tags_length = len(compared_post_tags.intersection(post_tags))
            if not match_tags_length:
                continue
            result.append([post['id'], match_tags_length])
        sorted(result, key=lambda i: i[1], reverse=True)
        result = [r[0] for r in result]
        return result
        