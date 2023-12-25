class Definition:
    def __init__(self, definition: str, classification: str):
        self.definition = polish(definition)
        self.classification = classification
    
    def __repr__(self):
        return "[{}] {}".format(self.classification, self.definition)

def polish(definition: str) -> str:
    definition = ensure_finishes_with_dot(definition)
    return remove_unwanted_prefixes(definition)

def ensure_finishes_with_dot(definition: str) -> str:
    definition = definition.strip()
    if not len(definition) >= 1:
        return definition
    if definition[-1] == ",":
        definition = definition[:-1] + "."
    if definition[-1] != ".":
        definition += "."
    return definition

def remove_unwanted_prefixes(definition: str) -> str:
    by_extension = "Por extensión, "
    if definition.startswith(by_extension):
        return definition[len(by_extension):].capitalize()
    figure = "Fig. "
    if definition.startswith(figure):
        return definition[len(figure):].capitalize()
    return definition
