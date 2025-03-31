
# Regular Expressions in Python 📝

Regular expressions (regex) are powerful pattern matching tools in Python. Here's a comprehensive mind map of regex concepts, functions, and best practices.

## 🔍 Introduction to Regex

- **Definition**: A sequence of characters that forms a search pattern[^4]
- **Purpose**: Check if strings contain specific patterns[^4]
- **Implementation**: Python's built-in `re` module[^3][^4]
- **Import syntax**: `import re`[^4]


## 🛠️ Core Functions in `re` Module

- **search()**: Returns a Match object if pattern found anywhere in string[^4]
- **findall()**: Returns a list containing all matches[^4]
- **split()**: Returns a list where string is split at each match[^4]
- **sub()**: Replaces matches with a string[^4]
- **match()**: Checks if pattern matches at beginning of string[^7]


## 📋 Metacharacters

| Character | Description | Example |
| :-- | :-- | :-- |
| `[]` | Set of characters | `[a-m]` matches any letter from a to m |
| `\` | Special sequence | `\d` matches any digit |
| `.` | Any character (except newline) | `he..o` matches "hello" |
| `^` | Starts with | `^hello` matches strings starting with "hello" |
| `$` | Ends with | `planet$` matches strings ending with "planet" |
| `*` | Zero or more occurrences | `he.*o` matches "hello", "heeeello", etc. |
| `+` | One or more occurrences | `he.+o` matches "hello" but not "heo" |
| `?` | Zero or one occurrence | `he.?o` matches "heo" and "helo" |
| `{}` | Specific number of occurrences | `he{2}o` matches "heeo" |
| `\|` | Either/or | `falls\|stays` matches "falls" or "stays" |
| `()` | Capture and group | Groups parts of the pattern[^4] |

## 🔤 Character Classes

- **\d**: Matches digits (0-9)[^4]
- **\D**: Matches non-digits[^4]
- **\w**: Matches word characters (a-z, A-Z, 0-9, _)[^4]
- **\W**: Matches non-word characters[^4]
- **\s**: Matches whitespace characters[^4]
- **\S**: Matches non-whitespace characters[^4]
- **Custom classes**: Use `[]` for custom character sets[^6]


## ⚓ Anchors and Boundaries

- **\A**: Matches start of string[^4]
- **\Z**: Matches end of string[^4]
- **\b**: Word boundary[^4]
- **\B**: Non-word boundary[^4]
- **^**: Start of line (or string in single-line mode)[^4]
- **\$**: End of line (or string in single-line mode)[^4]


## 🔄 Quantifiers

- **Greedy**: Match as much as possible
    - `*`: Zero or more (e.g., `i*` matches "", "i", "ii", etc.)[^1]
    - `+`: One or more (e.g., `i+` matches "i", "ii", etc.)[^1]
    - `?`: Zero or one
    - `{n}`: Exactly n times
    - `{n,}`: At least n times
    - `{n,m}`: Between n and m times
- **Lazy**: Match as little as possible
    - `*?`: Zero or more (lazy)
    - `+?`: One or more (lazy)[^2]
    - `??`: Zero or one (lazy)
    - `{n,}?`: At least n times (lazy)
    - `{n,m}?`: Between n and m times (lazy)[^6]


## 👀 Lookahead and Lookbehind

- **Positive lookahead** `(?=...)`: Matches if pattern follows[^7]
- **Negative lookahead** `(?!...)`: Matches if pattern doesn't follow[^7]
- **Positive lookbehind** `(?&lt;=...)`: Matches if pattern precedes[^7]
- **Negative lookbehind** `(?pattern)`[^7]
- **Non-capturing groups**: `(?:pattern)`
- **Accessing groups**:
    - `.group(0)`: Entire match
    - `.group(1)`, `.group(2)`, etc.: Captured groups
    - `.groups()`: All groups as tuple
    - `.groupdict()`: Named groups as dictionary[^7]


## 🚀 Performance Optimization

- **Use character classes** instead of `.` when possible[^6]
- **Be specific** with your patterns to avoid excessive backtracking[^6]
- **Compile patterns** for reuse with `re.compile()`
- **Use lazy quantifiers** when appropriate for better performance[^6]
- **Fail fast**: Structure patterns to reject non-matches quickly[^3]
- **Profile your regex**: Test performance with different approaches[^3]


## ⚠️ Common Mistakes to Avoid

- **Greedy quantifier pitfalls**: Using `*` and `+` without considering their greedy nature[^2]
- **Incorrect anchor usage**: Misplacing `^` and `$`[^2]
- **Forgetting to escape special characters**: Not using `\` before special characters when needed[^2]
- **Unnecessary backslashes**: Adding extra escapes where not needed[^2]
- **Improper grouping**: Not using parentheses correctly for scope definition[^2]
- **Regex abuse**: Using regex for tasks better handled by other methods[^5]


## 📊 Practical Examples

```python
# Email validation
email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')

# Phone number extraction
phone_pattern = re.compile(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b')

# Find words between tags
tag_pattern = re.search(r'&lt;(\w+)&gt;(.*?)&lt;/\1&gt;', text)

# Match multiple whitespace-separated digits
digits_pattern = re.search(r'\d\s*\d\s*\d', 'xx1 2 3xx')  # matches "1 2 3"[^1]
```

---

Remember that while regular expressions are powerful, they can be difficult to debug and maintain[^3][^5]. Always consider whether a regex is the most appropriate solution for your specific problem.



# Introduction to Regex

## Definition

1. **Basic Pattern Matching**:

```python
import re
pattern = r"hello"
text = "hello world"
result = re.search(pattern, text)
print(result.group())  # Output: hello
```

A regular expression is a sequence of characters that defines a search pattern. In this example, we're using the simplest form - a literal string "hello" that matches exactly that text in the target string. Regular expressions are much more powerful than simple string matching because they can describe patterns rather than just exact text.
2. **Pattern with Metacharacters**:

```python
import re
pattern = r"\d{3}-\d{3}-\d{4}"
text = "My phone number is 555-123-4567"
result = re.search(pattern, text)
print(result.group())  # Output: 555-123-4567
```

This regex uses metacharacters to define a pattern for US phone numbers. The pattern `\d{3}-\d{3}-\d{4}` matches three digits, followed by a hyphen, three more digits, another hyphen, and finally four digits - the standard format for US phone numbers.
3. **Complex Pattern**:

```python
import re
pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
emails = ["user@example.com", "invalid@email", "name.lastname@company.co.uk"]
for email in emails:
    if re.match(pattern, email):
        print(f"{email} is valid")
    else:
        print(f"{email} is invalid")
```

This complex regex validates email addresses. It checks for one or more word characters, dots, or special characters before the @ symbol, followed by a domain name, a dot, and a top-level domain of at least two characters. This demonstrates how regex can concisely express complex validation rules.

## Purpose

1. **Text Validation**:

```python
import re
password_pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&amp;])[A-Za-z\d@$!%*?&amp;]{8,}$"
passwords = ["Weak123", "Strong@123", "nouppercaseorspecial123"]
for password in passwords:
    if re.match(password_pattern, password):
        print(f"{password} is strong")
    else:
        print(f"{password} is weak")
```

This example uses regex to validate password strength. The pattern checks if a password has at least 8 characters, contains at least one uppercase letter, one lowercase letter, one digit, and one special character. Regular expressions are ideal for this kind of validation because they can check multiple criteria in a single operation.
2. **Data Extraction**:

```python
import re
html = "<p>First paragraph</p><p>Second paragraph with <a href="https://example.com">link</a></p>"
pattern = r"<p>(.*?)</p>"
paragraphs = re.findall(pattern, html)
print(paragraphs)  # Output: ['First paragraph', 'Second paragraph with <a href="https://example.com">link</a>']
```

Regular expressions excel at extracting specific data from structured text. In this example, we're extracting the content of paragraph tags from HTML. The pattern `<p>(.*?)</p>` captures everything between opening and closing p tags, with the parentheses creating a capturing group.
3. **Search and Replace**:

```python
import re
text = "The date is 2023-03-15 and another date is 2022-12-31."
pattern = r"(\d{4})-(\d{2})-(\d{2})"
formatted_text = re.sub(pattern, r"\2/\3/\1", text)
print(formatted_text)  # Output: The date is 03/15/2023 and another date is 12/31/2022.
```

Regular expressions are powerful for search and replace operations. In this example, we're converting dates from YYYY-MM-DD format to MM/DD/YYYY format. The pattern captures the year, month, and day as separate groups, and the replacement string rearranges them.

## Implementation

1. **Python's Built-in `re` Module**:

```python
import re

text = "Python was created in 1991 by Guido van Rossum."
year_pattern = r"\b\d{4}\b"

# Using re.search to find the first match
match = re.search(year_pattern, text)
if match:
    print(f"Found year: {match.group()}")  # Output: Found year: 1991
```

Python implements regular expressions through its built-in `re` module. This module provides functions like `search()`, `match()`, and `findall()` that apply regex patterns to strings. In this example, we're searching for a four-digit year in the text.
2. **JavaScript RegExp Object**:

```javascript
const text = "JavaScript was created in 1995 by Brendan Eich.";
const yearPattern = /\b\d{4}\b/;

// Using test() to check if pattern exists
if (yearPattern.test(text)) {
    // Using exec() to get the match
    const match = yearPattern.exec(text);
    console.log(`Found year: ${match[^0]}`);  // Output: Found year: 1995
}
```

JavaScript implements regex through its RegExp object. You can create regex patterns using literal notation with forward slashes or by using the RegExp constructor. JavaScript provides methods like `test()`, `exec()`, and string methods like `match()` and `replace()` that work with regular expressions.
3. **Java's `java.util.regex` Package**:

```java
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class RegexExample {
    public static void main(String[] args) {
        String text = "Java was created in 1995 by James Gosling.";
        String yearPattern = "\\b\\d{4}\\b";
        
        Pattern pattern = Pattern.compile(yearPattern);
        Matcher matcher = pattern.matcher(text);
        
        if (matcher.find()) {
            System.out.println("Found year: " + matcher.group());  // Output: Found year: 1995
        }
    }
}
```

Java implements regular expressions through its `java.util.regex` package. The package provides the Pattern class for compiling regex patterns and the Matcher class for applying those patterns to text. Note that in Java string literals, backslashes must be escaped, so `\d` becomes `\\d`.

## Import Syntax

1. **Basic Import in Python**:

```python
import re

text = "Regular expressions are powerful!"
pattern = r"powerful"

if re.search(pattern, text):
    print("Pattern found!")
else:
    print("Pattern not found.")
```

The simplest way to use regex in Python is to import the entire `re` module with `import re`. This gives you access to all the module's functions like `search()`, `match()`, and `findall()`. You prefix each function call with `re.` to indicate it comes from the re module.
2. **Selective Import in Python**:

```python
from re import search, findall, sub

text = "Regular expressions are powerful!"
pattern = r"powerful"

if search(pattern, text):
    print("Pattern found!")
```

You can also selectively import specific functions from the `re` module using the `from ... import ...` syntax. This allows you to call the functions directly without the `re.` prefix. This approach can make your code more concise but might make it less clear where the functions come from.
3. **Import with Alias in Python**:

```python
import re as regex

text = "Regular expressions are powerful!"
pattern = r"powerful"

if regex.search(pattern, text):
    print("Pattern found!")
```

You can import the `re` module with an alias using the `import ... as ...` syntax. This can be useful if you want to use a more descriptive name or avoid name conflicts. In this example, we're using `regex` as an alias for the `re` module, so we call functions with `regex.` instead of `re.`.

# Core Functions in `re` Module

## search()

1. **Basic Search**:

```python
import re

text = "Python is a programming language."
pattern = r"programming"

match = re.search(pattern, text)
if match:
    print(f"Found '{match.group()}' at position {match.start()}")
```

The `re.search()` function scans through the entire string looking for the first location where the pattern produces a match. It returns a match object if found, or None if no match exists. In this example, it finds "programming" in the text and reports its position. The `match.group()` method returns the matched text, and `match.start()` returns the starting position.
2. **Case-Insensitive Search**:

```python
import re

text = "Python is AWESOME!"
pattern = r"awesome"

match = re.search(pattern, text, re.IGNORECASE)
if match:
    print(f"Found '{match.group()}' at position {match.start()}")
```

The `re.search()` function accepts optional flags that modify how the pattern is applied. The `re.IGNORECASE` flag makes the search case-insensitive. In this example, even though the pattern is lowercase "awesome" and the text contains uppercase "AWESOME", the search still finds a match because of the case-insensitive flag.
3. **Search with Capturing Groups**:

```python
import re

text = "Contact us at support@example.com for assistance."
pattern = r"(\w+)@(\w+)\.(\w+)"

match = re.search(pattern, text)
if match:
    print(f"Full match: {match.group(0)}")
    print(f"Username: {match.group(1)}")
    print(f"Domain: {match.group(2)}")
    print(f"TLD: {match.group(3)}")
```

When you include capturing groups (parentheses) in your pattern, `re.search()` allows you to access those groups through the match object. In this example, we're extracting parts of an email address: `match.group(0)` returns the entire match, while `match.group(1)`, `match.group(2)`, etc. return the contents of each capturing group.

## findall()

1. **Finding All Occurrences**:

```python
import re

text = "The rain in Spain falls mainly in the plain."
pattern = r"\b\w*ain\b"

matches = re.findall(pattern, text)
print(matches)  # Output: ['rain', 'Spain', 'plain']
```

The `re.findall()` function returns all non-overlapping matches of the pattern in the string as a list of strings. In this example, we're finding all words that end with "ain". The pattern `\b\w*ain\b` matches word boundaries, followed by zero or more word characters, followed by "ain", followed by another word boundary.
2. **Finding with Capturing Groups**:

```python
import re

text = "Contacts: john@example.com, mary@gmail.com, support@company.org"
pattern = r"(\w+)@(\w+)\.(\w+)"

matches = re.findall(pattern, text)
print(matches)  # Output: [('john', 'example', 'com'), ('mary', 'gmail', 'com'), ('support', 'company', 'org')]

for username, domain, tld in matches:
    print(f"Email: {username}@{domain}.{tld}")
```

When your pattern includes capturing groups, `re.findall()` returns a list of tuples, where each tuple contains the captured groups for one match. In this example, we're extracting the username, domain, and TLD from each email address in the text. We can then unpack these tuples to work with the individual components.
3. **Finding Non-Overlapping Matches**:

```python
import re

