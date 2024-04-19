# Longhorn 1

Entering this challenge, you are put on an imitation Windows XP desktop, with 4 windows open. One telling you that you need to enter the key from `keygen.exe`, which is another window open on the desktop in the form of a DOS terminal.The other two windows are another mock terminal and a space to enter text named `prompt`. Output from the model entered in to `prompt` is printed to the mock DOS prompt above it. Entering the key, or any text too short results in your prompt being immediately denied. With some sleuthing in the page javascript, you find that the flag is shown in another window when the server responds with the flag.

## Solution

I quickly determined that this was a prompt injection challenge. So through expirementation using the keywords **summarize**, **above**, **repeat**, and **key**, I managed to get the AI to print the key in the response. This opened the flag window as expected. 

![Longhorn 1](assets/longhorn1.png)

The screenshot does not use the same prompt as I used to initially get the flag, but something similar.

# Longhorn 2

Similar to the last challenge, this one uses the same UI and objective. One thing to note in this one, the activation key is the same as the one before. This AI seems a little more difficult to break than the last one though.

## Solution

![Longhorn 1](assets/longhorn2.png)

With some simple changes to my prompt from the last challenge, using the first part of the key, I was able to get the AI to finish it for me.

# Longhorn 3

This challenge was much harder than the last two, in this one, you had to find the key hidden in audio. However, there audio files are only slightly different. There didn't seem to be any steganographic message or anything hidden in the spectrogram. Looking at the binary  data, there were very few bytes different. The closest I got to getting the AI to print the key was getting it to leak the second part of the key by adding a hyphen to my last prompt. This confirmed my suspiscion that the activation key was the same for all three challenges, but I could not be sure. So, I was stuck here.