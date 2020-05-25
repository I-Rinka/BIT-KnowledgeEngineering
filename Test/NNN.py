import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
 
word_to_ix = {'hello': 0, 'world': 1}
embeds = nn.Embedding(2, 5)
hello_idx = torch.tensor([word_to_ix['world']])
print(hello_idx)
# hello_idx = Variable(hello_idx)
hello_embed = embeds(hello_idx)
print(hello_embed)
hello_idx = torch.tensor([word_to_ix['hello']])#访问pytorch word embedding的维度只能通过torch的变量？
hello_embed = embeds(hello_idx)
print(hello_embed)
print(hello_embed+torch.ones_like(hello_embed))

embeds.weight.data.copy_(torch.tensor([[1,0,10,0,-1],[0,1,1,1,0]]))
# print(hello_embed*torch.zeros(5))
print(embeds(torch.tensor([1])))
print(embeds(torch.tensor([0])))