text = "ababababab"
pattern = r"aba"

matches = re.findall(pattern, text)
print(matches)  # Output: ['aba', 'aba']
print(len(matches))  # Output: 2
```

The `re.findall()` function only returns non-overlapping matches. In this example, even though "aba" could potentially match at positions 0, 2, 4, 6, and 8 in the string "ababababab", `findall()` only returns matches at positions 0, 4, and 8 because these don't overlap. This behavior is important to understand when working with patterns that could match overlapping portions of text.

## split()

1. **Splitting on a Simple Pattern**:

```python
import re

text = "apple,banana;cherry:orange"
pattern = r"[,;:]"

result = re.split(pattern, text)
print(result)  # Output: ['apple', 'banana', 'cherry', 'orange']
```

The `re.split()` function splits a string by the occurrences of the pattern. In this example, we're splitting the text on any of the characters comma, semicolon, or colon. The pattern `[,;:]` is a character class that matches any one of these characters. The result is a list of substrings.
2. **Limiting the Number of Splits**:

```python
import re

text = "apple,banana,cherry,orange,grape"
pattern = r","

# Split only on the first two occurrences
result = re.split(pattern, text, maxsplit=2)
print(result)  # Output: ['apple', 'banana', 'cherry,orange,grape']
```

The `re.split()` function accepts an optional `maxsplit` parameter that limits the number of splits. In this example, we're splitting on commas but only performing at most 2 splits. This results in a list with 3 elements, where the last element contains the remaining unsplit portion of the string.
3. **Capturing the Delimiters**:

```python
import re

text = "apple,banana;cherry:orange"
pattern = r"([,;:])"

result = re.split(pattern, text)
print(result)  # Output: ['apple', ',', 'banana', ';', 'cherry', ':', 'orange']
```

If you include capturing groups in your split pattern, the captured delimiters are also included in the result list. In this example, we're putting parentheses around the character class `[,;:]` to create a capturing group. The result is a list that includes both the split substrings and the delimiters that were matched.

## sub()

1. **Simple Substitution**:

```python
import re

text = "The rain in Spain falls mainly in the plain."
pattern = r"rain"
replacement = "sun"

result = re.sub(pattern, replacement, text)
print(result)  # Output: The sun in Spain falls mainly in the plain.
```

The `re.sub()` function replaces all occurrences of the pattern with the replacement string. In this example, we're replacing the word "rain" with "sun". The function returns a new string with the substitutions made.
2. **Using Backreferences**:

```python
import re

text = "2023-03-15, 2022-12-31, 2024-06-30"
pattern = r"(\d{4})-(\d{2})-(\d{2})"
replacement = r"\2/\3/\1"

result = re.sub(pattern, replacement, text)
print(result)  # Output: 03/15/2023, 12/31/2022, 06/30/2024
```

In the replacement string, you can use backreferences to refer to captured groups from the pattern. In this example, we're converting dates from YYYY-MM-DD format to MM/DD/YYYY format. The `\1`, `\2`, and `\3` in the replacement string refer to the first, second, and third capturing groups in the pattern.
3. **Using a Function for Replacement**:

```python
import re

def celsius_to_fahrenheit(match):
    celsius = float(match.group(1))
    fahrenheit = celsius * 9/5 + 32
    return f"{fahrenheit:.1f}°F"

text = "Today's temperature is 25°C, yesterday was 22°C."
pattern = r"(\d+(?:\.\d+)?)°C"

result = re.sub(pattern, celsius_to_fahrenheit, text)
print(result)  # Output: Today's temperature is 77.0°F, yesterday was 71.6°F.
```

Instead of a replacement string, you can provide a function that takes a match object and returns the replacement string. In this example, we're converting temperatures from Celsius to Fahrenheit. The function extracts the Celsius value from the match, performs the conversion, and returns a formatted string with the Fahrenheit value.

## match()

1. **Basic Matching at Start of String**:

```python
import re

text = "Python is a programming language."
pattern = r"Python"

match = re.match(pattern, text)
if match:
    print(f"Found '{match.group()}' at the beginning")
else:
    print("Pattern not found at the beginning")
```

The `re.match()` function checks if the pattern matches at the beginning of the string. It returns a match object if the pattern matches at the start, or None otherwise. In this example, "Python" is at the beginning of the text, so `match()` finds it.
2. **Match vs. Search**:

```python
import re

text = "Programming in Python is fun."
pattern = r"Python"

match_result = re.match(pattern, text)
search_result = re.search(pattern, text)

print(f"match(): {match_result}")  # Output: match(): None
print(f"search(): {search_result}")  # Output: search(): &lt;re.Match object; span=(14, 20), match='Python'&gt;
```

This example illustrates the difference between `re.match()` and `re.search()`. The `match()` function only matches at the beginning of the string, so it returns None because "Python" is not at the start. The `search()` function scans the entire string, so it finds "Python" at position 14.
3. **Matching with Groups**:

```python
import re

text = "2023-03-15 is today's date."
pattern = r"(\d{4})-(\d{2})-(\d{2})"

match = re.match(pattern, text)
if match:
    year, month, day = match.groups()
    print(f"Date: {month}/{day}/{year}")  # Output: Date: 03/15/2023
```

Like `search()`, the `match()` function supports capturing groups. In this example, we're matching a date at the beginning of the string and extracting the year, month, and day components. The `match.groups()` method returns a tuple of all captured groups.


# Metacharacters in Regular Expressions

Metacharacters are special characters in regular expressions that have specific meanings beyond their literal character value. Here's a detailed explanation of each metacharacter with examples.

## [] (Character Classes)

Character classes match any single character from the set of characters specified within the brackets.

1. **Matching Vowels**:

```python
import re
text = "Hello, world!"
vowels = re.findall(r"[aeiou]", text)
print(vowels)  # Output: ['e', 'o', 'o']
```

The character class `[aeiou]` matches any single vowel in the text.
2. **Matching Range of Characters**:

```python
import re
text = "The quick brown fox jumps over the lazy dog."
uppercase = re.findall(r"[A-Z]", text)
print(uppercase)  # Output: ['T']
```

The character class `[A-Z]` matches any uppercase letter.
3. **Negated Character Class**:

```python
import re
text = "Hello"
non_vowels = re.findall(r"[^aeiou]", text)
print(non_vowels)  # Output: ['H', 'l', 'l']
```

The negated character class `[^aeiou]` matches any character that is not a vowel.

## \ (Backslash)

The backslash is used to escape metacharacters, allowing them to be used as literal characters, and to introduce special character sequences.

1. **Escaping Metacharacters**:

```python
import re
text = "The price is $10.99"
dollar_sign = re.search(r"\$", text)
print(dollar_sign.group())  # Output: $
```

The backslash escapes the dollar sign, which is normally a metacharacter.
2. **Special Character Sequences**:

```python
import re
text = "Phone: 555-123-4567"
digits = re.findall(r"\d", text)
print(digits)  # Output: ['5', '5', '5', '1', '2', '3', '4', '5', '6', '7']
```

The `\d` sequence matches any digit.
3. **Word Boundaries**:

```python
import re
text = "The cat in the hat"
words = re.findall(r"\b\w{3}\b", text)
print(words)  # Output: ['The', 'cat', 'the', 'hat']
```

The `\b` sequence matches word boundaries.

## . (Dot)

The dot metacharacter matches any single character except a newline.

1. **Matching Any Character**:

```python
import re
text = "The cat in the hat"
matches = re.findall(r"c.t", text)
print(matches)  # Output: ['cat']
```

The pattern `c.t` matches "cat" because the dot matches 'a'.
2. **Matching Multiple Characters**:

```python
import re
text = "The quick brown fox"
matches = re.findall(r"qu..k", text)
print(matches)  # Output: ['quick']
```

The pattern `qu..k` matches "quick" because the two dots match 'i' and 'c'.
3. **Matching with DOTALL Flag**:

```python
import re
text = "Hello\nWorld"
matches = re.findall(r"Hello.World", text, re.DOTALL)
print(matches)  # Output: ['Hello\nWorld']
```

With the DOTALL flag, the dot also matches newlines.

## ^ (Caret)

The caret has two uses: it matches the start of a string or line, and it negates a character class when used as the first character inside square brackets.

1. **Matching Start of String**:

```python
import re
text = "Hello, world!"
match = re.search(r"^Hello", text)
print(match.group())  # Output: Hello
```

The pattern `^Hello` matches "Hello" only at the beginning of the string.
2. **Matching Start of Each Line**:

```python
import re
text = "Hello\nWorld"
matches = re.findall(r"^.", text, re.MULTILINE)
print(matches)  # Output: ['H', 'W']
```

With the MULTILINE flag, `^` matches the start of each line.
3. **Negating Character Class**:

```python
import re
text = "a1b2c3"
non_digits = re.findall(r"[^0-9]", text)
print(non_digits)  # Output: ['a', 'b', 'c']
```

Inside square brackets, `^` negates the character class, matching any character not in the class.

## \$ (Dollar)

The dollar sign matches the end of a string or line.

1. **Matching End of String**:

```python
import re
text = "Hello, world!"
match = re.search(r"world!$", text)
print(match.group())  # Output: world!
```

The pattern `world!$` matches "world!" only at the end of the string.
2. **Matching End of Each Line**:

```python
import re
text = "Hello\nWorld"
matches = re.findall(r".$", text, re.MULTILINE)
print(matches)  # Output: ['o', 'd']
```

With the MULTILINE flag, `$` matches the end of each line.
3. **Validating Input Format**:

```python
import re
def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email))

print(is_valid_email("user@example.com"))  # Output: True
print(is_valid_email("invalid@email"))     # Output: False
```

The `$` ensures the pattern matches the entire string.

## * (Asterisk)

The asterisk matches zero or more occurrences of the preceding character or group.

1. **Matching Zero or More Characters**:

```python
import re
text = "color colour"
matches = re.findall(r"colou*r", text)
print(matches)  # Output: ['color', 'colour']
```

The pattern `colou*r` matches both "color" (zero 'u's) and "colour" (one 'u').
2. **Greedy Matching**:

```python
import re
text = "<p>First paragraph</p><p>Second paragraph</p>"
match = re.search(r"<p>.*</p>", text)
print(match.group())  # Output: <p>First paragraph</p><p>Second paragraph</p>
```

The `.*` greedily matches everything between the first `<p>` and the last `</p>`.
3. **Matching File Extensions**:

```python
import re
filenames = ["file.txt", "image.jpg", "document"]
matches = re.findall(r"\.\w*", " ".join(filenames))
print(matches)  # Output: ['.txt', '.jpg']
```

The pattern `\.\w*` matches a dot followed by zero or more word characters.

## + (Plus)

The plus sign matches one or more occurrences of the preceding character or group.

1. **Matching One or More Characters**:

```python
import re
text = "color colour"
matches = re.findall(r"colou+r", text)
print(matches)  # Output: ['colour']
```

The pattern `colou+r` matches only "colour" (one or more 'u's).
2. **Extracting Words**:

```python
import re
text = "Hello, world! 123"
words = re.findall(r"\b[a-zA-Z]+\b", text)
print(words)  # Output: ['Hello', 'world']
```

The pattern `\b[a-zA-Z]+\b` matches one or more letters between word boundaries.
3. **Matching Consecutive Digits**:

```python
import re
text = "Phone: 555-123-4567"
digit_groups = re.findall(r"\d+", text)
print(digit_groups)  # Output: ['555', '123', '4567']
```

The pattern `\d+` matches one or more consecutive digits.

## ? (Question Mark)

The question mark matches zero or one occurrence of the preceding character or group.

1. **Optional Character**:

```python
import re
text = "color colour"
matches = re.findall(r"colou?r", text)
print(matches)  # Output: ['color', 'colour']
```

The pattern `colou?r` matches both "color" (zero 'u's) and "colour" (one 'u').
2. **Non-Greedy Matching**:

```python
import re
text = "<p>First paragraph</p><p>Second paragraph</p>"
matches = re.findall(r"<p>.*?</p>", text)
print(matches)  # Output: ['<p>First paragraph</p>', '<p>Second paragraph</p>']
```

The `.*?` non-greedily matches everything between each `<p>` and the next `</p>`.
3. **Optional Group**:

```python
import re
text = "Reg Regular RegEx RegExp Expression"
matches = re.findall(r"Reg(ular)? ?Ex(pression)?", text)
print([f"Reg{m[^0] if m[^0] else ''} Ex{m[^1] if m[^1] else ''}" for m in matches])
# Output: ['Reg Ex', 'Regular Ex']
```

The pattern makes both "ular" and "pression" optional.

## {} (Curly Braces)

Curly braces specify the exact number or range of occurrences of the preceding character or group.

1. **Exact Count**:

```python
import re
text = "The quick brown fox"
matches = re.findall(r"\b\w{5}\b", text)
print(matches)  # Output: ['quick', 'brown']
```

The pattern `\b\w{5}\b` matches exactly 5-letter words.
2. **Range of Counts**:

```python
import re
text = "The quick brown fox jumps over the lazy dog"
matches = re.findall(r"\b\w{3,5}\b", text)
print(matches)  # Output: ['The', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
```

The pattern `\b\w{3,5}\b` matches words with 3 to 5 letters.
3. **Minimum Count**:

```python
import re
text = "Phone numbers: 123, 4567, 12345678, 9876543210"
matches = re.findall(r"\b\d{7,}\b", text)
print(matches)  # Output: ['12345678', '9876543210']
```

The pattern `\b\d{7,}\b` matches numbers with 7 or more digits.

## | (Pipe)

The pipe character acts as an OR operator, matching either the expression before or after it.

1. **Alternative Words**:

```python
import re
text = "The cat and the dog"
matches = re.findall(r"cat|dog", text)
print(matches)  # Output: ['cat', 'dog']
```

The pattern `cat|dog` matches either "cat" or "dog".
2. **Alternative Patterns**:

```python
import re
text = "Phone: 555-123-4567, Email: user@example.com"
matches = re.findall(r"\d{3}-\d{3}-\d{4}|\w+@\w+\.\w+", text)
print(matches)  # Output: ['555-123-4567', 'user@example.com']
```

This pattern matches either a phone number or an email address.
3. **Alternative Groups**:

```python
import re
text = "color colour behavior behaviour"
matches = re.findall(r"colou?r|behaviou?r", text)
print(matches)  # Output: ['color', 'colour', 'behavior', 'behaviour']
```

This pattern matches American or British spelling of these words.

## () (Parentheses)

Parentheses group patterns together and capture the matched text.

1. **Grouping for Quantifiers**:

```python
import re
text = "hahaha haha ha"
matches = re.findall(r"(ha){2,}", text)
print(matches)  # Output: ['ha', 'ha']
```

The pattern `(ha){2,}` matches "ha" repeated at least twice.
2. **Capturing Groups**:

```python
import re
text = "Date: 2023-03-15"
match = re.search(r"(\d{4})-(\d{2})-(\d{2})", text)
print(f"Year: {match.group(1)}, Month: {match.group(2)}, Day: {match.group(3)}")
# Output: Year: 2023, Month: 03, Day: 15
```

The parentheses capture the year, month, and day components.
3. **Non-Capturing Groups**:

```python
import re
text = "Date: 2023-03-15"
match = re.search(r"(?:\d{4})-(\d{2})-(\d{2})", text)
print(f"Month: {match.group(1)}, Day: {match.group(2)}")
# Output: Month: 03, Day: 15
```

The `(?:...)` syntax creates a non-capturing group for the year.

These metacharacters form the foundation of regular expressions, allowing for powerful pattern matching and text processing capabilities.



# Character Classes in Regular Expressions

Character classes are one of the most fundamental and powerful features in regular expressions. They allow you to match specific sets of characters in a concise way.

## Basic Character Classes

### \d (Digit)

1. **Matching Phone Numbers**:

```python
import re
phone_pattern = r"\d{3}-\d{3}-\d{4}"
text = "Call me at 555-123-4567 or 800-555-9876"
matches = re.findall(phone_pattern, text)
print(matches)  # Output: ['555-123-4567', '800-555-9876']
```

The `\d` metacharacter matches any digit (0-9). In this example, we're using it with quantifiers to match the standard format for US phone numbers.
2. **Validating Numeric IDs**:

```python
import re
def is_valid_id(id_string):
    pattern = r"^\d{8}$"  # Exactly 8 digits
    return bool(re.match(pattern, id_string))

