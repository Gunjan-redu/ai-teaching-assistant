


def chunk_documents(path) -> list[dict]:
    chunks = []
    buffer = []
    index = 0
    with open(path, 'r') as file:
        content = file.readlines()

        heading = None
        for line in content:

            if line.startswith("## "):
                heading  = line[3: ].strip()
            elif line.strip() == "":

                text = "".join(buffer).strip()
                if text:
                    chunks.append({
                        "chunk_index": index,
                        "heading": heading,
                        "text": text,
                        "doc": path,
                    })
                    index += 1  # inside the guard
                buffer = []


            else:
                buffer.append(line)

        merged = []
        for c in chunks:
            if c["text"].startswith("```") and merged:
                merged[-1]["text"] += "\n\n" + c["text"]
            else:
                merged.append(c)

        for i, c in enumerate(merged):
            c["chunk_index"] = i
    return merged

if __name__ == "__main__":
    for c in chunk_documents("documents/02_loops.md"):
        print(f"[{c['chunk_index']}] ({c['heading']}) {len(c['text'])} chars: {c['text'][:60]!r}")