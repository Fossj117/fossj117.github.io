---
layout: post
title: "Mapping Colors & Emotions with LLMs"
date: 2024-01-27
latex: true
mathjax: true
comments: true
tag: ["llm"]
---

Today, I am continuing [my experiments from yesterday](https://jeffreyfossett.com/2024/01/26/notes-on-homo-silicus.html) in goofing around with LLMs via the `edsl` pacakage. Today, my vision is as follows: 

1. Have ChatGPT generate a list of emotions. 
2. Using `edsl`, map all the motions to colors in RGB color space. 
3. Visualize the results

This should be fairly straightforward, so let's do it. First, here is a list of emotions from chatGPT: 

{% highlight python %}
emotions = [
    "Happiness",
    "Sadness",
    "Anger",
    "Fear",
    "Disgust",
    "Surprise",
    "Love",
    "Joy",
    "Anxiety",
    "Excitement",
    "Jealousy",
    "Gratitude",
    "Contentment",
    "Hope",
    "Pride",
    "Shame",
    "Guilt",
    "Envy",
    "Frustration",
    "Curiosity",
    "Amusement",
    "Boredom",
    "Loneliness",
    "Empathy",
    "Sympathy",
    "Anticipation",
    "Disappointment",
    "Relief",
    "Nostalgia",
    "Awe",
    "Eagerness",
    "Confidence",
    "Insecurity",
    "Embarrassment",
    "Indifference",
    "Confusion",
    "Admiration",
    "Compassion",
    "Resentment",
    "Calmness",
    "Apprehension",
    "Sorrow",
    "Contempt",
    "Irritation",
    "Melancholy",
    "Bliss",
    "Regret",
    "Satisfaction",
    "Yearning",
    "Serenity"
]
{% endhighlight %}

Next, I will use `edsl` as I did previously. In this case, I will give each agent an emotional state via the `persona` specification that `edsl` supports.

{% highlight python %}
from edsl.agents import Agent
from edsl.questions import QuestionFreeText

emotion_string = "You are currently experiencing the emotion {emotion}"

agents = [Agent(traits = {'persona':emotion_string.format(emotion=e.lower())}) for e in emotions]

q = QuestionFreeText(
    question_name = "favorite_color",
    question_text = "What is the color that best represents how you are feeling right now? Respond with only an RGB code in the form (R,G,B) where each value is between 0 and 255."
)

result = q.by(agents).run()
{% endhighlight %}

Now I extract all the emotions and colors into a set of tuples: 

{% highlight python %}
import ast 
tups = list(zip([e.lower() for e in emotions], [ast.literal_eval(r.answer['favorite_color']) for r in result]))
{% endhighlight %}

Great, so now we have a list of emotions and colors. First, let's look at the raw results. Using chatgpt I write a function to convert my list of tuples into a table: 

{% highlight python %}
def generate_html_table(emotion_colors):
    # Starting the HTML for the table
    html = "<table border='1'>"

    # Adding headers
    html += "<tr><th>Emotion</th><th>RGB Value</th><th>Color</th></tr>"

    # Iterating over the list of tuples to fill the rows
    for emotion, color in emotion_colors:
        # Format the RGB color as a string
        color_rgb_string = f"({color[0]}, {color[1]}, {color[2]})"
        # Format the RGB color for HTML styling
        color_rgb_html = f"rgb{color}"
        # Adding a row with the emotion, the RGB string, and a colored cell
        html += f"<tr><td>{emotion}</td><td>{color_rgb_string}</td><td style='background-color: {color_rgb_html};'></td></tr>"

    # Closing the table tag
    html += "</table>"

    return html
{% endhighlight %}

Here is the table that results: 

<html><table border='1'><tr><th>Emotion</th><th>RGB Value</th><th>Color</th></tr><tr><td>happiness</td><td>(255, 255, 0)</td><td style='background-color: rgb(255, 255, 0);'></td></tr><tr><td>sadness</td><td>(0, 0, 255)</td><td style='background-color: rgb(0, 0, 255);'></td></tr><tr><td>anger</td><td>(255, 0, 0)</td><td style='background-color: rgb(255, 0, 0);'></td></tr><tr><td>fear</td><td>(0, 0, 0)</td><td style='background-color: rgb(0, 0, 0);'></td></tr><tr><td>disgust</td><td>(128, 0, 0)</td><td style='background-color: rgb(128, 0, 0);'></td></tr><tr><td>surprise</td><td>(255, 215, 0)</td><td style='background-color: rgb(255, 215, 0);'></td></tr><tr><td>love</td><td>(255, 0, 0)</td><td style='background-color: rgb(255, 0, 0);'></td></tr><tr><td>joy</td><td>(255, 255, 0)</td><td style='background-color: rgb(255, 255, 0);'></td></tr><tr><td>anxiety</td><td>(255, 165, 0)</td><td style='background-color: rgb(255, 165, 0);'></td></tr><tr><td>excitement</td><td>(255, 165, 0)</td><td style='background-color: rgb(255, 165, 0);'></td></tr><tr><td>jealousy</td><td>(255, 0, 0)</td><td style='background-color: rgb(255, 0, 0);'></td></tr><tr><td>gratitude</td><td>(173, 216, 230)</td><td style='background-color: rgb(173, 216, 230);'></td></tr><tr><td>contentment</td><td>(0, 128, 0)</td><td style='background-color: rgb(0, 128, 0);'></td></tr><tr><td>hope</td><td>(0, 255, 0)</td><td style='background-color: rgb(0, 255, 0);'></td></tr><tr><td>pride</td><td>(0, 255, 0)</td><td style='background-color: rgb(0, 255, 0);'></td></tr><tr><td>shame</td><td>(255, 0, 0)</td><td style='background-color: rgb(255, 0, 0);'></td></tr><tr><td>guilt</td><td>(128, 0, 0)</td><td style='background-color: rgb(128, 0, 0);'></td></tr><tr><td>envy</td><td>(0, 128, 0)</td><td style='background-color: rgb(0, 128, 0);'></td></tr><tr><td>frustration</td><td>(255, 0, 0)</td><td style='background-color: rgb(255, 0, 0);'></td></tr><tr><td>curiosity</td><td>(0, 128, 255)</td><td style='background-color: rgb(0, 128, 255);'></td></tr><tr><td>amusement</td><td>(255, 255, 0)</td><td style='background-color: rgb(255, 255, 0);'></td></tr><tr><td>boredom</td><td>(105, 105, 105)</td><td style='background-color: rgb(105, 105, 105);'></td></tr><tr><td>loneliness</td><td>(0, 0, 0)</td><td style='background-color: rgb(0, 0, 0);'></td></tr><tr><td>empathy</td><td>(255, 191, 0)</td><td style='background-color: rgb(255, 191, 0);'></td></tr><tr><td>sympathy</td><td>(0, 0, 255)</td><td style='background-color: rgb(0, 0, 255);'></td></tr><tr><td>anticipation</td><td>(255, 165, 0)</td><td style='background-color: rgb(255, 165, 0);'></td></tr><tr><td>disappointment</td><td>(70, 130, 180)</td><td style='background-color: rgb(70, 130, 180);'></td></tr><tr><td>relief</td><td>(0, 255, 0)</td><td style='background-color: rgb(0, 255, 0);'></td></tr><tr><td>nostalgia</td><td>(255, 211, 0)</td><td style='background-color: rgb(255, 211, 0);'></td></tr><tr><td>awe</td><td>(0, 255, 255)</td><td style='background-color: rgb(0, 255, 255);'></td></tr><tr><td>eagerness</td><td>(255, 165, 0)</td><td style='background-color: rgb(255, 165, 0);'></td></tr><tr><td>confidence</td><td>(0, 128, 0)</td><td style='background-color: rgb(0, 128, 0);'></td></tr><tr><td>insecurity</td><td>(255, 165, 0)</td><td style='background-color: rgb(255, 165, 0);'></td></tr><tr><td>embarrassment</td><td>(255, 0, 0)</td><td style='background-color: rgb(255, 0, 0);'></td></tr><tr><td>indifference</td><td>(128, 128, 128)</td><td style='background-color: rgb(128, 128, 128);'></td></tr><tr><td>confusion</td><td>(128, 128, 128)</td><td style='background-color: rgb(128, 128, 128);'></td></tr><tr><td>admiration</td><td>(0, 255, 0)</td><td style='background-color: rgb(0, 255, 0);'></td></tr><tr><td>compassion</td><td>(255, 102, 102)</td><td style='background-color: rgb(255, 102, 102);'></td></tr><tr><td>resentment</td><td>(255, 0, 0)</td><td style='background-color: rgb(255, 0, 0);'></td></tr><tr><td>calmness</td><td>(0, 128, 0)</td><td style='background-color: rgb(0, 128, 0);'></td></tr><tr><td>apprehension</td><td>(255, 165, 0)</td><td style='background-color: rgb(255, 165, 0);'></td></tr><tr><td>sorrow</td><td>(0, 0, 0)</td><td style='background-color: rgb(0, 0, 0);'></td></tr><tr><td>contempt</td><td>(0, 255, 0)</td><td style='background-color: rgb(0, 255, 0);'></td></tr><tr><td>irritation</td><td>(255, 69, 0)</td><td style='background-color: rgb(255, 69, 0);'></td></tr><tr><td>melancholy</td><td>(70, 89, 119)</td><td style='background-color: rgb(70, 89, 119);'></td></tr><tr><td>bliss</td><td>(0, 255, 0)</td><td style='background-color: rgb(0, 255, 0);'></td></tr><tr><td>regret</td><td>(128, 0, 0)</td><td style='background-color: rgb(128, 0, 0);'></td></tr><tr><td>satisfaction</td><td>(0, 255, 0)</td><td style='background-color: rgb(0, 255, 0);'></td></tr><tr><td>yearning</td><td>(255, 204, 0)</td><td style='background-color: rgb(255, 204, 0);'></td></tr><tr><td>serenity</td><td>(0, 176, 240)</td><td style='background-color: rgb(0, 176, 240);'></td></tr></table>
</html>

To be honest, I'm not super impressed with gpt3.5's work here. Among other tthings, there is a disappointing amount of color-reuse across distinct emotions. I wonder what happens if I try prompting GPT4 instead? Let's try  re-running with that via `edsl`. I think that's as simple as: 

{% highlight python %}
m4 = Model('gpt-4-1106-preview', cache=False)
result4 = q.by(agents).by(m4).run()
tups4 = list(zip([e.lower() for e in emotions], [ast.literal_eval(r.answer['favorite_color']) for r in result4]))
{% endhighlight %}

Here are the new results: 

<html>
<table border='1'><tr><th>Emotion</th><th>RGB Value</th><th>Color</th></tr><tr><td>happiness</td><td>(255, 223, 0)</td><td style='background-color: rgb(255, 223, 0);'></td></tr><tr><td>sadness</td><td>(105, 105, 105)</td><td style='background-color: rgb(105, 105, 105);'></td></tr><tr><td>anger</td><td>(255, 0, 0)</td><td style='background-color: rgb(255, 0, 0);'></td></tr><tr><td>fear</td><td>(0, 0, 0)</td><td style='background-color: rgb(0, 0, 0);'></td></tr><tr><td>disgust</td><td>(96, 123, 139)</td><td style='background-color: rgb(96, 123, 139);'></td></tr><tr><td>surprise</td><td>(255, 255, 0)</td><td style='background-color: rgb(255, 255, 0);'></td></tr><tr><td>love</td><td>(255, 105, 180)</td><td style='background-color: rgb(255, 105, 180);'></td></tr><tr><td>joy</td><td>(255, 223, 0)</td><td style='background-color: rgb(255, 223, 0);'></td></tr><tr><td>anxiety</td><td>(128, 123, 104)</td><td style='background-color: rgb(128, 123, 104);'></td></tr><tr><td>excitement</td><td>(255, 215, 0)</td><td style='background-color: rgb(255, 215, 0);'></td></tr><tr><td>jealousy</td><td>(102, 204, 0)</td><td style='background-color: rgb(102, 204, 0);'></td></tr><tr><td>gratitude</td><td>(255, 184, 108)</td><td style='background-color: rgb(255, 184, 108);'></td></tr><tr><td>contentment</td><td>(173, 216, 230)</td><td style='background-color: rgb(173, 216, 230);'></td></tr><tr><td>hope</td><td>(255, 223, 0)</td><td style='background-color: rgb(255, 223, 0);'></td></tr><tr><td>pride</td><td>(255, 215, 0)</td><td style='background-color: rgb(255, 215, 0);'></td></tr><tr><td>shame</td><td>(245, 245, 220)</td><td style='background-color: rgb(245, 245, 220);'></td></tr><tr><td>guilt</td><td>(128, 128, 128)</td><td style='background-color: rgb(128, 128, 128);'></td></tr><tr><td>envy</td><td>(76, 187, 23)</td><td style='background-color: rgb(76, 187, 23);'></td></tr><tr><td>frustration</td><td>(255, 0, 0)</td><td style='background-color: rgb(255, 0, 0);'></td></tr><tr><td>curiosity</td><td>(255, 165, 0)</td><td style='background-color: rgb(255, 165, 0);'></td></tr><tr><td>amusement</td><td>(255, 133, 27)</td><td style='background-color: rgb(255, 133, 27);'></td></tr><tr><td>boredom</td><td>(128, 128, 128)</td><td style='background-color: rgb(128, 128, 128);'></td></tr><tr><td>loneliness</td><td>(105, 105, 105)</td><td style='background-color: rgb(105, 105, 105);'></td></tr><tr><td>empathy</td><td>(79, 91, 213)</td><td style='background-color: rgb(79, 91, 213);'></td></tr><tr><td>sympathy</td><td>(255, 192, 203)</td><td style='background-color: rgb(255, 192, 203);'></td></tr><tr><td>anticipation</td><td>(255, 165, 0)</td><td style='background-color: rgb(255, 165, 0);'></td></tr><tr><td>disappointment</td><td>(105, 105, 105)</td><td style='background-color: rgb(105, 105, 105);'></td></tr><tr><td>relief</td><td>(135, 206, 250)</td><td style='background-color: rgb(135, 206, 250);'></td></tr><tr><td>nostalgia</td><td>(255, 192, 203)</td><td style='background-color: rgb(255, 192, 203);'></td></tr><tr><td>awe</td><td>(255, 215, 0)</td><td style='background-color: rgb(255, 215, 0);'></td></tr><tr><td>eagerness</td><td>(255, 165, 0)</td><td style='background-color: rgb(255, 165, 0);'></td></tr><tr><td>confidence</td><td>(255, 215, 0)</td><td style='background-color: rgb(255, 215, 0);'></td></tr><tr><td>insecurity</td><td>(128, 128, 128)</td><td style='background-color: rgb(128, 128, 128);'></td></tr><tr><td>embarrassment</td><td>(249, 132, 229)</td><td style='background-color: rgb(249, 132, 229);'></td></tr><tr><td>indifference</td><td>(128, 128, 128)</td><td style='background-color: rgb(128, 128, 128);'></td></tr><tr><td>confusion</td><td>(128, 128, 128)</td><td style='background-color: rgb(128, 128, 128);'></td></tr><tr><td>admiration</td><td>(255, 223, 0)</td><td style='background-color: rgb(255, 223, 0);'></td></tr><tr><td>compassion</td><td>(255, 105, 180)</td><td style='background-color: rgb(255, 105, 180);'></td></tr><tr><td>resentment</td><td>(153, 76, 0)</td><td style='background-color: rgb(153, 76, 0);'></td></tr><tr><td>calmness</td><td>(135, 206, 250)</td><td style='background-color: rgb(135, 206, 250);'></td></tr><tr><td>apprehension</td><td>(128, 128, 128)</td><td style='background-color: rgb(128, 128, 128);'></td></tr><tr><td>sorrow</td><td>(105, 105, 105)</td><td style='background-color: rgb(105, 105, 105);'></td></tr><tr><td>contempt</td><td>(64, 64, 72)</td><td style='background-color: rgb(64, 64, 72);'></td></tr><tr><td>irritation</td><td>(255, 0, 0)</td><td style='background-color: rgb(255, 0, 0);'></td></tr><tr><td>melancholy</td><td>(105, 105, 105)</td><td style='background-color: rgb(105, 105, 105);'></td></tr><tr><td>bliss</td><td>(135, 206, 250)</td><td style='background-color: rgb(135, 206, 250);'></td></tr><tr><td>regret</td><td>(105, 105, 105)</td><td style='background-color: rgb(105, 105, 105);'></td></tr><tr><td>satisfaction</td><td>(76, 175, 80)</td><td style='background-color: rgb(76, 175, 80);'></td></tr><tr><td>yearning</td><td>(72, 61, 139)</td><td style='background-color: rgb(72, 61, 139);'></td></tr><tr><td>serenity</td><td>(135, 206, 250)</td><td style='background-color: rgb(135, 206, 250);'></td></tr></table>
</html>

This feels a bit richer, intuitively, though still includes a lot of repetitions. To see this more clearly, here's a version of the table sorting by brightness: 

{% highlight python %}
def generate_html_table(emotion_colors):
    # Function to calculate the average brightness of an RGB color
    def calculate_brightness(rgb):
        return sum(rgb) / len(rgb)

    # Sorting the emotion_colors list by the average brightness of the colors
    sorted_emotion_colors = sorted(emotion_colors, key=lambda x: calculate_brightness(x[1]), reverse=True)

    # Starting the HTML for the table
    html = "<table border='1'>"

    # Adding headers
    html += "<tr><th>Emotion</th><th>RGB Value</th><th>Color</th></tr>"

    # Iterating over the sorted list of tuples to fill the rows
    for emotion, color in sorted_emotion_colors:
        # Format the RGB color as a string
        color_rgb_string = f"({color[0]}, {color[1]}, {color[2]})"
        # Format the RGB color for HTML styling
        color_rgb_html = f"rgb{color}"
        # Adding a row with the emotion, the RGB string, and a colored cell
        html += f"<tr><td>{emotion}</td><td>{color_rgb_string}</td><td style='background-color: {color_rgb_html};'></td></tr>"

    # Closing the table tag
    html += "</table>"

    return html
{% endhighlight %}

<html>
<table border='1'><tr><th>Emotion</th><th>RGB Value</th><th>Color</th></tr><tr><td>shame</td><td>(245, 245, 220)</td><td style='background-color: rgb(245, 245, 220);'></td></tr><tr><td>sympathy</td><td>(255, 192, 203)</td><td style='background-color: rgb(255, 192, 203);'></td></tr><tr><td>nostalgia</td><td>(255, 192, 203)</td><td style='background-color: rgb(255, 192, 203);'></td></tr><tr><td>contentment</td><td>(173, 216, 230)</td><td style='background-color: rgb(173, 216, 230);'></td></tr><tr><td>embarrassment</td><td>(249, 132, 229)</td><td style='background-color: rgb(249, 132, 229);'></td></tr><tr><td>relief</td><td>(135, 206, 250)</td><td style='background-color: rgb(135, 206, 250);'></td></tr><tr><td>calmness</td><td>(135, 206, 250)</td><td style='background-color: rgb(135, 206, 250);'></td></tr><tr><td>bliss</td><td>(135, 206, 250)</td><td style='background-color: rgb(135, 206, 250);'></td></tr><tr><td>serenity</td><td>(135, 206, 250)</td><td style='background-color: rgb(135, 206, 250);'></td></tr><tr><td>gratitude</td><td>(255, 184, 108)</td><td style='background-color: rgb(255, 184, 108);'></td></tr><tr><td>love</td><td>(255, 105, 180)</td><td style='background-color: rgb(255, 105, 180);'></td></tr><tr><td>compassion</td><td>(255, 105, 180)</td><td style='background-color: rgb(255, 105, 180);'></td></tr><tr><td>surprise</td><td>(255, 255, 0)</td><td style='background-color: rgb(255, 255, 0);'></td></tr><tr><td>happiness</td><td>(255, 223, 0)</td><td style='background-color: rgb(255, 223, 0);'></td></tr><tr><td>joy</td><td>(255, 223, 0)</td><td style='background-color: rgb(255, 223, 0);'></td></tr><tr><td>hope</td><td>(255, 223, 0)</td><td style='background-color: rgb(255, 223, 0);'></td></tr><tr><td>admiration</td><td>(255, 223, 0)</td><td style='background-color: rgb(255, 223, 0);'></td></tr><tr><td>excitement</td><td>(255, 215, 0)</td><td style='background-color: rgb(255, 215, 0);'></td></tr><tr><td>pride</td><td>(255, 215, 0)</td><td style='background-color: rgb(255, 215, 0);'></td></tr><tr><td>awe</td><td>(255, 215, 0)</td><td style='background-color: rgb(255, 215, 0);'></td></tr><tr><td>confidence</td><td>(255, 215, 0)</td><td style='background-color: rgb(255, 215, 0);'></td></tr><tr><td>curiosity</td><td>(255, 165, 0)</td><td style='background-color: rgb(255, 165, 0);'></td></tr><tr><td>anticipation</td><td>(255, 165, 0)</td><td style='background-color: rgb(255, 165, 0);'></td></tr><tr><td>eagerness</td><td>(255, 165, 0)</td><td style='background-color: rgb(255, 165, 0);'></td></tr><tr><td>amusement</td><td>(255, 133, 27)</td><td style='background-color: rgb(255, 133, 27);'></td></tr><tr><td>guilt</td><td>(128, 128, 128)</td><td style='background-color: rgb(128, 128, 128);'></td></tr><tr><td>boredom</td><td>(128, 128, 128)</td><td style='background-color: rgb(128, 128, 128);'></td></tr><tr><td>insecurity</td><td>(128, 128, 128)</td><td style='background-color: rgb(128, 128, 128);'></td></tr><tr><td>indifference</td><td>(128, 128, 128)</td><td style='background-color: rgb(128, 128, 128);'></td></tr><tr><td>confusion</td><td>(128, 128, 128)</td><td style='background-color: rgb(128, 128, 128);'></td></tr><tr><td>apprehension</td><td>(128, 128, 128)</td><td style='background-color: rgb(128, 128, 128);'></td></tr><tr><td>empathy</td><td>(79, 91, 213)</td><td style='background-color: rgb(79, 91, 213);'></td></tr><tr><td>disgust</td><td>(96, 123, 139)</td><td style='background-color: rgb(96, 123, 139);'></td></tr><tr><td>anxiety</td><td>(128, 123, 104)</td><td style='background-color: rgb(128, 123, 104);'></td></tr><tr><td>satisfaction</td><td>(76, 175, 80)</td><td style='background-color: rgb(76, 175, 80);'></td></tr><tr><td>sadness</td><td>(105, 105, 105)</td><td style='background-color: rgb(105, 105, 105);'></td></tr><tr><td>loneliness</td><td>(105, 105, 105)</td><td style='background-color: rgb(105, 105, 105);'></td></tr><tr><td>disappointment</td><td>(105, 105, 105)</td><td style='background-color: rgb(105, 105, 105);'></td></tr><tr><td>sorrow</td><td>(105, 105, 105)</td><td style='background-color: rgb(105, 105, 105);'></td></tr><tr><td>melancholy</td><td>(105, 105, 105)</td><td style='background-color: rgb(105, 105, 105);'></td></tr><tr><td>regret</td><td>(105, 105, 105)</td><td style='background-color: rgb(105, 105, 105);'></td></tr><tr><td>jealousy</td><td>(102, 204, 0)</td><td style='background-color: rgb(102, 204, 0);'></td></tr><tr><td>envy</td><td>(76, 187, 23)</td><td style='background-color: rgb(76, 187, 23);'></td></tr><tr><td>yearning</td><td>(72, 61, 139)</td><td style='background-color: rgb(72, 61, 139);'></td></tr><tr><td>anger</td><td>(255, 0, 0)</td><td style='background-color: rgb(255, 0, 0);'></td></tr><tr><td>frustration</td><td>(255, 0, 0)</td><td style='background-color: rgb(255, 0, 0);'></td></tr><tr><td>irritation</td><td>(255, 0, 0)</td><td style='background-color: rgb(255, 0, 0);'></td></tr><tr><td>resentment</td><td>(153, 76, 0)</td><td style='background-color: rgb(153, 76, 0);'></td></tr><tr><td>contempt</td><td>(64, 64, 72)</td><td style='background-color: rgb(64, 64, 72);'></td></tr><tr><td>fear</td><td>(0, 0, 0)</td><td style='background-color: rgb(0, 0, 0);'></td></tr></table>
</html>

Interesting. Here we can better see the color repetition. There seem to be clear nodes around (1) a shade of light blue that's assosciated with calmness/relief etc, (2) a shade of warm yellow/gold that's associated with positive emotions (happiness, joy, awe, confidence), (3) a shade of lighter gray associated with neutral/negative emotions (guilt, boredom, indifference), (4)a shade of darker grey associated with more negative emotions (sadness, loneliness, regret), and (5) bright red for anger/frustration/irritation. There's a few other more unique and intuitive picks like green for jealousy/envy and black for fear. Shame at the top as an off-white is somewhat surprising to me. 

I do notice that there seems to be a generally positive association between brightness (average RGB value) and the extent of "positivity" of the emotion, with the exception of shame, sympathy and nostalgia at the very top.

In general, it's also interesting that the set of colors are so different compared to GPT3.5 which is the default that was used above. I'm also curious how much results would differ with tweaks to the prompts (e.g. even just asking for hex codes or CMYK colors instead of RGB). 

There's various further analysis we could do here -- e.g. I considered doing a 2D embedding with t-SNE and visualizing the results. I'll save that for another day. My main goal here was just to experiment a bit more with `edsl` and get familiar. 