# 2 done
def display_words(path):
    with open(path, 'r') as file:
        file_2 = file.read()
        file_3 = file_2.split()
        return len(file_3)

print(display_words('story.txt'))