print(is_valid_id("12345678"))  # True
print(is_valid_id("1234567"))   # False (too short)
print(is_valid_id("A1234567"))  # False (contains non-digit)
```

Here, `\d{8}` matches exactly 8 digits, making it perfect for validating fixed-length numeric IDs.

### \D (Non-digit)

1. **Extracting Non-numeric Parts**:

```python
import re
text = "Product: ABC123, Price: $19.99"
non_digits = re.findall(r"\D+", text)
print(non_digits)  # Output: ['Product: ABC', ', Price: $', '.']
```

The `\D` metacharacter matches any character that is not a digit, helping extract text portions.
2. **Removing Digits**:

```python
import re
text = "My phone is 555-123-4567 and my zip code is 12345"
no_digits = re.sub(r"\d", "", text)
print(no_digits)  # Output: "My phone is -- and my zip code is "
```

Using `\D` with substitution removes all digits from the text.

### \w (Word Character)

1. **Extracting Words**:

```python
import re
text = "Hello, world! Python 3.9 is awesome."
words = re.findall(r"\w+", text)
print(words)  # Output: ['Hello', 'world', 'Python', '3', '9', 'is', 'awesome']
```

The `\w` metacharacter matches any word character (letters, digits, and underscore).
2. **Validating Usernames**:

```python
import re
def is_valid_username(username):
    pattern = r"^\w{3,16}$"  # 3-16 word characters
    return bool(re.match(pattern, username))

print(is_valid_username("user_123"))  # True
print(is_valid_username("user-123"))  # False (contains hyphen)
```

This pattern ensures usernames only contain letters, numbers, and underscores.

### \W (Non-word Character)

1. **Finding Separators**:

```python
import re
text = "name:John,age:30,city:New York"
separators = re.findall(r"\W+", text)
print(separators)  # Output: [':', ',', ':', ',', ':', ' ']
```

The `\W` metacharacter finds all non-word characters, which are often used as separators.
2. **Splitting on Non-word Characters**:

```python
import re
text = "name:John,age:30,city:New York"
parts = re.split(r"\W+", text)
print(parts)  # Output: ['name', 'John', 'age', '30', 'city', 'New', 'York']
```

This splits the text at any sequence of non-word characters.

### \s (Whitespace)

1. **Normalizing Whitespace**:

```python
import re
text = "This    has    irregular   spacing."
normalized = re.sub(r"\s+", " ", text)
print(normalized)  # Output: "This has irregular spacing."
```

The `\s` metacharacter matches any whitespace character (space, tab, newline).
2. **Parsing CSV-like Data**:

```python
import re
data = "Name    Age     City\nJohn    30      New York\nJane    25      Boston"
rows = data.split('\n')
for row in rows:
    fields = re.split(r'\s+', row.strip())
    print(fields)
```

This splits each line on whitespace, parsing tabular data.

### \S (Non-whitespace)

1. **Extracting Words and Symbols**:

```python
import re
text = "Hello, world! Python 3.9"
non_spaces = re.findall(r"\S+", text)
print(non_spaces)  # Output: ['Hello,', 'world!', 'Python', '3.9']
```

The `\S` metacharacter matches any non-whitespace character.
2. **Finding Continuous Text**:

```python
import re
text = "Error   code:   404   Not   Found"
continuous = re.findall(r"\S+", text)
print(continuous)  # Output: ['Error', 'code:', '404', 'Not', 'Found']
```

This finds all continuous sequences of characters.

## Custom Character Classes

### [abc] (Set of Characters)

1. **Matching Vowels**:

```python
import re
text = "Hello, world!"
vowels = re.findall(r"[aeiou]", text)
print(vowels)  # Output: ['e', 'o', 'o']
```

The character class `[aeiou]` matches any single vowel.
2. **Matching Specific Digits**:

```python
import re
numbers = "12345 67890"
even_digits = re.findall(r"[^02468]", numbers)
print(even_digits)  # Output: ['2', '4', '6', '8', '0']
```

This matches only even digits in the text.

### [^abc] (Negated Set)

1. **Finding Non-Vowels**:

```python
import re
text = "Hello"
non_vowels = re.findall(r"[^aeiou]", text)
print(non_vowels)  # Output: ['H', 'l', 'l']
```

The negated character class `[^aeiou]` matches any character that is not a vowel.
2. **Removing Special Characters**:

```python
import re
text = "Hello, world! 123"
clean_text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
print(clean_text)  # Output: "Hello world 123"
```

This removes all characters that are not letters, numbers, or spaces.

### [a-z] (Range)

1. **Matching Lowercase Letters**:

```python
import re
text = "Hello World"
lowercase = re.findall(r"[a-z]+", text)
print(lowercase)  # Output: ['ello', 'orld']
```

The character class `[a-z]` matches any lowercase letter.
2. **Validating Hexadecimal**:

```python
import re
def is_valid_hex(hex_string):
    pattern = r"^[0-9a-fA-F]+$"
    return bool(re.match(pattern, hex_string))

print(is_valid_hex("1a2b3c"))  # True
print(is_valid_hex("1a2g3c"))  # False (contains 'g')
```

This checks if a string contains only valid hexadecimal characters.

By understanding and effectively using character classes, you can create more precise and powerful regular expressions for pattern matching and text processing tasks.



# Anchors and Boundaries in Regular Expressions

Anchors and boundaries are special metacharacters in regular expressions that don't match characters, but rather positions within the text. They are essential for creating precise patterns that match only at specific locations.

## \A (Start of String)

The `\A` anchor matches only at the start of the entire string, regardless of multiline mode.

1. **Validating String Beginning**:

```python
import re

texts = ["Hello world", "World hello", "\nHello world"]
pattern = r"\AHello"

for text in texts:
    match = re.search(pattern, text)
    print(f"'{text}': {'Match' if match else 'No match'}")
# Output:
# 'Hello world': Match
# 'World hello': No match
# '
# Hello world': No match
```

The pattern `\AHello` matches "Hello" only when it appears at the absolute beginning of the string. Unlike `^`, it won't match at the beginning of a line in multiline text.
2. **Ensuring Proper Document Format**:

```python
import re

def validate_document(doc):
    # Document must start with "CONFIDENTIAL: "
    pattern = r"\ACONFIDENTIAL: "
    return bool(re.match(pattern, doc))

print(validate_document("CONFIDENTIAL: This is secret information"))  # True
print(validate_document("This is CONFIDENTIAL: information"))         # False
print(validate_document("\nCONFIDENTIAL: This is secret"))            # False
```

This example ensures a document starts with a specific header, regardless of any newlines that might be present.
3. **Difference Between \A and ^**:

```python
import re

text = "First line\nSecond line"

a_matches = re.findall(r"\AFirst", text)
caret_matches = re.findall(r"^First", text)

multiline_a_matches = re.findall(r"\AFirst", text, re.MULTILINE)
multiline_caret_matches = re.findall(r"^First", text, re.MULTILINE)

print(f"\\A matches: {a_matches}")                    # ['First']
print(f"^ matches: {caret_matches}")                  # ['First']
print(f"\\A with MULTILINE: {multiline_a_matches}")   # ['First']
print(f"^ with MULTILINE: {multiline_caret_matches}") # ['First']

# Now check for 'Second'
a_matches = re.findall(r"\ASecond", text)
caret_matches = re.findall(r"^Second", text)

multiline_a_matches = re.findall(r"\ASecond", text, re.MULTILINE)
multiline_caret_matches = re.findall(r"^Second", text, re.MULTILINE)

print(f"\\A matches: {a_matches}")                    # []
print(f"^ matches: {caret_matches}")                  # []
print(f"\\A with MULTILINE: {multiline_a_matches}")   # []
print(f"^ with MULTILINE: {multiline_caret_matches}") # ['Second']
```

This example demonstrates that `\A` only matches at the start of the entire string, while `^` can match at the start of each line when the MULTILINE flag is used.

## \Z (End of String)

The `\Z` anchor matches only at the end of the entire string or before the final newline.

1. **Validating String Ending**:

```python
import re

texts = ["Hello world", "Hello world!", "Hello world\n"]
pattern = r"world\Z"

for text in texts:
    match = re.search(pattern, text)
    print(f"'{text}': {'Match' if match else 'No match'}")
# Output:
# 'Hello world': Match
# 'Hello world!': No match
# 'Hello world
# ': Match
```

The pattern `world\Z` matches "world" only when it appears at the end of the string or right before the final newline.
2. **Validating File Extensions**:

```python
import re

def is_python_file(filename):
    pattern = r"\.py\Z"
    return bool(re.search(pattern, filename))

print(is_python_file("script.py"))      # True
print(is_python_file("script.py.bak"))  # False
print(is_python_file("script.py\n"))    # True
```

This function checks if a filename ends with the ".py" extension.
3. **Difference Between \Z and \$**:

```python
import re

text = "Line one\nLine two"

z_matches = re.findall(r"one\Z", text)
dollar_matches = re.findall(r"one$", text)

multiline_z_matches = re.findall(r"one\Z", text, re.MULTILINE)
multiline_dollar_matches = re.findall(r"one$", text, re.MULTILINE)

print(f"\\Z matches: {z_matches}")                      # []
print(f"$ matches: {dollar_matches}")                   # []
print(f"\\Z with MULTILINE: {multiline_z_matches}")     # []
print(f"$ with MULTILINE: {multiline_dollar_matches}")  # ['one']
```

This example shows that `\Z` only matches at the end of the entire string, while `$` can match at the end of each line when the MULTILINE flag is used.

## \b (Word Boundary)

The `\b` anchor matches at a position where a word character is not followed or preceded by another word character.

1. **Finding Whole Words**:

```python
import re

text = "The cat in the cathedral"
whole_word_matches = re.findall(r"\bcat\b", text)
any_matches = re.findall(r"cat", text)

print(f"Whole word 'cat': {whole_word_matches}")  # ['cat']
print(f"Any 'cat': {any_matches}")                # ['cat', 'cat']
```

The pattern `\bcat\b` matches "cat" only as a whole word, not as part of "cathedral".
2. **Replacing Specific Words**:

```python
import re

text = "The cat saw another cat in the cathedral"
replaced = re.sub(r"\bcat\b", "dog", text)

print(replaced)  # "The dog saw another dog in the cathedral"
```

This replaces only the whole word "cat" with "dog", leaving "cathedral" unchanged.
3. **Finding Words with Specific Prefixes**:

```python
import re

text = "preprocess preprocessing preprocessor present president"
pre_words = re.findall(r"\bpre\w+", text)

print(pre_words)  # ['preprocess', 'preprocessing', 'preprocessor', 'present', 'president']
```

The pattern `\bpre\w+` matches words that start with "pre".

## \B (Non-word Boundary)

The `\B` anchor matches at a position where `\b` does not match - that is, between two word characters or between two non-word characters.

1. **Finding Substrings Within Words**:

```python
import re

text = "The cat in the cathedral"
within_word_matches = re.findall(r"\Bcat\B", text)

print(within_word_matches)  # []

text = "The cat in the cathedral and education"
within_word_matches = re.findall(r"\Bcat\B", text)

print(within_word_matches)  # ['cat']
```

The pattern `\Bcat\B` matches "cat" only when it's surrounded by word characters on both sides, as in "education".
2. **Finding Internal Patterns**:

```python
import re

text = "class subclass classify classification"
internal_class = re.findall(r"\Bclass\b", text)

print(internal_class)  # ['class', 'class']
```

The pattern `\Bclass\b` matches "class" when it's preceded by word characters but is a complete word itself, as in "subclass".
3. **Finding Embedded Numbers**:

```python
import re

text = "abc123def 456 xyz789"
embedded_numbers = re.findall(r"\B\d+\B", text)

print(embedded_numbers)  # ['2']
```

The pattern `\B\d+\B` matches digits that are surrounded by other characters on both sides. In this case, only "2" in "abc123def" is completely surrounded.

## ^ (Start of Line)

The `^` anchor matches at the start of a string or at the start of a line in multiline mode.

1. **Matching Line Beginnings**:

```python
import re

text = "First line\nSecond line\nThird line"
first_words = re.findall(r"^\w+", text, re.MULTILINE)

print(first_words)  # ['First', 'Second', 'Third']
```

With the MULTILINE flag, the pattern `^\w+` matches the first word of each line.
2. **Validating Input Format**:

```python
import re

def is_valid_name(name):
    pattern = r"^[A-Z][a-z]+ [A-Z][a-z]+$"
    return bool(re.match(pattern, name))

