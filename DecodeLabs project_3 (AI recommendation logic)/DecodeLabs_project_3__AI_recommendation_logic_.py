# Project 3: AI Movie Recommendation System (Movie recommendations)

#import libraries
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Movie Dataset
movies = {
"Avengers Endgame":
    "action - superhero - marvel - fight - adventure",

"Titanic":
    "romance - drama - love - emotional",
         
"Batman The Dark Knight":
    "action - dark - hero - crime",

"Until Dawn":
    "horror - survival - mystery - monsters",

"Terrifier":
    "horror - clown - killer - scary",

"John Wick":
    "action - fight - gun - crime",

"Spider Man No Way Home":
    "action - superhero - marvel - multiverse",

"Frozen":
    "animation - disney - family - musical - fantasy",

"Fast and Furious":
    "cars - racing - action - adventure - speed",

"F1":
    "cars - racing - action - adventure - speed",

"Need for Speed":
    "cars - racing - action - speed",

"Harry Potter":
    "magic fantasy adventure wizard school",

"Joker":
    "drama - psychological - dark - crime",

"Toy Story":
    "animation - family - friendship - comedy",

"Shutter Island":
    "thriller - mystery - psychological - crime",

"Mission Impossible":
    "spy - action - adventure - mission - fight",

"Transformers":
    "robots - action - sci-fi - war",

"Jurassic World":
    "dinosaurs - adventure - action - sci-fi",

"Jumanji":
    "adventure - comedy - fantasy - jungle",

"Final Destination":
    "horror - death - mystery - suspense",
}

# Take User Interests
user_interest = input(
 "\nChoose your movie interests: \n \n"
 "(action - superhero - marvel - fight - adventure -"
 "\n romance - drama - love - emotional - dark - "
 "\n hero - crime - horror - survival - mystery -" 
 "\n monsters - clown - killer - scary - gun - "
 "\n multiverse - animation - disney - family - musical -" 
 "\n fantasy - cars - racing - speed - magic -" 
 "\n wizard - school - psychological - friendship - comedy -" 
 "\n thriller - spy - mission - robots - war -" 
 "\n dinosaurs - jungle - death - suspense): "
)

# Combine Movie Data + User Input
all_descriptions = list(movies.values())

# Add user interests to the list
all_descriptions.append(user_interest)

# Convert Text into Numerical Data
# Using TF-IDF
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(all_descriptions)

# Calculate Cosine Similarity
similarity = cosine_similarity(vectors)

# Compare User with Movies
user_scores = similarity[-1][:-1]

# Create Recommendation List
movie_names = list(movies.keys())

recommendations = []

for i in range(len(movie_names)):

    recommendations.append(
        (movie_names[i], user_scores[i])
    )

# Sort Recommendations
recommendations.sort(
    key=lambda x: x[1],
    reverse=True
)

# Display top five Recommended Movies
print("\n========== Recommended Movies ==========\n")

top_movies = recommendations[:5]

for movie, score in top_movies:

    print("Movie:", movie)

    print(
        "Match Score:",
        round(score * 100, 2),
        "% \n"
    )