"""########################################################################
# FILE : helpers.py
# WRITER : Joshua Herskowitz , jherskow , 321658379
# WRITER : Rachel Zilberberg, rachelz , 314421876                          # FILE : helpers.py
# EXERCISE : intro2cs ex9 2016-2017
# DESCRIPTION:
#######################################################################"""
import math

# ============ helper functions ===========================================

# ===== constants =====
STRAIT_DEG = 180
PI = math.pi()


# ===== Space_objects methods =========

def deg_to_radian(degs):
    """converts degrees to radians"""
    return (deg * PI) / STRAIT_DEG


def get_random_pos():
    """returns a random pos lol wut did u think """