print(is_valid_name("John Doe"))      # True
print(is_valid_name("john Doe"))      # False
print(is_valid_name("John doe"))      # False
print(is_valid_name("John Doe Jr."))  # False
```

This function validates that a name starts with capital letters and has exactly two parts.
3. **Finding Lines with Specific Content**:

```python
import re

log = """INFO: Operation started
ERROR: Connection failed
INFO: Retrying connection
WARNING: Timeout occurred
ERROR: Operation failed"""

error_lines = re.findall(r"^ERROR.*$", log, re.MULTILINE)

print(error_lines)  # ['ERROR: Connection failed', 'ERROR: Operation failed']
```

This pattern finds all lines that start with "ERROR".

## \$ (End of Line)

The `$` anchor matches at the end of a string or at the end of a line in multiline mode.

1. **Matching Line Endings**:

```python
import re

text = "Line one.\nLine two!\nLine three?"
punctuation = re.findall(r"[.!?]$", text, re.MULTILINE)

print(punctuation)  # ['.', '!', '?']
```

With the MULTILINE flag, the pattern `[.!?]$` matches the punctuation at the end of each line.
2. **Validating Complete Lines**:

```python
import re

csv_data = """name,age,city
John,30,New York
Jane,25,Boston
invalid line
Mark,40,Chicago"""

valid_lines = re.findall(r"^[^,]+,\d+,[^,]+$", csv_data, re.MULTILINE)

print(len(valid_lines))  # 3
```

This pattern validates CSV lines that have exactly three fields with the middle field being numeric.
3. **Finding Incomplete Sentences**:

```python
import re

text = """This is a complete sentence.
This is not
This is another complete sentence.
Neither is this"""

incomplete = re.findall(r"^.*[^.]$", text, re.MULTILINE)

print(incomplete)  # ['This is not', 'Neither is this']
```

This pattern finds lines that don't end with a period, potentially indicating incomplete sentences.

Understanding anchors and boundaries is crucial for creating precise regular expressions that match exactly what you want, where you want it. They allow you to constrain your patterns to specific positions in the text, making your regex more accurate and efficient.



# Quantifiers in Regular Expressions

Quantifiers in regular expressions specify how many times a character, group, or character class should be matched. They are powerful tools that allow for flexible pattern matching.

## Greedy Quantifiers

Greedy quantifiers match as much text as possible while still allowing the overall pattern to match.

### * (Asterisk) - Zero or More

The asterisk matches zero or more occurrences of the preceding element.

1. **Matching Optional Parts**:

```python
import re

text = "color colour"
matches = re.findall(r"colou*r", text)

print(matches)  # Output: ['color', 'colour']
```

The pattern `colou*r` matches "color" (with zero 'u's) and "colour" (with one 'u'). The asterisk allows the 'u' to appear zero or more times.
2. **Matching Everything Between Delimiters**:

```python
import re

html = "<div>Content 1</div><div>Content 2</div>"
content = re.search(r"<div>.*</div>", html)

print(content.group())  # Output: "<div>Content 1</div><div>Content 2</div>"
```

The pattern `<div>.*</div>` greedily matches everything from the first opening `<div>` to the last closing `</div>`. The asterisk causes the dot to match all characters in between.
3. **Finding All Comments**:

```python
import re

code = "x = 5; // Variable assignment\ny = 10; /* This is a\nmulti-line comment */ z = 15;"
comments = re.findall(r"//.*|/\*.*\*/", code, re.DOTALL)

print(comments)  # Output: ["// Variable assignment", "/* This is a\nmulti-line comment */"]
```

This pattern matches both single-line and multi-line comments. The `.*` greedily captures all characters.

### + (Plus) - One or More

The plus sign matches one or more occurrences of the preceding element.

1. **Matching Non-Empty Sequences**:

```python
import re

text = "a ab abc abcd"
matches = re.findall(r"ab+c", text)

print(matches)  # Output: ['abc']
```

The pattern `ab+c` matches 'a' followed by one or more 'b's, followed by 'c'. Only "abc" matches this pattern.
2. **Extracting Words**:

```python
import re

text = "Hello, world! 123"
words = re.findall(r"[A-Za-z]+", text)

print(words)  # Output: ['Hello', 'world']
```

The pattern `[A-Za-z]+` matches one or more letters, effectively extracting words.
3. **Parsing Numbers with Optional Decimals**:

```python
import re

text = "Prices: $10, $15.99, $3.50"
prices = re.findall(r"\$\d+(\.\d+)?", text)

print(["$" + match for match in re.findall(r"\d+(\.\d+)?", text)])  # Output: ['$10', '$15.99', '$3.50']
```

The pattern `\$\d+(\.\d+)?` matches a dollar sign followed by one or more digits, optionally followed by a decimal point and more digits.

### ? (Question Mark) - Zero or One

The question mark matches zero or one occurrence of the preceding element.

1. **Matching Optional Characters**:

```python
import re

text = "color colour"
matches = re.findall(r"colou?r", text)

print(matches)  # Output: ['color', 'colour']
```

The pattern `colou?r` matches both "color" and "colour" because the 'u' is optional.
2. **Matching HTML Tags**:

```python
import re

html = "<p>Paragraph</p><br>"
tags = re.findall(r"&lt;(\w+)( [^&gt;]*)?&gt;(.*?)&lt;/\1&gt;", html)

print(tags)  # Output: [('p', '', 'Paragraph')]
```

The pattern includes `( [^&gt;]*)?` which matches zero or one occurrence of a space followed by any characters that aren't '>', capturing optional HTML attributes.
3. **Matching Phone Numbers**:

```python
import re

text = "Call me at 555-123-4567 or 5551234567"
numbers = re.findall(r"\d{3}-?\d{3}-?\d{4}", text)

print(numbers)  # Output: ['555-123-4567', '5551234567']
```

The pattern `\d{3}-?\d{3}-?\d{4}` matches phone numbers with or without hyphens because the hyphen is made optional with `?`.

### {n} - Exactly n Times

The `{n}` quantifier matches exactly n occurrences of the preceding element.

1. **Matching Fixed-Length Codes**:

```python
import re

text = "Product codes: ABC123, XYZ456, PQ78"
codes = re.findall(r"[A-Z]{3}\d{3}", text)

print(codes)  # Output: ['ABC123', 'XYZ456']
```

The pattern `[A-Z]{3}\d{3}` matches exactly 3 uppercase letters followed by exactly 3 digits.
2. **Validating Zip Codes**:

```python
import re

addresses = ["New York, NY 10001", "Boston, MA 02110", "Chicago, IL 6061"]
zip_codes = [re.search(r"\b\d{5}\b", address) for address in addresses]

print([match.group() if match else "Invalid zip" for match in zip_codes])
# Output: ['10001', '02110', 'Invalid zip']
```

The pattern `\b\d{5}\b` matches exactly 5 digits between word boundaries, validating standard US zip codes.
3. **Parsing Fixed-Format Data**:

```python
import re

data = "USER0001JOHN DOE     ADMIN"
pattern = r"USER(\d{4})([A-Z ]{12})([A-Z]+)"
match = re.search(pattern, data)

if match:
    print(f"ID: {match.group(1)}, Name: {match.group(2).strip()}, Role: {match.group(3)}")
# Output: "ID: 0001, Name: JOHN DOE, Role: ADMIN"
```

This pattern parses fixed-width data where each field has a specific length.

### {n,} - At Least n Times

The `{n,}` quantifier matches n or more occurrences of the preceding element.

1. **Matching Long Words**:

```python
import re

text = "The antidisestablishmentarianism is a long word"
long_words = re.findall(r"\b\w{15,}\b", text)

print(long_words)  # Output: ['antidisestablishmentarianism']
```

The pattern `\b\w{15,}\b` matches words that are at least 15 characters long.
2. **Validating Strong Passwords**:

```python
import re

def is_strong_password(password):
    # At least 8 characters, with at least one uppercase, one lowercase, and one digit
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$"
    return bool(re.match(pattern, password))

print(is_strong_password("Passw0rd"))  # Output: True
print(is_strong_password("weak"))      # Output: False
```

The pattern uses lookaheads to ensure various character types, then `.{8,}` to ensure at least 8 characters.
3. **Finding Long Sequences**:

```python
import re

dna = "ACGTACGTACGTACGTACGTACGTACGTACGT"
repeats = re.findall(r"((?:ACGT){3,})", dna)

print(repeats)  # Output: ['ACGTACGTACGTACGTACGTACGTACGTACGT']
```

This pattern finds sequences where "ACGT" is repeated at least 3 times.

### {n,m} - Between n and m Times

The `{n,m}` quantifier matches between n and m occurrences of the preceding element.

1. **Matching Medium-Length Words**:

```python
import re

text = "The quick brown fox jumps over the lazy dog"
medium_words = re.findall(r"\b\w{4,6}\b", text)

print(medium_words)  # Output: ['quick', 'brown', 'jumps']
```

The pattern `\b\w{4,6}\b` matches words that are between 4 and 6 characters long.
2. **Validating Product Codes**:

```python
import re

codes = ["A123", "AB12", "ABC1", "ABCD"]
valid_codes = [code for code in codes if re.match(r"^[A-Z]{1,3}\d{1,3}$", code)]

print(valid_codes)  # Output: ['A123', 'AB12', 'ABC1']
```

The pattern `^[A-Z]{1,3}\d{1,3}$` matches codes that start with 1-3 uppercase letters followed by 1-3 digits.
3. **Finding Date Patterns**:

```python
import re

text = "Dates: 1/1/2023, 01/01/2023, 1/01/2023, 01/1/2023"
dates = re.findall(r"\b\d{1,2}/\d{1,2}/\d{4}\b", text)

print(dates)  # Output: ['1/1/2023', '01/01/2023', '1/01/2023', '01/1/2023']
```

This pattern matches date formats with 1-2 digits for day and month, and exactly 4 digits for year.

## Lazy Quantifiers

Lazy (or non-greedy) quantifiers match as little text as possible while still allowing the overall pattern to match.

### *? - Zero or More (Lazy)

The `*?` quantifier lazily matches zero or more occurrences of the preceding element.

1. **Matching HTML Tags**:

```python
import re

html = "<div>Content 1</div><div>Content 2</div>"

# Greedy approach
greedy_match = re.findall(r"<div>.*</div>", html)
print(f"Greedy: {greedy_match}")  # Output: Greedy: ['<div>Content 1</div><div>Content 2</div>']

# Lazy approach
lazy_match = re.findall(r"<div>.*?</div>", html)
print(f"Lazy: {lazy_match}")      # Output: Lazy: ['<div>Content 1</div>', '<div>Content 2</div>']
```

The lazy pattern `<div>.*?</div>` matches each div tag pair separately, rather than greedily matching from the first opening tag to the last closing tag.
2. **Extracting Quoted Strings**:

```python
import re

text = 'He said "hello" and then "goodbye"'

# Greedy approach would fail
greedy_match = re.findall(r'".*"', text)
print(f"Greedy: {greedy_match}")  # Output: Greedy: ['"hello" and then "goodbye"']

# Lazy approach
lazy_match = re.findall(r'".*?"', text)
print(f"Lazy: {lazy_match}")      # Output: Lazy: ['"hello"', '"goodbye"']
```

The lazy pattern `".*?"` matches each quoted string separately.
3. **Finding Minimal Blocks**:

```python
import re

text = "{{block1}} some text {{block2}} more text {{block3}}"

# Greedy approach
greedy_match = re.findall(r'{{.*}}', text)
print(f"Greedy: {greedy_match}")  # Output: Greedy: ['{{block1}} some text {{block2}} more text {{block3}}']

# Lazy approach
lazy_match = re.findall(r'{{.*?}}', text)
print(f"Lazy: {lazy_match}")      # Output: Lazy: ['{{block1}}', '{{block2}}', '{{block3}}']
```

The lazy pattern `{{.*?}}` matches each block separately.

### +? - One or More (Lazy)

The `+?` quantifier lazily matches one or more occurrences of the preceding element.

1. **Parsing XML Elements**:

```python
import re

xml = "&lt;item&gt;&lt;name&gt;Product 1&lt;/name&gt;&lt;price&gt;19.99&lt;/price&gt;&lt;/item&gt;&lt;item&gt;&lt;name&gt;Product 2&lt;/name&gt;&lt;/item&gt;"

# Greedy approach
greedy_match = re.findall(r'&lt;name&gt;.+&lt;/name&gt;', xml)
print(f"Greedy: {greedy_match}")  # Output: Greedy: ['&lt;name&gt;Product 1&lt;/name&gt;&lt;price&gt;19.99&lt;/price&gt;&lt;/item&gt;&lt;item&gt;&lt;name&gt;Product 2&lt;/name&gt;']

# Lazy approach
lazy_match = re.findall(r'&lt;name&gt;.+?&lt;/name&gt;', xml)
print(f"Lazy: {lazy_match}")      # Output: Lazy: ['&lt;name&gt;Product 1&lt;/name&gt;', '&lt;name&gt;Product 2&lt;/name&gt;']
```

The lazy pattern `&lt;name&gt;.+?&lt;/name&gt;` matches each name element separately.
2. **Finding Minimal Word Sequences**:

```python
import re

text = "aaabaaabaaab"

# Greedy approach
greedy_match = re.findall(r'a.+b', text)
print(f"Greedy: {greedy_match}")  # Output: Greedy: ['aaabaaabaaab']

# Lazy approach
lazy_match = re.findall(r'a.+?b', text)
print(f"Lazy: {lazy_match}")      # Output: Lazy: ['aaab', 'aaab', 'aaab']
```

The lazy pattern `a.+?b` matches each 'a...b' sequence minimally.
3. **Extracting URL Parameters**:

```python
import re

url = "https://example.com/search?q=regex&amp;page=1&amp;sort=desc"

# Greedy approach would match the entire query string
greedy_match = re.search(r'\?.+=.+', url)
print(f"Greedy: {greedy_match.group()}")  # Output: Greedy: ?q=regex&amp;page=1&amp;sort=desc

# Lazy approach to extract individual parameters
lazy_matches = re.findall(r'[?&amp;]([^=]+)=([^&amp;]+)', url)
print(f"Lazy: {lazy_matches}")  # Output: Lazy: [('q', 'regex'), ('page', '1'), ('sort', 'desc')]
```

This example uses character classes rather than `+?`, but demonstrates the concept of minimal matching for URL parameters.

### ?? - Zero or One (Lazy)

The `??` quantifier lazily matches zero or one occurrence of the preceding element.

1. **Optional HTML Attributes**:

```python
import re

