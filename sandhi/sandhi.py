#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Hrishikesh Terdalkar (hrishikeshrt.samskrit@gmail.com)
Form sandhi based on ashtAdhyAyI rules

Perl Source:
    Samsaadhanii Git
    (Commit: 4c9331a53059d3153f97e46e949decc755749180)
"""

###############################################################################
#  Copyright for the Perl-based implementation
#
#  Copyright (C) 2002-2006 Sushama Vempati
#  Copyright (C) 2002-2012 Amba Kulkarni (ambapradeep@gmail.com)
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either
#  version 2 of the License, or (at your option) any later
#  version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
###############################################################################

import re

from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate as tl

###############################################################################

from .apavaada import apavAdaniyamAH
from .niyama import RULES

###############################################################################

DEBUG = False

# Headers

pra = "praWamapaxam"
dvi = "xviwIyapaxam"
sam = "saMhiwapaxam"
sa = "sanXiH"
sut = "sUwram/vArwikam"
pra1 = "prakriyA"

###############################################################################


class Sandhi:
    def __init__(self, rules=RULES):
        self.rules = rules

    def _wx_sandhi(self, first, second):
        complete = first + "+" + second
        ans, ans1, ans2, cont = apavAdaniyamAH(complete)

        if DEBUG:
            print(f"ans from apavAda niyama = {ans}\n")

        if cont == 1:
            m = re.search("^(.*)(.)$", first)
            f_rem1 = m.group(1) if m else ""
            lf1 = m.group(2) if m else ""

            m = re.search("^(.*)(..)$", first)
            f_rem2 = m.group(1) if m else ""
            lf2 = m.group(2) if m else ""

            m = re.search("^(.)(.*)$", second)
            sf = m.group(1) if m else ""
            s_rem = m.group(2) if m else ""

            srch_str1 = f"{lf1},{sf}"
            srch_str2 = f"{lf2},{sf}"

            if DEBUG:
                print(f"srch_str1={srch_str1}")
            if DEBUG:
                print(f"srch_str2={srch_str2}")

            for rule in self.rules:
                if DEBUG:
                    print(f"rule={rule}")

                m = re.search("^" + srch_str1 + ",([^,]+),", rule)
                if m:
                    sandhi = m.group(1)
                    rule2 = rule.replace('"', "").split(",")
                    Sakya_uwwaras = sandhi.split("/")
                    for Sakya_uwwara in Sakya_uwwaras:
                        Sakya_uwwara = Sakya_uwwara.replace(" ", "  ")
                        an = f"{f_rem1}{Sakya_uwwara}{s_rem}"
                        ans = f"{ans}:{an}"
                        an1 = rule2[3]  # + "-sanXiH"
                        ans1 = f"{ans1}:{an1}"
                        an2 = rule2[4]
                        ans2 = f"{ans2}:{an2}"
                else:
                    m = re.search("^" + srch_str2 + ",([^,]+),", rule)
                    if m:
                        sandhi = m.group(1)
                        rule2 = rule.replace('"', "").split(",")
                        Sakya_uwwaras = sandhi.split("/")
                        for Sakya_uwwara in Sakya_uwwaras:
                            Sakya_uwwara = Sakya_uwwara.replace(" ", "  ")
                            an = f"{f_rem2}{Sakya_uwwara}{s_rem}"
                            ans = f"{ans}:{an}"
                            an1 = rule2[3]  # + "-sanXiH"
                            ans1 = f"{ans1}:{an1}"
                            an2 = rule2[4]
                            ans2 = f"{ans2}:{an2}"

            if ans != "":
                result = [ans, ans1, ans2]
                # , pra, dvi, sam, sa, sut, pra1]
            else:
                result = [f"{first}{second}", second, ""]
                # , pra, dvi, sam, sa, sut, pra1]
        else:
            ans = f":{ans}"
            ans1 = f":{ans1}-sanXiH"
            ans2 = f":{ans2}"
            result = [ans, ans1, ans2]
            # , pra, dvi, sam, sa, sut, pra1]

        return result

    def sandhi(self, w1, w2, input_scheme=sanscript.DEVANAGARI):
        wx_w1 = tl(w1, input_scheme, sanscript.WX)
        wx_w2 = tl(w2, input_scheme, sanscript.WX)

        answers = self._wx_sandhi(wx_w1, wx_w2)

        formed_sandhis = answers[0].split(":")
        sandhi_types = answers[1].split(":")
        sutras = answers[2].split(":")

        answers = []

        for idx, answer in enumerate(formed_sandhis):
            answer = answer.replace("><", "__").replace("Z", "'")
            answer = tl(answer, sanscript.WX, input_scheme)
            answer = answer.replace("__", "><")

            if len(sandhi_types) > idx:
                sandhi_type = sandhi_types[idx]
                sandhi_type = sandhi_type.replace("><", "__").replace("Z", "'")
                sandhi_type = tl(sandhi_type, sanscript.WX, input_scheme)
                sandhi_type = sandhi_type.replace("__", "><")
            else:
                sandhi_type = ""

            if len(sutras) > idx:
                sutra = sutras[idx]
                sutra = sutra.replace("><", "__").replace("Z", "'")
                sutra = tl(sutra, sanscript.WX, input_scheme)
                sutra = sutra.replace("__", "><")
            else:
                sutra = ""

            # string non-empty
            if answer:
                answers.append([answer, sutra, sandhi_type])

        return answers

    def __repr__(self):
        return f"{self.__class__.__name__}({len(self.rules)} rules)"


###############################################################################
