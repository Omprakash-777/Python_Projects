def remove_common_chars(name1, name2):
    name1 = list(name1)
    name2 = list(name2)

    for i in name1[:]:
        if i in name2:
            name1.remove(i)
            name2.remove(i)

    return len(name1) + len(name2)

def get_flames_result(count):
    flames = ['F', 'L', 'A', 'M', 'E', 'S']

    while len(flames) > 1:
        index = (count % len(flames)) - 1
        if index >= 0:
            right = flames[index+1:]
            left = flames[:index]
            flames = right + left
        else:
            flames = flames[:len(flames)-1]

    final_letter = flames[0]
    mapping = {
        'F': 'Friends',
        'L': 'Love',
        'A': 'Affection',
        'M': 'Marriage',
        'E': 'Enemy',
        'S': 'Siblings'
    }

    return mapping[final_letter]

# Main function
def flames_game():
    name1 = input("Enter first name: ").lower().replace(" ", "")
    name2 = input("Enter second name: ").lower().replace(" ", "")

    count = remove_common_chars(name1, name2)
    result = get_flames_result(count)

    print("Relationship:", result)

# Run the game
flames_game()
