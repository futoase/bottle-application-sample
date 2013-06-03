# -*- coding:utf-8 -*-

import sqlite3

def migrate():
  con = sqlite3.connect('app.db')
  cur = con.cursor()

  try:
    print('create comments table.')
    cur.execute('''
      CREATE TABLE `comments` (
        `comment_id` INTEGER NOT NULL PRIMARY KEY,
        `user_name` TEXT NOT NULL,
        `body` TEXT NOT NULL,
        `created_at` INTEGER NOT NULL
      )
    ''')
  except sqlite3.Error as e:
    print("ERROR!", e)
  else:
    con.commit()
    print('created!')
  finally:
    cur.close()
    con.close()

if __name__ == '__main__':
  migrate()
