import markovify
num_sentances = 5
with open("shakespeare.txt") as f:
    text = f.read()
text_model = markovify.Text(text)
output = " ".join(text_model.make_sentence() for i in range(5))
print(output)