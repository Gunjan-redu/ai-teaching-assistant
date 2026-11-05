# I built an AI teaching assistant, and it found gaps in my own teaching material



I've been teaching coding for quite a few years now. Since I'm also trying to transition into a career in IT, I've been working on learning new skills and building projects along the way.

One of those projects was a RAG-based teaching assistant that could answer questions about Python concepts like variables, loops and functions.

I wrote all the documents myself. They weren't scraped from the internet. I wanted the assistant to work with the same beginner-friendly explanations I use when teaching students.

The first question I asked it was: "What is a function?"

It gave me a correct explanation of how functions work and the different ways of using them in Python. But it also pointed out something interesting: the provided context didn't actually contain a definition of a function.

And it was right. I hadn't written one anywhere in my documents.

## What I built, in four steps

The basic flow looks like this:

Corpus → Chunks and embeddings → Retrieval and threshold check → Claude generates an answer with citations.

The process started with building the corpus. I had to write all the documents about functions, variables and loops myself.

I tried to keep the explanations simple and beginner-friendly. From my experience teaching students, I've found that this works best, especially when someone is learning Python as their first programming language.

Once the documents were ready, I had to split them into smaller chunks.

I decided to use a heading + paragraph approach, along with a merge pass that reattaches code blocks to their explanations. I didn't want the retrieval system returning a piece of code without the explanation that goes with it.

I then converted these chunks into 1024-dimensional vectors using Voyage AI and stored them in my PostgreSQL database along with their document names and headings.

When a user asks a question, I send it through Voyage AI as well to generate its embedding. I then compare it against the stored vectors and retrieve the three closest chunks.

I also added a threshold check. If even the closest chunk has a distance greater than 0.93, the system stops there, without making a call to Claude.

Otherwise, the text from those three chunks (not the vectors themselves) is passed to Claude, which uses that context to generate an answer.

Finally, the answer is displayed on the frontend along with its sources and citations.

## The audit story

As I mentioned earlier, my first question to the assistant was "What is a function?"

The answer did two things. It explained functions correctly using the available context, but it also pointed out that the context didn't contain an actual definition of a function.

I found this particularly interesting.

I wouldn't call myself an expert, but I've been teaching these concepts for years. And I think this is something that can happen when you've been teaching the same subject for a long time.

Sometimes, we assume that beginners already know certain things because they seem too obvious to us.

That's exactly what I had done.

I had explained the different ways of using functions, how they work and how to write them. Somewhere along the way, I assumed that explaining all these things would automatically help a student understand what a function actually is.

But I had never explicitly defined it in my document.

The reason the assistant caught this was quite simple: I had instructed it to answer ONLY using the provided context.

As a teacher, I automatically fill in gaps when explaining something. The definition of a function is something I probably say at the whiteboard without even thinking about it. So I never noticed that it was missing from my written material.

The assistant couldn't do that. It wasn't allowed to make assumptions, and that made the missing information obvious.

I went back and added a definition:

"In Python, a function is a reusable block of code that executes only when called."

But that wasn't the end of it. While reviewing the documents, I found a few more things that needed attention:

- What happens when a function doesn't return anything? (The whole `None` surprise.)
- What's the difference between parameters and arguments?
- Some examples had code but didn't show what the actual output would look like.

I fixed these as well.

Then I just had to run `python store.py` to chunk the documents again, generate new embeddings and store everything in the database.

When I asked "What is a function?" again, the assistant now started with an actual definition.

What I liked most about this was that the project became more than just a tool for answering questions about my course material. It also helped me improve the material itself.

And I can repeat this process whenever I want: ask questions, see where the assistant struggles or points out missing information, update the documents and run the ingestion process again.

In a way, the assistant ended up auditing the very material it was built to teach.

## The threshold story

One thing I struggled with while building this project was deciding on the right threshold for rejecting questions that were outside the scope of my documents.

Initially, I assumed that questions my documents could answer would have a smaller distance from the stored chunks than questions they couldn't answer.

But when I started testing, the results weren't what I expected.

For example:

- "What is a float?" (a topic covered in my documents) scored 0.853.
- "What is a dictionary?" (a topic not covered in my documents) scored 0.852.

The distances were almost identical.

However, when I tried something completely unrelated, like "Who is the PM of India?", the distance was 0.957.

This made me realise something about how embeddings work in this particular setup.

Questions about floats and dictionaries are both Python-related questions. Even though my documents didn't cover dictionaries, the embedding model still placed that question close to my Python-related content.

In other words, being semantically close doesn't necessarily mean that my documents contain the answer.

I had seen tutorials suggesting thresholds around 0.78, but using that value would have rejected a question about floats that my documents could actually answer.

After experimenting with my own data, I settled on 0.93.

I deliberately kept it quite high because I didn't want to reject questions just because their nearest chunks weren't particularly close.

This also changed how I thought about the threshold.

Its main purpose isn't to decide whether a question is relevant or not. It's more of a first-level filter to catch obviously unrelated questions before making an API call to Claude.

Anything that sounds like a Python-related question gets a chance to go through. Claude then reads the retrieved chunks and decides whether there's enough information in the context to answer.

So, the actual decision about whether the answer exists in my documents happens at the LLM stage, not through the distance threshold.

## Deployment day

For deployment, I initially planned to use Render's free tier for both the application and the database.

But while going through their pricing page, I noticed something important: free-tier databases are deleted after 30 days.

I didn't want to risk losing all the documents and embeddings I'd worked on, so I decided to split the deployment.

The application is hosted on Render, while the PostgreSQL database (with pgvector) is hosted on Supabase.

Another interesting thing I learned during deployment was how differently Windows and Linux handle environment variables.

My first deployment on Render failed because I was using an environment variable called `DB_Port`.

It had been working perfectly fine on my Windows machine for weeks. But Windows environment variables are case-insensitive, whereas Linux environment variables are case-sensitive.

So `DB_Port` and `DB_PORT` weren't treated as the same thing.

The fix was just one character, but it took down the entire production deployment.

After fixing it, all I had to do was push the changes to GitHub. Render automatically picked them up and redeployed the application.

This was also when I realised how useful it was to have all my database configuration handled through environment variables.

For example, when I wanted to point the application to a database in Tokyo, I only had to make a small change in my configuration file. I didn't have to change the application code at all.

## What's live now

The teaching assistant is now deployed, and I can ask it questions about the Python concepts covered in my documents.

[Live Demo](https://ai-teaching-assistant-d2tw.onrender.com/)

![AI teaching assistant](assets/demo-screenshot.png)

[Github repo](https://github.com/Gunjan-redu/ai-teaching-assistant)


There are still things I'd like to improve, especially around retrieval quality and testing how well the assistant handles questions that aren't covered in the documents.

But this project taught me quite a bit, not just about RAG, embeddings, vector databases and deployment, but also about something I hadn't expected: how building a tool to teach something can sometimes reveal gaps in the way you teach it yourself.

