def main():
    """Get user input, convert text to emoji, and print the result"""
    emotion = input("Happy or upset")
    result = convert(emotion)
    print(result)

def convert(emotion):
    emotion1 = emotion.replace(":)",'🙂')
    emotion2 = emotion1.replace(":(",'🙁')

    return emotion2
main()
