# I built an AI teaching assistant and it found holes in my own teaching docs

## The hook
I am a coding teacher, I have been teaching coding for quite a few years now. Since I am trying to transition
into a career in IT, I am trying to gain alot of new skills. Part of this skill learning process was to make RAG 
assistant which can answer to questions about python concepts(variables, loops, functions). I prepared all the documents myself
(not scraped from the internet). The first question I asked the assistant was what is a function, although it answered
correctly telling me how a function works and what are the different ways of using a function python,
it also mentioned that the context doesn't include a definition of a function, which was correct. I hadn't mentioned
what exactly a function anywhere in the document.


Recently while trying to make a RAG assistant 
## What I built, in four beats
- (corpus → chunks+vectors → retrieval+threshold → Claude with citations; live URL)

## The audit story
- (before-answer vs after-answer; the doc enrichment loop)

## The threshold story
- (0.853 vs 0.852 — the numbers; why distance can't judge relevance)

## Deployment day
- (DB_Port and Linux; Render's 30-day DB discovery; the Tokyo swap)

## What's live now
- (URL, screenshot, what I'd do next)