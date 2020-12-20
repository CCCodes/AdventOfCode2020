inp_f = open("input/day7.txt", "r")
inp = inp_f.read()
inp_list = [line for line in inp.split("\n") if line != ""]

bag_dict_colors = {}
bag_dict = {}
for line in inp_list:
    bag_name = line.split(" bags contain ")[0]
    bag_contains = line.split(" bags contain ")[1]
    colors = [" ".join(color.split(" ")[1:-1]) for color in bag_contains.split(", ") if color != "no other bags."]
    counts = [int(color.split(" ")[0]) for color in bag_contains.split(", ") if color != "no other bags."]
    bag_dict_colors[bag_name] = colors
    bag_dict[bag_name] = {colors[i]: counts[i] for i in range(len(colors))}


def part1(color):
    all_bags = []
    for bag in bag_dict_colors:
        if color in bag_dict_colors[bag]:
            all_bags.append(bag)
            all_bags += part1(bag)
    return all_bags


def part2(color):
    sum = 0
    for bag in bag_dict[color]:
        sum += (part2(bag) + 1) * bag_dict[color][bag]
    return sum


if __name__ == "__main__":
    print(len(set(part1("shiny gold"))))
    print(part2("shiny gold"))
