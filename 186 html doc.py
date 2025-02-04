class Tag(object):

    def __init__(self, name, contents):
        self.start_tag = '<{}>'.format(name)
        self.end_tag = '</{}>'.format(name)
        self.contents = contents

    def __str__(self):
        return "{0.start_tag}{0.contents}{0.end_tag}".format(self)

    def display(self, file=None):
        print(self, file=file)


class DocType(Tag):

    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" '
                         '"http://www.w3.org/TR/html4/strict.dtd', '')
        self.end_tag = ''   # DOCTYPE doesn't have an end_tag


class Head(Tag):

    def __init__(self, title=None):
        super().__init__('head', '')  # contents need to be added separately
        if title:
            self._title_tag = Tag('title', title)
            self.contents = str(self._title_tag)


class Body(Tag):

    def __init__(self):
        super().__init__('body', '') # contents need to be added separately
        self._body_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)

    def display(self, file=None):
        for tag in self._body_contents:
            self.contents += str(tag)

        super().display(file=file)


class HtmlDoc(object):

    def __init__(self, doc_type, head, body):
        self._doc_type = doc_type
        self._head = head
        self._body = body

    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)

    def display(self, file=None):
        self._doc_type.display(file=file)
        print("<html>", file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print("</html>", file=file)


if __name__ == "__main__":

    # my_page = HtmlDoc("Strona domowa")
    # my_page.add_tag("H1", "Main heading")
    # my_page.add_tag("H2", "Subheading")
    # my_page.add_tag("p", "Paragraph")
    # with open("e:\\index.html", "w") as index:
    #     my_page.display(index)

    new_body = Body()

    new_body.add_tag("H1", "agregation")
    new_body.add_tag("p", "W przeciwieństwie do <strong>compozycji </strong>"
                          "agregacja używa istniejących funkcji")
    new_body.add_tag("p", "Objekt compozycji nie przejmuje praw nad objektem"
                          "z którego powstał, usuwając go nie niszczymy obiektów")
    new_docType = DocType()
    new_header = Head("Agregation document")
    my_page = HtmlDoc(new_docType, new_header, new_body)

    with open("index3.html", "w") as index:
        my_page.display(file=index)