html = '<div><p>Content</p></div>'

# Greedy approach
greedy_match = re.search(r'&lt;div.*?&gt;', html)
print(f"Greedy: {greedy_match.group()}")  # Output: Greedy: <div>

# Lazy approach
lazy_match = re.search(r'&lt;div(.*?)&gt;', html)
print(f"Lazy attributes: {lazy_match.group(1)}")  # Output: Lazy attributes:  class="container"
```

The lazy pattern `&lt;div(.*?)&gt;` captures the attributes minimally.
2. **Matching Optional Parts**:

```python
import re

words = ["color", "colour"]

for word in words:
    # Greedy approach
    greedy_match = re.search(r'colou?r', word)
    # Lazy approach
    lazy_match = re.search(r'colo(u??)', word)
    
    print(f"Word: {word}")
    print(f"Greedy match: {greedy_match.group()}")
    print(f"Lazy 'u' present: {'Yes' if lazy_match.group(1) else 'No'}")
```

The lazy pattern `u??` will prefer not to match the 'u' if possible, but will if necessary for the overall pattern to match.
3. **Finding Minimal Patterns**:

```python
import re

text = "This (is) a (test) with (parentheses)"

# Greedy approach
greedy_match = re.findall(r'\(.*?\)', text)
print(f"Greedy: {greedy_match}")  # Output: Greedy: ['(is)', '(test)', '(parentheses)']

# Even lazier approach
lazy_match = re.findall(r'\((.*?)\)', text)
print(f"Lazy content: {lazy_match}")  # Output: Lazy content: ['is', 'test', 'parentheses']
```

Both approaches use lazy matching, but the second one captures just the content inside parentheses.

### {n,}? - At Least n Times (Lazy)

The `{n,}?` quantifier lazily matches at least n occurrences of the preceding element.

1. **Minimal Matching of Repeated Characters**:

```python
import re

text = "aaaaa"

# Greedy approach
greedy_match = re.search(r'a{2,}', text)
print(f"Greedy: {greedy_match.group()}")  # Output: Greedy: aaaaa

# Lazy approach
lazy_match = re.search(r'a{2,}?', text)
print(f"Lazy: {lazy_match.group()}")      # Output: Lazy: aa
```

The lazy pattern `a{2,}?` matches only two 'a's, the minimum required.


2. **Finding Shortest Valid Sequences**:

```python
import re

text = "The passwords are: Pass123, Password123456, Pwd1"

# Greedy approach
greedy_matches = re.findall(r'\b[A-Za-z]{3,}\d{1,}\b', text)
print(f"Greedy: {greedy_matches}")  # Output: Greedy: ['Pass123', 'Password123456', 'Pwd1']

# Lazy approach
lazy_matches = re.findall(r'\b[A-Za-z]{3,}?\d{1,}?\b', text)
print(f"Lazy: {lazy_matches}")      # Output: Lazy: ['Pass123', 'Password123456', 'Pwd1']
```

In this case, both approaches yield the same results because the word boundaries constrain the matches, but the lazy quantifier would try to match as few letters and digits as possible while still satisfying the pattern.
3. **Extracting Code Blocks**:

```python
import re

code = """function start() {
    console.log("Hello");
}

function end() {
    return true;
}"""

# Greedy approach
greedy_matches = re.findall(r'function.*?{.*?}', code, re.DOTALL)
print(f"Greedy: {len(greedy_matches)}")  # Output: Greedy: 1

# Lazy approach with minimum lines
lazy_matches = re.findall(r'function.*?{.{1,}?}', code, re.DOTALL)
print(f"Lazy: {len(lazy_matches)}")      # Output: Lazy: 2
```

The lazy pattern ensures we match each function block separately by using `.{1,}?` to match the minimum content inside braces.

### {n,m}? - Between n and m Times (Lazy)

The `{n,m}?` quantifier lazily matches between n and m occurrences of the preceding element, preferring the minimum.

1. **Matching Shortest Acceptable Substrings**:

```python
import re

text = "aaaaa"

# Greedy approach
greedy_match = re.search(r'a{2,4}', text)
print(f"Greedy: {greedy_match.group()}")  # Output: Greedy: aaaa

# Lazy approach
lazy_match = re.search(r'a{2,4}?', text)
print(f"Lazy: {lazy_match.group()}")      # Output: Lazy: aa
```

The lazy pattern `a{2,4}?` matches only two 'a's, the minimum required in the range.
2. **Finding Variable-Length Codes**:

```python
import re

text = "Product codes: A1, AB12, ABC123, ABCD1234"

# Greedy approach
greedy_matches = re.findall(r'[A-Z]{1,4}\d{1,4}', text)
print(f"Greedy: {greedy_matches}")  # Output: Greedy: ['A1', 'AB12', 'ABC123', 'ABCD1234']

# Lazy approach
lazy_matches = re.findall(r'[A-Z]{1,4}?\d{1,4}?', text)
print(f"Lazy: {lazy_matches}")      # Output: Lazy: ['A1', 'AB12', 'ABC123', 'ABCD1234']
```

In this case, both approaches yield the same results because the pattern is constrained by the character classes, but the lazy quantifier would try to match as few characters as possible.
3. **Extracting Minimal XML Tags**:

```python
import re

xml = "&lt;tag attr='value'&gt;content&lt;/tag&gt;&lt;longertag&gt;more content&lt;/longertag&gt;"

# Greedy approach
greedy_matches = re.findall(r'&lt;(\w{1,10}).*?&gt;.*?&lt;/\1&gt;', xml)
print(f"Greedy: {greedy_matches}")  # Output: Greedy: ['tag', 'longertag']

# Lazy approach
lazy_matches = re.findall(r'&lt;(\w{1,10}?).*?&gt;.*?&lt;/\1&gt;', xml)
print(f"Lazy: {lazy_matches}")      # Output: Lazy: ['tag', 'longertag']
```

The lazy pattern `\w{1,10}?` would match the shortest possible tag name that allows the overall pattern to match.

## Key Differences Between Greedy and Lazy Quantifiers

1. **Matching Strategy**:

```python
import re

text = "<p>First paragraph</p><p>Second paragraph</p>"

# Greedy approach
greedy_match = re.search(r'<p>.*</p>', text)
print(f"Greedy: {greedy_match.group()}")  # Output: <p>First paragraph</p><p>Second paragraph</p>

# Lazy approach
lazy_match = re.search(r'<p>.*?</p>', text)
print(f"Lazy: {lazy_match.group()}")      # Output: <p>First paragraph</p>
```

Greedy quantifiers match as much as possible, while lazy quantifiers match as little as possible.
2. **Performance Considerations**:

```python
import re
import time

# Generate a long string with many potential matches
text = "a" * 1000 + "b" * 1000

# Greedy approach (potentially faster in this case)
start = time.time()
greedy_match = re.search(r'a+b', text)
greedy_time = time.time() - start

# Lazy approach (potentially slower in this case)
start = time.time()
lazy_match = re.search(r'a+?b', text)
lazy_time = time.time() - start

print(f"Greedy time: {greedy_time:.6f}s")
print(f"Lazy time: {lazy_time:.6f}s")
```

Lazy quantifiers can sometimes be less efficient because they may need to backtrack more frequently.
3. **Practical Usage**:

```python
import re

html = """<div>
    <h1>Title</h1>
    <p>First paragraph</p>
    <p>Second paragraph</p>
</div>"""

# Extract all paragraph content
paragraphs = re.findall(r'<p>(.*?)</p>', html)
print(paragraphs)  # Output: ['First paragraph', 'Second paragraph']

# Extract the entire content of the div
div_content = re.search(r'&lt;div.*?&gt;(.*?)', html, re.DOTALL)
print(div_content.group(1).strip())
```

Lazy quantifiers are particularly useful for parsing HTML and XML, where you want to match specific tags without capturing too much.

Understanding the difference between greedy and lazy quantifiers is crucial for effective pattern matching. Greedy quantifiers are the default and work well in many cases, but lazy quantifiers are essential when you need to match the smallest possible substring that satisfies your pattern.


# Lookahead and Lookbehind in Regular Expressions

Lookahead and lookbehind assertions are zero-width assertions in regular expressions that allow you to match a pattern only if it's followed by or preceded by another pattern, without including the latter in the match result.

## Positive Lookahead (?=...)

Positive lookahead asserts that what immediately follows the current position in the string is a match for the given pattern.

1. **Matching Words Followed by Specific Punctuation**:
```python
import re

text = "Hello, world! Hello? Hello."
matches = re.findall(r'\b\w+(?=[!?.])', text)
print(matches)  # Output: ['Hello', 'Hello', 'Hello']
```

This pattern matches words that are immediately followed by '!', '?', or '.', without including the punctuation in the match.

2. **Validating Password Strength**:
```python
import re

def is_strong_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&amp;])[A-Za-z\d@$!%*?&amp;]{8,}$'
    return bool(re.match(pattern, password))

print(is_strong_password("Weak123"))        # False
print(is_strong_password("Strong123!"))     # True
```

This pattern uses multiple positive lookaheads to ensure the password contains uppercase, lowercase, digit, and special characters.

3. **Finding Words Preceding Specific Words**:
```python
import re

text = "The quick brown fox jumps over the lazy dog"
matches = re.findall(r'\b\w+(?=\s+(?:fox|dog))', text)
print(matches)  # Output: ['brown', 'lazy']
```

This pattern matches words that are immediately followed by either "fox" or "dog".

## Negative Lookahead (?!...)

Negative lookahead asserts that what immediately follows the current position in the string is not a match for the given pattern.

1. **Matching Words Not Followed by Specific Punctuation**:
```python
import re

text = "Hello, world! Greetings. Hi there"
matches = re.findall(r'\b\w+\b(?![!?.])', text)
print(matches)  # Output: ['world', 'Hi', 'there']
```

This pattern matches words that are not immediately followed by '!', '?', or '.'.

2. **Finding Numbers Not Followed by Specific Units**:
```python
import re

text = "100km 200m 300cm 400mm 500"
matches = re.findall(r'\d+(?!\s*(?:km|m|cm|mm))', text)
print(matches)  # Output: ['500']
```

This pattern matches numbers that are not followed by units of length.

3. **Excluding Specific Words**:
```python
import re

text = "good dog, bad dog, good cat, bad cat"
matches = re.findall(r'\b(?!(?:bad|dog)\b)\w+', text)
print(matches)  # Output: ['good', 'good', 'cat', 'cat']
```

This pattern matches words that are neither "bad" nor "dog".

## Positive Lookbehind (?<=...)

Positive lookbehind asserts that what immediately precedes the current position in the string is a match for the given pattern.

1. **Matching Words Preceded by Specific Words**:
```python
import re

text = "The quick brown fox jumps over the lazy dog"
matches = re.findall(r'(?&lt;=(?:quick|lazy)\s)\w+', text)
print(matches)  # Output: ['brown', 'dog']
```

This pattern matches words that are immediately preceded by either "quick" or "lazy".

2. **Extracting Values After Specific Labels**:
```python
import re

text = "Name: John, Age: 30, City: New York"
matches = re.findall(r'(?&lt;=:\s)\w+(?:\s\w+)*', text)
print(matches)  # Output: ['John', '30', 'New York']
```

This pattern extracts values that come after labels followed by a colon and space.

3. **Finding Words After Punctuation**:
```python
import re

text = "Hello! How are you? I'm fine. Thanks."
matches = re.findall(r'(?&lt;=[.!?]\s)\w+', text)
print(matches)  # Output: ['How', "I'm", 'Thanks']
```

This pattern matches words that come immediately after sentence-ending punctuation and a space.

## Negative Lookbehind (?\w+ \w+), Age: (?P<age>\d+)", text)

if match:
print(match.groupdict())  \# Output: {'name': 'John Doe', 'age': '30'}

```

- `.groupdict()`: Get named groups as dictionary

Using lookahead and lookbehind assertions enables precise and flexible pattern matching based on context. Non-capturing groups help organize complex patterns, and capturing groups enable easy access to specific parts of the matched text.

# Performance Optimization in Regular Expressions

Regular expressions can be powerful but also computationally expensive if not optimized properly. Here are detailed strategies for optimizing regex performance with examples.

## Use Character Classes Instead of . When Possible

The dot (.) metacharacter matches any character except newlines, making it very broad and potentially inefficient.

1. **Replacing Dots with Specific Character Classes**:

```python
import re
import time

text = "The quick brown fox jumps over the lazy dog." * 10000

# Using dot (less efficient)
start = time.time()
matches_dot = re.findall(r'f.x', text)
dot_time = time.time() - start

# Using character class (more efficient)
start = time.time()
matches_class = re.findall(r'f[a-z]x', text)
class_time = time.time() - start

print(f"Dot time: {dot_time:.6f}s")
print(f"Character class time: {class_time:.6f}s")
print(f"Improvement: {(dot_time - class_time) / dot_time * 100:.2f}%")
```

Using a character class `[a-z]` instead of `.` narrows down the matching possibilities, making the regex engine work more efficiently.
2. **Optimizing Email Pattern**:

```python
import re

# Less efficient pattern
email_pattern_dot = r'\w+@.+\..+'

# More efficient pattern
email_pattern_optimized = r'\w+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

emails = ["user@example.com", "invalid@email", "test@sub.domain.co.uk"]

for email in emails:
    match_dot = re.match(email_pattern_dot, email)
    match_opt = re.match(email_pattern_optimized, email)
    print(f"{email}: Dot pattern: {'Match' if match_dot else 'No match'}, Optimized: {'Match' if match_opt else 'No match'}")
```

The optimized pattern is not only more precise but also more efficient because it restricts the character set at each position.
3. **Matching Numbers with Specific Format**:

```python
import re

# Less efficient pattern
pattern_dot = r'\d\d\d.\d\d\d.\d\d\d\d'

# More efficient pattern
pattern_optimized = r'\d{3}[-. ]\d{3}[-. ]\d{4}'

phone_numbers = ["123-456-7890", "123.456.7890", "123 456 7890", "123-456-789"]

for number in phone_numbers:
    match_dot = re.match(pattern_dot, number)
    match_opt = re.match(pattern_optimized, number)
    print(f"{number}: Dot pattern: {'Match' if match_dot else 'No match'}, Optimized: {'Match' if match_opt else 'No match'}")
```

The optimized pattern explicitly defines the separators, reducing the number of potential matches the engine needs to consider.

