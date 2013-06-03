# -*- coding:utf-8 -*-

import sqlite3
from datetime import datetime
from contextlib import contextmanager

@contextmanager
def transaction():
  try:
    yield Database.cursor()
  finally:
    Database.commit()  
    Database.disconnect()

@contextmanager
def select():
  try:
    yield Database.cursor()
  finally:
    Database.disconnect()

class Database(object):
  con = None
  cur = None

  @staticmethod
  def connect():
    if Database.con is None:
      Database.con = sqlite3.connect('app.db')
    return Database.con

  @staticmethod
  def cursor():
    Database.connect()
    if Database.cur is None:
      Database.cur = Database.con.cursor()
    return Database.cur

  @staticmethod
  def disconnect():
    if not Database.cur is None:
      Database.cur.close()
      Database.cur = None

    if not Database.con is None:
      Database.con.close()
      Database.con = None
  
  @staticmethod
  def close_cursor():
    if not Database.cur is None:
      Database.cur.close()
      Database.cur = None

  @staticmethod
  def commit():
    if Database.con is None:
      return False
    Database.con.commit()

  @staticmethod
  def moulding_dataset():
    rows = Database.cur.fetchall()
    column_names = list(
      map(lambda x: x[0], Database.cur.description)
    )
    return [dict(zip(column_names, r)) for r in rows]
