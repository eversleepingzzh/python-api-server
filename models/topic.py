from models import Mongua

class Topic(Mongua):
    __fields__ = Mongua.__fields__ + [
        ('title', str, ''),
        ('content', str, ''),
        ('user_id', int, 0),
        ('views', int, 0)
    ]

    @classmethod
    def get(cls, id):
        m = cls.find_by(id=id)
        print(m)
        if m is not None:
            m.views += 1
            m.save()
        return m
