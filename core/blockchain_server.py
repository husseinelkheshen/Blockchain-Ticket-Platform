from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Ticket(Resource):
    def get(self, ticket_id):
        return {"get ticket": ticket_id}

class TicketList(Resource):
    def get(self):
        return {"list tickets": "TODO"}


api.add_resource(TicketList, "/tickets")
api.add_resource(Ticket, "/tickets/<ticket_id>")

if __name__ == "__main__":
    app.run(debug=True)
