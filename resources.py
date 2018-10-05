# The most awesome database ever! Mongo, you've got nothing on us...
item_votes = {}


class UpvoteResource():
    def on_get(self, req, resp):
        item_name = req.params['item_name']

        self.upvote(item_name)

        resp.body = "{} now has {} votes".format(item_name, item_votes[item_name])

    def on_post(self, req, resp):
        json_data = req.media
        item_name = json_data['item_name']

        self.upvote(item_name)

        resp.body = "{} now has {} votes".format(item_name, item_votes[item_name])

    def upvote(self, item_name):
        item_votes.setdefault(item_name, 0)
        item_votes[item_name] += 1


class DownvoteResource():
    def on_get(self, req, resp):
        item_name = req.params['item_name']

        item_votes.setdefault(item_name, 0)
        item_votes[item_name] -= 1

        resp.body = "{} now has {} votes".format(item_name, item_votes[item_name])


class TallyResource():
    def on_get(self, req, resp):
        resp.media = item_votes


class DefaultResource():
    def on_get(self, req, resp):
        resp.body = "Hello!"
