from models import Mongua
from models.user import User
from models.reply import Reply


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
        if m is not None:
            m.views += 1
            m.save()
        return m

    @classmethod
    def get_all(cls):
        ms = cls.all()
        for m in ms:
            id = m.user_id
            u = User.find_by(id=id)
            setattr(m, "username", u.username)
            # 加上评论数
            res = Reply.all(topic_id=m.id)
            setattr(m, 're_count', len(res))
        return ms

