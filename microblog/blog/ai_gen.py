from .models import Post,Comment
from transformers import pipeline
from concurrent.futures import ProcessPoolExecutor
import asyncio
"""
async def roberta(post):
    question_answerer = pipeline("question-answering", model="deepset/roberta-base-squad2")
    result = question_answerer(question="Why was this person having such a nice day?", context=str(post.body))
    Comment.objects.create(name="roberta", body=result['answer'], post =post)

async def bert(post):
    question_answerer = pipeline("question-answering", model="deepset/bert-base-cased-squad2")
    result = question_answerer(question="Why was this person having such a nice day?", context=str(post.body))
    Comment.objects.create(name="small_bert", body=result['answer'], post =post)

async def saleforce_discord_qa(post):
    question_answerer = pipeline("question-answering", model="Salesforce/discord_qa")
    result = question_answerer(question="Why was this person having such a nice day?", context=str(post.body))
    Comment.objects.create(name="saleforce_discord_qa", body=result['answer'], post =post)

async def distilled_bert(post):
    question_answerer = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
    result = question_answerer(question="Why was this person having such a nice day?", context=str(post.body))
    Comment.objects.create(name="distilled_bert", body=result['answer'], post =post)

async def large_bert(post):
    question_answerer = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")
    result = question_answerer(question="Why was this person having such a nice day?", context=str(post.body))
    Comment.objects.create(name="large_bert", body=result['answer'], post =post)

async def gpt2(post):
    question_answerer = pipeline("question-answering", model="anas-awadalla/gpt2-large-lr-1e5-span-head-finetuned-squad")
    result = question_answerer(question="Why was this person having such a nice day?", context=str(post.body))
    Comment.objects.create(name="gpt2", body=result['answer'], post =post)
"""

def roberta(post):
    question_answerer = pipeline("question-answering", model="deepset/roberta-base-squad2")
    result = question_answerer(question="Why was this person having such a nice day?", context=str(post.body))
    Comment.objects.create(name="roberta", body=result['answer'], post =post)

def bert(post):
    question_answerer = pipeline("question-answering", model="deepset/bert-base-cased-squad2")
    result = question_answerer(question="Why was this person having such a nice day?", context=str(post.body))
    Comment.objects.create(name="small_bert", body=result['answer'], post =post)

def saleforce_discord_qa(post):
    question_answerer = pipeline("question-answering", model="Salesforce/discord_qa")
    result = question_answerer(question="Why was this person having such a nice day?", context=str(post.body))
    Comment.objects.create(name="saleforce_discord_qa", body=result['answer'], post =post)

def distilled_bert(post):
    question_answerer = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
    result = question_answerer(question="Why was this person having such a nice day?", context=str(post.body))
    Comment.objects.create(name="distilled_bert", body=result['answer'], post =post)

def large_bert(post):
    question_answerer = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")
    result = question_answerer(question="Why was this person having such a nice day?", context=str(post.body))
    Comment.objects.create(name="large_bert", body=result['answer'], post =post)

def gpt2(post):
    question_answerer = pipeline("question-answering", model="anas-awadalla/gpt2-large-lr-1e5-span-head-finetuned-squad")
    result = question_answerer(question="Why was this person having such a nice day?", context=str(post.body))
    Comment.objects.create(name="gpt2", body=result['answer'], post =post)

def generate_comments(post):

    roberta(post)
    bert(post)
    #saleforce_discord_qa(post)
    distilled_bert(post)
    large_bert(post)
    #gpt2(post)
"""
    loop = asyncio.get_event_loop()
    gather = asyncio.gather(
        roberta(post),
        bert(post),
        saleforce_discord_qa(post),
        distilled_bert(post),
        large_bert(post),
        gpt2(post)
    )
    
    loop.run_until_complete(gather)
"""