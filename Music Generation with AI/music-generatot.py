import os
import glob
import random
from collections import defaultdict
from music21 import converter, instrument, note, chord, stream

# AUTOMATIC PATH FIX: Yeh line code ko batayegi ke woh kis folder ke andar baitha hai
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MIDI_FOLDER = os.path.join(BASE_DIR, "midi_songs")

# 1. Load MIDI Data
def load_midi_notes():
    notes = []
    # Automatic sahi folder check karega
    search_path = os.path.join(MIDI_FOLDER, "*.mid")
    for file in glob.glob(search_path):
        print(f"Parsing {os.path.basename(file)}...")
        try:
            midi = converter.parse(file)
            parts = instrument.partitionByInstrument(midi)
            notes_to_parse = parts.parts[0].recurse() if parts else midi.flat.notes
            
            for element in notes_to_parse:
                if isinstance(element, note.Note):
                    notes.append(str(element.pitch))
                elif isinstance(element, chord.Chord):
                    notes.append('.'.join(str(n) for n in element.normalOrder))
        except Exception as e:
            print(f"Skipping broken file {os.path.basename(file)}: {e}")
    return notes

# Create directory if it doesn't exist yet
if not os.path.exists(MIDI_FOLDER):
    os.makedirs(MIDI_FOLDER)
    print(f"⚠️ Created 'midi_songs' folder inside: {MIDI_FOLDER}")
    print("Please drop some .mid files in it and re-run!")
    exit()

notes_dataset = load_midi_notes()

if len(notes_dataset) < 2:
    print(f"⚠️ Please drop a few .mid files inside this specific folder:\n👉 {MIDI_FOLDER}")
    exit()

# 2. Build the AI Markov Chain Model
print("Learning musical patterns...")
markov_model = defaultdict(list)

for i in range(len(notes_dataset) - 1):
    current_note = notes_dataset[i]
    next_note = notes_dataset[i+1]
    markov_model[current_note].append(next_note)

# 3. Generate a New Musical Sequence
print("Generating new music sequence...")
generated_sequence = []
current_note = random.choice(notes_dataset)

for _ in range(100):
    generated_sequence.append(current_note)
    next_possibilities = markov_model[current_note]
    if next_possibilities:
        current_note = random.choice(next_possibilities)
    else:
        current_note = random.choice(notes_dataset)

# 4. Convert to MIDI
offset = 0
output_notes = []

for pattern in generated_sequence:
    if ('.' in pattern) or pattern.isdigit():
        notes_in_chord = pattern.split('.')
        notes_arr = [note.Note(int(n)) for n in notes_in_chord]
        for n in notes_arr:
            n.storedInstrument = instrument.Piano()
        new_chord = chord.Chord(notes_arr)
        new_chord.offset = offset
        output_notes.append(new_chord)
    else:
        new_note = note.Note(pattern)
        new_note.offset = offset
        new_note.storedInstrument = instrument.Piano()
        output_notes.append(new_note)

    offset += 0.5

# Save output in the exact same folder as the code
output_file_path = os.path.join(
BASE_DIR, 'markov_generated_music.mid')
midi_stream = stream.Stream(output_notes)
midi_stream.write('midi', fp=output_file_path)
print(f"🎉 Success! Saved your unique track at:\n👉 {output_file_path}")