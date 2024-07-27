# Movie Recommendation Web App

## Author
Anand Dubey

## Description
This project is a self-initiated data science endeavor focused on building a movie recommendation system. The application utilizes collaborative filtering to suggest movies based on user ratings. Given the massive size of the ratings dataset (over 10 million rows), handling and analyzing this data required converting the data format from CSV to Parquet for enhanced performance and efficiency.



## Key Features
- **Collaborative Filtering**: Provides personalized movie recommendations based on user ratings.
- **Efficient Data Handling**: Data was converted from CSV to Parquet format to manage and analyze large datasets more effectively.
- **TF-IDF Vectorization**: Utilizes TF-IDF (Term Frequency-Inverse Document Frequency) to compute movie title similarities.
- **Debounced Search**: Implements a debounced search mechanism to optimize performance and reduce unnecessary computations.
- **Interactive Widgets**: Features interactive widgets for dynamic user input and real-time recommendations.

## Project Components

### 1. Data Loading and Preparation
- **Movies Dataset**: Contains movie details such as titles and metadata.
- **Ratings Dataset**: Includes user ratings for various movies.
- **Data Cleaning**: Processes movie titles to remove special characters and standardizes text for improved matching.

### 2. Similarity Calculation
- **TF-IDF Vectorization**: Converts movie titles into numerical vectors to facilitate similarity measurement.
- **Cosine Similarity**: Calculates the similarity between the search query and movie titles to find the most relevant matches.

### 3. User Interaction
- **Search Functionality**: Allows users to input a movie title and get a list of similar movies.
- **Debounced Search**: Uses a debounced approach to optimize search performance and ensure efficient querying.

### 4. Recommendation Generation
- **Collaborative Filtering**: Recommends movies by analyzing user preferences and identifying similar users.
- **Recommendation Scoring**: Calculates scores based on the overlap between user preferences and overall ratings.

## How It Works
1. **Data Ingestion**: Load the movie and rating datasets into the application.
2. **Data Transformation**: Clean and preprocess the data to prepare it for analysis.
3. **Vectorization**: Apply TF-IDF vectorization to transform movie titles into numerical representations.
4. **Search Mechanism**: Implement a search function that uses cosine similarity to match user queries with movie titles.
5. **Recommendation System**: Use collaborative filtering to generate recommendations based on user ratings and preferences.

## Benefits
- **Improved Performance**: Converting data to Parquet format enhances processing speed and efficiency.
- **Personalized Recommendations**: Offers tailored movie suggestions based on individual user preferences.
- **Real-Time Interaction**: Provides immediate feedback and recommendations through interactive widgets.

## Future Improvements
- **Expanded Dataset**: Integrate additional data sources to enrich the recommendation system.
- **Advanced Filtering**: Develop more sophisticated filtering techniques to refine recommendations further.
- **User Interface**: Enhance the user interface for a better overall experience.


