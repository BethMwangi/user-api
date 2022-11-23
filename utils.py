from flask_smorest import Page


class CursorPage(Page):
    """Flask smorest Extension class that extends Pagination"""
    @property
    def item_count(self):
        return self.collection.count()
