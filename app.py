# Step 1: Store your name in a variable
name = "Darius Kibagendi"

# Step 2: Function to display n characters from the left
def display_n_characters(name, n):
    # Display the first n characters of the name
    return name[:n]

# Step 3: Function to count the number of vowels in the name
def count_vowels(name):
    vowels = "aeiouAEIOU"  # Include both lowercase and uppercase vowels
    count = sum(1 for char in name if char in vowels)  # Count vowels using a generator expression
    return count

# Step 4: Function to reverse the name
def reverse_name(name):
    return name[::-1]  # Use slicing to reverse the string

# Main execution block
if __name__ == "__main__":
    # Accept user input for n
    n = int(input("Enter the number of characters to display from the left: "))

    # Display n characters from the left
    left_characters = display_n_characters(name, n)
    print(f"First {n} characters from the left: {left_characters}")

    # Count the number of vowels
    vowel_count = count_vowels(name)
    print(f"Number of vowels in '{name}': {vowel_count}")

    # Reverse the name
    reversed_name = reverse_name(name)
    print(f"Reversed name: {reversed_name}")
