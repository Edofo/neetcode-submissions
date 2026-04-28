class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        validEmails = set()

        for email in emails:
            correct = ""
            plus = False
            arro = False
            for letter in email:
                if letter == "+":
                    plus = True
                    continue;
                elif letter == "@":
                    plus = False
                    arro = True

                if plus == False:
                    if arro == False and letter == ".":
                        continue;
                    correct += letter
            
            validEmails.add(correct)  

        return len(validEmails)  