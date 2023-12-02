from pathlib import Path

infile_example = Path(__file__).parent / "example1"
infile_data = Path(__file__).parent / "data1"

max = {"blue": 14, "red": 12, "green": 13}
score = 0

with open(infile_data) as f:
    for line in f.readlines():
        possible = True
        gamenumstr, gameresults = line.split(":")
        rounds = gameresults.split(";")
        for round in rounds:
            elements = round.split(",")
            for element in elements:
                element = element.strip()
                num, colour = element.split(" ")
                if int(num) > max[colour]:
                    possible = False
        if possible:
            score += int(gamenumstr.split(" ")[-1])

print(score)
