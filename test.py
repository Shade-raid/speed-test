import random
import time

# List of sample texts in Azerbaijani for typing test
sample_texts = [
    "Çox qısa müddətdə qələmimə yaza biləcəyimiz ən çox dəyərli şey - ələfdir.",
    "Söhbəti əslində qısa, sadə və məqbul edən hər hansı bir dil yoxdur.",
    "Yarın kim bilir nə olacaq, amma indi səni sevirəm.",
    "Həyatda insanlar üçün ən pis şeylərdən biri də böyük səbəblər və mənasız həyatdır.",
    "Sevgi zamanı mədənə, yaxşılıq vaxtı testə çəkilməlidir.",
    "Əgər bir şeyi sevirsinizsə, onu azad buraxın. Əgər o geri dönərsə, o sizin idi. Əgər geri qayıtmazsa, o heç vaxt sizin olmamışdır.",
    "Ən çox istədiyiniz şey, ən çox xəyallarınızdır.",
    "Qalbi sevgidən əsirgəyənlər, ruhlarından məhrum qalacaqlar.",
    "Sizi gülüşə qaldıran şeylərə qalib gəlin, sizi düşündürənlərə isə qaşları sərp.",
    "Mənə sevgi dəyər verənlərin ümumi təşəkkür hissəsiyəm."
]

# Function to start the test
def start_test():
    # Select a random sample text
    sample_text = random.choice(sample_texts)
    print("Sample Text:")
    print(sample_text)

    # Record the start time
    start_time = time.time()

    # Get user input
    user_input = input("Start typing: ")

    # Record the end time
    end_time = time.time()

    # Calculate the elapsed time in seconds
    time_diff = end_time - start_time

    # Calculate the number of words typed per minute
    word_count = len(user_input.split())
    words_per_minute = round(word_count / (time_diff / 60))

    # Calculate the accuracy by comparing the user input with the sample text
    accuracy = calculate_accuracy(user_input, sample_text)

    # Display the results
    print(f"Time: {time_diff:.2f}s | Words per Minute: {words_per_minute} | Accuracy: {accuracy:.2f}%")

# Function to calculate the accuracy
def calculate_accuracy(user_input, sample_text):
    correct_characters = sum(1 for i, j in zip(user_input, sample_text) if i == j)
    accuracy = (correct_characters / len(sample_text)) * 100
    return accuracy

# Start the typing test
start_test()
