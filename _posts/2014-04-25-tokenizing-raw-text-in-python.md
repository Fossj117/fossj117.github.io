---
layout: post
title: Tokenizing Raw Text in Python
date: 2014-04-25 23:24:28
comments: true
tag: ["coding"]
---

Tokenizing raw text data is an important pre-processing step for many NLP methods. As explained [on wikipedia](http://en.wikipedia.org/wiki/Tokenization), tokenization is "the process of breaking a stream of text up into words, phrases, symbols, or other meaningful elements called tokens." In the context of actually working through an NLP analysis, this usually translates to converting a string like `"My favorite color is blue"` to a list or array like `["My", "favorite", "color", "is", "blue"]`.

In Python, there are a number of methods for quickly tokenizing text. The most naive method for doing this is to simply the `split()` function associated with Python strings. For example:

```python
>>> mystring = "My favorite color is blue"
>>> mystring.split()
['My', 'favorite', 'color', 'is', 'blue']
```

By default, `split()` simply splits the string into a list by whitespace characters, (although you can also pass it a string of characters to split on, making the behavior slightly more subtle). This works well for simple cases, but behaves sub-optimally (from an NLP perspective) when the target text contains punctuation. For example:

```python
>>> mystring = "My favorite colors are blue, red, and green."
>>> mystring.split()
['My', 'favorite', 'colors', 'are', 'blue,', 'red,', 'and', 'green.']
```

Note that the punctuation marks are grouped in with their adjacent word (e.g. `blue,`). This is problematic for NLP applications, as the goal of tokenization is generally to divide a set (corpus) of documents into a common set of building blocks that can then be used as a basis for comparison. Hence, it's no good if "blue" in `"My favorite color is blue"` doesn't match with "blue" in `"My favorite colors are blue, red, and green."` since the latter is tokenized as `blue,` rather than `blue`.

Fortunately, the awesome Python package [Natural Language Toolkit](http://www.nltk.org/) ships with a number of useful utilities for more intelligently tokenizing raw text. For example, NLTK's `word_tokenize` solves the problem just mentioned:

```python
>>> import nltk
>>> mystring = "My favorite color is blue"
>>> mystring2 = "My favorite colors are blue, red, and green."
>>> nltk.word_tokenize(mystring)
['My', 'favorite', 'color', 'is', 'blue']
>>> nltk.word_tokenize(mystring2)
['My', 'favorite', 'colors', 'are', 'blue', ',', 'red', ',', 'and', 'green', '.']
```

When dealing with well-formed, formal text, this standard word tokenizer makes a lot of sense and is likely to be sufficient. However, the same cannot be said for cases when our text data comes from more casual, slang-ridden sources like Twitter. For example, consider a prototypical tweet:

```pythong
"@john lol that was #awesome :)"
```

And now see what happens when we use the NLTK `word_tokenize()` method:

```python
>>> mytweet = "@john lol that was #awesome :)"
>>> nltk.word_tokenize(mytweet)
['@', 'john', 'lol', 'that', 'was', '#', 'awesome', ':', ')']
```

Although this behavior might be desirable in some cases, it's most likely that we'd prefer for `@` and `john` to be tokenized together as `@john`, and `#` and `awesome` to be tokenized together as `#awesome`. This is because we'd expect that word usage in the context of hastags or at-mentions is likely different from usage in plain text. Moreover, we would prefer that `:` and `)` to be tokenized together as `:)`, as `:)` is certainly more informative (e.g. for sentiment analysis) than the sum of its parts.

To overcome these problems, we can make use of regular expressions to design our own (arbitrarily-specified) tokenizer. Though we could use Python's built-in `re.findall()` for this purpose, it turns out that NLTK's `regexp_tokenize` function is more efficient for these purposes. The following regex is what I have found to be most effective for tokenizing Twitter data. It solves the problems mentioned above, as well as several others. The pattern has been split across several lines for clarity (although I seem to be having formatting difficulties):

```python
pattern = r'''(?x)    #verbose regex flag
         ([A-Z]\.)+	 #abbreviations
        |\d+:\d		#times, e.g. 5:23
        |(https?://)?(\w+\.)(\w{2,})+([\w/]+) #URLs
        |[@\#]?\w+(?:[-']\w+)*	#word,@user, words
        |\$\d+(\.\d+)?%? #currency, pcts
        |\.\.\.		#ellipses
        |[!?]+		#!!!, ???
    	'''
```

Although this might look complicated (especially if you're not familiar with regex), it's really not that bad. Essentially, each line of the expression specifies another textual pattern that we want to match as a token (e.g. `\d+:\d+` is included to capture time tokens like "2:34" or "12:15"). The `|` separators simply say that a valid token can match any of these pattterns. As such, this pattern can extended to match more (or less) token patterns.

It's worth noting that, as is, this method will get rid of most punctuation (e.g. `,`, `.` will not be counted as tokens), although strings of `!` and/or `?` will be retained, as will `...`). Here it is in action, tokenizing our earlier example:

```python
>>> pattern = r'''(?x)
...          ([A-Z]\.)+
...         |\d+:\d+
...         |(https?://)?(\w+\.)(\w{2,})+([\w/]+)?
...         |[@\#]?\w+(?:[-']\w+)*
...         |\$\d+(\.\d+)?%?
...         |\\[Uu]\w+
...         |\.\.\.
...         |[!?]+
...     '''
>>> nltk.regexp_tokenize(mytweet, pattern)
['@john', 'lol', 'that', 'was', '#awesome']
```

For more on tokenizing text and NLTK/NLP in Python more generally, I would highly recommmend [Natural Language Processing with Python](http://www.nltk.org/book) which is available in full online for free ([chapter 3](<(http://www.nltk.org/book/ch03.html)>) has a good discussion of tokenization in Python). For a good intro to regular expressions, you can look at [Learn Regex the Hard Way](http://regex.learncodethehardway.org/book/)
