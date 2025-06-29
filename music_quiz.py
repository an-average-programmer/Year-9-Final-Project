import random

# List of songs and artists
SONGS = [
    ("Shape of You", "Ed Sheeran"),
    ("Blinding Lights", "The Weeknd"),
    ("Bohemian Rhapsody", "Queen"),
    ("Bad Guy", "Billie Eilish"),
    ("Uptown Funk", "Mark Ronson ft. Bruno Mars"),
    ("Someone You Loved", "Lewis Capaldi"),
    ("Rolling in the Deep", "Adele"),
    ("Despacito", "Luis Fonsi ft. Daddy Yankee"),
    ("Dance Monkey", "Tones and I"),
    ("Levitating", "Dua Lipa ft. DaBaby"),
    ("Watermelon Sugar", "Harry Styles"),
    ("Stay", "The Kid LAROI & Justin Bieber"),
    ("Starboy", "The Weeknd ft. Daft Punk"),
    ("Perfect", "Ed Sheeran"),
    ("As It Was", "Harry Styles"),
    ("Sunflower", "Post Malone & Swae Lee"),
    ("Sweater Weather", "The Neighbourhood"),
    ("One Dance", "Drake ft. Wizkid & Kyla"),
    ("Old Town Road", "Lil Nas X ft. Billy Ray Cyrus"),
    ("Shallow", "Lady Gaga & Bradley Cooper"),
    ("Somebody That I Used to Know", "Gotye ft. Kimbra"),
    ("Thinking Out Loud", "Ed Sheeran"),
    ("Lose Yourself", "Eminem"),
    ("Halo", "Beyoncé"),
    ("I Will Always Love You", "Whitney Houston"),
    ("Billie Jean", "Michael Jackson"),
    ("Smells Like Teen Spirit", "Nirvana"),
    ("Sweet Child O' Mine", "Guns N' Roses"),
    ("Hotel California", "Eagles"),
    ("Hey Jude", "The Beatles"),
    ("Like a Rolling Stone", "Bob Dylan"),
    ("Wonderwall", "Oasis"),
    ("Back in Black", "AC/DC"),
    ("Stairway to Heaven", "Led Zeppelin"),
    ("Born to Run", "Bruce Springsteen"),
    ("Rasputin", "Boney M."),
    ("Let It Be", "The Beatles"),
    ("Viva La Vida", "Coldplay"),
    ("Wake Me Up", "Avicii"),
    ("Believer", "Imagine Dragons"),
]

EXIT_COMMANDS = ["exit", "quit", "q", "ESC"]

def get_initials(song_title):
    # Returns the first letter of each word in the song title, separated by spaces
    words = song_title.split()
    initials_list = []
    for word in words:
        initials_list.append(word[0])
    initials_string = ''
    for letter in initials_list:
        initials_string = initials_string + letter + ' '
    return initials_string.strip()

def get_user_guess(artist, initials):
    # Prints the artist and initials, then asks the user for a guess
    print("Artist: " + artist)
    print("Song initials: " + initials)
    print("Type", EXIT_COMMANDS[0], "or", EXIT_COMMANDS[1], "to end the game at any time.")
    user_guess = input("What is the song name? ")
    return user_guess

def play():
    score = 0
    print("Welcome to the Music Quizz")
    print("Try to guess the song name. You have 2 chances for each song. The game ends if you miss both guesses for one song, or if you type 'exit' to quit.")
    print("Your score will be shown after each round.")

    # Copy of SONGS to allow for random selection without repetition
    available_songs = list(SONGS)

    while available_songs:
        # Pick a random song from the list and remove it so it can't repeat
        song_index = random.randint(0, len(available_songs) - 1)
        song_title, artist = available_songs.pop(song_index)
        initials = get_initials(song_title)

        # First guess
        user_guess = get_user_guess(artist, initials)
        if user_guess.lower().strip() in EXIT_COMMANDS:
            print("\nYou chose to exit the game.")
            break
        if user_guess.lower().strip() == song_title.lower():
            print("Correct! You get 3 points.")
            score = score + 3
            print("Current score: ", score)
            continue

        # Second guess
        print("Incorrect. Try one more time.")
        user_guess = input("What is the song name? ")
        if user_guess.lower().strip() in EXIT_COMMANDS:
            print("\nYou chose to exit the game.")
            break
        if user_guess.lower().strip() == song_title.lower():
            print("Correct! You get 1 point.")
            score = score + 1
            print("Current score:", score)
            continue
        else:
            print("Sorry, that's wrong. The song was: " + song_title)
            break

    print("\nGame over! Your final score is: " + str(score))

play()