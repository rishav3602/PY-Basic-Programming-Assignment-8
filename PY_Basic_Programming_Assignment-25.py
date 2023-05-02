"""
Question1
Create a function that takes three integer arguments (a, b, c) and returns the amount of
integers which are of equal value.
Examples
equal(3, 4, 3) ➞ 2
equal(1, 1, 1) ➞ 3
equal(3, 4, 1) ➞ 0
Notes
Your function must return 0, 2 or 3.
"""

def equal(a, b, c):
    if a == b == c:
        return 3
    elif a == b or b == c or c == a:
        return 2
    else:
        return 0


"""
Question2
Write a function that converts a dictionary into a list of keys-values tuples.
Examples
dict_to_list({
&quot;D&quot;: 1,
&quot;B&quot;: 2,
&quot;C&quot;: 3
}) ➞ [(&quot;B&quot;, 2), (&quot;C&quot;, 3), (&quot;D&quot;, 1)]
dict_to_list({
&quot;likes&quot;: 2,
&quot;dislikes&quot;: 3,
&quot;followers&quot;: 10
}) ➞ [(&quot;dislikes&quot;, 3), (&quot;followers&quot;, 10), (&quot;likes&quot;, 2)]
Notes
Return the elements in the list in alphabetical order.
"""

def dict_to_list(dct):
    return sorted(list(dct.items()))


"""
Question3
Write a function that creates a dictionary with each (key, value) pair being the (lower case,
upper case) versions of a letter, respectively.
Examples
mapping([&quot;p&quot;, &quot;s&quot;]) ➞ { &quot;p&quot;: &quot;P&quot;, &quot;s&quot;: &quot;S&quot; }

mapping([&quot;a&quot;, &quot;b&quot;, &quot;c&quot;]) ➞ { &quot;a&quot;: &quot;A&quot;, &quot;b&quot;: &quot;B&quot;, &quot;c&quot;: &quot;C&quot; }
mapping([&quot;a&quot;, &quot;v&quot;, &quot;y&quot;, &quot;z&quot;]) ➞ { &quot;a&quot;: &quot;A&quot;, &quot;v&quot;: &quot;V&quot;, &quot;y&quot;: &quot;Y&quot;, &quot;z&quot;: &quot;Z&quot; }
Notes
All of the letters in the input list will always be lowercase.
"""

def mapping(letters):
    return {l: l.upper() for l in letters}


"""
Question4
Write a function, that replaces all vowels in a string with a specified vowel.
Examples
vow_replace(&quot;apples and bananas&quot;, &quot;u&quot;) ➞ &quot;upplus und bununus&quot;
vow_replace(&quot;cheese casserole&quot;, &quot;o&quot;) ➞ &quot;chooso cossorolo&quot;
vow_replace(&quot;stuffed jalapeno poppers&quot;, &quot;e&quot;) ➞ &quot;steffed jelepene peppers&quot;
Notes
All words will be lowercase. Y is not considered a vowel.
"""

def vow_replace(word, vowel):
    vowels = "aeiouAEIOU"
    for v in vowels:
        word = word.replace(v, vowel)
    return word


"""
Question5
Create a function that takes a string as input and capitalizes a letter if its ASCII code is even
and returns its lower case version if its ASCII code is odd.
Examples
ascii_capitalize(&quot;to be or not to be!&quot;) ➞ &quot;To Be oR NoT To Be!&quot;
ascii_capitalize(&quot;THE LITTLE MERMAID&quot;) ➞ &quot;THe LiTTLe meRmaiD&quot;
ascii_capitalize(&quot;Oh what a beautiful morning.&quot;) ➞ &quot;oH wHaT a BeauTiFuL
moRNiNg.&quot;
"""

def ascii_capitalize(string):
    result = ""
    for c in string:
        if ord(c) % 2 == 0:
            result += c.upper()
        else:
            result += c.lower()
    return result
