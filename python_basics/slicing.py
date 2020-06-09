text = "X-DSPAM-Confidence:    0.8475";

pos = text.find(':')
out=text[pos+2:]
b=float(out)
print(b)