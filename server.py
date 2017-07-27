import webapp2

class Storage:
    messages = []


class Message:
    def __init__(self, user_name, text):
        self.user_name = user_name
        self.text = text

    def __str__(self):
        return self.user_name + ": " + self.text


class MainHandler(webapp2.RequestHandler):

    def get(self):
        self.response.write('Hello world!')


class MessageHandler(webapp2.RequestHandler):

    def get(self):
        request = self.request

        message = Message(request.get('user_name'), request.get('text'))

        Storage.messages.append(message)


class GetAllMessages(webapp2.RequestHandler):

    def get(self):
        for message in Storage.messages:
            self.response.write(message)
            self.response.write("\n")


class Clear(webapp2.RequestHandler):

   def get(self):
       Storage.messages = []


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/message', MessageHandler),
    ('/getAllMessages', GetAllMessages),
    ('/clear', Clear)

], debug=True)