## Be Specific with Your Patterns to Avoid Excessive Backtracking

Backtracking occurs when the regex engine needs to try different paths to find a match, which can lead to exponential time complexity.

1. **Avoiding Nested Quantifiers**:

```python
import re
import time

# Create a string that causes catastrophic backtracking
text = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"

# Pattern with nested quantifiers (very inefficient)
bad_pattern = r'(a+)+b'

# More efficient pattern
good_pattern = r'a+b'

# Measure performance
try:
    start = time.time()
    match_bad = re.search(bad_pattern, text)
    bad_time = time.time() - start
    print(f"Bad pattern time: {bad_time:.6f}s")
except re.error:
    print("Bad pattern caused a timeout or error")

start = time.time()
match_good = re.search(good_pattern, text)
good_time = time.time() - start
print(f"Good pattern time: {good_time:.6f}s")
```

The pattern `(a+)+b` can cause catastrophic backtracking because it creates nested repetition, while `a+b` is straightforward and efficient.
2. **Using Atomic Groups or Possessive Quantifiers**:

```python
import re
import time

text = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"

# Standard greedy quantifier (can backtrack)
greedy_pattern = r'a+b'

# Possessive quantifier (no backtracking) - Python doesn't support this directly
# possessive_pattern = r'a++b'  # This would be in languages like Java

# Atomic group simulation in Python
atomic_pattern = r'(?&gt;(a+))b'  # This is not standard Python regex syntax

# Alternative approach: use a non-capturing group with a greedy quantifier
alternative_pattern = r'(?:a+)b'

start = time.time()
match_greedy = re.search(greedy_pattern, text)
greedy_time = time.time() - start

start = time.time()
match_alternative = re.search(alternative_pattern, text)
alternative_time = time.time() - start

print(f"Greedy pattern time: {greedy_time:.6f}s")
print(f"Alternative pattern time: {alternative_time:.6f}s")
```

While Python doesn't directly support possessive quantifiers or atomic groups, using non-capturing groups can sometimes help reduce backtracking.
3. **Using Anchors to Limit Search Space**:

```python
import re
import time

text = "This is a test string with some test words test test test."

# Without anchors (less efficient)
unanchored_pattern = r'test'

# With word boundary anchors (more efficient)
anchored_pattern = r'\btest\b'

# Measure performance
start = time.time()
matches_unanchored = re.findall(unanchored_pattern, text)
unanchored_time = time.time() - start

start = time.time()
matches_anchored = re.findall(anchored_pattern, text)
anchored_time = time.time() - start

print(f"Unanchored pattern time: {unanchored_time:.6f}s")
print(f"Anchored pattern time: {anchored_time:.6f}s")
print(f"Unanchored matches: {len(matches_unanchored)}")
print(f"Anchored matches: {len(matches_anchored)}")
```

Using word boundary anchors `\b` helps the regex engine quickly determine where to look for matches, reducing unnecessary work.

## Compile Patterns for Reuse with re.compile()

When using the same pattern multiple times, compiling it once can significantly improve performance.

1. **Basic Pattern Compilation**:

```python
import re
import time

text = "The quick brown fox jumps over the lazy dog." * 1000

# Without compilation
start = time.time()
for i in range(100):
    matches = re.findall(r'\b\w{4}\b', text)
uncompiled_time = time.time() - start

# With compilation
start = time.time()
pattern = re.compile(r'\b\w{4}\b')
for i in range(100):
    matches = pattern.findall(text)
compiled_time = time.time() - start

print(f"Uncompiled time: {uncompiled_time:.6f}s")
print(f"Compiled time: {compiled_time:.6f}s")
print(f"Improvement: {(uncompiled_time - compiled_time) / uncompiled_time * 100:.2f}%")
```

Compiling the pattern once avoids the overhead of parsing and compiling the pattern on each use.
2. **Compiling with Flags**:

```python
import re
import time

text = "HELLO world\nHello WORLD"

# Without compilation
start = time.time()
for i in range(10000):
    matches = re.findall(r'hello', text, re.IGNORECASE | re.MULTILINE)
uncompiled_time = time.time() - start

# With compilation
start = time.time()
pattern = re.compile(r'hello', re.IGNORECASE | re.MULTILINE)
for i in range(10000):
    matches = pattern.findall(text)
compiled_time = time.time() - start

print(f"Uncompiled time: {uncompiled_time:.6f}s")
print(f"Compiled time: {compiled_time:.6f}s")
print(f"Improvement: {(uncompiled_time - compiled_time) / uncompiled_time * 100:.2f}%")
```

Compiling with flags is especially beneficial when using multiple flags that would otherwise need to be processed each time.
3. **Reusing Patterns in Functions**:

```python
import re

# Inefficient approach: compiling in each function call
def validate_email_inefficient(email):
    pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    return bool(pattern.match(email))

# Efficient approach: compile once outside the function
EMAIL_PATTERN = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

def validate_email_efficient(email):
    return bool(EMAIL_PATTERN.match(email))

# Test with multiple emails
emails = ["user@example.com", "invalid@email", "test@domain.co.uk"] * 1000

import time

start = time.time()
for email in emails:
    validate_email_inefficient(email)
inefficient_time = time.time() - start

start = time.time()
for email in emails:
    validate_email_efficient(email)
efficient_time = time.time() - start

print(f"Inefficient time: {inefficient_time:.6f}s")
print(f"Efficient time: {efficient_time:.6f}s")
print(f"Improvement: {(inefficient_time - efficient_time) / inefficient_time * 100:.2f}%")
```

Compiling patterns outside of functions that are called repeatedly can provide significant performance benefits.

## Use Lazy Quantifiers When Appropriate for Better Performance

Lazy quantifiers match as little as possible, which can sometimes be more efficient than greedy quantifiers.

1. **Parsing HTML Tags**:

```python
import re
import time

html = "<div><p>First paragraph</p><p>Second paragraph</p><p>Third paragraph</p></div>" * 1000

# Greedy approach
start = time.time()
greedy_matches = re.findall(r'<p>.*</p>', html)
greedy_time = time.time() - start

# Lazy approach
start = time.time()
lazy_matches = re.findall(r'<p>.*?</p>', html)
lazy_time = time.time() - start

print(f"Greedy time: {greedy_time:.6f}s")
print(f"Lazy time: {lazy_time:.6f}s")
print(f"Greedy matches: {len(greedy_matches)}")
print(f"Lazy matches: {len(lazy_matches)}")
```

The lazy quantifier `.*?` can be more efficient when you want to match the smallest possible substring, especially in HTML parsing.
2. **Extracting Quoted Strings**:

```python
import re
import time

text = 'He said "hello" and then "goodbye" and "many" "other" "words"' * 1000

# Greedy approach (potentially problematic)
start = time.time()
greedy_matches = re.findall(r'".*"', text)
greedy_time = time.time() - start

# Lazy approach
start = time.time()
lazy_matches = re.findall(r'".*?"', text)
lazy_time = time.time() - start

print(f"Greedy time: {greedy_time:.6f}s")
print(f"Lazy time: {lazy_time:.6f}s")
print(f"Greedy matches: {len(greedy_matches)}")
print(f"Lazy matches: {len(lazy_matches)}")
```

The lazy quantifier is usually more efficient for extracting quoted strings because it stops at the first closing quote.
3. **When Greedy is Better**:

```python
import re
import time

# Create a string where greedy matching might be more efficient
text = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab" * 1000

# Greedy approach
start = time.time()
greedy_matches = re.findall(r'a*b', text)
greedy_time = time.time() - start

# Lazy approach
start = time.time()
lazy_matches = re.findall(r'a*?b', text)
lazy_time = time.time() - start

print(f"Greedy time: {greedy_time:.6f}s")
print(f"Lazy time: {lazy_time:.6f}s")
```

In some cases, greedy quantifiers can be more efficient, especially when the pattern is simple and the match is expected to consume most of the input.

## Fail Fast: Structure Patterns to Reject Non-Matches Quickly

Designing patterns to quickly identify non-matches can significantly improve performance.

1. **Using Anchors and Fixed Prefixes**:

```python
import re
import time

text = "There are 1000 lines in this text, but only a few start with 'START: '" + "\n".join([f"Line {i}" for i in range(1000)]) + "\nSTART: This is what we want"

# Less efficient pattern
start_time = time.time()
inefficient_matches = re.findall(r'.*START: .*', text)
inefficient_time = time.time() - start_time

# More efficient pattern
start_time = time.time()
efficient_matches = re.findall(r'^START: .*', text, re.MULTILINE)
efficient_time = time.time() - start_time

print(f"Inefficient time: {inefficient_time:.6f}s")
print(f"Efficient time: {efficient_time:.6f}s")
```

Using the `^` anchor allows the regex engine to quickly skip lines that don't start with "START: ".
2. **Checking Length Constraints First**:

```python
import re
import time

# Generate test data
words = ["short", "medium_word", "very_long_word_that_exceeds_limit"] * 10000
text = " ".join(words)

# Less efficient pattern
start_time = time.time()
inefficient_matches = re.findall(r'\b\w{5,10}\b', text)
inefficient_time = time.time() - start_time

# More efficient approach using Python's len() first
start_time = time.time()
efficient_matches = [word for word in text.split() if 5 &lt;= len(word) &lt;= 10 and re.match(r'^\w+$', word)]
efficient_time = time.time() - start_time

print(f"Inefficient time: {inefficient_time:.6f}s")
print(f"Efficient time: {efficient_time:.6f}s")
```

For some tasks, it can be more efficient to use Python's built-in functions to filter candidates before applying regex.
3. **Using Lookahead for Validation**:

```python
import re
import time

# Generate passwords
valid_passwords = ["Strong1!", "Secure2@", "Complex3#"] * 1000
invalid_passwords = ["weak", "nodigit!", "NOUPPER1", "nolower1"] * 1000
all_passwords = valid_passwords + invalid_passwords

# Less efficient pattern (checks the entire string)
inefficient_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&amp;*]).{8,}$'

# More efficient pattern (fails fast on length)
efficient_pattern = r'^.{8,}$(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&amp;*])'

start_time = time.time()
inefficient_valid = [p for p in all_passwords if re.match(inefficient_pattern, p)]
inefficient_time = time.time() - start_time

start_time = time.time()
# For demonstration - in practice, we'd use the regex directly
efficient_valid = [p for p in all_passwords if len(p) &gt;= 8 and re.search(r'[A-Z]', p) and re.search(r'[a-z]', p) and re.search(r'\d', p) and re.search(r'[!@#$%^&amp;*]', p)]
efficient_time = time.time() - start_time

print(f"Inefficient time: {inefficient_time:.6f}s")
print(f"Efficient time: {efficient_time:.6f}s")
```

Breaking down complex validation into simpler checks can be more efficient, especially when many inputs will fail validation.

## Profile Your Regex: Test Performance with Different Approaches

Measuring the performance of different regex patterns is crucial for optimization.

1. **Simple Timing Comparison**:

```python
   import re
   import time
   
   text = "The quick brown fox jumps over the lazy dog." * 10000
   
   patterns = [
       r'\b\w+\b',             # Match words
       r'\b[a-zA-Z]+\b',       # Match only alphabetic words
       r'\b[a-zA-Z]{3,}\b',    # Match alphabetic words with 3+ letters
   ]
   
   for i, pattern in enumerate(patterns):
       start_time = time.time()
       matches = re.findall(pattern, text)
       elapsed_time = time.time() - start_time
       print(f"Pattern {i+1}: {pattern}")
       print(f"  Time: {elapsed_time:.6f}s")
       print(f"  Matches: {len(matches)}")
       print()
```

2. **Comparing Compiled vs. Uncompiled Patterns**:

```python
import re
import time

text = "The quick brown fox jumps over the lazy dog." * 10000
pattern_string = r'\b\w+\b'

# Uncompiled
start_time = time.time()
matches_uncompiled = re.findall(pattern_string, text)
uncompiled_time = time.time() - start_time

# Compiled
compiled_pattern = re.compile(pattern_string)
start_time = time.time()
matches_compiled = compiled_pattern.findall(text)
compiled_time = time.time() - start_time

print(f"Uncompiled time: {uncompiled_time:.6f}s")
print(f"Compiled time: {compiled_time:.6f}s")
print(f"Improvement: {(uncompiled_time - compiled_time) / uncompiled_time * 100:.2f}%")
```

3. **Profiling with Different Input Sizes**:

```python
import re
import time
import matplotlib.pyplot as plt

pattern = re.compile(r'\b\w+\b')
base_text = "The quick brown fox jumps over the lazy dog. "

sizes = [1000, 2000, 5000, 10000, 20000, 50000]
times = []

for size in sizes:
    text = base_text * size
    start_time = time.time()
    matches = pattern.findall(text)
    elapsed_time = time.time() - start_time
    times.append(elapsed_time)
    print(f"Size: {size}, Time: {elapsed_time:.6f}s, Matches: {len(matches)}")

# If you have matplotlib installed, you can visualize the results
plt.figure(figsize=(10, 6))
plt.plot(sizes, times, marker='o')
plt.title('Regex Performance vs. Input Size')
plt.xlabel('Input Size (repetitions)')
plt.ylabel('Time (seconds)')
plt.grid(True)
plt.savefig('regex_performance.png')
plt.show()
```


By implementing these optimization strategies, you can significantly improve the performance of your regular expressions, especially when dealing with large inputs or complex patterns. Remember that the most efficient regex is often the simplest one that correctly solves your problem.

# Common Mistakes to Avoid

Regular expressions are powerful but can be tricky. Here are some common mistakes to avoid:

## Greedy Quantifier Pitfalls

1. **Matching HTML Tags Incorrectly**:

```python
import re

html = "<div><p>First paragraph</p><p>Second paragraph</p></div>"

# Incorrect approach (greedy)
greedy_match = re.search(r'<p>.*</p>', html)
print(f"Greedy match: {greedy_match.group()}")
# Output: <p>First paragraph</p><p>Second paragraph</p>

# Correct approach (lazy)
lazy_match = re.search(r'<p>.*?</p>', html)
print(f"Lazy match: {lazy_match.group()}")
# Output: <p>First paragraph</p>
```

The greedy quantifier `.*` matches as much as possible, capturing both paragraph tags, while the lazy quantifier `.*?` correctly matches each tag separately.

## Incorrect Anchor Usage

1. **Misplacing Start and End Anchors**:

