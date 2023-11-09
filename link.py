import json

class Link:
    def __init__(self, url, title, context):
        self.url = url
        self.title = title
        self.context = context

class LinkCollection:
    def __init__(self):
        self.links = []

    def add_link(self, link):
        self.links.append(link)

    def remove_link(self, link):
        self.links.remove(link)

    def search_links(self, query):
        results = []
        for link in self.links:
            if query.lower() in link.title.lower():
                results.append(link)
        return results

    def save_to_file(self, filename):
        data = []
        for link in self.links:
            data.append({
                'url': link.url,
                'title': link.title,
                'context': link.context
            })
        with open(filename, 'w') as file:
            json.dump(data, file)

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        for item in data:
            link = Link(item['url'], item['title'], item['context'])
            self.add_link(link)


link_collection = LinkCollection()


link1 = Link('https://docs.djangoproject.com/en/4.2/intro/tutorial01/', 'Example Website', 'Web Resources')
link2 = Link('https://www.youtube.com/watch?v=PtQiiknWUcI&t=17s', 'Example Organization', 'Resources')
link3 = Link('https://www.youtube.com/watch?v=gDUzaANQ01A', 'Example Video', 'Video Materials')
link_collection.add_link(link1)
link_collection.add_link(link2)
link_collection.add_link(link3)

# Пошук посилань
search_results = link_collection.search_links('example')
for result in search_results:
    print(result.title, result.url)

link_collection.save_to_file('links.json')


link_collection.load_from_file('links.json')
 