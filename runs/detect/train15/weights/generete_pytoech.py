import torch

# Carregue o modelo treinado
model = torch.load('best.pt', map_location='cpu')
model.eval()

# Converta para TorchScript
scripted_model = torch.jit.script(model)
scripted_model.save('best.torchscript')