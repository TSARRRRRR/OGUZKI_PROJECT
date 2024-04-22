from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Создаем базовый класс модели
Base = declarative_base()

# Определяем модель данных User
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)

# Создаем базу данных в памяти
engine = create_engine('sqlite:///:memory:')

# Создаем таблицы в базе данных
Base.metadata.create_all(engine)

# Создаем сессию для работы с базой данных
Session = sessionmaker(bind=engine)
session = Session()

# Пример добавления пользователя в базу данных
new_user = User(username='john_doe', password='secret_password')
session.add(new_user)
session.commit()

# Пример запроса пользователя из базы данных
user = session.query(User).filter_by(username='john_doe').first()
if user:
    print(f'Найден пользователь: {user.username}')
else:
    print('Пользователь не найден')
