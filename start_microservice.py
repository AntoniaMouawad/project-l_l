from wsgiref import simple_server

import falcon

from resources import UpvoteResource, DownvoteResource, DefaultResource, TallyResource

app = falcon.API()

app.add_route('/', DefaultResource())
app.add_route('/upvote', UpvoteResource())
app.add_route('/downvote', DownvoteResource())
app.add_route('/current_tally', TallyResource())

if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    print("Running!")
    httpd.serve_forever()
