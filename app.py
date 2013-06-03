# -*- coding:utf-8 -*-
#!/usr/bin/env python

import sys
from bottle import route, request, redirect, run, template

from model.comment import Comment

@route('/', method="GET")
def comments():
  with open('view/comments.html') as t:
    renderd = template(t.read(), rows=Comment.list())
  return renderd

@route('/comment', method="POST")
def post_comment():
  user_name = request.params.get('user_name', '')
  comment = request.params.get('comment', '')

  if len(user_name) == 0 or len(comment) == 0:
    redirect('/')

  Comment.add(user_name, comment)
  redirect('/')

if __name__ == '__main__':
  run(host='127.0.0.1', port=3000, reloader=True, debug=True)

