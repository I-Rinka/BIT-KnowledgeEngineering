import torch

class LSTM(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lstm=torch.nn.LSTM(
            input_size=20,
            hidden_size=5,
            num_layers=1
        )
        self.out=torch.nn.Linear(5,3)
    
    def forward(self,x):
        output,(h_n,c_n)=self.lstm(x)
        output_in_last_timestep=h_n[-1,:,:]
        x=self.out(output_in_last_timestep)
        return  x
    
net=LSTM()
# x=torch.randn(7,1,20)
x=torch.rand(2,20)
print(x)
print(x.unsqueeze(1))
print(x.unsqueeze(0).shape)
print(net(x.unsqueeze(0)))