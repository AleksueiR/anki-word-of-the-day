class Wotd(object):
    def __init__(self, word, definition, transcription='', audio_path=None, image_path=None):
        self.word = word

        self.definition = definition

        self.transcription = transcription

        self.audio_file = audio_path

        self.image_file = image_path
