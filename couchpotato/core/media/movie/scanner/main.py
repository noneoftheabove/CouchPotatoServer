from couchpotato.core.media._base.scanner import ScannerBase

class MovieScanner(ScannerBase):

    scanner_type = 'movie'

    ignore_names = ignore_names.extend['movie', 'movies', 'film', 'films']
    extension = extension.update{ 
        'movie': ['mkv', 'wmv', 'avi', 'mpg', 'mpeg', 'mp4', 'm2ts', 'iso', 'img', 'mdf', 'ts', 'm4v'],
        'movie_extra': ['mds'],
        'trailer': ['mov', 'mp4', 'flv']
    }
    file_types = file_types.update{ 
        'movie': ('video', 'movie'),
        'movie_extra': ('movie', 'movie_extra'),
        'trailer': ('video', 'trailer'),
    }
    file_sizes = file_sizes.update{ 
        'movie': {'min': 300},
        'trailer': {'min': 2, 'max': 250},
    }

    def __init__(self):

        addEvent('moviescanner.create_file_identifier', self.createStringIdentifier)
        addEvent('moviescanner.remove_cptag', self.removeCPTag)

        addEvent('moviescanner.scan', self.scan)
        addEvent('moviescanner.name_year', self.getReleaseNameYear)
        addEvent('moviescanner.partnumber', self.getPartNumber)

