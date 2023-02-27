import requests
from pprint import pprint as print
from bs4 import BeautifulSoup


# url = f"https://namozvaqti.uz/shahar/{viloyat}"


def bugun(viloyat):
    url = f"https://namozvaqti.uz/shahar/{viloyat}"
    r = requests.get(url).text
    soup = BeautifulSoup(r, "html.parser")
    bugun = soup.select(".vil")[0].text
    return bugun


def hozirgi(viloyat):
    url = f"https://namozvaqti.uz/shahar/{viloyat}"
    r = requests.get(url).text
    soup = BeautifulSoup(r, "html.parser")
    bugun = soup.select(".current_time")[0].text
    return bugun


def bomdod(viloyat):
    url = f"https://namozvaqti.uz/shahar/{viloyat}"
    r = requests.get(url).text
    soup = BeautifulSoup(r, "html.parser")
    bugun = soup.select(".time")[0].text
    return bugun


def quyosh(viloyat):
    url = f"https://namozvaqti.uz/shahar/{viloyat}"
    r = requests.get(url).text
    soup = BeautifulSoup(r, "html.parser")
    bugun = soup.select(".time")[1].text
    return bugun


def peshin(viloyat):
    url = f"https://namozvaqti.uz/shahar/{viloyat}"
    r = requests.get(url).text
    soup = BeautifulSoup(r, "html.parser")
    bugun = soup.select(".time")[2].text
    return bugun


def asr(viloyat):
    url = f"https://namozvaqti.uz/shahar/{viloyat}"
    r = requests.get(url).text
    soup = BeautifulSoup(r, "html.parser")
    bugun = soup.select(".time")[3].text
    return bugun


def shom(viloyat):
    url = f"https://namozvaqti.uz/shahar/{viloyat}"
    r = requests.get(url).text
    soup = BeautifulSoup(r, "html.parser")
    bugun = soup.select(".time")[4].text
    return bugun


def xufton(viloyat):
    url = f"https://namozvaqti.uz/shahar/{viloyat}"
    r = requests.get(url).text
    soup = BeautifulSoup(r, "html.parser")
    bugun = soup.select(".time")[5].text
    return bugun



#
# print(f"bomdod: {bomdod('Toshkent')}")
# print(f"quyosh: {quyosh('Toshkent')}")
# print(f"peshin: {peshin('Toshkent')}")
# print(f"asr: {asr('Toshkent')}")
# print(f"shom: {shom('Toshkent')}")
# print(f"xufton: {xufton('Toshkent')}")


# print(f"bugun: {bugun('Toshkent')}")

