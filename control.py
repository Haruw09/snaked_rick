import pygame
from random import randint

import input
import model_objects as mo
import vis
import time
from math import hypot


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
    :return: True или False в зависимости от того является ли событие нажатием по кнопке
    """
    if event.type == pygame.MOUSEBUTTONDOWN:
        if 0 <= event.pos[0] / size / width - x <= delta_x and 0 <= event.pos[1] / size / height - y <= delta_y:
            return True
    return False


def click_circle(event: pygame.event, x, y, r, size, width, height):
    """
    Функция определяет, является ли событие нажатием в области окружности
    :param event: событие пайгейма
    :param x: абсцисса левого верхнего угла прямоугольника
    :param y: ордината
    :param r: радиус кнопки
    :param size: число пикселей в одном квадратике
    :param width: ширина поля в пикселях
    :param height: высота поля в пикселях
    :return: True или False в зависимости от того является ли событие нажатием по кнопке
    """
    if event.type == pygame.MOUSEBUTTONDOWN:
        if hypot(x - event.pos[0] / size / width, y - event.pos[1] / size / height) <= r:
            return True
    return False


def start_display(event, size):
    """
    Функция начального экрана, которая позволяет выбрать одну из трех игровых локаций
    :param event: событие в пайгейме
    :param size: число пикселей в одном игровом квадратике
    :return: число от 1 до 3 - выбранный уровень или 0 если уровень не выбран
    """
    for number_button in range(1, 4):
        if click_rect(event, (20 * number_button - 11) / 70, 1 / 3, 99 / 500, 1 / 9, size, mo.WIDTH, mo.HEIGHT):
            return number_button
    return 0


def table_buttons(event, size):
    for i in range(1, 4):
        if click_circle(event, (-5 + 20 * i) / 70, 2 / 3, 1 / 10, size, mo.WIDTH, mo.HEIGHT):
            return i
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


def update(event: pygame.event):
    """
    Проверка на закрытие программы
    :param event: пайгеймовский евент
    :return: True если евент был закрытие программы, иначе False
    """
    if event.type == pygame.QUIT:
        return True
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        return True
    else:
        return False
