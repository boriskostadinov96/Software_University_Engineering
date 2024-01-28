def concatenate(*words, **kw):
    text = "".join(words)

    for key, value in kw.items():
        text = text.replace(key, value)

    return text


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))