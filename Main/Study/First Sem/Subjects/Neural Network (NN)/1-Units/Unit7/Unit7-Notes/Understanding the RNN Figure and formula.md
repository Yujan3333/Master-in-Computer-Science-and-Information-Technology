This figure illustrates the basic architecture and computation flow of a Recurrent Neural Network (RNN). 

## Left Side - Basic RNN Cell

The left diagram shows a single RNN cell with three components:

- **x** (blue): Input at the current time step
- **h** (yellow): Hidden state that carries information from previous time steps
- **y** (gray): Output at the current time step

The connections show:

- **Wx**: Weight matrix for the input
- **Wh**: Weight matrix for the hidden state (recurrent connection)
- **Wy**: Weight matrix for the output

## Right Side - Unfolded RNN

The right diagram shows how the RNN "unfolds" over time, revealing the sequential nature:

- Each time step (t₁, t₂, t₃, ...) has its own input (x₁, x₂, x₃)
- The hidden states (h₁, h₂, h₃) flow from left to right, carrying information forward
- Each time step produces its own output (y₁, y₂, y₃)

## Key Equations

The figure shows two fundamental RNN computations:

1. **Hidden state computation**: `ht = f(Wh*ht-1 + Wx*xt)`
    
    - The current hidden state depends on both the previous hidden state and current input
    - `f` is typically an activation function like tanh or ReLU
2. **Output computation**: `yt = f(Wy*ht)`
    
    - The output at each time step is computed from the current hidden state

## The Key Insight

The "≡" symbol shows that these are equivalent representations - the compact RNN cell on the left is the same as the unfolded sequence on the right. This unfolding helps visualize how RNNs process sequential data by maintaining memory through the hidden state connections.