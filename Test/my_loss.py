import torch
inp=torch.randn([4,3])
print(inp)
target=torch.tensor([0,1,2,1])#这输入的是标签
loss=torch.nn.CrossEntropyLoss()
print(loss(inp,target))