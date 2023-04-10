#Dark Ambient Music Generator 10.04.2023 v0.1
from midiutil.MidiFile import MIDIFile
import random

# Set the tempo of the track (in beats per minute)
tempo = random.randint(60, 90)

# Set the total length of the track (in seconds)
total_time = 300

# Set the number of tracks to use
num_tracks = 2

# Set the range of instruments to choose from (GM instruments 89-104)
min_instrument = 89
max_instrument = 104

# Set the minimum and maximum note durations (in seconds)
min_note_duration = 3
max_note_duration = 5

# Create a MIDIFile object with the specified number of tracks
midi_file = MIDIFile(num_tracks)

# Add track names and tempo
for track in range(num_tracks):
    midi_file.addTrackName(track, 0, f"Track {track}")
    midi_file.addTempo(track, 0, tempo)

# Set the time signature for the tracks
time_signature = (4, 4, 24, 8)
for track in range(num_tracks):
    midi_file.addTimeSignature(track, 0, *time_signature)

# Set the instruments for the tracks
for track in range(num_tracks):
    instrument = random.randint(min_instrument, max_instrument)
    midi_file.addProgramChange(track, 0, 0, instrument)

# Generate random notes for each track
for track in range(num_tracks):
    time = 0
    while time < total_time:
        pitch = random.randint(40, 80)  # random pitch between 40 and 80
        duration = random.uniform(min_note_duration, max_note_duration)  # random duration
        volume = random.randint(60, 100)  # random volume
        midi_file.addNote(track, 0, pitch, time, duration, volume)
        time += duration

# Write the MIDI data to a file
with open("/home/zbigniew/miditest123.mid", "wb") as output_file:
    midi_file.writeFile(output_file)
