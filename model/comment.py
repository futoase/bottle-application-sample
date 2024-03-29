# -*- coding:utf-8 -*-

from datetime import datetime
from database import Database, transaction, select

class Comment(Database):
  def __init__(self, **kwargs):
    for key in kwargs:
      self.__dict__[key] = kwargs[key]
  
  @staticmethod
  def add(user_name, comment):
    user_name = user_name.encode('latin1').decode('utf8')
    comment = comment.encode('latin1').decode('utf8')
    created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with transaction() as cursor:
      cursor.execute('''
        INSERT INTO `comments`
          (`user_name`, `body`, `created_at`)
          VALUES
          (?, ?, ?)
        ''',  
        (user_name, comment, created_at)
      )

  @staticmethod
  def list():
    results = []
    with select() as cursor:
      cursor.execute('''
        SELECT * FROM `comments` 
          ORDER BY `comment_id` DESC
      ''')
      records = Database.moulding_dataset()
      for record in records:
        results.append(Comment(**record)) 

    return results
