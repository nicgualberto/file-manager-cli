import argparse
from pathlib import Path
from file_manager import (
    listar_arquivos, 
    criar_arquivo, 
    renomear_arquivo, 
    remover_arquivo
)


def main():
    parse = argparse.ArgumentParser(description='Gerenciador de Arquivos - CLI')
    
    subparsers = parse.add_subparsers(dest='comando', required=True)
    
    listar = subparsers.add_parser('listar', help='Listar arquivos')
    listar.add_argument('caminho', type=Path)
    
    criar = subparsers.add_parser('criar', help='Criar um novo arquivo')
    criar.add_argument('caminho', type=Path)
    criar.add_argument('nome_arquivo')
    
    renomear = subparsers.add_parser('renomear', help='Renomear um arquivo')
    renomear.add_argument('caminho', type=Path)
    renomear.add_argument('nome_atual')
    renomear.add_argument('novo_nome')
    
    remover = subparsers.add_parser('remover', help='Remover arquivo')
    remover.add_argument('caminho', type=Path)
    remover.add_argument('nome_arquivo')
    

    args = parse.parse_args()
    
    if args.comando == 'listar':
        sucesso, msg = listar_arquivos(args.caminho)
    
    elif args.comando == 'criar':
        sucesso, msg = criar_arquivo(args.caminho, args.nome_arquivo)
    
    elif args.comando == 'renomear':
        sucesso, msg = renomear_arquivo(
            args.caminho, args.nome_atual, args.novo_nome
        )

    
    elif args.comando == 'remover':
        sucesso, msg = remover_arquivo(args.caminho, args.nome_arquivo)
        
    
    print(msg)
    

if __name__== '__main__':
    main()