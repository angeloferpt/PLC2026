import re
import sys


def inline_to_html(text):
    text = re.sub(r'!\[([^]]*)\]\(([^)]+)\)', r'<img src="\2" alt="\1"/>', text)
    text = re.sub(r'\[([^]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)
    return text


def markdown_to_html(markdown):
    html = []
    in_list = False

    for line in markdown.splitlines():
        item = re.match(r'^\d+\.\s+(.+)$', line)

        if item:
            if not in_list:
                html.append('<ol>')
                in_list = True

            html.append(f'<li>{inline_to_html(item.group(1))}</li>')
            continue

        if in_list:
            html.append('</ol>')
            in_list = False

        header = re.match(r'^(#{1,3})\s+(.+)$', line)

        if header:
            level = len(header.group(1))
            content = inline_to_html(header.group(2))
            html.append(f'<h{level}>{content}</h{level}>')
        else:
            html.append(inline_to_html(line))

    if in_list:
        html.append('</ol>')

    return '\n'.join(html)


def main():
    if len(sys.argv) != 2:
        print(f'Uso: python3 {sys.argv[0]} ficheiro.md')
        sys.exit(1)

    with open(sys.argv[1], 'r', encoding='utf-8') as file:
        markdown = file.read()

    print(markdown_to_html(markdown))


if __name__ == '__main__':
    main()
