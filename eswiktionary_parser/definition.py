class Definition:
    def __init__(self, definition: str, classification: str):
        self.definition = ensure_finishes_with_dot(definition)
        self.classification = classification
    
    def __repr__(self):
        return "[{}] {}".format(self.classification, self.definition)

def ensure_finishes_with_dot(definition: str) -> str:
    if not len(definition) >= 1:
        return definition
    
    if definition[-1] == ",":
        definition = definition[:-1] + "."
    if definition[-1] != ".":
        definition += "."
    
    return definition