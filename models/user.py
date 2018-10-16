from models import Mongua


class User(Mongua):
    """
    User 是一个保存用户数据的 model
    现在只有两个属性 username 和 password
    """
    __fields__ = Mongua.__fields__ + [
        ('username', str, ''),
        ('password', str, ''),
    ]

    def salted_password(self, password, salt='$!@><?>HUI&DWQa`'):
        import hashlib
        def sha256(ascii_str):
            return hashlib.sha256(ascii_str.encode('ascii')).hexdigest()
        hash1 = sha256(password)
        hash2 = sha256(hash1 + salt)
        return hash2


    def from_form(self, form):
        self.id = form.get('id', None)
        self.username = form.get('username', '')
        self.password = form.get('password', '')


    @classmethod
    def register(cls, form):
        name = form.get('username', '')
        pwd = form.get('password', '')
        if len(name) > 2:
            u = User.new(form)
            u.password = u.salted_password(pwd)
            u.save()
            return u
        else:
            return None

    @classmethod
    def validate_login(cls, form):
        u = User()
        u.from_form(form)
        user = User.find_by(username=u.username)
        print(user.__dict__)
        if user is not None and user.password == u.salted_password(u.password):
            return user
        else:
            return None
