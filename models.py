from exts import db


class Course(db.Model):
    __tablename__ = 'iv_course'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    price = db.Column(db.Numeric(6, 2))
    teacher_id = db.Column(db.Integer, db.ForeignKey('iv_teacher.id'))

    def __repr__(self):
        return 'Course:%s' % self.name


class Student(db.Model):
    __tablename__ = 'iv_student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)
    age = db.Column(db.SmallInteger)
    sex = db.Column(db.Boolean, default=1)

    def __repr__(self):
        return 'Student:%s' % self.name


class Teacher(db.Model):
    __tablename__ = 'iv_teacher'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # 关联
    courses = db.relationship('Course', backref='teacher', lazy='subquery')

    def __repr__(self):
        return 'Teacher:%s' % self.name

