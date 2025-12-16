from pathlib import Path


def listar_arquivos(caminho: Path):
    """_summary_

    Args:
        caminho (Path): caminho do arquivo

    Returns:
        (bool or dict, str): Sucesso da operação e mensagem descritiva.
    """
    if not caminho.exists():
        return False, 'O caminho não existe.'
    if not caminho.is_dir():
        return False, 'O caminho não é um diretório.'
    item = list(caminho.iterdir())
    if not item:
        return True, item
    else:
        return True, item 
      

def criar_arquivo(caminho: Path, nome_arquivo: str):
    """_summary_

    Args:
        caminho (Path): caminho do arquivo
        nome_arquivo (str): nome do arquivo

    Returns:
        (bool , str): Sucesso da operação e mensagem descritiva.
    """
    if not nome_arquivo.strip():
        return False, 'Nome do arquivo inválido.'
    
    if not caminho.exists():
        return False, 'O caminho informado não existe.'

    arquivo = caminho / nome_arquivo
    
    if arquivo.exists():
        return False, 'O arquivo já existe.'
    
    try:
        arquivo.touch()
        return True, f'Arquivo "{arquivo.name}" criado com sucesso.'
    except PermissionError:
        return False, 'Permissão negada ao criar o arquivo.'
    except OSError:
        return False, 'Erro do sistema ao criar o arquivo.'
    
    

def renomear_arquivo(caminho: Path, nome_atual: str, novo_nome: str):
    """_summary_

    Args:
        caminho (Path): caminho do arquivo
        nome_arquivo (str): nome do arquivo

    Returns:
        (bool , str): Sucesso da operação e mensagem descritiva.
    """
    if not caminho.exists():
        return False, 'O caminho selecionado não existe!'
    arquivo_a = caminho / nome_atual
    if not arquivo_a.exists():
        return False, 'O arquivo selecionado não existe.'
    arquivo_n = caminho / novo_nome
    if arquivo_n.exists():
        return False, 'O novo nome do arquivo já existe em outro. Digite um nome diferente!'
    try:
        arquivo_a.rename(arquivo_n)
        return True, f'Nome antigo -> "{nome_atual}" / Novo nome -> "{novo_nome}".'
    except Exception as e:
        return False, f'Não foi possível alterar o nome do arquivo!'
    if arquivo_a.is_dir():
        try:
            arquivo_a.rename(arquivo_n)
            return True, f'Nome antigo do diretóprio -> "{nome_atual}" / Novo nome do diretório -> "{novo_nome}".'
        except Exception as e:
            return False, f'Não foi possível alterar o nome do diretório!'
        
def remover_arquivo(caminho: Path, nome_arquivo: str):
    """_summary_

    Args:
        caminho (Path): Caminho do arquivo
        nome_arquivo (str): Nome do arquivo

    Returns:
         (bool, str): Sucesso da operação e mensagem descritiva.
    """
    if not caminho.exists():
        return False, 'O diretório escolhido não existe.'
    
    arquivo = caminho / nome_arquivo
    
    if not arquivo.exists():
        return False, 'O arquivo selecionado não existe.'
    
    if arquivo.is_file():
        try:
            arquivo.unlink()
            return True, f'Arquivo "{arquivo.name}" foi removido com sucesso!'
        except Exception as e:
            return False, f'Erro ao remover o arquivo. Tente novamente.'
    
    if arquivo.is_dir():
        item = list(arquivo.iterdir())
        if not item:
            try:
                arquivo.rmdir()
                return True,  f'O diretório "{arquivo.name}" está vazio e foi removido.'
            except Exception as e:
                return False, f'Não foi possível deletar o diretório. Tente novamente!'
        else:
            return False, f'O diretório "{arquivo.name}" contém itens.'
        
  

    





