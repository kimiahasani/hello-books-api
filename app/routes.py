from crypt import methods
from urllib import response
from flask import Blueprint, jsonify
class Book:
    def __init__(self, id, title, description) -> None:
        self.id = id
        self.title = title
        self.description = description
books = [
    Book(1, "Fictional Book", "A fantasy novel set in an imaginary world."),
    Book(2, "Wheel of Time", "A fantasy novel set in an imaginary"),
    Book(3, "Fictional Book Title", "A fantsy novel set in an imaginary world"),
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
@books_bp.route("/<book_id>", methods=["GET"])
def handle_book(book_id):
    try:
        book_id = int(book_id)
    except:
        return {"message":f"book {book_id} invalid"}, 404

    for book in books:
        if book.id == book_id:
            return {
                "id": book.id,
                "title": book.title,
                "description": book.description,
            }
    return {"message":f"book {book_id} not found"}, 404



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