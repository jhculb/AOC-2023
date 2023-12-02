from pathlib import Path

infile_example = Path(__file__).parent / "example2"
infile_data = Path(__file__).parent / "data1"

units3 = ["one", "two", "six"]
nums3 = [1, 2, 6]
units4 = ["four", "five", "nine"]
nums4 = [4, 5, 9]
units5 = ["three", "seven", "eight"]
nums5 = [3, 7, 8]

count = 0
with open(infile_data) as f:
    for line in f.readlines():
        listline = []
        start_word = 0
        print("\n", line)
        line = line[0:-1]
        while start_word < len(line):
            if line[start_word].isnumeric():
                listline.append(int(line[start_word]))
                print(f"Numeric Found: {int(line[start_word])}")
            if start_word + 3 <= len(line):
                if line[start_word : start_word + 3] in units3:
                    listline.append(
                        nums3[units3.index(line[start_word : start_word + 3])]
                    )
                    print(f"Len3 Found: {line[start_word:start_word+3]}")
            if start_word + 4 <= len(line):
                if line[start_word : start_word + 4] in units4:
                    listline.append(
                        nums4[units4.index(line[start_word : start_word + 4])]
                    )
                    print(f"Len4 Found: {line[start_word:start_word+4]}")
            if start_word + 5 <= len(line):
                if line[start_word : start_word + 5] in units5:
                    listline.append(
                        nums5[units5.index(line[start_word : start_word + 5])]
                    )
                    print(f"Len5 Found: {line[start_word:start_word+5]}")
            print(f"Nothing found: {line[start_word:start_word+5]}")
            start_word += 1
        score = int(str(listline[0]) + str(listline[-1]))
        print("score = ", score)
        if score < 10:
            input()
        count += score

print(count)
