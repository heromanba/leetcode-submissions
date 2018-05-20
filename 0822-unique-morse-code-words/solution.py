class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",\
                      ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",\
                      "...","-","..-","...-",".--","-..-","-.--","--.."]
        morse_dict = {chr(i + ord('a')):morse_code[i] for i in range(len(morse_code))}
        transformations = []
        for word in words:
            code = ""
            for character in word:
                code += morse_dict[character]
            transformations.append(code)
        return len(set(transformations))
