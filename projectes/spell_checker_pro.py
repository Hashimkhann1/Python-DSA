from spellchecker import SpellChecker


class spellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()


    def correct_spell(self , text):
        words = text.split()
        corrected_words = []

        for word in words:
            corrected_word = self.spell.correction(word)

            if corrected_word != word.lower():
                print(f"Correcting {word} to {corrected_word}")
                corrected_words.append(corrected_word)
        
        return ' '.join(corrected_words)
    

    def run(self):

        while True:
            text = input(f"Enter text to check (or type 'exit')")

            if text.lower() == 'exit':
                print("Closing the programme")
                break

            corrected_text = self.correct_spell(text)
            print(f"Corrected text : {corrected_text}")


if __name__ == "__main__":
    spellCheckerApp().run()