def calculate_love_score(name1, name2):
    true_letters = ['T','R','U','E']
    love_letters = ['L','O','V','E']
    
    combined_names = (name1 + name2).lower()
    
    score_true = 0
    score_love = 0
    
    for letter in true_letters:
        score_true += combined_names.count(letter.lower())
        
    for letter in love_letters:
        score_love += combined_names.count(letter.lower())
    
    love_score = int(str(score_true) + str(score_love))
    
    print(love_score)

# Call the function
calculate_love_score("Kanye West", "Kim Kardashian")
