def number_to_words(num):
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = ["", "Thousand"]

    def convert_hundreds(n):
        if n < 10:
            return ones[n]
        elif n < 20:
            return teens[n-10]
        elif n < 100:
            return tens[n//10] + " " + ones[n%10]
        else:
            return ones[n//100] + " Hundred " + convert_hundreds(n % 100)

    def convert_thousands(n):
        if n < 1000:
            return convert_hundreds(n)
        else:
            return convert_hundreds(n//1000) + " Thousand " + convert_hundreds(n % 1000)

    return convert_thousands(num).strip()

# Example usage
num1 = 1978
num2 = 108
print(number_to_words(num1))  # Output: One Thousand Nine Hundred Seventy Eight
print(number_to_words(num2))  # Output: One Hundred Eight
