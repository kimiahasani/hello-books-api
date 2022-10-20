from crypt import methods
from urllib import response
from flask import Blueprint, jsonify
class Book:
    def __init__(self, id, title, description) -> None:
        self.id = id
        self.title = title
        self.description = description
books = [
    Book(1, "Book A", "Description A"),
    Book(2, "Book B", "Description B"),
    Book(3, "Book C", "Description C"),
]
hello_world_bp = Blueprint("hello_world", __name__)

books_bp = Blueprint("books", __name__, url_prefix= "/books")

@books_bp.route("", methods=["GET"])
def handle_books():
    books_response = []
    for book in books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "description":book.description,
        })
    return jsonify(books_response), 200
# @books_bp.route("/<book_id>", methods = ["GET"])
# def handel_book(book_id):
#     book_id = int(book_id)
#     for book in books:
#         if book.id == book_id:
#             return {
#                 "id": book.id,
#                 "title": book.title,
#                 "description": book.description
#             }



@hello_world_bp.route("/hello-world", methods =["GET"]
)
def say_hello_world():
    my_beatiful_world= "Hello, World!"
    return my_beatiful_world, 200

@hello_world_bp.route("/hello/JSON", methods =["GET"])
def say_hello_json():
    return {
        "name":"kimia",
        "message": "Love Her Family",
        "hobbies": ["hiking", "coding", "cooking"]
    },200

@hello_world_bp.route("/broken-endpoint-with-broken-server-code", methods=["GET"])
def broken_endpoint():
    response_body = {
        "name": "My Lovely Family","message": "I Love You","hobbies": ["Swimming", "Watching TV"]
    }
    new_hobby = "Surfing"
    response_body["hobbies"].append(new_hobby) 
    return response_body