from models import Mongua
from models.user import User
from utils import obj_from_model


class Reply(Mongua):
    __fields__ = Mongua.__fields__ + [
        ('user_id', int, 0),
        ('content', str, ''),
        ('topic_id', int, ''),
    ]

    @classmethod
    def user_reply(cls, **kwargs):
        res = cls.all(**kwargs)
        for r in res:
            id  = r.__dict__['user_id']
            u = User.find_by(id=id)
            name = u.__dict__['username']
            print('name', name)
            setattr(r, 'username', name)
        return res


