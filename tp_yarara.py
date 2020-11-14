#!/usr/bin/python
# -*- coding: utf-8 -*-
from menu import Menu

def main():
    menu = Menu()
    menu.ejecutar()
    target = menu.get_target()
    # scraper = Scraper()
    # scraper.buscar(target)

def out():
    print('Para volver a ejecutar ingrese: python tp_yarara.py')

if __name__ == '__main__':
    main()
    out()