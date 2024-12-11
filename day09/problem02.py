def calculate_sum(length, block):
    return length * (2 * block + length - 1) // 2

with open("input.txt", "r") as input_file:
    input_data = input_file.read()

input_data = list(map(int, list(input_data)))
input_data.append(0)

yikes = {}

for i in range(0, len(input_data), 2):
    yikes[i // 2] = {
        "l": input_data[i],
        "f": input_data[i + 1],
        "s": [],
    }

for candidate_id in reversed(yikes):
    c = yikes[candidate_id]
    for target_free_id in yikes:
        if candidate_id <= target_free_id:
            break
        t = yikes[target_free_id]
        if t["f"] >= c["l"] > 0:
            t["s"].append({"l": c["l"], "id": candidate_id})
            t["f"] -= c["l"]
            c["ff"] = c["l"]
            c["l"] = 0
            break
checksum = 0
block = 0
for file_id, file in yikes.items():
    if "ff" in file:
        block += file["ff"]
    else:
        checksum += file_id * calculate_sum(file["l"], block)
        block += file["l"]

    for subfile in file["s"]:
        checksum += subfile["id"] * calculate_sum(subfile["l"], block)
        block += subfile["l"]
    block += file["f"]

print(checksum)