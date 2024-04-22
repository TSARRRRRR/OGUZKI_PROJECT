from flask import Flask, request, render_template
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Создаем базовый класс Flask-приложения
app = Flask(__name__)

# Создаем базу данных в памяти
engine = create_engine('sqlite:///:memory:')
Base = declarative_base()

# Определяем модель данных User
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Маршрут для отображения страницы регистрации
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        new_user = User(username=username, password=password)
        session.add(new_user)
        session.commit()
        
        return 'Пользователь зарегистрирован успешно!'
    
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
