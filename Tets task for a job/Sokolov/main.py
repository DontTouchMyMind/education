import psycopg2

from node_structure import Node


def get_roots() -> list:
    return [list_nodes[i].name for i in range(len(list_nodes)) if list_nodes[i].level == 0]


def get_children(node: str) -> list:
    return [list_nodes[i].name for i in range(len(list_nodes)) if list_nodes[i].parent == node]


def get_tree(root: str) -> dict:
    subtree = []
    tree = {'name': root}
    for child in get_children(root):
        subtree.append(get_tree(child))
    tree['children'] = subtree
    return tree


def get_formatted_tree() -> list:
    return [get_tree(root) for root in get_roots()]


connection = psycopg2.connect(dbname='testdb', user='postgres', password='+', host='localhost')

list_nodes = []

try:
    with connection:
        with connection.cursor() as curs:
            curs.execute('SELECT * FROM myapp_tree ORDER BY sort')
            for entity in curs.fetchall():
                list_nodes.append(Node(*entity))
finally:
    connection.close()
