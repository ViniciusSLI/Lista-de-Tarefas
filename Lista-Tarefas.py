class ToDoList:
    def __init__(self):
        # Inicializa a lista de tarefas vazia.
        self.tasks = []

    def add_task(self, task):
        # Adiciona uma nova tarefa à lista de tarefas.
        self.tasks.append({"task": task, "completed": False})

    def remove_task(self, task_index):
        # Remove uma tarefa da lista com base no índice fornecido.
        del self.tasks[task_index]

    def mark_task_completed(self, task_index):
        # Marca uma tarefa como concluída com base no índice fornecido.
        self.tasks[task_index]["completed"] = True

    def display_tasks(self):
        # Exibe todas as tarefas na lista junto com seu status (concluída ou pendente).
        if not self.tasks:
            print("Nenhuma tarefa na lista.")
        else:
            for index, task in enumerate(self.tasks):
                status = "Concluída" if task["completed"] else "Pendente"
                print(f"{index + 1}. {task['task']} - {status}")

def get_task_index(todo_list):
    # Função auxiliar para obter o índice da tarefa do usuário.
    while True:
        try:
            index = int(input("Digite o número da tarefa: ")) - 1
            if 0 <= index < len(todo_list.tasks):
                return index
            else:
                print("Número de tarefa inválido.")
        except ValueError:
            print("Por favor, insira um número válido.")

def main():
    todo_list = ToDoList()
    
    while True:
        print("\n===== Lista de Tarefas =====")
        print("1. Adicionar tarefa")
        print("2. Remover tarefa")
        print("3. Marcar tarefa como concluída")
        print("4. Mostrar tarefas")
        print("5. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            # Adiciona uma nova tarefa à lista.
            task = input("Digite a tarefa: ")
            todo_list.add_task(task)
            print("Tarefa adicionada com sucesso!")

        elif choice == "2":
            # Remove uma tarefa da lista, se houver.
            if todo_list.tasks:
                index = get_task_index(todo_list)
                todo_list.remove_task(index)
                print("Tarefa removida com sucesso!")
            else:
                print("Lista de tarefas vazia.")

        elif choice == "3":
            # Marca uma tarefa como concluída, se houver.
            if todo_list.tasks:
                index = get_task_index(todo_list)
                todo_list.mark_task_completed(index)
                print("Tarefa marcada como concluída com sucesso!")
            else:
                print("Lista de tarefas vazia.")

        elif choice == "4":
            # Exibe todas as tarefas na lista.
            todo_list.display_tasks()

        elif choice == "5":
            # Encerra o programa.
            print("Obrigado por usar a Lista de Tarefas. Até mais!")
            break

        else:
            # Exibe uma mensagem de erro se o usuário fornecer uma opção inválida.
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
