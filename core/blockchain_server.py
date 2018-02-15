from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Ticket(Resource):
    def get(self, ticket_id):
        return {"get ticket": ticket_id}


class TicketByEvent(Resource): 
    """

    Endpoint that lists all the tickets available for an event.

    """

    def get(self):
        return {"list tickets": "TODO"}


class TicketByUser(Resource): 
    """

    Endpoint that lists all the tickets owned by a given user.

    """
    def get(self, user_id):
        return {"list tickets": "TODO"}


class TicketBuy(Resource):
    def post(self):
        return {"put ticket": "TODO"}


api.add_resource(TicketByUser, "/tickets/")
api.add_resource(TicketBuy, "/tickets/buy")
api.add_resource(Ticket, "/tickets/<ticket_id>")

if __name__ == "__main__":
    app.run(debug=True)
