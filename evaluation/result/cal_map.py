with open("evaluation/result/ap_paris.txt", "r") as file:
    lines = file.readlines()
    numbers = [float(line.strip()) for line in lines]

average = sum(numbers) / len(numbers)
print("The mAP is:", average)
