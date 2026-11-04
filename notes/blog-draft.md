# I built an AI teaching assistant and it found holes in my own teaching docs

## The hook
I am a coding teacher, I have been teaching coding for quite a few years now. Since I am trying to transition
into a career in IT, I am trying to gain alot of new skills. Part of this skill learning process was to make RAG 
assistant which can answer to questions about python concepts(variables, loops, functions). I prepared all the documents myself
(not scraped from the internet). The first question I asked the assistant was what is a function, although it answered
correctly telling me how a function works and what are the different ways of using a function python,
it also mentioned that the context doesn't include a definition of a function, which was correct. I hadn't mentioned
what exactly a function anywhere in the document.


## What I built, in four beats
- (corpus → chunks+vectors → retrieval+threshold → Claude with citations; live URL)

## What I built, in four beats

The process began by building the corpus, which means I had to type all the
documents about functions, variables and loops myself. These documents are
carefully written in beginner-friendly language. I intentionally simplify the
concept explanations because, from my experience of teaching students, that is
the best way to explain things to a kid who is probably learning Python as
their very first programming language.

After building the corpus, the next step was to divide it into chunks. I
decided to chunk the corpus by heading + paragraph, with a merge pass that
re-attaches code blocks to their explanations — so retrieval never returns
code without its context. These chunks were then converted into 1024-length
vectors with the help of Voyage AI and stored in the database along with their
heading and document name.

When we receive a question from the user, we use Voyage AI again to get its
vector, then compare this vector to all the stored vectors and get the top
three chunks whose vectors are closest to it. If
even the nearest chunk is farther than 0.93, we consider that we don't have
what they are looking for, and stop right there — before any LLM call.

Otherwise, the top three chunks' text — never the vectors themselves — goes
to Claude, which prepares a response for the user.
This response is then rendered to the UI with sources and citations.




## The audit story
- (before-answer vs after-answer; the doc enrichment loop)

## The threshold story
- (0.853 vs 0.852 — the numbers; why distance can't judge relevance)

## Deployment day
- (DB_Port and Linux; Render's 30-day DB discovery; the Tokyo swap)

## What's live now
- (URL, screenshot, what I'd do next)