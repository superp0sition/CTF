# The nano GPT

In this challenge the flavortext of the challenge describes a scenerio where humanity has been overthrown by AI. Seemingly unconnected, the last sentence says that we caught a **nanoGPT**. In the challenge we are provided two files, `ckpt.pt` and `meta.pkl`. Through some simple googling you find that `meta.pkl` is a binary that contains data from a model using the pickle library.

I initially wrote/used a short unpickler based on a [stackoverflow post](https://stackoverflow.com/questions/70022516/how-to-open-a-pkl-file) to find the data inside. At the same time I looked up [nanoGPT](https://github.com/karpathy/nanoGPT), but didn't understand why it was named in the challenge, and didn't look into it. Through running the unpicker I saw that that file just contained dictionary information. So, I  added a line to load the ckpt.pt file using pytorch and printed the output. This file contained a lot of metadata and tensors.

## Solution

After some more googling I realized that a model class would be necessary to load the model, and went back to [nanoGPT](https://github.com/karpathy/nanoGPT). Through slight ajustments to `sample.py` using the directory found in the ckpt.pt model, I was able to load the model. Initially I was confusd by the output since it just made up scenarios _The Matrix_. Looking through the file, I found the string used to prompt the model and get samples, changed it to the beginning of the flag format and got similar string. Looking at thte string, it looked like a simple ROT cypher, so I took it to [cyberchef](https://gchq.github.io/CyberChef/) and tried different offsets since it wasn't the standard ROT13. This yielded the flag.

# The nano GPT: Re

Similar to the other nanoGPT challenge, you had to load the model and data into nanoGPT to begin. I first loaded the model to find the correct folder to place the data into since the way this script works is that it takes an output directory from the model and reads it for metadata. Loading the model similarly to before an encrypted flag is provided. This time, you are provided with a decrypt script to decipher the flag. Looking at the challenge description, the bottom has the text **vgnr**, which if you're familiar with ciphers tells you that this is using a vigenere cipher. 

Through some slight modification of the python file provided, you can decipher the first four letters **'flag'** to the key **'behd'**. This is the point from which I could not advance. The first thing I tried was to brute force the key, but there were not any output with valid english words. Then I looked back to the challenge description, which mentioned that the key was the **'sum of logits'**. So I repurposed the `generate` function in the model class to output logits, which I then put through the `sum` function from pytorch. This sadly did not seem to provide a useful key, so I stopped here.

## What is missing

For this problem, I'm just missing the key, or confirmation of the key. I'm assuming now that I should have appened the letters relating to the numbers from the sum of logits, and submitted whatever came out.