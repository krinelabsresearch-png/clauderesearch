"""Classifica il sito di ogni scheda (nessuno / social / portale / proprio) e prova i siti propri per trovare quelli rotti."""
import json, math, os, ssl, sys, urllib.request, concurrent.futures as cf
from urllib.parse import urlparse

DUOMO = (43.7731, 11.2560)
MAX_KM = 1.8
SOCIAL = ["facebook.", "fb.com", "fb.me", "instagram.", "linktr.ee", "tiktok.", "youtube.", "wa.me", "whatsapp.", "t.me", "linkin.bio", "beacons.ai"]
PORTALS = ["booking.", "tripadvisor.", "airbnb.", "miodottore.", "dottori.it", "idoctors.", "doctolib.", "paginegialle.",
           "paginebianche.", "prontopro.", "treatwell.", "uala.", "fresha.", "booksy.", "planity.", "houzz.", "instapro.",
           "habitissimo.", "starofservice.", "cylex", "misterimprese.", "virgilio.it", "tuttocitta.", "subito.it",
           "expedia.", "hotels.com", "linkedin.", "g.page", "google.com", "goo.gl", "maps.app", "guidapsicologi.",
           "psicologi-italia.", "paginesi.", "infobel.", "yelp.", "quandoo.", "thefork.", "getyourguide.", "viator.",
           "mynutritional.", "overplace.", "beb.it", "hotelsitalo.", "justeat.", "deliveroo.", "glovo", "ubereats.",
           "business.site", "wixsite.com/", "sumup.", "satispay.", "plateform.", "menu.", "jameda", "top-doctors.",
           "dottorionline", "ilmiodottore", "idealista.", "immobiliare.it", "casa.it", "wikipedia."]


def km(a, b):
    dy = (a[0] - b[0]) * 111.2
    dx = (a[1] - b[1]) * 111.2 * math.cos(math.radians(a[0]))
    return math.hypot(dx, dy)


def kind(u):
    if not u:
        return "nessuno"
    p = urlparse(u); h = (p.netloc + p.path[:40]).lower()
    if any(s in h for s in SOCIAL):
        return "social"
    if any(s in h for s in PORTALS):
        return "portale"
    return "proprio"


