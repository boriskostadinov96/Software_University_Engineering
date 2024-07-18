from sqlalchemy.orm import sessionmaker
from models import User, engine

Session = sessionmaker(bind=engine)
with Session as session:
    user_to_update = session.query(User).filter_by(username='ivan').first()

    if user_to_update:
        user_to_update.email = 'some_mail.abv.bg'
        session.commit()
        print('User upadted')

    else:
        print('False')