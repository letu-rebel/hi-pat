# Introduction

Attention all LeTourneau students! Have you been skipping chapel, hoping for divine intervention to make up those credits? Well, consider this your answered prayer. Welcome to this no-nonsense repository, where AI-generated chapel summaries come to your rescue.

## Here's The Drill:

1. **Fetching Transcripts**: Like a diligent student pulling all-nighters, we extract auto-generated subtitles from closed captions, preparing the text for our dedicated Language Learning Model (LLM).

2. **Generating Summaries**: We introduce these transcripts to the Claude API from Anthropic. It might not match up to ChatGPT-3.5, but it sure can handle up to 100k tokens at once. It's like cramming for finals - takes in everything in one go.

3. **Pushing to GitHub**: As the last step, these summarised notes are posted on this GitHub repository. Think of it as your digital binder for chapel summaries.

This system is as automated as those reminders about your overdue chapel credits. Timely updates follow every new chapel event.

## Usage

These text files are open for all, like LeTourneau's heart for late chapel-goers. You're welcome to peruse them at your convenience.

## Disclaimer

Like the chances of making up chapel credits at the eleventh hour, the accuracy of these summaries depends on the quality of the transcripts and the AI's comprehension. They aim for perfection but expect some bumps along the way.

## Contribution

Before you reach out, please note: I don't exist. My voicemail setup is still pending, much like your overdue chapel credits.

## License

Under the umbrella of the MIT License, this project operates. Use it wisely, kind of like scheduling your chapel make-ups well ahead of time.

{% assign image_names = "40izk9od7n771.gif,1984.gif,among-us-amogus.gif,ea.gif,elon-musk-smoke.gif,ezgif.com-gif-maker_4.giffuturama-checkmate.gif,huh.gif,image0.gif,IMG_1368.gif,IMG_4866.jpg,lithiumare-kiracord.gif,wide-putin.gif,yes-sir-yes-boss.gif" | split: "," %}
{% assign random_image_name = image_names | sample %}
{% assign random_image_url = "https://github.com/letu-rebel/hi-pat/blob/main/photos/" | append: random_image_name | append: "?raw=true" %}

<img src="{{ random_image_url }}" alt="Random Image" width="200"/>
