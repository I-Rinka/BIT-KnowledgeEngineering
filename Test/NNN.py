import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
 
word_to_ix = {'hello': 0, 'world': 1}
embeds = nn.Embedding(2, 5).cuda()
hello_idx = torch.tensor([word_to_ix['world']]).cuda()
print(hello_idx)
# hello_idx = Variable(hello_idx)
hello_embed = embeds(hello_idx)
print(hello_embed)
hello_idx = torch.tensor([word_to_ix['hello']]).cuda()#访问pytorch word embedding的维度只能通过torch的变量？
#只有cuda能访问cuda
hello_embed = embeds(hello_idx)
print(hello_embed)
print(hello_embed+torch.ones_like(hello_embed).cuda())

embeds.weight.data.copy_(torch.tensor([[1,0,10,0,-1],[0,1,1,1,0]]).cuda())
# print(hello_embed*torch.zeros(5))
print(embeds(torch.tensor([1]).cuda()))
print(embeds(torch.tensor([0]).cuda()))

theta=torch.randn(10000).cuda()
for i in range(2000):
    theta+=torch.ones(10000).cuda()
    print(theta)