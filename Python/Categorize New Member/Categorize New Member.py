def open_or_senior(data):
    output = []
    for i in range(len(data)):
        if data[i][0] >= 55 and data[i][1] >= 7:
            output.append("Senior")
        else:
            output.append("Open")
    return output


input = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
open_or_senior(input)
