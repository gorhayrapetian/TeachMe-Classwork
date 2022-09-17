# 4 done
def display_words(path):
    ll = []
    with open(path, 'r') as file:
        file_2 = file.read()
        file_3 = file_2.split()
        for i in file_3:
            if len(i) < 4:
                ll.append(i)
        return ll

print(display_words('story.txt'))