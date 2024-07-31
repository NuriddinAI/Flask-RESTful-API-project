from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

books = ["book 1", "book 2"]

class Book(Resource):
    def get(self, book_id):
        for book in books:
            if book['id'] == book_id:
                return book, 200
        return {"message": "Book not found"}, 404

    def post(self, book_id):
        data = request.get_json()
        for book in books:
            if book['id'] == book_id:
                return {"message": f"Book with id {book_id} already exists"}, 400
        book = {
            'id': book_id,
            'title': data['title'],
            'author': data['author']
        }
        books.append(book)
        return book, 201

    def delete(self, book_id):
        global books
        books = [book for book in books if book["id"] != book_id]
        return {"message": f"Book with id {book_id} is deleted."}, 200

class BookList(Resource):
    def get(self):
        return books, 200

class HelloWorld(Resource):
    def get(self):
        return {"message": "Welcome to the Books API"}, 200

api.add_resource(Book, "/book/<int:book_id>")
api.add_resource(BookList, "/books")
api.add_resource(HelloWorld, "/")

if __name__ == '__main__':
    app.run(debug=True)

