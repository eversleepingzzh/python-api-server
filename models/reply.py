from models import Mongua

class Reply(Mongua):
    __fields__ = Mongua.__fields__ + [
        ('user_id', int, 0),
        ('content', str, ''),
        ('topic_id', str, ''),
    ]

