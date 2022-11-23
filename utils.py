from flask_smorest import Page
from extensions import cache


class CursorPage(Page):
    """Flask smorest Extension class that extends Pagination"""

    @property
    def item_count(self):
        return self.collection.count()


def clear_cache(key_prefix):
    keys = [key for key in cache.cache._cache.keys() if key.startswith(key_prefix)]
    cache.delete_many(*keys)
