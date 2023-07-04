from datetime import datetime
from app.db import Base
from datetime import datetime
from app.db import Base
from .Vote import Vote
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, select, func
from sqlalchemy.orm import relationship, column_property

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    post_url = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    user = relationship('User')
    comments = relationship('Comment', cascade='all,delete')
    votes = relationship('Vote', cascade='all,delete')

    #stmt = select(func.count(Vote.id)).where(Vote.id == "spongebob")
    # stmt = select(func.count(Vote.id))
    # print(stmt)

    #print(select(func.count(Vote.id)).select_from(Vote))
    #print(select(func.count(Vote.id)).where(Vote.post_id == id))

    vote_count = column_property(
      select(func.count(Vote.id)).where(Vote.post_id == id).scalar_subquery()
    )