```python
import re

text = "The quick brown fox"

# Incorrect pattern (anchors in wrong position)
incorrect_pattern = r'\bquick\b^.*$'
incorrect_match = re.search(incorrect_pattern, text)
print(f"Incorrect match: {incorrect_match}")
# Output: Incorrect match: None

# Correct pattern
correct_pattern = r'^.*\bquick\b.*$'
correct_match = re.search(correct_pattern, text)
print(f"Correct match: {correct_match.group()}")
# Output: Correct match: The quick brown fox
```

The `^` and `$` anchors must be at the beginning and end of the pattern, respectively.

## Forgetting to Escape Special Characters

1. **Literal Dots and Plus Signs**:

```python
import re

text = "1+2=3, 2+2=4, 3.14"

# Incorrect pattern (unescaped special characters)
incorrect_pattern = r'\d+\+\d+=\d+'
incorrect_matches = re.findall(incorrect_pattern, text)
print(f"Incorrect matches: {incorrect_matches}")
# This will fail because + is a special character

# Correct pattern (escaped special characters)
correct_pattern = r'\d+\+\d+=\d+'
correct_matches = re.findall(correct_pattern, text)
print(f"Correct matches: {correct_matches}")
# Output: Correct matches: ['1+2=3', '2+2=4']
```

Special characters like `.`, `+`, `*`, `?`, `^`, `$`, `|`, `(`, `)`, `[`, `]`, `{`, `}` must be escaped with a backslash when you want to match them literally.

## Unnecessary Backslashes

1. **Over-Escaping Normal Characters**:

```python
import re

text = "Hello, world!"

# Incorrect pattern (unnecessary escapes)
incorrect_pattern = r'H\e\l\l\o'
incorrect_match = re.search(incorrect_pattern, text)
print(f"Incorrect match: {incorrect_match}")
# This might not work as expected

# Correct pattern
correct_pattern = r'Hello'
correct_match = re.search(correct_pattern, text)
print(f"Correct match: {correct_match.group()}")
# Output: Correct match: Hello
```

Only escape characters that have special meaning in regex. Escaping normal characters can lead to unexpected behavior.

## Improper Grouping

1. **Missing or Misplaced Parentheses**:

```python
import re

text = "apple banana cherry"

# Incorrect pattern (misplaced parentheses)
incorrect_pattern = r'(apple|banana cherry)'
incorrect_matches = re.findall(incorrect_pattern, text)
print(f"Incorrect matches: {incorrect_matches}")
# Output: Incorrect matches: ['apple']

# Correct pattern
correct_pattern = r'(apple|banana|cherry)'
correct_matches = re.findall(correct_pattern, text)
print(f"Correct matches: {correct_matches}")
# Output: Correct matches: ['apple', 'banana', 'cherry']
```

Parentheses define groups and affect how alternation (`|`) works. Misplacing them can change the meaning of your pattern.

## Regex Abuse

1. **Using Regex for Simple String Operations**:

```python
import re
import time

text = "Hello, world!"

# Inefficient approach (regex)
start_time = time.time()
for _ in range(10000):
    has_hello_regex = bool(re.search(r'Hello', text))
regex_time = time.time() - start_time

# Efficient approach (string method)
start_time = time.time()
for _ in range(10000):
    has_hello_string = 'Hello' in text
string_time = time.time() - start_time

print(f"Regex time: {regex_time:.6f}s")
print(f"String time: {string_time:.6f}s")
print(f"Regex is {regex_time / string_time:.1f}x slower")
```

For simple string operations like checking if a substring exists, Python's built-in string methods are usually much faster than regex.

By avoiding these common mistakes, you can write more efficient, correct, and maintainable regular expressions.


...

## References:

