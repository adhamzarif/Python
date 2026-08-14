with open("Shakespear.txt",mode="r") as s_file:
    # for line in s_file.readlines():
    #     # print(line.strip(),end="")
    #     words = line.strip().split(" ")
    #     print(words)
    words_all = []
    for line in s_file.readlines():
            words = line.strip().split(" ")
            words_all += words
unique_words = set(words_all)
print(len(words_all))
print(len(unique_words))
print(words_all)

with open("unique_words.txt",mode="w") as write_file:
      for item in sorted(unique_words):
            write_file.write(item)
            write_file.write("\n")
print("finished")