import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk

# Constantes
API_OPTION_CHATGPT = "ChatGPT"
API_OPTION_LM_STUDIO = "LM Studio"
FORMAT_EPUB = "Epub"
FORMAT_PDF = "PDF"


def send_data():
    """Função para coletar e enviar os dados inseridos pelo usuário."""
    clear_log()
    data = {
        "name": entry_name.get(),
        "site": entry_site.get(),
        "start_chapter": entry_start_chapter.get(),
        "end_chapter": entry_end_chapter.get(),
        "chapters_per_file": entry_chapters_per_file.get(),
        "format_type": var_format.get(),
        "save_location": entry_save_location.get(),
        "has_metadata": metadata_var.get(),
        "selected_option": option_var.get(),
        "api_key": entry_api_key.get() if option_var.get() == API_OPTION_CHATGPT else ""
    }

    log("Enviando dados...")
    if data["selected_option"] == API_OPTION_CHATGPT and not data["api_key"]:
        log("Erro: A API Key não pode estar vazia quando a opção ChatGPT é selecionada.")
        return

    if not data["save_location"]:
        log("Por favor, insira o local de salvamento, ele não pode estar vazio.")
        return

    for key, value in data.items():
        if key == "api_key" and not value:
            return

        log(f'{key.capitalize().replace("_", " ")}: {value}')

    log("Dados enviados com sucesso!")


def select_directory():
    """Função para abrir o diálogo de seleção de diretório."""
    directory = filedialog.askdirectory()
    if directory:
        entry_save_location.delete(0, tk.END)
        entry_save_location.insert(0, directory)


def log(message):
    """Função para exibir mensagens de log na interface."""
    text_log.config(state=tk.NORMAL)
    text_log.insert(tk.END, message + "\n")
    text_log.config(state=tk.DISABLED)
    text_log.yview(tk.END)


def clear_log():
    """Função para limpar o log."""
    text_log.config(state=tk.NORMAL)
    text_log.delete(1.0, tk.END)
    text_log.config(state=tk.DISABLED)


def update_interface(event=None):
    """Função para atualizar a interface conforme a opção selecionada."""
    if option_var.get() == API_OPTION_CHATGPT:
        label_api_key.grid(column=0, row=1, padx=10, pady=5, sticky="W")
        entry_api_key.grid(column=1, row=1, padx=10, pady=5, sticky="EW")
    else:
        label_api_key.grid_remove()
        entry_api_key.grid_remove()


def validate_numeric_input(action, value_if_allowed):
    """Função para validar entradas numéricas."""
    return action != '1' or value_if_allowed.isdigit()


def create_interface():
    """Função para criar e configurar a interface gráfica."""
    global entry_api_key, entry_name, entry_site, entry_start_chapter, entry_end_chapter, entry_chapters_per_file, var_format, text_log, entry_save_location, metadata_var, option_var, label_api_key

    root = tk.Tk()
    root.title("Novel Downloader")
    root.geometry("510x550")
    root.resizable(False, False)

    # Seção de seleção de opção
    ttk.Label(root, text="Selecione a Opção:").grid(column=0, row=0, padx=10, pady=5, sticky="W")
    option_var = tk.StringVar(value=API_OPTION_CHATGPT)
    option_menu = ttk.Combobox(root, textvariable=option_var, values=[API_OPTION_CHATGPT, API_OPTION_LM_STUDIO], state="readonly")
    option_menu.grid(column=1, row=0, padx=10, pady=5, sticky="EW")
    option_menu.bind("<<ComboboxSelected>>", update_interface)

    # Labels e Entradas para API Key e Idioma da Novel
    label_api_key = ttk.Label(root, text="API Key:")
    entry_api_key = ttk.Entry(root, width=50)

    # Labels e Entradas para Nome e URL
    ttk.Label(root, text="Nome:").grid(column=0, row=3, padx=10, pady=5, sticky="W")
    entry_name = ttk.Entry(root, width=50)
    entry_name.grid(column=1, row=3, padx=10, pady=5, sticky="EW")

    ttk.Label(root, text="URL:").grid(column=0, row=4, padx=10, pady=5, sticky="W")
    entry_site = ttk.Entry(root, width=50)
    entry_site.grid(column=1, row=4, padx=10, pady=5, sticky="EW")

    # Validador para entrada numérica
    vcmd = (root.register(validate_numeric_input), '%d', '%P')

    # Labels e Entradas para Capítulos
    ttk.Label(root, text="Capítulo Inicial:").grid(column=0, row=5, padx=10, pady=5, sticky="W")
    entry_start_chapter = ttk.Entry(root, width=50, validate='key', validatecommand=vcmd)
    entry_start_chapter.grid(column=1, row=5, padx=10, pady=5, sticky="EW")

    ttk.Label(root, text="Capítulo Final:").grid(column=0, row=6, padx=10, pady=5, sticky="W")
    entry_end_chapter = ttk.Entry(root, width=50, validate='key', validatecommand=vcmd)
    entry_end_chapter.grid(column=1, row=6, padx=10, pady=5, sticky="EW")

    ttk.Label(root, text="Capítulos por Arquivo:").grid(column=0, row=7, padx=10, pady=5, sticky="W")
    entry_chapters_per_file = ttk.Entry(root, width=50, validate='key', validatecommand=vcmd)
    entry_chapters_per_file.grid(column=1, row=7, padx=10, pady=5, sticky="EW")

    # Checkbutton para Metadata
    ttk.Label(root, text="Opções:").grid(column=0, row=8, padx=10, pady=5, sticky="W")
    metadata_var = tk.BooleanVar()
    ttk.Checkbutton(root, text="Metadata", variable=metadata_var).grid(column=1, row=8, padx=10, pady=5, sticky="W")

    # Labels e Entrada para Local de Salvamento
    ttk.Label(root, text="Local de Salvamento:").grid(column=0, row=9, padx=10, pady=5, sticky="W")
    entry_save_location = ttk.Entry(root, width=50)
    entry_save_location.grid(column=1, row=9, padx=10, pady=5, sticky="EW")

    # Ícone de pasta para selecionar diretório
    image = Image.open("./files/images/folder_image.jpg")  # Substitua pelo caminho do seu ícone de pasta
    image = image.resize((20, 20))
    folder_icon = ImageTk.PhotoImage(image)
    label_icon = ttk.Label(root, image=folder_icon, cursor="hand2")
    label_icon.grid(column=2, row=9, padx=10, pady=5)
    label_icon.bind("<Button-1>", lambda event: select_directory())

    # Botões de rádio para selecionar formato
    var_format = tk.StringVar(value=FORMAT_EPUB)
    ttk.Radiobutton(root, text="Epub", variable=var_format, value=FORMAT_EPUB).grid(column=0, row=10, padx=10, pady=5, sticky="W")
    ttk.Radiobutton(root, text="PDF", variable=var_format, value=FORMAT_PDF).grid(column=1, row=10, padx=10, pady=5, sticky="W")

    # Área de log para exibir o progresso da aplicação
    text_log = tk.Text(root, height=10, state=tk.DISABLED)
    text_log.grid(column=0, row=11, columnspan=3, padx=10, pady=10, sticky="EW")

    # Botão de envio
    ttk.Button(root, text="Enviar", command=send_data).grid(column=0, row=12, columnspan=3, padx=10, pady=10, sticky="EW")

    # Configurar grade responsiva
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=0)  # Coluna do ícone não redimensiona

    root.rowconfigure(11, weight=1)  # Linha do texto redimensiona verticalmente

    # Inicializar a interface
    update_interface()

    # Executar a aplicação
    root.mainloop()


