import pygame
from random import randint

import input
import model_objects as mo
import vis
import time


def click_rect(event, x, y, delta_x, delta_y, size, width, height):
    """
    Функция определяет, является ли событие нажатием в области прямоугольника
    :param event: событие пайгейма
    :param x: абсцисса левого верхнего угла прямоугольника
    :param y: ордината
    :param delta_x: размер по абсциссе
    :param delta_y: размер по ординате
    :param size: число пикселей в одном квадратике
    :param width: ширина поля в пикселях
    :param height: высота поля в пикселях
    :return: True или False в зависимости от того является ли событие нажатием
    """
    if event.type == pygame.MOUSEBUTTONDOWN:
        if x * size * width <= event.pos[0] <= (x + delta_x) * size * width:
            if y * size * height <= event.pos[1] <= (y + delta_y) * size * height:
                return True
    return False


def start_display(event, size):
    """
    Функция начального экрана, которая позволяет выбрать одну из трех игровых локаций
    :param event: событие в пайгейме
    :param size: число пикселей в одном игровом квадратике
    :return: число от 1 до 3 - выбранный уровень или 0 если уровень не выбран
    """
    for number_button in range(0, 3, 1):
        if click_rect(event, (20 * number_button + 9) / 70, 1 / 3, 99 / 500, 1 / 9, size, mo.WIDTH, mo.HEIGHT):
            return number_button + 1
    return 0


def table_buttons(event, size):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (event.pos[0] - size * 15 * mo.WIDTH / 70) ** 2 + (event.pos[1] - size * 2 * mo.HEIGHT / 3) ** 2 <= (
                size * mo.HEIGHT / 10) ** 2:
            return 1
        elif (event.pos[0] - size * 35 * mo.WIDTH / 70) ** 2 + (event.pos[1] - size * 2 * mo.HEIGHT / 3) ** 2 <= (
                size * mo.HEIGHT / 10) ** 2:
            return 2
        elif (event.pos[0] - size * 55 * mo.WIDTH / 70) ** 2 + (event.pos[1] - size * 2 * mo.HEIGHT / 3) ** 2 <= (
                size * mo.HEIGHT / 10) ** 2:
            return 3
    return 0


def choice_display(event, size):
    """
    Функция определяет, какой уровень сложности выбрал пользователь
    :param event: событие в пайгейме
    :param size: число пикселей в одном игровом квадратике
    :return: если событие - это нажатие на одну из кнопок, то выводит, какая кнопка нажата
    """
    for number_button in range(0, 3, 1):
        if click_rect(event, 1 / 3, (1 + 2 * number_button) / 7, 1 / 3, 1 / 7, size, mo.WIDTH, mo.HEIGHT):
            return number_button + 1
    return 0


def update(event):
    """
    Проверка на закрытие программы
    :param event: пайгеймовский евент
    :return: True если евент был закрытие программы, иначе False
    """
    if event.type == pygame.QUIT:
        return True
    elif event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
        return True
    else:
        return False
