import os

from reader.compressed import bzipped, gzipped

# Open with the correct opener for the given extension.

extension_map = {
    '.bz2': bzipped.opener,
    '.gz': gzipped.opener,
}

# We give the reader a filename, get it's extension, and from the dictionary we get the value of it.
# opener = dcitionary.get(key/extension/, open/value to return if key not found/
# f class attribute = opener/gzip.open or bzip.open/(filename, ReadText)
# Then a method for closing and reading the f file.
class Reader:
    def __init__(self, filename):
        extension = os.path.splitext(filename)[1]   # We split the filename, and get the extension ([1])
        opener = extension_map.get(extension, open) # Opener will be either bzipped.opener or gzipped.opener or open(default)
        self.f = opener(filename, 'rt')             # Read Text of the filename with correct opener.

    def close(self):
        self.f.close()                              # Close the file.

    def read(self):
        return self.f.read()                        # Read the file.