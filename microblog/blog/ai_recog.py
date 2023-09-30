from .models import Post,Comment
from transformers import pipeline
import asyncio

async def del_bad(comment):
    pipe = pipeline("text-classification")
    result=pipe(comment.body)
    if "N" in str(result[0]):
        print("========NEGATIVE=======\n")
        print(f"NEGATIVE : {comment.body}\n")
        print(f"{result[0]}\n")
        return comment.name
    else:
        print("========POSITIVE========\n")
        print(f"POSITIVE : {comment.body}\n")
        print(f"{result[0]}\n")
        return None
    

def identify_ifbad(this_comment=None):
    if this_comment != None:
        records=Comment.objects.filter(name=del_bad(comment))
        records.delete()
    else:
        del_name=[]
        for comment in Comment.objects.all():
            name=asyncio.run(del_bad(comment))
            if name!=None:
                del_name.append(name)
        print(del_name)
        for name in del_name:
            records=Comment.objects.filter(name=name)
            records.delete()
