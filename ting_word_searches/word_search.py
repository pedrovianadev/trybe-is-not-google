def exists_word(word, instance):
    """Aqui irá sua implementação"""
    result = list()

    for i in range(0, len(instance)):
        file = instance.search(i)
        occurrences = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": list()
        }

        for line, text in enumerate(file["linhas_do_arquivo"]):
            if word.casefold() in text.casefold():
                occurrences["ocorrencias"].append({
                    "linha": line + 1
                    })

        if len(occurrences["ocorrencias"]) > 0:
            result.append(occurrences)

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
