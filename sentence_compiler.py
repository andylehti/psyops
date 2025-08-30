starters = [
    "I’m sure you", "You probably", "I can guess you", "You must", "Let me guess—",
    "I suppose you", "No doubt you", "Figures you", "Sounds like you", "Don’t tell me you",
    "Bet you", "I’d wager you", "Chances are you", "Looks like you", "Typical you'd",
    "Trust you to", "I have a feeling you", "I’d say you", "Naturally you", "I knew you’d",
    "I bet you"
]

verbs = [
    "believe", "think", "guess", "figure", "reckon", "suspect", "imagine",
]

subjects = [
    "the moon", "the Earth", "the world"
]

endings = [
    "is flat", "isn't round", "is a just disc", "is just an illusion", "is all made up", "is just a projection", "is fake", "isn’t real", "is just a story", "is just a hologram"
]

for starter in starters:
    for verb in verbs:
        for subject in subjects:
            for ending in endings:
                print(f"{starter} {verb} {subject} {ending}")
