from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    create_tables()

    author1 = Author(name="Author 1")
    author2 = Author(name="Author 2")

    magazine1 = Magazine(name="Magazine 1", category="Tech")
    magazine2 = Magazine(name="Magazine 2", category="Health")

    article1 = Article(author=author1, magazine=magazine1, title="Article Title 1")
    article2 = Article(author=author1, magazine=magazine2, title="Article Title 2")
    article3 = Article(author=author2, magazine=magazine1, title="Article Title 3")

    print("Author 1 Articles:", author1.articles())
    print("Author 1 Magazines:", author1.magazines())
    
    print("Magazine 1 Articles:", magazine1.articles())
    print("Magazine 1 Contributors:", magazine1.contributors())
    print("Magazine 1 Article Titles:", magazine1.article_titles())
    print("Magazine 1 Contributing Authors:", magazine1.contributing_authors())

if __name__ == "__main__":
    main()