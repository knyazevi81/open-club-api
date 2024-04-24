from sqlalchemy.orm import sessionmaker
from schemas import engine, User


Session = sessionmaker(autoflush=False, bind=engine)
db = Session()


#tom = User(name="Khasan", user_status=1)
#db.add(tom)
#db.commit()


#data = db.query(User).all()

#for c in data:
#    print(f"{c.id}-{c.name}-{c.user_status}")\

data = db.get(User, 1)

print(f"{data.id}{data.name}{data.user_status}")