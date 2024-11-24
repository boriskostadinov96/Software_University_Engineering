from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category) -> None:
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic) -> None:
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document) -> None:
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str) -> None:
        category_obj = next(filter(lambda c: c.id == category_id, self.categories))
        category_obj.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic_obj = next(filter(lambda t: t.id == topic_id, self.topics))
        topic_obj.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        document_obj = next(filter(lambda d: d.id == document_id, self.documents))
        document_obj.edit(new_file_name)

    def delete_category(self, category_id: int) -> None:
        category_obj = next(filter(lambda c: c.id == category_id, self.categories))
        self.categories.remove(category_obj)

    def delete_topic(self, topic_id: int) -> None:
        topic_obj = next(filter(lambda t: t.id == topic_id, self.topics))
        self.topics.remove(topic_obj)

    def delete_document(self, document_id: int) -> None:
        document_obj = next(filter(lambda d: d.id == document_id, self.documents))
        self.documents.remove(document_obj)

    def get_document(self, document_id) -> int:
        document_obj = next(filter(lambda d: d.id == document_id, self.documents))
        return document_obj.id

    def __repr__(self) -> str:
        return '\n'.join(str(d) for d in self.documents)
