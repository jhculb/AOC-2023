from pathlib import Path

infile_example = Path(__file__).parent / "example1"
infile_data = Path(__file__).parent / "data1"
score = 0
with open(infile_data) as f:
    for line in f.readlines():
        max = {"blue": 0, "red": 0, "green": 0}
        gamenumstr, gameresults = line.split(":")
        rounds = gameresults.split(";")
        for round in rounds:
            elements = round.split(",")
            for element in elements:
                element = element.strip()
                num, colour = element.split(" ")
                if int(num) > max[colour]:
                    max[colour] = int(num)
        score += max["blue"] * max["green"] * max["red"]

print(score)
