from contacts_analyzer import contacts_analyzer, output
from time import time_ns


if __name__ == "__main__":
    ca = contacts_analyzer()

    # Exercício 01
    starttime = time_ns()
    ca.build_data("/res/sample")
    endtime = time_ns()
    print(f"{(endtime - starttime) / 1000000000:.2f}s")
    output(ca, path="/out", filename="exer01.txt")

    # Exercício 02
    starttime = time_ns()
    info = f"Ordem: {ca.amount_contacts()}\nTamanho: {ca.amount_messages()}\n"
    info += "\n\n20 indivíduos com maiores graus de saída:\n"
    info += "\n".join([f"{sender}: {sent_messages}" for sender, sent_messages in ca.biggest_senders(20, unique_receivers=True)])
    info += "\n\n20 indivíduos com maiores graus de entrada:\n"
    info += "\n".join([f"{receiver}: {received_messages}" for receiver, received_messages in ca.biggest_receivers(20, unique_senders=True)])
    endtime = time_ns()
    print(f"{(endtime - starttime) / 1000000000:.2f}s")
    output(info, path="/out", filename="exer02.txt")

    # Exercício 03
    starttime = time_ns()
    result = ca.is_contacts_graph_eulerian()
    info = f"O grafo é Euleriano?\n{'Sim' if result[0] else 'Não'}\n"
    info += "\nMotivos (se não for Euleriano):\n" + ";\n".join(result[1]) + "."
    endtime = time_ns()
    print(f"{(endtime - starttime) / 1000000000:.2f}s")
    output(info, path="/out", filename="exer03.txt")

    # Exercício 04
    starttime = time_ns()
    info = "Caminho: daniel.muschar@enron.com > james.derrick@enron.com\n"
    info += "\n".join(ca.get_path_between_contacts("daniel.muschar@enron.com", "james.derrick@enron.com"))
    endtime = time_ns()
    print(f"{(endtime - starttime) / 1000000000:.2f}s")
    output(info, path="/out", filename="exer04.txt")

    # Exercício 05
    starttime = time_ns()
    info = "Contatos próximos \"daniel.muschar@enron.com\":\n"
    info += "\n".join(ca.get_near_contacts("daniel.muschar@enron.com", 20))
    endtime = time_ns()
    print(f"{(endtime - starttime) / 1000000000:.2f}s")
    output(info, path="/out", filename="exer05.txt")

    # Exercício 06
    starttime = time_ns()
    result = ca.get_diameter()
    info = "Diâmetro:\n"
    info += "\n".join(result[0]) + "\n" + str(result[1])
    endtime = time_ns()
    print(f"{(endtime - starttime) / 1000000000:.2f}s")
    output(info, path="/out", filename="exer06.txt")
