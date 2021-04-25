import pytest
from main import *

def test_create_bd():
    expected =[
        "Tabla creada",
        "La tabla ya existe"
    ]
    assert create_bd() in expected

def test_create_json():
    create_json()
    with open('data.json') as file:
        data_out = file.read()

def test_search_region():
    expected =[
        "Asia",
        "Europe",
        "Africa",
        "Oceania",
        "Americas",
        "Polar",
        ""
    ]
    assert search_region()[0] == expected[0]

def test_search_country():
    expected =[
        "American Samoa",
        "Australia",
        "Christmas Island",
        "Cocos (Keeling) Islands",
        "Cook Islands",
        "Fiji",
        "French Polynesia",
        "Guam",
        "Kiribati",
        "Marshall Islands",
        "Micronesia (Federated States of)",
        "Nauru",
        "New Caledonia",
        "New Zealand",
        "Niue",
        "Norfolk Island",
        "Northern Mariana Islands",
        "Palau",
        "Papua New Guinea",
        "Pitcairn",
        "Samoa",
        "Solomon Islands",
        "Tokelau",
        "Tonga",
        "Tuvalu",
        "Vanuatu",
        "Wallis and Futuna"
    ]
    assert search_country("oceania") in expected

def test_search_language():
    assert search_language("France") == "French"