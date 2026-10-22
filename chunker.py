


def chunk_documents(path) -> list[dict]:
    chunks = []
    buffer = []
    index = 0
    with open(path, 'r') as file:
        content = file.readlines()


        for line in content:

            if line.startswith("## "):
                heading  = line
            elif line.strip() == "":
                index += 1
                chunks.append({
                    "chunk_index" : index,
                    "heading": heading,
                    "text": "".join(buffer).strip()
                })
                buffer = []
                heading = ""
            else:
                buffer.append(line)
    return chunks


if __name__== "__main__":
    print(chunk_documents("documents/01_variables.md"))