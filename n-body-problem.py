#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 09:53:28 2022

@author: Ludmilla ALLARD

Écrire un programme permettant, à partir d'une condition initiale donnée (masses, vitesses et positions
de toutes les particules), de déterminer le positions et vitesses à un instant t quelconque

Partie préliminaire : modélisation du mouvement de la Lune autour de la Terre
"""

import numpy as np

r = 384400  # distance des centres de masse Terre/Lune en km
m_T = 5,972*10**24  # masse Terre en kg
m_L = 7,6342*10**22 # masse Lune en kg

T = 27*24   # periode de revolution de la Lune en heure


