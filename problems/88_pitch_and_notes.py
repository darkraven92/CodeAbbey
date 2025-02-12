def note_to_frequency(note):
    # Reference note: A4 = 440 Hz
    ref_note = "A4"
    ref_freq = 440.0

    # Extract note name and octave
    note_name = note[:-1]
    octave = int(note[-1])

    # List of notes in order
    notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

    # Find the index of the note in the list
    note_index = notes.index(note_name)

    # Find the index of the reference note (A4)
    ref_index = notes.index("A")

    # Calculate the semitone difference
    semitone_diff = (octave - 4) * 12 + (note_index - ref_index)

    # Calculate the frequency
    frequency = ref_freq * (2 ** (semitone_diff / 12))

    # Round to the nearest integer
    return round(frequency)

# Read input
n = int(input())
notes = input().split()

# Calculate frequencies
frequencies = [note_to_frequency(note) for note in notes]

# Output the result
print(" ".join(map(str, frequencies)))