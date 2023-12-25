def source_url_or_default(source_url: str = None) -> str:
    if source_url:
        return source_url
    return "https://dumps.wikimedia.org/eswiktionary/latest/eswiktionary-latest-pages-articles.xml.bz2"

def target_filename_or_default(target_filename: str = None) -> tuple:
    if target_filename:
        return "{}.bz2".format(target_filename), target_filename
    compressed_filename="downloads/eswiktionary-latest-pages-articles.xml.bz2"
    target_filename = compressed_filename[:-4]
    return compressed_filename, target_filename
