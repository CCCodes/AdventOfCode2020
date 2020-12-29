inp_f = open("input/day21.txt", "r")
inp = inp_f.read()
inp_list = [line for line in inp.split("\n") if line != ""]


def part1():
    allergen_to_ingredients = {}
    all_ingredients = []
    ingredient_lines = []
    for line in inp_list:
        split = line.split(" (contains ")
        ingredients = split[0].split(" ")
        allergens = split[1][:-1].split(", ")
        for allergen in allergens:
            if allergen not in allergen_to_ingredients:
                allergen_to_ingredients[allergen] = []
            allergen_to_ingredients[allergen].append(set(ingredients))
        for ingredient in ingredients:
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)
        ingredient_lines.append(ingredients)

    allergen_intersection = {}
    possible_ingredients = []
    impossible_ingredients = []
    for allergen in allergen_to_ingredients:
        allergen_intersection[allergen] = set.intersection(*allergen_to_ingredients[allergen])
        for ingredient in allergen_intersection[allergen]:
            if ingredient not in possible_ingredients:
                possible_ingredients.append(ingredient)

    for ingredient in all_ingredients:
        if ingredient not in possible_ingredients:
            impossible_ingredients.append(ingredient)
    count = 0
    for ingredient in impossible_ingredients:
        for ingredients in ingredient_lines:
            if ingredient in ingredients:
                count += 1
    return count


def part2():
    allergen_to_ingredients = {}
    for line in inp_list:
        split = line.split(" (contains ")
        ingredients = split[0].split(" ")
        allergens = split[1][:-1].split(", ")
        for allergen in allergens:
            if allergen not in allergen_to_ingredients:
                allergen_to_ingredients[allergen] = []
            allergen_to_ingredients[allergen].append(set(ingredients))
    allergen_intersection = []
    for allergen in allergen_to_ingredients:
        allergen_intersection.append((allergen, set.intersection(*allergen_to_ingredients[allergen])))
    allergen_intersection.sort(key=lambda item: len(item[1]))

    res_all = []
    while len(res_all) < len(allergen_intersection):
        for allergen, ingredients in allergen_intersection:
            ingredients = ingredients.difference(set([combo[1] for combo in res_all]))
            if len(ingredients) == 1:
                ingredient = list(ingredients)[0]
                if (allergen, ingredient) in res_all:
                    continue
                res_all.append((allergen, ingredient))
            else:
                continue
            
    res_all.sort(key=lambda item: item[0])
    res = [combo[1] for combo in res_all]
    return ','.join(res)


if __name__ == "__main__":
    print(part1())
    print(part2())
