from word_of_the_day.sources.dictionary_com import DictionaryComSource

dictionaryComWotd = DictionaryComSource()
wotd = dictionaryComWotd.today

print wotd.definition
print wotd.transcription
print wotd.audio_file
print wotd.image_file






#from PIL import Image, ImageFilter

#Read image
# im = Image.open("_image.png")
#http://pillow.readthedocs.org/en/3.0.x/handbook/tutorial.html#copying-a-subrectangle-from-an-image
#crop = im.crop((0, 55, 455, 395))
#crop.load()

#crop.save("image_cropped.png")



# m = mw.col.models.byName("TOEFL")
#note = anki.notes.Note(mw.col, m)
#
#note.fields[0] = '1'
#note.fields[2] = "dfsdf"
#
##acd = aqt.dialogs.open("AddCards", self)
##acd.addNote(note) # saves note to the database, probably not need this
##acd.editor.setNote(note)
#
#
#
#pp(mw.col.models.fieldNames(m))
#
#pp(mw.col.models.fieldMap(m))
#
##pp(acd.editor)
##pp(note.fields)