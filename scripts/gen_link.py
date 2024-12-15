from jinja2 import Environment, FileSystemLoader
import pathlib
import sys
import glob
import dataclasses as dc

environment = Environment(loader=FileSystemLoader(pathlib.Path(__file__).parents[0] / "templates"))
template = environment.get_template("content.template.html")


@dc.dataclass
class Book:
    link: str
    name: str


@dc.dataclass
class Author:
    name: str
    books: list[Book]


def generate(input_dir: str, output_file: str):
    authors = []
    for author_dir in glob.glob(input_dir + '/*'):
        author_path = pathlib.Path(author_dir)
        author = Author(author_path.name, [])
        if author_path.is_dir():
            for book_file in glob.glob(f'{str(author_path)}/*'):
                book = Book(name=pathlib.Path(book_file).stem,
                            link=pathlib.Path(book_file).as_posix())
                author.books.append(book)
        else:
            author.books.append(Book(name=author_path.stem,
                                     link=author_path.as_posix()))
        authors.append(author)
    #print(authors)

    with open(output_file, mode="w", encoding="utf-8") as results:
        context = {
            'title': '######',
            "authors": authors,
            'add_wikipedia': False,
        }
        results.write(template.render(context))


if len(sys.argv) != 3:
    print(f'{pathlib.Path(sys.argv[0]).name} <text dir> <out file>')
    exit(-1)

generate(sys.argv[1], sys.argv[2])
