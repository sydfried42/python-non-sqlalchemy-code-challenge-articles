class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
           if isinstance(new_title, str) and 5 <= len(new_title) <= 50 and not hasattr(self, "_title"):
                self._title = new_title
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_author):
           if isinstance(new_author, Author):
                self._author = new_author

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, new_magazine):
           if isinstance(new_magazine, Magazine):
                self._magazine = new_magazine
        
class Author:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
           if isinstance(new_name, str) and len(new_name) > 0 and not hasattr(self, "_name"):
                self._name = new_name

    def articles(self):
        return [article for article in Article.all if article.author is self and isinstance(article, Article)]

    def magazines(self):
        magazine_list = []
        for article in Article.all:
            if article.author is self and isinstance(article.magazine, Magazine) and article.magazine not in magazine_list:
                magazine_list.append(article.magazine)
        return magazine_list

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        category_list = []
        for article in Article.all:
            if article.author is self and article.magazine.category not in category_list:
                category_list.append(article.magazine.category)  
        if len(category_list) == 0:
            return None
        return category_list


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
           if isinstance(new_name, str) and 2 <= len(new_name) <= 16:
                self._name = new_name

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, new_category):
           if isinstance(new_category, str) and len(new_category) > 0:
                self._category = new_category

    def articles(self):
        return [article for article in Article.all if article.magazine is self and isinstance(article, Article)]

    def contributors(self):
        authors_list = []
        for article in Article.all:
            if article.magazine is self and isinstance(article.author, Author) and article.author not in authors_list:
                authors_list.append(article.author)
        return authors_list

    def article_titles(self):
        titles_list = []
        for article in Article.all:
            if article.magazine is self:
                titles_list.append(article.title)
        if len(titles_list) == 0:
            return None
        return titles_list

    def contributing_authors(self):
        duplicate_list = []
        for article in Article.all:
            if article.magazine is self and isinstance(article.author, Author):
                duplicate_list.append(article.author)
        
        author_article_counts = {}
        for author in duplicate_list:
            if author in author_article_counts:
                author_article_counts[author] += 1
            else:
                author_article_counts[author] = 1
        
        contributing_authors = [author for author, count in author_article_counts.items() if count > 2]
        
        if len (contributing_authors) == 0:
            return None
        return contributing_authors