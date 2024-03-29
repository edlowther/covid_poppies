import music21

from app.phrase_collections import PhraseCollections

class ScoreManager:
    def __init__(self, instruments, orchestration_mapper, fp):
        self.instruments = instruments
        self.orchestration_mapper = orchestration_mapper
        self.score = self.initialise_score()
        self.phrase_collections = PhraseCollections()
        self.articulations = {
            'stac': music21.articulations.Staccato(),
            'accent': music21.articulations.Accent()
        }
        self.fp = fp

    def initialise_score(self):
        score = music21.stream.Score()
        score.insert(0, music21.metadata.Metadata())
        score.metadata.movementName = 'Coronavirus data by\nvaccination status'
        score.metadata.composer = 'Ed Lowther'
        for instrument in self.instruments:
            s = music21.stream.Part()
            s.partName = instrument.name
            s.partAbbreviation = instrument.abbr
            s.append(music21.meter.TimeSignature('4/4'))
            s.keySignature = music21.key.Key('D', 'minor')
            s.previous_dynamic = None
            score.insert(0, s)
        return score

    def add_bar(self, vaccination_status, dynamic, clip):
        if dynamic == 'bar_of_rest':
            instruments_to_orchestrate = []
            phrase_collection = None
        else:
            instruments_to_orchestrate = self.orchestration_mapper[dynamic]
            phrase_collection = self.phrase_collections.lookup[dynamic]
        for instrument in [instrument for instrument in self.instruments if instrument.vaccination_status == vaccination_status]:
            part = self.get_part_from_score(self.score, instrument)
            # print(vaccination_status, dynamic, instruments_to_orchestrate)
            if instrument.abbr in instruments_to_orchestrate:
                self.handle_dynamic_annotation(part, dynamic)
                phrase = phrase_collection.phrases[instrument.phrase_idx]
                for source_note_idx, source_note in enumerate(phrase.notes):
                    self.add_note_to_part(source_note_idx, source_note, part, phrase, clip)
            else:
                bar_of_rest = music21.note.Rest(duration = music21.duration.Duration(4))
                part.append(bar_of_rest)

    def get_part_from_score(self, score, instrument):
        return [_ for _ in score.parts if _.partAbbreviation == instrument.abbr][0]

    def handle_dynamic_annotation(self, part, dynamic):
        if dynamic != part.previous_dynamic:
            part.append(music21.dynamics.Dynamic(dynamic))
        part.previous_dynamic = dynamic

    def add_note_to_part(self, source_note_idx, source_note, part, phrase, clip):
        output_note = music21.note.Note(duration = music21.duration.Duration(source_note.duration), midi = source_note.pitch)
        self.handle_accents(source_note, output_note)
        self.handle_slurs(source_note_idx, source_note, output_note, part, phrase)
        # Shorten dotted minim in lowest bucket according to sub-buckets:
        if clip and source_note.duration == 3:
            output_note.duration = music21.duration.Duration(clip)
            part.append(output_note)
            rest_duration = 3 - clip
            if rest_duration > 0:
                part.append(music21.note.Rest(duration = music21.duration.Duration(rest_duration)))
        else:
            part.append(output_note)

    def handle_accents(self, source_note, output_note):
        if source_note.accent:
            accent = self.articulations[source_note.accent]
            output_note.articulations.append(accent)

    def handle_slurs(self, source_note_idx, source_note, output_note, part, phrase):
        try:
            previous_note = phrase.notes[source_note_idx - 1]
            next_note = phrase.notes[source_note_idx + 1]
            if source_note.duration == 1/3 and previous_note.duration == 1/3 and previous_note.accent == 'accent' and next_note.duration == 1/3:
                part.append(music21.spanner.Slur([part.notes[-1], output_note]))
        except IndexError:
            pass

    def write(self):
        self.score.write(fmt = 'musicxml', fp = self.fp)
