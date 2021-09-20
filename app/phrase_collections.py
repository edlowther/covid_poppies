from collections import namedtuple

class PhraseCollections:
    def __init__(self):
        self.lookup = self.initialise_lookup()

    def initialise_lookup(self):
        Note = namedtuple('Note', ['pitch', 'duration', 'accent'])
        Note.__new__.__defaults__ = (None,) * len(Note._fields)
        Phrase = namedtuple('Phrase', 'notes')
        PhraseCollection = namedtuple('PhraseCollection', 'phrases')
        lookup = {
            'pp': PhraseCollection([Phrase([Note(69, 3), Note(69, 1)]),
                   Phrase([Note(62, 3), Note(60, 1)]),
                   Phrase([Note(53, 3), Note(52, 1)]),
                   Phrase([Note(43, 3), Note(43, 1)])]),

            'p' : PhraseCollection([Phrase([Note(70, 1), Note(74, 2, 'accent'), Note(70, 1)]),
                   Phrase([Note(62, 1), Note(62, 2, 'accent'), Note(62, 1)]),
                   Phrase([Note(53, 1), Note(53, 2, 'accent'), Note(53, 1)]),
                   Phrase([Note(43, 1), Note(46, 2, 'accent'), Note(43, 1)])]),

            'mp': PhraseCollection([Phrase([Note(70, 1, 'stac'), Note(69, 1, 'stac'), Note(67, 1, 'stac'), Note(69, 1)]),
                   Phrase([Note(62, 1, 'stac'), Note(62, 1, 'stac'), Note(62, 1, 'stac'), Note(60, 1)]),
                   Phrase([Note(53, 1, 'stac'), Note(53, 1, 'stac'), Note(53, 1, 'stac'), Note(53, 1)]),
                   Phrase([Note(43, 1, 'stac'), Note(45, 1, 'stac'), Note(46, 1, 'stac'), Note(45, 1)])]),

            'mp': PhraseCollection([Phrase([Note(70, 1), Note(70, 1, 'stac'), Note(69, 1, 'stac'), Note(67, 1, 'stac')]),
                   Phrase([Note(62, 1), Note(62, 1, 'stac'), Note(62, 1, 'stac'), Note(62, 1, 'stac')]),
                   Phrase([Note(53, 1), Note(53, 1, 'stac'), Note(53, 1, 'stac'), Note(53, 1, 'stac')]),
                   Phrase([Note(43, 1), Note(43, 1, 'stac'), Note(45, 1, 'stac'), Note(46, 1, 'stac')])]),

            'mf': PhraseCollection([Phrase([Note(74, 3), Note(74, 1/3, 'stac'), Note(74, 1/3, 'stac'),
                         Note(74, 1/3, 'stac')]),
                   Phrase([Note(62, 3), Note(72, 1/3, 'stac'), Note(70, 1/3, 'stac'),
                         Note(69, 1/3, 'stac')]),
                   Phrase([Note(62, 3), Note(60, 1/3, 'stac'), Note(58, 1/3, 'stac'),
                         Note(57, 1/3, 'stac')]),
                   Phrase([Note(48, 3), Note(48, 1/3, 'stac'), Note(48, 1/3, 'stac'),
                         Note(48, 1/3, 'stac')])]),

            'f' : PhraseCollection([Phrase([Note(74, 3/4), Note(70, 1/4),
                         Note(70, 1/3, 'accent'), Note(74, 1/3), Note(74, 1/3, 'stac'),
                         Note(74, 1/3, 'accent'), Note(79, 1/3), Note(77, 1/3, 'stac'),
                         Note(77, 1/3, 'accent'), Note(81, 1/3), Note(81, 1/3, 'stac')]),
                   Phrase([Note(67, 3/4), Note(67, 1/4),
                         Note(67, 1/3, 'accent'), Note(70, 1/3), Note(70, 1/3, 'stac'),
                         Note(70, 1/3, 'accent'), Note(74, 1/3), Note(74, 1/3, 'stac'),
                         Note(74, 1/3, 'accent'), Note(77, 1/3), Note(77, 1/3, 'stac')]),
                   Phrase([Note(55, 3/4), Note(62, 1/4),
                         Note(62, 1/3, 'accent'), Note(67, 1/3), Note(65, 1/3, 'stac'),
                         Note(65, 1/3, 'accent'), Note(69, 1/3), Note(69, 1/3, 'stac'),
                         Note(69, 1/3, 'accent'), Note(72, 1/3), Note(72, 1/3, 'stac')]),
                   Phrase([Note(53, 3/4), Note(50, 1/4),
                         Note(50, 1/3, 'accent'), Note(55, 1/3), Note(55, 1/3, 'stac'),
                         Note(55, 1/3, 'accent'), Note(58, 1/3), Note(58, 1/3, 'stac'),
                         Note(58, 1/3, 'accent'), Note(65, 1/3), Note(65, 1/3, 'stac')])]),

            'ff': PhraseCollection([Phrase([Note(62, 1/4,'accent'), Note(65, 1/4), Note(63, 1/4), Note(62, 1/4),
                         Note(70, 1/4,'accent'), Note(74, 1/4), Note(72, 1/4), Note(70, 1/4),
                         Note(74, 1/4,'accent'), Note(77, 1/4), Note(75, 1/4), Note(74, 1/4),
                         Note(82, 1/4,'accent'), Note(86, 1/4), Note(84, 1/4), Note(82, 1/4)]),
                   Phrase([Note(62, 1/4,'accent'), Note(65, 1/4), Note(63, 1/4), Note(62, 1/4),
                         Note(70, 1/4,'accent'), Note(74, 1/4), Note(72, 1/4), Note(70, 1/4),
                         Note(74, 1/4,'accent'), Note(77, 1/4), Note(75, 1/4), Note(74, 1/4),
                         Note(70, 1/4,'accent'), Note(74, 1/4), Note(72, 1/4), Note(70, 1/4)]),
                   Phrase([Note(50, 1/4,'accent'), Note(53, 1/4), Note(51, 1/4), Note(50, 1/4),
                         Note(58, 1/4,'accent'), Note(62, 1/4), Note(60, 1/4), Note(58, 1/4),
                         Note(62, 1/4,'accent'), Note(65, 1/4), Note(63, 1/4), Note(62, 1/4),
                         Note(58, 1/4,'accent'), Note(62, 1/4), Note(60, 1/4), Note(58, 1/4)]),
                   Phrase([Note(38, 1/4,'accent'), Note(41, 1/4), Note(39, 1/4), Note(38, 1/4),
                         Note(46, 1/4,'accent'), Note(50, 1/4), Note(48, 1/4), Note(46, 1/4),
                         Note(50, 1/4,'accent'), Note(53, 1/4), Note(51, 1/4), Note(50, 1/4),
                         Note(58, 1/4,'accent'), Note(62, 1/4), Note(60, 1/4), Note(58, 1/4)])])
        }
        return lookup
