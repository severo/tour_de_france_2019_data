# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re

def timestring_to_seconds(string, regexp):
    matches = re.match(regexp, string)
    seconds = 0
    if matches:
        groups = list(matches.groups())
        sec = groups.pop()
        if (sec):
            seconds += int(sec)
        min = groups.pop()
        if (min):
            seconds += int(min) * 60
        hours = groups.pop()
        if (hours):
            seconds += int(hours) * 3600
    return seconds

def parse_time(time):
    return timestring_to_seconds(time, "(?:([0-9]+)h )?(?:([0-9]+)' )?(?:([0-9]+)'')")

def parse_gap(gap):
    return timestring_to_seconds(gap, "\+ (?:([0-9]+)h )?(?:([0-9]+)' )?(?:([0-9]+)'')")

def parse_bonif(bonif):
    return timestring_to_seconds(bonif, "B : (?:([0-9]+)h )?(?:([0-9]+)' )?(?:([0-9]+)'')")

def parse_penal(penal):
    return timestring_to_seconds(penal, "P : (?:([0-9]+)h )?(?:([0-9]+)' )?(?:([0-9]+)'')")

def parse_stage(html):
    soup = BeautifulSoup(html, "lxml")

    rtable = soup.find("div", {"data-id": "rtable"})
    rows = rtable.table.tbody.findAll("tr")

    export_table = []

    for row in rows:
        cols = row.findAll('td')

        rank = cols[0].getText().strip()
        name = cols[1].a.getText().strip()
        number = cols[2].getText().strip()
        team = cols[3].a.getText().strip()
        time = cols[4].getText().strip()
        gap = cols[5].getText().strip()
        bonif = cols[6].getText().strip()
        penal = cols[7].getText().strip()

        raw = f"{rank}|{name}|{number}|{team}|{time}|{gap}|{bonif}|{penal}"

        export_table.append({
            'rank': int(rank),
            'name': name,
            'number': int(number),
            'team': team,
            'time': parse_time(time),
            'gap': parse_gap(gap),
            'bonif': parse_bonif(bonif),
            'penal': parse_penal(penal),
            'raw': raw
            })

    return export_table
