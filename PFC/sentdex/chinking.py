import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

#we can separate by sentence, word, and part of speech tag

#we can only chunk things that are touching.

#train_text = state_union.raw("2005-GWBush.txt")
#sample_text = state_union.raw("2006-GWBush.txt")

train_text = "Hello President George Bush"
sample_text = '''
Well, Seymour, I made it- despite your directions. 
Ah. Superintendent Chalmers. Welcome. - I hope you're prepared for an unforgettable luncheon. 
- Yeah. Oh, egads! My roast is ruined. 
But what if I were to purchase fast food and disguise it as my own cooking? 
Delightfully devilish, Seymour. 
Ah- Skinner with his crazy explanations 
The superintendent's gonna need his medication When he hears Skinner's lame exaggerations 
There'll be trouble in town tonight 
Seymour! Superintendent, I was just- uh, just stretching my calves on the windowsill. 
Isometric exercise. Care to join me? Why is there smoke coming out of your oven, Seymour? 
Uh- Oh. That isn't smoke. It's steam. Steam from the steamed clams we're having. Mmm. 
Steamed clams. Whew. Superintendent, I hope you're ready for mouthwatering hamburgers. 
I thought we were having steamed clams. D'oh, no. I said steamed hams. 
That's what I call hamburgers. You call hamburgers steamed hams? 
Yes. It's a regional dialect. - Uh-huh. Uh, what region? - 
Uh, upstate New York. Really. Well, I'm from Utica, and 
I've never heard anyone use the phrase "steamed hams. " Oh, not in Utica. No. 
It's an Albany expression. I see. You know, these hamburgers are quite similar to the ones they have at 
Krusty Burger. Oh, no. Patented Skinner burgers. Old family recipe. - 
For steamed hams. - Yes. Yes. 
And you call them steamed hams despite the fact that they are obviously grilled. 
Ye- You know, the- One thing I should- - Excuse me for one second. - 
Of course. Well, that was wonderful. A good time was had by all. I'm pooped.
 Yes. I should be- Good Lord! What is happening in there? - Aurora borealis. - 
 Uh- Aurora borealis at this time of year at this time of day in this part of 
 the country localized entirely within your kitchen? - Yes. - May I see it? 
 No. Seymour. ! The house is on fire. ! No, Mother. It's just the northern lights. 
 Well, Seymour, you are an odd fellow but I must say you steam a good ham.
'''
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)


def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)

            chunkGram = r"""Chunk: {<.*>+}
                                    }<NNP | PRP>+{ """
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            chunked.draw()
    except Exception as e:
        print(str(e))


process_content()