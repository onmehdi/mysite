from django.shortcuts import render,get_object_or_404
from blog.models import Post

# Create your views here.
def blog_view(request):
    posts = Post.objects.filter(status = 1)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    post = get_object_or_404(Post,pk=pid,status=1)
    context = {'post':post}
    # context = {'title':'bitcoin crash again!!!','content':'The listing expands access to TRX for U.S. market participants through a regulated trading venue, providing investors and institutions with an additional platform to access the native utility token of the TRON blockchain. TRX supports transactions, smart contract execution, decentralized applications, and network governance across one of the world’s most active blockchain ecosystems. TRON is recognized as a leading blockchain for stablecoin activity and digital asset settlement, hosting more than $89 billion in circulating USDT and over $27 billion in total value locked (TVL).'}
    return render(request,'blog/blog-single.html',context)


def test_view(request,pid):
    # post = Post.objects.get(id=pid)
    post = get_object_or_404(Post,pk=pid)
    context = {'post':post}
    return render(request,'blog/test.html',context)