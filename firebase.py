import pyrebase
from parse import parse_form
from search import get_jobs
firebaseConfig = {
  'apiKey': "AIzaSyBLnSVPKdzgp0EqSwbOUnqeN0RBrBggdiw",
  'authDomain': "recogx-603c8.firebaseapp.com",
  'databaseURL': "https://recogx-603c8.firebaseio.com",
  'projectId': "recogx-603c8",
  'storageBucket': "recogx-603c8.appspot.com",
#   'messagingSenderId': "840991282038",
#   'appId': "1:840991282038:web:0e2dbce09c7fbedd60e057",
#   'measurementId': "G-Z7XYVP2KZ3"
}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

users = db.child('users').get()
keys = []

def stream_handler(message):
  data = message["data"]
  print("message: ", data)
  for key in data.keys():
    resume = db.child('resumes').child(key).get()
    if resume.val() != None:
        link = resume.val()['link']
        skills = parse_form(firebaseConfig['projectId'], link)
        jobs = []
        for skill in skills:
          companies, titles, descs, errors = get_jobs(skill)
          dupls = []
          for i in range(len(companies)):
            if titles[i] in dupls:
              continue
            dupls.append(titles[i])
            job = {
              'company': companies[i],
              'title': titles[i],
              'description': descs[i],
              'error': None
            }
            jobs.append(job)
            if jobs == []:
              jobs = 'No jobs found!'
        db.child('resumes').child(key).update({'skills': skills})
        db.child('resumes').child(key).update({'jobs':jobs})

def listen():
  my_stream = db.child("resumes").stream(stream_handler)

  while True:
    data = input("[{}] Type exit to disconnect: ".format('?'))
    if data.strip().lower() == 'exit':
      print('Stopped Stream Handler')
      my_stream.close()
      break
listen()

from flask import Flask
app = Flask(__name__)

if __name__ == '__main__':
  app.run()