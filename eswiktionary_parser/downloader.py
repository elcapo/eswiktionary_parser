import bz2
from os import remove
from os.path import isfile
from urllib.request import urlretrieve
from eswiktionary_parser import defaults

def download(source_url: str = None, target_filename: str = None):
    source_url = defaults.source_url_or_default(source_url)
    compressed_filename, target_filename = defaults.target_filename_or_default(target_filename)
    
    if isfile(compressed_filename) or isfile(target_filename):
        return
    urlretrieve(source_url, compressed_filename)
    
    zipfile = bz2.BZ2File(compressed_filename)
    uncompressed_data = zipfile.read()
    open(target_filename, "wb").write(uncompressed_data)

    remove(compressed_filename)

if __name__ == "__main__":
    download()