https://www3.ntu.edu.sg/home/ehchua/programming/howto/Regexe.html
https://coderpad.io/blog/development/the-complete-guide-to-regular-expressions-regex/
https://developers.google.com/edu/python/regular-expressions
https://realpython.com/regex-python-part-2/
https://www.ibm.com/docs/en/informix-servers/12.10?topic=matching-metacharacters
https://www.regextutorial.org/regular-expression-metacharacters.php
https://learn.microsoft.com/en-us/dotnet/standard/base-types/character-classes-in-regular-expressions
https://learn.microsoft.com/en-us/dotnet/standard/base-types/anchors-in-regular-expressions
https://www.studyplan.dev/pro-cpp/regex-capture-groups/q/greedy-vs-lazy-quantifiers
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Lookahead_assertion
https://www.hackerrank.com/challenges/re-group-groups/problem
https://arjancodes.com/blog/regex-performance-optimization-and-security-best-practices/
https://buildregex.com/common-regex-mistakes-and-how-to-avoid-them/
https://en.wikipedia.org/wiki/Regular_expression
https://www.w3schools.com/python/python_regex.asp
https://www.liquidweb.com/blog/what-are-regular-expressions/
https://regexone.com
https://www.w3schools.com/java/java_regex.asp
https://www.kaggle.com/code/bhatnagardaksh/introduction-to-regular-expressions
https://learn.microsoft.com/en-us/dotnet/standard/base-types/regular-expression-language-quick-reference
https://www.freecodecamp.org/news/practical-regex-guide-with-real-life-examples/
https://d2h1bfu6zrdxog.cloudfront.net/wp-content/uploads/2022/04/img_625491e9ce092.png?sa=X\&ved=2ahUKEwjuyNiS37OMAxUjmq8BHU3hM70Q_B16BAgGEAI
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions
https://www.digitalocean.com/community/tutorials/an-introduction-to-regular-expressions
https://docs.python.org/3/library/re.html
https://docs.icewarp.com/Content/IceWarp-Server/Administration-Nodes/Domains/Accounts/Simple/RegEx/Tutorial.html
https://www.youtube.com/watch?v=rhzKDrUiJVk
https://www.wscubetech.com/resources/python/regular-expression
https://www.simplilearn.com/tutorials/python-tutorial/python-regular-expressions
https://www.youtube.com/watch?v=8GKaA1aqnBg
https://www.codecademy.com/resources/docs/python/regex/split
https://stackoverflow.com/questions/20448688/python-regular-expressions-re-findall-split-a-string-into-two
https://www.microfocus.com/documentation/net-express/nx51ws01/uoregx.htm
https://www.w3schools.com/python/gloss_python_regex_metacharacters.asp
https://www.youtube.com/watch?v=j6A28L6Tmxw
https://docs.python.org/3/howto/regex.html
https://www.ibm.com/docs/en/netcoolomnibus/8.1?topic=filters-pattern-matching-meta-characters
https://ds100.org/sp22/resources/assets/hw/regex_reference.pdf
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Character_classes
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class
https://stackoverflow.com/questions/6775383/can-i-define-custom-character-class-shorthands
https://docs.oracle.com/javase/tutorial/essential/regex/char_classes.html
https://simpleregex.dev/character-class/
https://javascript.info/regexp-character-classes
https://support.bettercloud.com/s/article/Creating-your-own-Custom-Regular-Expression-bc72153
https://stackoverflow.com/questions/66740811/regex-anchor-versus-b-for-word-boundary
https://www.regular-expressions.info/anchors.html
https://www.sonarsource.com/blog/setting-the-right-regex-boundaries-is-important/
https://stackoverflow.com/questions/6664151/difference-between-b-and-b-in-regex-word-boundary-assertion
https://www.regular-expressions.info/wordboundaries.html
https://www.youtube.com/watch?v=YTMJ4E5qVkM
https://www.ibm.com/docs/en/netcoolomnibus/8.1?topic=library-minimal-non-greedy-quantifiers
https://formulashq.com/lazy-match-regular-expressions-regex-explained/
https://unix.stackexchange.com/questions/71888/greedy-and-lazy-regular-expressions-comprehension-question
https://www.youtube.com/watch?v=2n4Cu61DDAM
https://javascript.info/regexp-greedy-and-lazy
https://www.rexegg.com/regex-quantifiers.php
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Quantifiers
https://www.jetbrains.com/help/objc/regular-expression-syntax-reference.html
https://www.youtube.com/watch?v=AjTy0DBK-18
https://www.rexegg.com/regex-lookarounds.php
https://javascript.info/regexp-lookahead-lookbehind
https://exploringjs.com/deep-js/ch_regexp-lookaround-assertions.html
https://stackoverflow.com/questions/6418985/capturing-group-in-regex
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Capturing_group
https://learn.saylor.org/mod/book/view.php?id=29235\&chapterid=4749
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Groups_and_backreferences
https://www.reddit.com/r/learnpython/comments/1g5kwwn/can_someone_explain_group_groups_and_groupdict_to/
https://stackoverflow.com/questions/432493/how-do-you-access-the-matched-groups-in-a-javascript-regular-expression
https://stackoverflow.com/questions/62689107/groupdict-in-regex
https://regexone.com/lesson/capturing_groups
https://www.pythontutorial.net/python-regex/python-regex-capturing-group/
https://blog.codinghorror.com/regex-performance/
https://www.youtube.com/watch?v=L5Vqm-REhAU
https://stackoverflow.com/questions/1252194/regex-performance-optimization-tips-and-tricks
https://library.humio.com/kb/kb-regex-vs-string-performance.html
https://www.syncfusion.com/succinctly-free-ebooks/regularexpressions/optimizing-your-regex
https://www.usna.edu/Users/cs/wcbrown/courses/F00SI472/resources/regexp/CommonMistakes.html
https://blog.codinghorror.com/regular-expressions-now-you-have-two-problems/
https://robinwinslow.uk/regex
https://www.linkedin.com/pulse/tips-tricks-mastering-regex-best-practices-pitfalls-avoid-soni
https://library.humio.com/kb/kb-avoiding-regex-pitfalls.html
https://stackoverflow.com/questions/998997/should-i-avoid-regular-expressions
https://softwareengineering.stackexchange.com/questions/113237/when-you-should-not-use-regular-expressions
https://bradt.ca/blog/stop-avoiding-regular-expressions-damn-it/
https://www.freecodecamp.org/news/how-to-import-a-regular-expression-in-python/
https://www.sitepoint.com/python-regex/
https://www.cybrosys.com/blog/python-regex-common-methods-in-the-python-re-module
https://www.programiz.com/python-programming/regex
https://www.ibm.com/docs/en/netcoolomnibus/8.1?topic=library-metacharacters
https://pynative.com/python-regex-metacharacters/
https://www.codecademy.com/resources/docs/python/regex/metacharacters
https://www.php.net/manual/en/regexp.reference.meta.php
https://www.tutorialsteacher.com/regex/metacharacters
https://www.lenovo.com/us/en/glossary/metacharacter/
https://www.iitk.ac.in/esc101/05Aug/tutorial/extra/regex/char_classes.html
https://pynative.com/python-regex-special-sequences-and-character-classes/
https://www.tutorialsteacher.com/regex/character-classes
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class_escape
https://www.regular-expressions.info/charclass.html
https://learnbyexample.github.io/py_regular_expressions/character-class.html
https://www.codeguage.com/courses/regexp/character-classes
https://formulashq.com/anchors-regular-expressions-regex-explained/
https://launchschool.com/books/regex/read/anchors
https://refrf.dev/en/chapters/anchors
https://www.rexegg.com/regex-boundaries.php
https://www.freecodecamp.org/news/regex-in-javascript/
https://www.rexegg.com/regex-anchors.php
https://www.regular-expressions.info/possessive.html
https://formulashq.com/quantifiers-regular-expressions-regex-explained/
https://docs.oracle.com/javase/tutorial/essential/regex/quant.html
https://learn.microsoft.com/en-us/dotnet/standard/base-types/quantifiers-in-regular-expressions
https://mtsknn.fi/blog/lazy-and-greedy-quantifiers-in-regex/
https://github.com/dotnet/docs/blob/main/docs/standard/base-types/quantifiers-in-regular-expressions.md
https://stackoverflow.com/questions/2301285/what-do-lazy-and-greedy-mean-in-the-context-of-regular-expressions
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Lookbehind_assertion
https://developers.redhat.com/articles/2022/10/13/advanced-regex-capture-groups-lookaheads-and-lookbehinds
https://www.regular-expressions.info/lookaround.html
https://ko.javascript.info/regexp-lookahead-lookbehind
https://www.regextutorial.org/positive-and-negative-lookahead-assertions.php
https://stackoverflow.com/questions/2973436/regex-lookahead-lookbehind-and-atomic-groups
https://tr.javascript.info/regexp-lookahead-lookbehind
https://learn.microsoft.com/en-us/dotnet/standard/base-types/grouping-constructs-in-regular-expressions
https://pynative.com/python-regex-capturing-groups/
https://python.pages.doc.ic.ac.uk/lessons/regex/07-groups/02-named.html
https://www.tutorialsteacher.com/regex/grouping
https://github.com/abrahamalbert18/HackerRank-Solutions-in-Python/blob/master/Regex/and/Parsing/Group,/Groups/and/GroupDict.py
https://formulashq.com/grouping-regular-expressions-regex-explained/
https://www.reddit.com/r/programming/comments/3c3vl0/five_invaluable_techniques_to_improve_regex/
https://www.loggly.com/blog/five-invaluable-techniques-to-improve-regex-performance/
https://tigerabrodi.blog/regex-performance-optimization-in-javascript
https://www.rexegg.com/regex-optimizations.php
https://learn.microsoft.com/en-us/dotnet/standard/base-types/best-practices-regex
https://stackoverflow.com/questions/36146129/error-in-regular-expression
https://jhall.io/posts/2022-03-05-regular-expressions/
https://www.ask.com/news/common-mistakes-avoid-regex-special-characters
https://www.sonarsource.com/blog/vulnerable-regular-expressions-javascript/
https://hackernoon.com/regexes-or-regular-expressions-and-the-common-mistakes-programmers-make-while-using-them-zh4p33it
https://www.loggly.com/blog/regexes-the-bad-better-best/
https://www3.ntu.edu.sg/home/ehchua/programming/howto/Regexe.html
https://www.tutorialsteacher.com/regex/character-classes
https://www.w3schools.com/python/gloss_python_regex_metacharacters.asp
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Character_classes
https://www.codecademy.com/resources/docs/python/regex/metacharacters
https://learn.microsoft.com/en-us/dotnet/standard/base-types/character-classes-in-regular-expressions
https://www.tutorialsteacher.com/regex/metacharacters
https://howtodoinjava.com/java/regex/regular-expressions-meta-characters/
https://formulashq.com/escaped-characters-regular-expressions-regex-explained/
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/escape
https://formulashq.com/metacharacters-regular-expressions-regex-explained/
https://pynative.com/python-regex-metacharacters/
https://www.freecodecamp.org/news/what-does-the-caret-mean-in-regex-how-to-match-the-start-of-a-line-in-regular-expressions/
https://www.lenovo.com/us/en/glossary/metacharacter/
https://www.tutorialspoint.com/regular-expression-dollar-metacharacter-in-java
https://www.freecodecamp.org/news/what-does-mean-in-regex/
https://airsdk.dev/docs/development/core-actionscript-classes/using-regular-expressions/regular-expression-syntax/characters-metacharacters-and-metasequences
https://www.freecodecamp.org/news/how-do-i-make-regex-optional-specify-optional-pattern-in-regular-expressions/
http://damiantgordon.com/RegExThursday/Page22.pdf
https://alvin.codes/snippets/regex-curly-brackets-two-whitespace
https://docs.oracle.com/cd/E35636_01/doc.11116/e29134/app_regexp.htm
https://www.lenovo.com/ca/en/glossary/metacharacter/
https://www.youtube.com/watch?v=MwzIRleH47o
https://stackoverflow.com/questions/14755608/need-a-regex-that-matches-only-a-single-instance-of-the-pipe-character
https://www.youtube.com/watch?v=4EpTntKTlKY
https://www.ibm.com/docs/en/netcoolomnibus/8.1?topic=filters-pattern-matching-meta-characters
https://statmath.wu.ac.at/courses/data-analysis/itdtHTML/node97.html
https://www.stat.auckland.ac.nz/~paul/ItDT/HTML/node84.html
https://docs.oracle.com/javase/tutorial/essential/regex/char_classes.html
https://www.regular-expressions.info/charclass.html
https://www.ibm.com/docs/en/informix-servers/12.10?topic=matching-metacharacters
https://www.iitk.ac.in/esc101/05Aug/tutorial/extra/regex/char_classes.html
https://www.freecodecamp.org/news/what-does-d-mean-in-regex/
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class
https://www.microfocus.com/documentation/net-express/nx51ws01/uoregx.htm
https://javascript.info/regexp-character-classes
https://www.codeguage.com/courses/regexp/character-classes
https://stackoverflow.com/questions/6525556/regular-expression-to-match-escaped-characters-quotes
https://www.threesl.com/blog/special-characters-regular-expressions-escape/
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape
https://learn.microsoft.com/en-us/dotnet/standard/base-types/character-escapes-in-regular-expressions
https://blog.robertelder.org/regular-expression-character-escaping/
https://www.jmp.com/support/help/en/18.1/jmp/escaped-characters-in-regular-expressions.shtml
https://help.ivanti.com/ps/help/en_US/VTM/22.x/tsg/ps-vtm-tscript/escaping_regular_express.htm
https://stackoverflow.com/questions/3674930/java-regex-meta-character-and-ordinary-dot
https://www.regular-expressions.info/dot.html
https://learnbyexample.github.io/learn_js_regexp/dot-metacharacter-and-quantifiers.html
https://www.w3schools.com/jsref/jsref_regexp_dot.asp
https://regexone.com/lesson/wildcards_dot
https://www.tutorialspoint.com/regular-expression-dot-metacharacter-in-java
https://docs.logicaldoc.com/en/document-metadata/barcodes/regular-expressions
https://stackoverflow.com/questions/16944357/carets-in-regular-expressions
https://www.tutorialspoint.com/regular-expression-caret-metacharacter-in-java
https://www.codechef.com/learn/course/advanced-python/CPOPPY22/problems/ADVPPY186
https://stackoverflow.com/questions/3853726/java-regular-expressions-and-dollar-sign
https://www.hscripts.com/tutorials/regular-expression/metacharacters/dollar.php
https://docs.snowflake.com/en/sql-reference/functions-regexp
https://www.linkedin.com/posts/free-code-camp_what-does-mean-in-regex-activity-7054832140923846656-Tx1f
https://www.stat.berkeley.edu/~nolan/stat133/Fall05/lectures/RegExExamples.html
https://stackoverflow.com/questions/22239317/asterisk-in-regex
https://superuser.com/questions/1858625/highlight-characters-between-asterisk-using-regular-expression
https://unix.stackexchange.com/questions/242991/bash-regex-asterisk-metacharacter-kills-redundant-newline-characters
https://www.microfocus.com/documentation/reuze/60d/uoregx.htm
https://askubuntu.com/questions/681637/grep-the-asterisk-doesnt-always-work
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions
https://stackoverflow.com/questions/53927817/is-plus-part-of-basic-regular-expressions
https://stackoverflow.com/questions/5583579/question-marks-in-regular-expressions
https://regexone.com/lesson/optional_characters
https://docs.moodle.org/en/Regular_Expression_Short-Answer_question_type
https://docs.python.org/3/howto/regex.html
https://stackoverflow.com/questions/413071/regex-to-get-string-between-curly-braces
https://salesforce.stackexchange.com/questions/198652/regex-including-curly-brackets
https://docs.umbrella.com/cloudlock-documentation/docs/write-regular-expressions
https://www.ibm.com/docs/en/netcoolomnibus/8.1?topic=library-metacharacters
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Cheatsheet
https://www.regular-expressions.info/alternation.html
https://www.optimizesmart.com/regular-expression-guide-for-seos/
https://blog.devgenius.io/regex-parentheses-examples-of-every-type-aba8441be761
https://stackoverflow.com/questions/24135006/regex-that-match-any-character-inside-a-parenthesis
https://forum.bubble.io/t/regex-expression-to-include-parentheses/221425
https://www.tutorialsteacher.com/regex/character-classes
https://pynative.com/python-regex-special-sequences-and-character-classes/
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class
https://www3.ntu.edu.sg/home/ehchua/programming/howto/Regexe.html
https://docs.python.org/3/howto/regex.html
https://en.wikipedia.org/wiki/Regular_expression
https://learn.microsoft.com/en-us/dotnet/standard/base-types/character-classes-in-regular-expressions
https://www.w3schools.com/python/python_regex.asp
https://formulashq.com/escaped-characters-regular-expressions-regex-explained/
https://www.scaler.com/topics/escape-string-python/
https://stackoverflow.com/questions/3115150/how-to-escape-regular-expression-special-characters-using-javascript
https://www.tutorialspoint.com/How-to-escape-any-special-character-in-Python-regular-expression
https://blog.robertelder.org/regular-expression-character-escaping/
https://learn.microsoft.com/en-us/dotnet/api/system.text.regularexpressions.regex.escape?view=net-9.0
https://howtodoinjava.com/java/regex/match-any-set-of-characters/
https://www.squash.io/how-to-use-regex-to-match-any-character-in-python/
https://stackoverflow.com/questions/38982637/regex-to-match-any-character-or-none
https://javascript.info/regexp-anchors
https://www.tutorialspoint.com/How-to-match-at-the-beginning-of-string-in-python-using-Regular-Expression
https://stackoverflow.com/questions/5516119/regular-expression-to-match-characters-at-beginning-of-line-only
https://howtodoinjava.com/java/regex/start-end-of-string/
https://www.jobsity.com/blog/how-to-use-regular-expressions-in-python
https://www.mpi.nl/corpus/html/trova/ch01s04.html
https://www.tutorialspoint.com/How-to-match-at-the-end-of-string-in-python-using-Regular-Expression
https://www.freecodecamp.org/news/what-does-mean-in-regex/
https://stackoverflow.com/questions/12187799/regular-expression-in-python-wont-match-end-of-a-string
https://news.ycombinator.com/item?id=39763750
https://www.tutorialspoint.com/How-can-I-match-the-start-and-end-in-Python-s-regex
https://learn.microsoft.com/en-us/dotnet/standard/base-types/quantifiers-in-regular-expressions
https://web.mit.edu/gnu/doc/html/regex_3.html
https://javascript.info/regexp-quantifiers
https://stackoverflow.com/questions/47322372/understanding-zero-or-more-operator-using-re-search
https://chortle.ccsu.edu/finiteautomata/Section07/sect07_19.html
https://community.splunk.com/t5/Splunk-Search/REGEX-meaning/m-p/208605
https://stackoverflow.com/questions/56280652/check-the-occurrence-of-zero-or-one-substring
https://chortle.ccsu.edu/finiteautomata/Section07/sect07_14.html
https://realpython.com/regex-python/
https://upskilld.com/learn/matching-a-certain-number-of-repetitions-with-regex/
https://www.freecodecamp.org/news/practical-regex-guide-with-real-life-examples/
https://www.ocpsoft.org/tutorials/regular-expressions/or-in-regex/
https://stackoverflow.com/questions/8020848/how-is-the-and-or-operator-represented-as-in-regular-expressions
https://pynative.com/python-regex-capturing-groups/
https://www.codeguage.com/courses/regexp/grouping
https://formulashq.com/grouping-regular-expressions-regex-explained/
https://sparkbyexamples.com/python/python-regex-groups/
https://www.tutorialsteacher.com/regex/grouping
https://learn.microsoft.com/en-us/dotnet/standard/base-types/grouping-constructs-in-regular-expressions
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Groups_and_backreferences
https://stackoverflow.com/questions/6479423/does-d-in-regex-mean-a-digit
https://unix.stackexchange.com/questions/414226/difference-between-0-9-digit-and-d
https://www.freecodecamp.org/news/what-does-d-mean-in-regex/
https://www.regextutorial.org/regex-for-numbers-and-ranges.php
https://www.rexegg.com/regex-class-operations.php
https://docs.oracle.com/javase/tutorial/essential/regex/char_classes.html
https://www.w3schools.com/python/gloss_python_regex_metacharacters.asp
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Character_classes
https://docs.python.org/3/library/re.html
https://www.regular-expressions.info/charclass.html
https://stackoverflow.com/questions/58153219/how-to-get-a-complete-list-of-character-class-of-python-regex-to-lookup-a-specif
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Cheatsheet
https://learnbyexample.github.io/py_regular_expressions/character-class.html
https://support.google.com/a/answer/1371417
https://developers.google.com/edu/python/regular-expressions
https://www.w3schools.com/java/java_regex.asp
https://stackoverflow.com/questions/7177771/what-is-the-purpose-of-regex-escape
https://stackoverflow.com/questions/280435/escaping-regex-string
https://learn.microsoft.com/en-us/dotnet/standard/base-types/character-escapes-in-regular-expressions
https://hyperskill.org/learn/step/9754
https://www.threesl.com/blog/special-characters-regular-expressions-escape/
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape
https://www.youtube.com/watch?v=F6LY3qo3J9c
https://esdiscuss.org/topic/regexp-escape
https://javascript.info/regexp-escaping
https://www.intel.com/content/www/us/en/programmable/quartushelp/17.0/reference/glossary/def_reg_express.htm
https://stackoverflow.com/questions/2912894/how-to-match-any-character-in-regular-expression
https://www.keycdn.com/support/regex-cheat-sheet
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions
https://coderpad.io/blog/development/the-complete-guide-to-regular-expressions-regex/
https://learn.microsoft.com/en-us/dotnet/standard/base-types/regular-expression-language-quick-reference
https://www.geekster.in/articles/regex-in-python/
https://www.regular-expressions.info/anchors.html
https://www.programiz.com/python-programming/regex
https://stackoverflow.com/questions/31400362/using-to-match-beginning-of-line-in-python-regex
https://stackoverflow.com/questions/12083308/in-regex-match-either-the-end-of-the-string-or-a-specific-character
https://stackoverflow.com/questions/6494915/regex-pattern-to-match-the-end-of-a-string
https://cran.r-project.org/web/packages/stringr/vignettes/regular-expressions.html
https://askubuntu.com/questions/822779/difference-between-and-in-regular-expressions
https://stackoverflow.com/questions/4304360/regular-expression-zero-or-more-occurrences-of-optional-character
https://users.cs.cf.ac.uk/Dave.Marshall/Internet/NEWS/regexp.html
https://forum.freecodecamp.org/t/solved-regex-lesson-help-zero-or-more-times-and-lazy-matching/201880
https://stackoverflow.com/questions/23112584/python-regular-expression-zero-or-more-occurences/23112631
https://mimo.org/glossary/python/regex-regular-expressions
https://stackoverflow.com/questions/23091427/regex-for-one-or-more-letters-digits-and-zero-or-more-spaces
https://regexone.com
https://stackoverflow.com/questions/37830849/python-regex-one-or-more-occurrences-of-a-string
http://www.w3schools.com/jS/js_regexp.asp
https://www.jetbrains.com/help/objc/regular-expression-syntax-reference.html
https://stackoverflow.com/questions/5797178/regex-match-zero-or-one-time-a-string
https://stackoverflow.com/a/48166847
https://stackoverflow.com/questions/33777047/regex-to-match-exactly-n-occurrences-of-letters-and-m-occurrences-of-digits
https://learn.microsoft.com/en-us/dotnet/api/system.text.regularexpressions.regex.count?view=net-9.0
https://stackoverflow.com/questions/43507957/python-regex-how-to-match-a-string-for-n-times-of-occurrences
https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap09.html
https://www.wscubetech.com/resources/python/regular-expression
https://stackoverflow.com/questions/1649435/regular-expression-to-limit-number-of-characters-to-10
https://www.tutorialspoint.com/how-to-match-n-number-of-occurrences-of-an-expression-using-java-regex
https://forum.uipath.com/t/regex-expression-meaning/631651
https://stackoverflow.com/questions/8609597/python-regular-expressions-or
https://www.youtube.com/watch?v=Jd3YyiJj8aM
https://spacelift.io/blog/terraform-regex
https://cs.lmu.edu/~ray/notes/regex/
https://docs.oracle.com/javase/tutorial/essential/regex/groups.html
https://stackoverflow.com/questions/48719537/capture-groups-with-regular-expression-python
https://www.youtube.com/watch?v=vYOeAt83C7o
https://regexone.com/lesson/capturing_groups
https://www.youtube.com/watch?v=NrzFle7RD0g
https://labex.io/tutorials/python-how-to-use-regex-capture-groups-in-python-420906
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Capturing_group
http://www.w3schools.com/Jsref/jsref_regexp_digit_non.asp
https://docs.pexip.com/admin/regex_reference.htm
http://automatetheboringstuff.com/chapter7/
https://www.codingforentrepreneurs.com/blog/python-regular-expressions
https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/55535344/4c98fd54-8a82-497a-b13d-c1d871114dec/paste.txt

...