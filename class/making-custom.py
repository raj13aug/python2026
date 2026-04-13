class TagCloud:
    def __init__(self):
        self.tags = {}
        
    def __add__(self, tag):
        new = TagCloud() 
        new.tags = self.tags.copy()
        tag = tag.lower()
        new.tags[tag] = new.tags.get(tag, 0) + 1
        return new
        
cloud = TagCloud()
cloud = cloud + "python"
print(cloud.tags)