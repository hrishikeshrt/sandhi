#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Hrishikesh Terdalkar (hrishikeshrt.samskrit@gmail.com)

Perl Source:
    Samsaadhanii Git (sandhi/apavAxa_any.pl)
    (Commit: 4c9331a53059d3153f97e46e949decc755749180)
"""

###############################################################################
#  Copyright for the Perl-based implementation
#
#  Copyright (C) 2002-2012 Pankaj Vyays
#  Copyright (C) 2002-2012 Sivaja Nair
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

###############################################################################


def apavAdaniyamAH(s):
    ans = ''
    ans1 = ''
    ans2 = ''
    found = 0
    cont = 1
    first, second = s.split('+', 1)

    if False:
        # `second` is "Af"
        m = re.search(r"^(.*)[aA]\+(.*)", s)
        if m:
            ans = f"{m.group(1)}{m.group(2)}"
            ans1 = "pararUpa"
            ans2 = "omAfoSca(6.1.95)"
            cont = 0
        # TODO: show morph analysis in a tooltip
    else:
        if False:
            # `first` ends in I, U or e
            if False:
                # dvivachana
                found = 1

        if found:
            ans = "*" + first + " " + second
            ans1 = "pragqhya"
            ans2 = "IxUxexxvivacanam pragqhyam (1.1.11)-> pluwapragqhyA aci niwyam (6.1.125); $first paxasya xvivacana viSleRaNam aXikqwya";
            cont = 1

        m = re.search(r"^akRa\+Uhin(.*)", s)
        if m:
            ans = f"akROhiN{m.group(1)}"
            ans1 = "vqxXi"
            ans2 = "akRAxUhinyAmupasaMKyAnam (vA 3604)"
            cont = 0

        # if (an eq f"akRa+UhinI"){ans = akROhiNI;
        m = re.search(r"^sva\+Irin(.*)", s)
        if m:
            ans = f"svErin{m.group(1)}"
            ans1 = "vqxXi"
            ans2 = "svAxIreriNoH (vA 3606)"
            cont = 0

        m = re.search(r"^sva\+IraH", s)
        if m:
            ans = "svEraH"
            ans1 = "vqxXi"
            ans2 = "svAxIreriNoH (vA 3606)"
            cont = 0

        m = re.search(r"^sva\+IriN(.*)", s)
        if m:
            ans = f"svEriN{m.group(1)}"
            ans1 = "vqxXi"
            ans2 = "svAxIreriNoH (vA 3606)"
            cont = 0

        m = re.search(r"^pra\+Uh(.*)", s)
        if m:
            ans = f"prOh{m.group(1)}"
            ans1 = "vqxXi"
            ans2 = "prAxUhoDoDyeRERyeRu (vA 3605)"
            cont = 0

        m = re.search(r"^pra\+UD(.*)", s)
        if m:
            ans = f"prOD{m.group(1)}"
            ans1 = "vqxXi"
            ans2 = "prAxUhoDoDyeRERyeRu (vA 3605)"
            cont = 0

        m = re.search(r"^pra\+eRy(.*)", s)
        if m:
            ans = f"prERy{m.group(1)}"
            ans1 = "vqxXi"
            ans2 = "prAxUhoDoDyeRERyeRu (vA 3605)"
            cont = 0

        m = re.search(r"^pra\+eR(.*)", s)
        if m:
            ans = f"prER{m.group(1)}"
            ans1 = "vqxXi"
            ans2 = "prAxUhoDoDyeRERyeRu (vA 3605)"
            cont = 0

        m = re.search(r"^pra\+qN(.*)", s)
        if m:
            ans = f"prArN{m.group(1)}"
            ans1 = "vqxXi"
            ans2 = "pravawsawarakambalavasanArNaxaSAnAmqNe (vA 3608-9)"
            cont = 0

        else:
            m = re.search(r"^pra\+q(.*)", s)
            if m:
                ans = f"prAr{m.group(1)}"
                ans1 = "vqxXi"
                ans2 = "upasargAxqwi XAwoH (6.1.91)"
                cont = 0

        m = re.search(r"^vawsawara\+qN(.*)", s)
        if m:
            ans = f"vawsawarArN{m.group(1)}"
            ans1 = "vqxXi"
            ans2 = "pravawsawarakambalavasanArNaxaSAnAmqNe (vA 3608-9)"
            cont = 0

        m = re.search(r"^kambala\+qN(.*)", s)
        if m:
            ans = f"kambalArN{m.group(1)}"
            ans1 = "vqxXi"
            ans2 = "pravawsawarakambalavasanAqNaxaSAnAmqNe (vA 3608-9)"
            cont = 0

        m = re.search(r"^vasana\+qN(.*)", s)
        if m:
            ans = f"vasanArN{m.group(1)}"
            ans1 = "vqxXi"
            ans2 = "pravawsawarakambalavasanAqNaxaSAnAmqNe (vA 3608-9)"
            cont = 0

        m = re.search(r"^qNa\+qN(.*)", s)
        if m:
            ans = f"qNArN{m.group(1)}"
            ans1 = "vqxXi"
            ans2 = "pravawsawarakambalavasanAqNaxaSAnAmqNe (vA 3608-9)"
            cont = 0

        m = re.search(r"^xaSa\+qN(.*)", s)
        if m:
            ans = f"xaSArN{m.group(1)}"
            ans1 = "vqxXi"
            ans2 = "pravawsawarakambalavasanArNaxaSAnAmqNe (vA 3608-9)"
            cont = 0

        m = re.search(r"(.*)o\+yam$", s)
        if m:
            ans = f"{m.group(1)}avyam"
            ans1 = "vAnwa"
            ans2 = "vAnwo yi prawyaye (6.1.79)"
            cont = 0

        m = re.search(r"(.*)O\+yam$", s)
        if m:
            ans = f"{m.group(1)}Avyam"
            ans1 = "vAnwa"
            ans2 = "vAnwo yi prawyaye (6.1.79)"
            cont = 0

        m = re.search(r"^go\+yUw(.*)", s)
        if m:
            ans = f"gavyUw{m.group(1)}"
            ans1 = "vAnwa"
            ans2 = "aXvaparimANe ca (vA 3544)"
            cont = 0

        m = re.search(r"^Saka\+anXuH$", s)
        if m:
            ans = "SakanXuH"
            ans1 = "pararUpa"
            ans2 = "SakanXvAxiRu pararUpam vAcyam (vA 3632)"
            cont = 0

        m = re.search(r"^karka\+anXuH$", s)
        if m:
            ans = "karkanXuH"
            ans1 = "pararUpa"
            ans2 = "SakanXvAxiRu pararUpam vAcyam (vA 3632)"
            cont = 0

        m = re.search(r"^kula\+atA$", s)
        if m:
            ans = "kulatA"
            ans1 = "pararUpa"
            ans2 = "SakanXvAxiRu pararUpam vAcyam (vA 3632)"
            cont = 0

        m = re.search(r"^hala\+IRA$", s)
        if m:
            ans = "halIRA"
            ans1 = "pararUpa"
            ans2 = "SakanXvAxiRu pararUpam vAcyam (vA 3632)"
            cont = 0

        m = re.search(r"^lAfgala\+IRA$", s)
        if m:
            ans = "lAfgalIRA"
            ans1 = "pararUpa"
            ans2 = "SakanXvAxiRu pararUpam vAcyam (vA 3632)"
            cont = 0

        m = re.search(r"^mArwa\+aNdaH$", s)
        if m:
            ans = "mArwaNdaH"
            ans1 = "pararUpa"
            ans2 = "SakanXvAxiRu pararUpam vAcyam (vA 3632)"
            cont = 0

        m = re.search(r"^sIman\+anwaH$", s)
        if m:
            ans = "sImanwaH"
            ans1 = "pararUpa"
            ans2 = "sImanwaH keSaveSe (vA 3633)"
            cont = 0

        m = re.search(r"^sAra\+afg(.*)", s)
        if m:
            ans = f"sArafg{m.group(1)}"
            ans1 = "pararUpa"
            ans2 = "sArafgaH paSupakRiNoH (gaNa sUwram 136)"
            cont = 0

        m = re.search(r"^manas\+IRA$", s)
        if m:
            ans = "manIRA"
            ans1 = "pararUpa"
            ans2 = "SakanXvAxiRu pararUpam vAcyam (vA 3632)"
            cont = 0

        m = re.search(r"^pawaw\+aFjaliH$", s)
        if m:
            ans = "pawaFjaliH"
            ans1 = "pararUpa"
            ans2 = "SakanXvAxiRu pararUpam vAcyam (vA 3632)"
            cont = 0

        m = re.search(r"(.*)([aA])\+owuH", s)
        if m:
            ans = f"{m.group(1)}owuH"
            ans1 = "pararUpa"
            ans2 = "owvoRTayoH samAse vA (vA 3634)"
            cont = 1

        # The following condition already exists in any_sandhi.pl Hence commented by Amba 13.10.2016
        # if(an=~/(.*)([aA])\+owuH/){ans =ans.":". f"{m.group(1)}OwuH"ans1 =ans1.":"."vqxXi"ans2 =ans2.":"."vqxXireci (6.1.88)"
        m = re.search(r"(.*)([aA])\+oRT(.*)", s)
        if m:
            ans = f"{m.group(1)}oRT{m.group(3)}"
            ans1 = "pararUpa"
            ans2 = "owvoRTayoH samAse vA (vA 3634)"
            cont = 1

        # The following condition already exists in any_sandhi.pl Hence commented by Amba 13.10.2016
        # if(an=~/(.*)([aA])\+oRT(.*)/){ans =ans.":". f"{m.group(1)}ORT{m.group(3)}"ans1 =ans1.":"."vqxXi"ans2 =ans2.":"."vqxXireci (6.1.88)"
        m = re.search(r"^kaH\+kaH$", s)
        if m:
            ans = "kaskaH"
            ans1 = "sakAra"
            ans2 = "kaskAxiRu ca (8.3.48)"
            cont = 0

        m = re.search(r"^kOwaH\+kuwaH$", s)
        if m:
            ans = "kOwaskuwaH"
            ans1 = "sakAra"
            ans2 = "kaskAxiRu ca (8.3.48)"
            cont = 0

        m = re.search(r"^BrAwuH\+puwraH$", s)
        if m:
            ans = "BrAwuRpuwraH"
            ans1 = "sakAra"
            ans2 = "kaskAxiRu ca (8.3.48)"
            cont = 0

        m = re.search(r"^SunaH\+karNaH$", s)
        if m:
            ans = "SunaskarNaH"
            ans1 = "sakAra"
            ans2 = "kaskAxiRu ca (8.3.48)"
            cont = 0

        m = re.search(r"^saxyaH\+kAlaH$", s)
        if m:
            ans = "saxyaskAlaH"
            ans1 = "sakAra"
            ans2 = "kaskAxiRu ca (8.3.48)"
            cont = 0

        m = re.search(r"^saxyaH\+krIH$", s)
        if m:
            ans = "saxyaskrIH"
            ans1 = "sakAra"
            ans2 = "kaskAxiRu ca (8.3.48)"
            cont = 0

        m = re.search(r"^sAxyaH\+kaH$", s)
        if m:
            ans = "sAxyaskaH"
            ans1 = "sakAra"
            ans2 = "kaskAxiRu ca (8.3.48)"
            cont = 0

        m = re.search(r"^kAMH\+kAn$", s)
        if m:
            ans = "kAMskAn"
            ans1 = "sakAra"
            ans2 = "kaskAxiRu ca (8.3.48)"
            cont = 0

        m = re.search(r"^sarpiH\+kuNdikA$", s)
        if m:
            ans = "sarpiRkuNdikA"
            ans1 = "sakAra"
            ans2 = "kaskAxiRu ca (8.3.48)"
            cont = 0

        m = re.search(r"^XanuH\+kapAlam$", s)
        if m:
            ans = "XanuRkapAlam"
            ans1 = "sakAra"
            ans2 = "kaskAxiRu ca (8.3.48)"
            cont = 0

        m = re.search(r"^bahiH\+palam$", s)
        if m:
            ans = "bahiRpalam"
            ans1 = "sakAra"
            ans2 = "kaskAxiRu ca (8.3.48)"
            cont = 0

        m = re.search(r"^barhiH\+palam$", s)
        if m:
            ans = "barhiRpalam"
            ans1 = "sakAra"
            ans2 = "kaskAxiRu ca (8.3.48)"
            cont = 0

        m = re.search(r"^yajuH\+pAwram$", s)
        if m:
            ans = "yajuRpAwram"
            ans1 = "sakAra"
            ans2 = "kaskAxiRu ca (8.3.48)"
            cont = 0

        m = re.search(r"^ayaH\+kAnwaH$", s)
        if m:
            ans = "ayaskAnwaH"
            ans1 = "sakAra"
            ans2 = "kaskAxiRu ca (8.3.48)"
            cont = 0

        m = re.search(r"^wamaH\+kANdaH$", s)
        if m:
            ans = "wamaskANdaH"
            ans1 = "sakAra"
            ans2 = "kaskAxiRu ca (8.3.48)"
            cont = 0

        m = re.search(r"^ayaH\+kANdaH$", s)
        if m:
            ans = "ayaskANdaH"
            ans1 = "sakAra"
            ans2 = "kaskAxiRu ca (8.3.48)"
            cont = 0

        m = re.search(r"^mexaH\+piNdaH$", s)
        if m:
            ans = "mexaspiNdaH"
            ans1 = "sakAra"
            ans2 = "kaskAxiRu ca (8.3.48)"
            cont = 0

        m = re.search(r"^BAH\+karaH$", s)
        if m:
            ans = "BAskaraH"
            ans1 = "sakAra"
            ans2 = "kaskAxiRu ca (8.3.48)"
            cont = 0

        m = re.search(r"^ahaH\+karaH$", s)
        if m:
            ans = "ahaskaraH"
            ans1 = "sakAra"
            ans2 = "kaskAxiRu ca (8.3.48)"
            cont = 0

        m = re.search(r"^namaH\+([kp].*)", s)
        if m:
            ans = f"namas{m.group(1)}"
            ans1 = "sakAra"
            ans2 = "namaspurasorgawyoH (8.3.40)"
            cont = 0

        m = re.search(r"^puraH\+([kp].*)", s)
        if m:
            ans = f"puras{m.group(1)}"
            ans1 = "sakAra"
            ans2 = "namaspurasorgawyoH (8.3.40)"
            cont = 0

        m = re.search(r"^wiraH\+([kp].*)", s)
        if m:
            ans = f"wiras{m.group(1)}"
            ans1 = "sakAra"
            ans2 = "wirasoZnyawarasyAm (8.3.42)"
            cont = 0

        m = re.search(r"^wiraH\+([kp].*)", s)
        if m:
            ans = ans + f":wiraH {m.group(1)}"
            ans1 = ans1 + ":sawwvABAve"
            ans2 = ans2 + ":wirasoZnyawarasyAm (8.3.42)"
            cont = 0

        m = re.search(r"^apa\+q(.*)", s)
        if m:
            ans = f"apAr{m.group(1)}"
            ans1 = "vqxXi"
            ans2 = "upasargAxqwi XAwoH(6.1.91)"
            cont = 0

        m = re.search(r"^ava\+q(.*)", s)
        if m:
            ans = f"avAr{m.group(1)}"
            ans1 = "vqxXi"
            ans2 = "upasargAxqwi XAwoH(6.1.91)"
            cont = 0

        m = re.search(r"^upa\+q(.*)", s)
        if m:
            ans = f"upAr{m.group(1)}"
            ans1 = "vqxXi"
            ans2 = "upasargAxqwi XAwoH(6.1.91)"
            cont = 0

        m = re.search(r"(.*)pra\+([eo].*)", s)
        if m:
            ans = f"{m.group(1)}pr{m.group(2)}"
            ans1 = "pararUpa"
            ans2 = "efi pararUpam (6.1.94)"
            cont = 0

        m = re.search(r"(.*[aAou])pa\+([eo].*)", s)
        if m:
            ans = f"{m.group(1)}p{m.group(2)}"
            ans1 = "pararUpa"
            ans2 = "efi pararUpam(6.1.94)"
            cont = 0

        m = re.search(r"(.*[aA])va\+([eo].*)", s)
        if m:
            ans = f"{m.group(1)}v{m.group(2)}"
            ans1 = "pararUpa"
            ans2 = "efi pararUpam(6.1.94)"
            cont = 0

        m = re.search(r"(.*)a\+(o[mzfFnN].*)", s)
        if m:
            ans = f"{m.group(1)}{m.group(2)}"
            ans1 = "pararUpa"
            ans2 = "omAfoSca(6.1.95)"
            cont = 0

        m = re.search(r"^go\+(a.*)", s)
        if m:
            ans = f"go {m.group(1)}"
            ans1 = "prakqwiBAva"
            ans2 = "sarvawra viBARA goH(6.1.122)"
            cont = 0

        m = re.search(r"^go\+a(.*)", s)
        if m:
            ans = ans + ":" + f"gavA{m.group(2)}"
            ans1 = ans1 + ":" + "avafAxeSa"
            ans2 = ans2 + ":" + "avaf sPotAyanasya(6.1.123)-> akaH savarNe xIrGaH (6.1.101)"
            cont = 1

        # The following condition already exists in any_sandhi.pl Hence commented by Amba 13.10.2016
        # if(an=~/^go\+a(.*)/){ans =ans.":"."goZ{m.group(1)}"ans1 =ans1.":"."pararUpa"ans2 =ans2.":"."efaH paxAnwAxawi (6.1.109)"
        m = re.search(r"^go\+([iI])(.*)", s)
        if m:
            ans = f"gave{m.group(2)}"
            ans1 = "avafAxeSa"
            ans2 = "avaf sPotAyanasya(6.1.123)-> Ax guNaH (6.1.87)"
            cont = 0

        m = re.search(r"^go\+([uU])(.*)", s)
        if m:
            ans = f"gavo{m.group(2)}"
            ans1 = "avafAxeSa"
            ans2 = "avaf sPotAyanasya(6.1.123)-> Ax guNaH (6.1.87)"
            cont = 0

        m = re.search(r"^go\+([qQ])(.*)", s)
        if m:
            ans = f"gavar{m.group(2)}"
            ans1 = "avafAxeSa"
            ans2 = "avaf sPotAyanasya(6.1.123)-> Ax guNaH (6.1.87)"
            cont = 0

        m = re.search(r"^go\+(L)(.*)", s)
        if m:
            ans = f"gaval{m.group(2)}"
            ans1 = "avafAxeSa"
            ans2 = "avaf sPotAyanasya(6.1.123)-> Ax guNaH (6.1.87)"
            cont = 0

        m = re.search(r"^go\+([eE])(.*)", s)
        if m:
            ans = f"gavE{m.group(2)}"
            ans1 = "avafAxeSa"
            ans2 = "avaf sPotAyanasya(6.1.123)-> Ax guNaH (6.1.87)"
            cont = 0

        m = re.search(r"^go\+([oO])(.*)", s)
        if m:
            ans = f"gavO{m.group(2)}"
            ans1 = "avafAxeSa"
            ans2 = "avaf sPotAyanasya(6.1.123)-> Ax guNaH (6.1.87)"
            cont = 0

        m = re.search(r"^go\+inxr(.*)", s)
        if m:
            ans = f"gavenxr{m.group(1)}"
            ans1 = "avafAxeSa"
            ans2 = "inxre ca(6.1.124)-> Ax guNaH (6.1.87)"
            cont = 0

        m = re.search(r"(.*)[tTdDN]\+nAm", s)
        if m:
            ans = f"{m.group(1)}NNAm"
            ans1 = "jaSwva-> RtuwvaniReXaH-> Nawva"
            ans2 = "JalAM jaSoZnwe # (8.2.39)-> RtunA RtuH # (8.4.41)[Rtuwve prApwe]-> na paxAnwAttoranAm # (8.4.42)-> anAmnavawinagarINAmiwi vAcyam(vA 5016)-> yaroZnunAsikeZnunAsiko vA (8.4.45)-> prawyaye BARAyAm niwyam (vA 5017)"
            cont = 0

        m = re.search(r"(.*)[tTdDN]\+navawi$", s)
        if m:
            ans = f"{m.group(1)}NNavawi"
            ans1 = "jaSwva-> RtuwvaniReXaH-> Nawva-> anunAsikawvam"
            ans2 = "JalAM jaSoZnwe # (8.2.39)-> RtunA RtuH # (8.4.41)[Rtuwve prApwe]-> na paxAnwAttoranAm # (8.4.42)-> anAmnavawinagarINAmiwi vAcyam(vA 5016)-> yaroZnunAsikeZnunAsiko vA (8.4.45)"
            cont = 1

        # The following condition already exists in any_sandhi.pl Hence commented by Amba 13.10.2016
        # if(an=~/(.*)[tTdD]\+navawi/){ans =ans.":". f"{m.group(1)}dNavawi"ans1 =ans1.":"."jaSwva-> RtuwvaniReXaH-> Nawva"ans2 =ans2.":"."JalAM jaSoZnwe # (8.2.39)-> RtunA RtuH # (8.4.41)[Rtuwve prApwe]-> na paxAnwAttoranAm # (8.4.42)-> anAmnavawinagarINAmiwi vAcyam(vA 5016)"

        m = re.search(r"(.*)[tTdDN]\+nagar(.*)", s)
        if m:
            ans = f"{m.group(1)}NNagar{m.group(2)}"
            ans1 = "jaSwva-> RtuwvaniReXaH-> Nawva-> anunAsikawvam"
            ans2 = "JalAM jaSoZnwe # (8.2.39)-> RtunA RtuH # (8.4.41)[Rtuwve prApwe]-> na paxAnwAttoranAm # (8.4.42)-> anAmnavawinagarINAmiwi vAcyam(vA 5016)-> yaroZnunAsikeZnunAsiko vA (8.4.45)"
            cont = 1


        # The following condition already exists in any_sandhi.pl Hence commented by Amba 13.10.2016
        # if(an=~/(.*)[tTdD]\+nagar(.*)/){ans =ans.":". f"{m.group(1)}dNagar{m.group(2)}"ans1 =ans1.":"."jaSwva->RtuwvaniReXaH->Nawva"ans2 =ans2.":"."JalAM jaSoZnwe # (8.2.39)->RtunA RtuH # (8.4.41)[Rtuwve prApwe]->na paxAnwAttoranAm # (8.4.42)->anAmnavawinagarINAmiwi vAcyam(vA 5016)"
        m = re.search(r"^amI\+(.*)", s)
        if m:
            ans = f"amI {m.group(1)}"
            ans1 = "prakqwiBAva"
            ans2 = "axaso mAw(1.1.12)"
            cont = 0

        m = re.search(r"^amU\+(.*)", s)
        if m:
            ans = f"amU {m.group(1)}"
            ans1 = "prakqwiBAva"
            ans2 = "axaso mAw(1.1.12)"
            cont = 0

        m = re.search(r"^uw\+sWA(.*)", s)
        if m:
            ans = f"uwWA{m.group(1)}"
            ans1 = "pUrvasavarNaH->lopaH"
            ans2 = "uxaH sWAswamBoH pUrvasya (8.4.61)->Jaro Jari savarNe (8.4.65)"
            cont = 0

        m = re.search(r"^uw\+sWA(.*)", s)
        if m:
            ans = ans + ":" + f"uwWWA{m.group(1)}"
            ans1 = ans1 + ":" + "pUrvasavarNaH->lopABAvaH"
            ans2 = ans2 + ":" + "uxaH sWAswamBoH pUrvasya (8.4.61)->Jaro Jari savarNe (8.4.65)"
            cont = 0

        m = re.search(r"^uw\+swamB(.*)", s)
        if m:
            ans = f"uwwamB{m.group(1)}"
            ans1 = "pUrvasavarNaH->lopaH"
            ans2 = "uxaH sWAswamBoH pUrvasya (8.4.61)->Jaro Jari savarNe (8.4.65)"
            cont = 0

        m = re.search(r"^uw\+swamB(.*)", s)
        if m:
            ans = ans + ":" + f"uwWwamB{m.group(1)}"
            ans1 = ans1 + ":" + "pUrvasavarNaH->lopABAvaH"
            ans2 = ans2 + ":" + "uxaH sWAswamBoH pUrvasya (8.4.61)->Jaro Jari savarNe (8.4.65)"
            cont = 0

        m = re.search(r"(.*)([kKgG])\+S([aAiIuUqQLeEoOhyvr])(.*)", s)
        if m:
            ans = f"{m.group(1)}kC{m.group(3)}{m.group(4)}"
            ans1 = "jaSwva->carwva->Cawva"
            ans2 = "JalAM jaSoZnwe (8.2.39)->Kari ca (8.4.55)->SaSCoZti (8.4.63)"
            cont = 1


        # The following condition already exists in any_sandhi.pl Hence commented by Amba 13.10.2016
        # if(an=~/(.*)([kKgG])\+S([aAiIuUqQLeEoOhyvr])(.*)/){ans =ans.":". f"{m.group(1)}kS{m.group(3)}{m.group(4)}"ans1 =ans1.":"."jaSwva->carwva->CawvABAva"ans2 =ans2.":"."JalAM jaSoZnwe (8.2.39)->Kari ca (8.4.55)"
        m = re.search(r"(.*)([cCjJ])\+S([aAiIuUqQLeEoOhyvr])(.*)", s)
        if m:
            ans = f"{m.group(1)}cC{m.group(3)}{m.group(4)}"
            ans1 = "jaSwva->carwva->Cawva"
            ans2 = "JalAM jaSoZnwe (8.2.39)->Kari ca (8.4.55)->SaSCoZti (8.4.63)"
            cont = 1

        # The following condition already exists in any_sandhi.pl Hence commented by Amba 13.10.2016
        # if(an=~/(.*)([cCjJ])\+S([aAiIuUqQLeEoOhyvr])(.*)/){ans =ans.":". f"{m.group(1)}cS{m.group(3)}{m.group(4)}"ans1 =ans1.":"."jaSwva->carwva->CawvABAva"ans2 =ans2.":"."JalAM jaSoZnwe (8.2.39)->Kari ca (8.4.55)"
        m = re.search(r"(.*)([tTdD])\+S([aAiIuUqQLeEoOhyvr])(.*)", s)
        if m:
            ans = f"{m.group(1)}tC{m.group(3)}{m.group(4)}"
            ans1 = "jaSwva->carwva->Cawva"
            ans2 = "JalAM jaSoZnwe (8.2.39)->Kari ca (8.4.55)->SaSCoZti (8.4.63)"
            cont = 1

        # The following condition already exists in any_sandhi.pl Hence commented by Amba 13.10.2016
        # if(an=~/(.*)([tTdD])\+S([aAiIuUqQLeEoOhyvr])(.*)/){ans =ans.":". f"{m.group(1)}tS{m.group(3)}{m.group(4)}"ans1 =ans1.":"."jaSwva->carwva->CawvABAva"ans2 =ans2.":"."JalAM jaSoZnwe (8.2.39)->Kari ca (8.4.55)"
        m = re.search(r"(.*)([wWxX])\+S([aAiIuUqQLeEoOhyvr])(.*)", s)
        if m:
            ans = f"{m.group(1)}cC{m.group(3)}{m.group(4)}"
            ans1 = "jaSwva->Scuwva->carwva->Cawva"
            ans2 = "JalAM jaSoZnwe (8.2.39)->swoH ScunA ScuH (8.4.40)->Kari ca (8.4.55)->SaSCoZti (8.4.63)"
            cont = 1


        # The following condition already exists in any_sandhi.pl Hence commented by Amba 13.10.2016
        # if(an=~/(.*)([wWxX])\+S([aAiIuUqQLeEoOhyvr])(.*)/){ans =ans.":". f"{m.group(1)}cS{m.group(3)}{m.group(4)}"ans1 =ans1.":"."jaSwva->Scuwva->carwva->CawvABAva"ans2 =ans2.":"."JalAM jaSoZnwe (8.2.39)->swoH ScunA ScuH (8.4.40)->Kari ca (8.4.55)"
        m = re.search(r"(.*)([pPbB])\+S([aAiIuUqQLeEoOhyvr])(.*)", s)
        if m:
            ans = f"{m.group(1)}pC{m.group(3)}{m.group(4)}"
            ans1 = "jaSwva->carwva->Cawva"
            ans2 = "JalAM jaSoZnwe (8.2.39)->Kari ca (8.4.55)->SaSCoZti (8.4.63)"
            cont = 1

        # The following condition already exists in any_sandhi.pl Hence commented by Amba 13.10.2016
        # if(an=~/(.*)([pPbB])\+S([aAiIuUqQLeEoOhyvr])(.*)/){ans =ans.":". f"{m.group(1)}pS{m.group(3)}{m.group(4)}"ans1 =ans1.":"."jaSwva->carwva->CawvABAva"ans2 =ans2.":"."JalAM jaSoZnwe (8.2.39)->Kari ca (8.4.55)"
        m = re.search(r"(.*)(n)\+S([aAiIuUqQLeEoOhyvr])(.*)", s)
        if m:
            ans = f"{m.group(1)}FC{m.group(3)}{m.group(4)}"
            ans1 = "wugAgama->Scuwva->carwva->Cawva->lopaH"
            ans2 = "Si wuk (8.3.31)->swoH ScunA ScuH (8.4.40)->Kari ca (8.4.55)->SaSCoZti (8.4.63)->Jaro Jari savarNe (8.4.65)"
            cont = 1

        m = re.search(r"(.*)(n)\+S([aAiIuUqQLeEoOhyvr])(.*)", s)
        if m:
            ans = ans + ":" + f"{m.group(1)}FcC{m.group(3)}{m.group(4)}"
            ans1 = ans1 + ":" + "wugAgama->Scuwva->carwva->Cawva->lopABAvaH"
            ans2 = ans2 + ":" + "Si wuk (8.3.31)->swoH ScunA ScuH (8.4.40)->Kari ca (8.4.55)->SaSCoZti (8.4.63)"
            cont = 1

        # if(an=~/(.*)(n)\+S([aAiIuUqQLeEoOhyvr])(.*)/){ans =ans.":". f"{m.group(1)}FcS{m.group(3)}{m.group(4)}"ans1 =ans1.":"."wugAgama->Scuwva->carwva->CawvABAvaH"ans2 =ans2.":"."Si wuk (8.3.31)->swoH ScunA ScuH (8.4.40)->Kari ca (8.4.55)"
        # if(an=~/(.*)(n)\+S([aAiIuUqQLeEoOhyvr])(.*)/){ans =ans.":". f"{m.group(1)}FS{m.group(3)}{m.group(4)}"ans1 =ans1.":"."Scuwva"ans2 =ans2.":"."swoH ScunA ScuH (8.4.40)"
        m = re.search(r"(.*)([kKgG])\+S([lfmFNn])(.*)", s)
        if m:
            ans = f"{m.group(1)}kC{m.group(3)}{m.group(4)}"
            ans1 = "jaSwva->carwva->Cawva"
            ans2 = "JalAM jaSoZnwe (8.2.39)->Kari ca (8.4.55)->CawvamamIwi vAcyam (vA 5025)"
            cont = 0

        m = re.search(r"(.*)([kKgG])\+S([lfmFNn])(.*)", s)
        if m:
            ans = ans + ":" + f"{m.group(1)}kS{m.group(3)}{m.group(4)}"
            ans1 = ans1 + ":" + f"jaSwva->carwva->CawvABAva"
            ans2 = ans2 + ":" + f"JalAM jaSoZnwe (8.2.39)->Kari ca (8.4.55)"
            cont = 0

        m = re.search(r"(.*)([cCjJ])\+S([lFmfNn])(.*)", s)
        if m:
            ans = f"{m.group(1)}cC{m.group(3)}{m.group(4)}"
            ans1 = "jaSwva->carwva->Cawva"
            ans2 = "JalAM jaSoZnwe (8.2.39)->Kari ca (8.4.55)->CawvamamIwi vAcyam (vA 5025)"
            cont = 0

        m = re.search(r"(.*)([cCjJ])\+S([lFmfNn])(.*)", s)
        if m:
            ans = ans + ":" + f"{m.group(1)}cS{m.group(3)}{m.group(4)}"
            ans1 = ans1 + ":" + "jaSwva->carwva->CawvABAva"
            ans2 = ans2 + ":" + "JalAM jaSoZnwe (8.2.39)->Kari ca (8.4.55)"
            cont = 0

        m = re.search(r"(.*)([tTdD])\+S([lFmfNn])(.*)", s)
        if m:
            ans = f"{m.group(1)}tC{m.group(3)}{m.group(4)}"
            ans1 = "jaSwva->carwva->Cawva"
            ans2 = "JalAM jaSoZnwe (8.2.39)->Kari ca (8.4.55)->CawvamamIwi vAcyam (vA 5025)"
            cont = 0

        m = re.search(r"(.*)([tTdD])\+S([lFmfNn])(.*)", s)
        if m:
            ans = ans + ":" + f"{m.group(1)}tS{m.group(3)}{m.group(4)}"
            ans1 = ans1 + ":" + "jaSwva->carwva->CawvABAva"
            ans2 = ans2 + ":" + "JalAM jaSoZnwe (8.2.39)->Kari ca (8.4.55)"
            cont = 0

        m = re.search(r"(.*)([wWxX])\+S([lFmfNn])(.*)", s)
        if m:
            ans = f"{m.group(1)}cC{m.group(3)}{m.group(4)}"
            ans1 = "jaSwva->Scuwva->carwva->Cawva"
            ans2 = "JalAM jaSoZnwe (8.2.39)->swoH ScunA ScuH (8.4.40)->Kari ca (8.4.55)->CawvamamIwi vAcyam (vA 5025)"
            cont = 0

        m = re.search(r"(.*)([wWxX])\+S([lFmfNn])(.*)", s)
        if m:
            ans = ans + ":" + f"{m.group(1)}cS{m.group(3)}{m.group(4)}"
            ans1 = ans1 + ":" + "jaSwva->Scuwva->carwva->CawvABAva"
            ans2 = ans2 + ":" + "JalAM jaSoZnwe (8.2.39)->swoH ScunA ScuH (8.4.40)->Kari ca (8.4.55)"
            cont = 0

        m = re.search(r"(.*)([pPbB])\+S([lfFmnN])(.*)", s)
        if m:
            ans = f"{m.group(1)}pC{m.group(3)}{m.group(4)}"
            ans1 = "jaSwva->carwva->Cawva"
            ans2 = "JalAM jaSoZnwe (8.2.39)->Kari ca (8.4.55)->CawvamamIwi vAcyam (vA 5025)"
            cont = 0

        m = re.search(r"(.*)([pPbB])\+S([lfFmnN])(.*)", s)
        if m:
            ans = ans + ":" + f"{m.group(1)}pS{m.group(3)}{m.group(4)}"
            ans1 = ans1 + ":" + "jaSwva->carwva->CawvABAva"
            ans2 = ans2 + ":" + "JalAM jaSoZnwe (8.2.39)->Kari ca (8.4.55)"
            cont = 0

        m = re.search(r"(.*)n\+([cC])([aAiIuUqQLeEoOhyvr])(.*)", s)
        if m:
            ans = f"{m.group(1)}zS{m.group(2)}{m.group(3)}{m.group(4)}"
            ans1 = "ruwva"
            ans2 = "naSCavyapraSAn (8.3.7)-> awrAnunAsikaH pUrvasya wu vA (8.3.2)-> KaravasAnayorvisarjanIyaH (8.3.15)-> visarjanIyasya saH (8.3.34)-> swoH ScunA ScuH (8.4.40)"
            cont = 0

        m = re.search(r"(.*)n\+([cC])([aAiIuUqQLeEoOhyvr])(.*)", s)
        if m:
            ans = ans + ":" + f"{m.group(1)}MS{m.group(2)}{m.group(3)}{m.group(4)}"
            ans1 = ans1 + ":" + "ruwva"
            ans2 = ans2 + ":" + "naSCavyapraSAn (8.3.7)->anunAsikAw paroZnusvAraH (8.3.4)->KaravasAnayorvisarjanIyaH (8.3.15)->visarjanIyasya saH (8.3.34)->swoH ScunA ScuH (8.4.40)"
            cont = 0

        m = re.search(r"(.*)n\+([tT])([aAiIuUqQLeEoOhyvr])(.*)", s)
        if m:
            ans = f"{m.group(1)}zR{m.group(2)}{m.group(3)}{m.group(4)}"
            ans1 = "ruwva"
            ans2 = "naSCavyapraSAn (8.3.7)->awrAnunAsikaH pUrvasya wu vA (8.3.2)->KaravasAnayorvisarjanIyaH (8.3.15)->visarjanIyasya saH (8.3.34)->RtunA RtuH (8.4.41)"
            cont = 0

        m = re.search(r"(.*)n\+([tT])([aAiIuUqQLeEoOhyvr])(.*)", s)
        if m:
            ans = ans + ":" + f"{m.group(1)}MR{m.group(2)}{m.group(3)}{m.group(4)}"
            ans1 = ans1 + ":" + "ruwva"
            ans2 = ans2 + ":" + "naSCavyapraSAn (8.3.7)->anunAsikAw paroZnusvAraH (8.3.4)->KaravasAnayorvisarjanIyaH (8.3.15)->visarjanIyasya saH (8.3.34)->RtunA RtuH (8.4.41)"
            cont = 0

        m = re.search(r"(.*)n\+([wW])([aAiIuUqQLeEoOhyvr])(.*)", s)
        if m:
            ans = f"{m.group(1)}zs{m.group(2)}{m.group(3)}{m.group(4)}"
            ans1 = "ruwva"
            ans2 = "naSCavyapraSAn (8.3.7)->awrAnunAsikaH pUrvasya wu vA (8.3.2)->KaravasAnayorvisarjanIyaH (8.3.15)->visarjanIyasya saH (8.3.34)"
            cont = 0

        m = re.search(r"(.*)n\+([wW])([aAiIuUqQLeEoOhyvr])(.*)", s)
        if m:
            ans = ans + ":" + f"{m.group(1)}Ms{m.group(2)}{m.group(3)}{m.group(4)}"
            ans1 = ans1 + ":" + "ruwva"
            ans2 = ans2 + ":" + "naSCavyapraSAn (8.3.7)->anunAsikAw paroZnusvAraH (8.3.4)->KaravasAnayorvisarjanIyaH (8.3.15)->visarjanIyasya saH (8.3.34)"
            cont = 0

        m = re.search(r"^praSAn\+([cC])([aAiIuUqQLeEoOhyvr])(.*)", s)
        if m:
            ans = f"praSAF{m.group(1)}{m.group(2)}{m.group(3)}"
            ans1 = "ruwvaniReXa->Scuwva"
            ans2 = "naSCavyapraSAn (8.3.7)-> swoH ScunA ScuH (8.4.40)"
            cont = 0

        m = re.search(r"^praSAn\+([tT])([aAiIuUqQLeEoOhyvr])(.*)", s)
        if m:
            ans = f"praSAN{m.group(1)}{m.group(2)}{m.group(3)}"
            ans1 = "ruwvaniReXa->Rtuwva"
            ans2 = "naSCavyapraSAn (8.3.7)-> RtunA RtuH (8.4.41)"
            cont = 0

        m = re.search(r"^praSAn\+([wW])([aAiIuUqQLeEoOhyvr])(.*)", s)
        if m:
            ans = f"praSAn{m.group(1)}{m.group(2)}{m.group(3)}"
            ans1 = "ruwvaniReXa"
            ans2 = "naSCavyapraSAn (8.3.7)"
            cont = 0

        m = re.search(r"^nQn\+p(.*)", s)
        if m:
            ans = f"nQz><p{m.group(1)}"
            ans1 = "ruwva"
            ans2 = "nQnpe (8.3.10)->awrAnunAsikaH pUrvasya wu vA (8.3.2)->KaravasAnayorvisarjanIyaH (8.3.15)->kupvoH><ka><pO ca (8.3.37)"
            cont = 0

        m = re.search(r"^nQn\+p(.*)", s)
        if m:
            ans = ans + ":" + f"nQM><p{m.group(1)}"
            ans1 = ans1 + ":" + "ruwva"
            ans2 = ans2 + ":" + "nQnpe (8.3.10)->anunAsikAw paroZnusvAraH (8.3.4)->KaravasAnayorvisarjanIyaH (8.3.15)->kupvoH><ka><pO ca (8.3.37)"
            cont = 0

        m = re.search(r"^nQn\+p(.*)", s)
        if m:
            ans = ans + ":" + f"nQzHp{m.group(1)}"
            ans1 = ans1 + ":" + "ruwva"
            ans2 = ans2 + ":" + "nQnpe (8.3.10)->awrAnunAsikaH pUrvasya wu vA (8.3.2)->KaravasAnayorvisarjanIyaH (8.3.15)->visarjanIyasya saH (8.3.34)"
            cont = 0

        m = re.search(r"^nQn\+p(.*)", s)
        if m:
            ans = ans + ":" + f"nQMHp{m.group(1)}"
            ans1 = ans1 + ":" + "ruwva"
            ans2 = ans2 + ":" + "nQnpe (8.3.10)->anunAsikAw paroZnusvAraH (8.3.4)->KaravasAnayorvisarjanIyaH (8.3.15)->visarjanIyasya saH (8.3.34)"
            cont = 0

        m = re.search(r"^nQn\+p(.*)", s)
        if m:
            ans = ans + ":" + f"nQnp{m.group(1)}"
            ans1 = ans1 + ":" + "ruwvABAve"
            ans2 = ans2 + ":" + "nQnpe (8.3.10)"
            cont = 0

        m = re.search(r"^kAn\+kAn$", s)
        if m:
            ans = "kAzskAn"
            ans1 = "ruwva"
            ans2 = "kAnAmrediwe (8.3.12)->awrAnunAsikaH pUrvasya wu vA (8.3.2)->KaravasAnayorvisarjanIyaH (8.3.15)->saMpuMkAnAM so vakwavyaH (vA 4892)"
            cont = 0

        m = re.search(r"^kAn\+kAn$", s)
        if m:
            ans = ans + ":" + "kAMskAn"
            ans1 = ans1 + ":" + "ruwva"
            ans2 = ans2 + ":" + "kAnAmrediwe (8.3.12)->anunAsikAw paroZnusvAraH (8.3.4)->KaravasAnayorvisarjanIyaH (8.3.15)->saMpuMkAnAM so vakwavyaH (vA 4892)"
            cont = 0

        m = re.search(r"pum\+([kKcCtTwWpP])([aAiIuUqQLeEoOhyvr])(.*)", s)
        if m:
            ans = f"puMs{m.group(1)}{m.group(2)}{m.group(3)}"
            ans1 = "ruwva"
            ans2 = "pumaH Kayyampare (8.3.6)->anunAsikAw paroZnusvAraH (8.3.4)->KaravasAnayorvisarjanIyaH (8.3.15)->saMpuMkAnAM so vakwavyaH (vA 4892)"
            cont = 0

        m = re.search(r"pum\+([kKcCtTwWpP])([aAiIuUqQLeEoOhyvr])(.*)", s)
        if m:
            ans = ans + ":" + f"puzs{m.group(1)}{m.group(2)}{m.group(3)}"
            ans1 = ans1 + ":" + "ruwva"
            ans2 = ans2 + ":" + "pumaH Kayyampare (8.3.6)->awrAnunAsikaH pUrvasya wu vA (8.3.2)->KaravasAnayorvisarjanIyaH (8.3.15)->saMpuMkAnAM so vakwavyaH (vA 4892)"
            cont = 0

        # if(an=~/(.*)([aAiIuUqQLeEoO])([rh])\+([yvrlfmFNnJBGDXjbgdxKPCTWctwkpSRs])(.*)/){ ans ="{m.group(1)}{m.group(2)}{m.group(3)}{m.group(4)}{m.group(4)}{m.group(5)}"ans1 ="xviwva"ans2 ="aco rahAByAM xve (8.4.46)"
        m = re.search(r"(.*)H\+([KPCTWctwkpSRs])([SRs])(.*)", s)
        if m:
            ans = f"{m.group(1)}H {m.group(2)}{m.group(3)}{m.group(4)}"
            ans1 = "visarga"
            ans2 = "Sarpare visarjanIyaH (8.3.35)"
            cont = 0

        m = re.search(r"(.*)H\+([SRs])([KPCTWctwkpSRs])(.*)", s)
        if m:
            ans = f"{m.group(1)} {m.group(2)}{m.group(3)}{m.group(4)}"
            ans1 = "visargalopaH"
            ans2 = "Karpare Sari vA visargalopo vakwavyaH (vA 4906)"
            cont = 0

        m = re.search(r"(.*)H\+([SRs])([KPCTWctwkpSRs])(.*)", s)
        if m:
            ans = ans + ":" + f" {m.group(1)}H {m.group(2)}{m.group(3)}{m.group(4)}"
            ans1 = ans1 + ":" + "visargalopABAve"
            ans2 = ans2 + ":" + "Karpare Sari vA visargalopo vakwavyaH (vA 4906)"
            cont = 0

        m = re.search(r"(.*)H\+([SRs])([KPCTWctwkpSRs])(.*)", s)
        if m:
            ans = ans + ":" + f" {m.group(1)}{m.group(2)}{m.group(2)}{m.group(3)}{m.group(4)}"
            ans1 = ans1 + ":" + "sawva"
            ans2 = ans2 + ":" + "visarjanIyasya saH (8.3.34)"
            cont = 0

        m = re.search(r"^sam\+rAt", s)
        if m:
            ans = "samrAt"
            ans1 = "mawva"
            ans2 = "mo rAji samaH kvO (8.2.35)"
            cont = 0

        m = re.search(r"(.*)m\+hm(.*)", s)
        if m:
            ans = f"{m.group(1)}m hm{m.group(2)}"
            ans1 = "mawva"
            ans2 = "he mapare vA (8.3.26)"
            cont = 0

        m = re.search(r"(.*)m\+hm(.*)", s)
        if m:
            ans = ans + ":" + f" {m.group(1)}Mhm{m.group(2)}"
            ans1 = ans1 + ":" + "anusvAraH"
            ans2 = ans2 + ":" + "moZnusvAraH (8.3.23)"
            cont = 0

        m = re.search(r"(.*)m\+h([yvl])(.*)", s)
        if m:
            ans = f"{m.group(1)}{m.group(2)}z h{m.group(2)}{m.group(3)}"
            ans1 = "anunAsika"
            ans2 = "yavalapare yavalA vewi vakwavyam (vA 4902)"
            cont = 0

        m = re.search(r"(.*)m\+h([yvl])(.*)", s)
        if m:
            ans = ans + ":" + f"{m.group(1)}M h{m.group(2)}{m.group(3)}"
            ans1 = ans1 + ":" + "anusvAraH"
            ans2 = ans2 + ":" + "moZnusvAraH (8.3.23)"
            cont = 0

        m = re.search(r"(.*)m\+hn(.*)", s)
        if m:
            ans = f"{m.group(1)}n hn{m.group(2)}"
            ans1 = "nawva"
            ans2 = "na pare naH (8.3.27)"
            cont = 0

        m = re.search(r"(.*)m\+hn(.*)", s)
        if m:
            ans = ans + ":" + f" {m.group(1)}M hn{m.group(2)}"
            ans1 = ans1 + ":" + "anusvAraH"
            ans2 = ans2 + ":" + "moZnusvAraH (8.3.23)"
            cont = 0

        m = re.search(r"^(eRa|sa)H\+([gGfcCjJFtTdDNwWxXnbBmyrlvh])(.*)", s)
        if m:
            ans = f"{m.group(1)} {m.group(2)}{m.group(3)}"
            ans1 = "visargalopa"
            ans2 = "ewawwaxoH sulopoZkoranaFsamAse hali (6.1.132)"
            cont = 0

        ## kKpP are apavAdas, See following rules
        #"H,k,><k,jihvAmUlIya,kupvo><ka><pO ca (8.3.37),",
        #"H,k,H k,visarga,kupvo><ka><pO ca (8.3.37),",
        #"H,K,><K,jihvAmUlIya,kupvo><ka><pO ca (8.3.37),",
        #"H,K,H K,visarga,kupvo><ka><pO ca (8.3.37),",
        #"H,p,><p,upaXmAnIya,kupvo><ka><pO ca (8.3.37),",
        #"H,p,H p,visarga,kupvo><ka><pO ca (8.3.37),",
        #"H,P,><P,upaXmAnIya,kupvo><ka><pO ca (8.3.37),",
        #"H,P,H P,visarga,kupvo><ka><pO ca (8.3.37),",
        # Similarly sSR are apavAdas, See following Rules
        #"aH,S,aSS,sawva -> Scuwva,visarjanIyasya saH (8.3.34)-> swoH ScunA ScuH (8.4.40),",
        #"aH,S,aH S,visarga,vA Sari (8.3.36),",
        #"aH,R,aRR,sawva -> Rtuwva,visarjanIyasya saH (8.3.34)-> RtunA RtuH (8.4.41),",
        #"aH,R,aH R,visarga,vA Sari (8.3.36),",
        #"aH,s,ass,sawva,visarjanIyasya saH (8.3.34),",
        #"aH,s,aH s,visarga,vA Sari (8.3.36),",
        # and similary for iH, uH, ...

        m = re.search(r"(.*)[aA]\+e(wi|Ri|mi|wA|wArO|wAraH|wAsi|wAsWaH|wAsWa|wAsmi|wAsvaH|wAsmaH|Ryawi|RyawaH|Ryanwi|Ryasi|RyaWaH|RyaWa|RyAmi|RyAvaH|RyAmaH|wu)$", s)
        if m:
            ans = f"{m.group(1)}E{m.group(2)}"
            ans1 = "vqxXi"
            ans2 = "ewyeXawyUTsu (6.1.86)"
            cont = 0

        m = re.search(r"(.*)[aA]\+E(w|wAm|H|wam|wa|va|ma|Ryaw|RyawAm|Ryan|RyaH|Ryawam|Ryawa|Ryam|RyAva|RyAma)$", s)
        if m:
            ans = f"{m.group(1)}E{m.group(2)}"
            ans1 = "vqxXi"
            ans2 = "ewyeXawyUTsu (6.1.86)"
            cont = 0

        m = re.search(r"(.*)[aA]\+[eE]X(.*)", s)
        if m:
            ans = f"{m.group(1)}EX{m.group(2)}"
            ans1 = "vqxXi"
            ans2 = "ewyeXawyUTsu (6.1.86)"
            cont = 0

        m = re.search(r"(.*)[aA]\+Uha(.*)", s)
        if m:
            ans = f"{m.group(1)}Oha{m.group(2)}"
            ans1 = "vqxXi"
            ans2 = "ewyeXawyUTsu (6.1.86)"
            cont = 0

        # if(an=~/(.*)a\+ewi/){ans ="{m.group(1)}Ewi"ans1 ="vqxXi"ans2 ="ewyeXawyUTsu (6.1.86)"
        # if(an=~/(.*)a\+eXawe/){ans ="{m.group(1)}EXawe"ans1 ="vqxXi"ans2 ="ewyeXawyUTsu (6.1.86)"

        m = re.search(r"^ahan\+rUpa(.*)", s)
        if m:
            ans = f"aho rUpa{m.group(1)}"
            ans1 = "ruwva-> uwva-> guNa"
            ans2 = "roZsupi (8.2.69)(prApwe) -> rUparAwri raWanwareRuruwvam vAcyam (vA 4847)-> haSi ca (6.1.114)-> Ax guNaH (6.1.87)"
            cont = 0

        m = re.search(r"^ahan\+rAwr(.*)", s)
        if m:
            ans = f"aho rAwr{m.group(1)}"
            ans1 = "ruwva-> uwva-> guNa"
            ans2 = "roZsupi (8.2.69) (prApwe) -> rUparAwri raWanwareRuruwvam vAcyam (vA 4847)-> haSi ca (6.1.114)-> Ax guNaH (6.1.87)"
            cont = 0

        m = re.search(r"^ahan\+raWanwara(.*)", s)
        if m:
            ans = f"aho raWanwara{m.group(1)}"
            ans1 = "ruwva-> uwva-> guNa"
            ans2 = "roZsupi (8.2.69) (prApwe) -> rUparAwriraWanwareRu ruwvam vAcyam (vA 4847)-> haSi ca (6.1.114)-> Ax guNaH (6.1.87)"
            cont = 0

        m = re.search(r"^ahan\+pawi(.*)", s)
        if m:
            ans = f"aharpawi{m.group(1)}"
            ans1 = "rePa"
            ans2 = "roZsupi (8.2.69)-> KaravasAnayorvisarjanIyaH (8.3.15) (prApwe)-> aharAxInAm pawyAxiRu vA rePaH (vA 4851)"
            cont = 0

        m = re.search(r"^ahan\+pawi(.*)", s)
        if m:
            ans = ans + ":" + f" ahaH pawi{m.group(1)}"
            ans1 = ans1 + ":" + "visarga"
            ans2 = ans2 + ":" + "roZsupi (8.2.69) -> KaravasAnayorvisarjanIyaH (8.3.15)-> kupvo><ka><pO ca (8.3.37)"
            cont = 0

        m = re.search(r"^ahan\+pawi(.*)", s)
        if m:
            ans = ans + ":" + f" aha><pawi{m.group(1)}"
            ans1 = ans1 + ":" + "upaXmAnIya"
            ans2 = ans2 + ":" + "roZsupi (8.2.69)->  KaravasAnayorvisarjanIyaH (8.3.15) -> kupvo><ka><pO ca (8.3.37)"
            cont = 0

        m = re.search(r"^ahan\+gaNa(.*)", s)
        if m:
            ans = f"ahargaNa{m.group(1)}"
            ans1 = "rePa"
            ans2 = "roZsupi (8.2.69)"
            cont = 0

        # if(an=~/^ahan\+gaNa(.*)/){ans =ans.":"." ahaH gaNa{m.group(1)}"ans1 =ans1.":"."visarga"ans2 =ans2.":"."roZsupi (8.2.69)-> visarjanIyasya saH (8.3.34)"
        m = re.search(r"^ahan\+puwra(.*)", s)
        if m:
            ans = f"aharpuwra{m.group(1)}"
            ans1 = "rePa"
            ans2 = "roZsupi (8.2.69)-> aharAxInAm pawyAxiRu vA rePaH (vA 4851)"
            cont = 0

        m = re.search(r"^ahan\+puwra(.*)", s)
        if m:
            ans = ans + ":" + f" aha><puwra{m.group(1)}"
            ans1 = ans1 + ":" + "upaXmAnIya"
            ans2 = ans2 + ":" + "roZsupi (8.2.69)-> kupvo><ka><pO ca (8.3.37)"
            cont = 0

        m = re.search(r"^ahan\+puwra(.*)", s)
        if m:
            ans = ans + ":" + f" ahaH puwra{m.group(1)}"
            ans1 = ans1 + ":" + "visarga"
            ans2 = ans2 + ":" + "roZsupi (8.2.69)-> kupvo><ka><pO ca (8.3.37)"
            cont = 0

        m = re.search(r"^gIr\+pawi(.*)", s)
        if m:
            ans = f"gIrpawi{m.group(1)}"
            ans1 = "rePa"
            ans2 = "KaravasAnayorvisarjanIyaH (8.3.15)(prApwe) -> aharAxInAm pawyAxiRu vA rePaH (vA 4851)"
            cont = 0

        m = re.search(r"^gIr\+pawi(.*)", s)
        if m:
            ans = ans + ":" + f" gI><pawi{m.group(1)}"
            ans1 = ans1 + ":" + "upaXmAnIya"
            ans2 = ans2 + ":" + "KaravasAnayorvisarjanIyaH (8.3.15)-> kupvo><ka><pO ca (8.3.37)"
            cont = 0

        m = re.search(r"^gIr\+pawi(.*)", s)
        if m:
            ans = ans + ":" + f" gIH pawi{m.group(1)}"
            ans1 = ans1 + ":" + "visarga"
            ans2 = ans2 + ":" + "KaravasAnayorvisarjanIyaH (8.3.15)-> kupvo><ka><pO ca (8.3.37)"
            cont = 0

        m = re.search(r"^gIr\+gaNa(.*)", s)
        if m:
            ans = f"gIrgaNa{m.group(1)}"
            ans1 = "rePa"
            ans2 = "roZsupi (8.2.69)"
            cont = 0

        # if(an=~/^gIr\+gaNa(.*)/){ans =ans.":"." gIH gaNa{m.group(1)}"ans1 =ans1.":"."visarga"ans2 =ans2.":"."visarjanIyasya saH (8.3.34)"
        m = re.search(r"^gIr\+puwra(.*)", s)
        if m:
            ans = f"gIrpuwra{m.group(1)}"
            ans1 = "rePa"
            ans2 = "roZsupi (8.2.69)-> aharAxInAm pawyAxiRu vA rePaH (vA 4851)"
            cont = 0

        m = re.search(r"^gIr\+puwra(.*)", s)
        if m:
            ans = ans + ":" + f" gIH puwra{m.group(1)}"
            ans1 = ans1 + ":" + "visarga"
            ans2 = ans2 + ":" + "roZsupi (8.2.69)-> kupvo><ka><pO ca (8.3.37)"
            cont = 0

        m = re.search(r"^gIr\+puwra(.*)", s)
        if m:
            ans = ans + ":" + f" gI><puwra{m.group(1)}"
            ans1 = ans1 + ":" + "upaXmAnIya"
            ans2 = ans2 + ":" + "roZsupi (8.2.69)-> kupvo><ka><pO ca (8.3.37)"
            cont = 0

        m = re.search(r"^XUr\+pawi(.*)", s)
        if m:
            ans = f"XUrpawi{m.group(1)}"
            ans1 = "rePa"
            ans2 = "KaravasAnayorvisarjanIyaH (8.3.15)(prApwe)-> aharAxInAm pawyAxiRu vA rePaH (vA 4851)"
            cont = 0

        m = re.search(r"^XUr\+pawi(.*)", s)
        if m:
            ans = ans + ":" + f" XU><pawi{m.group(1)}"
            ans1 = ans1 + ":" + "upaXmAnIya"
            ans2 = ans2 + ":" + "KaravasAnayorvisarjanIyaH (8.3.15)-> kupvo><ka><pO ca (8.3.37)"
            cont = 0

        m = re.search(r"^XUr\+pawi(.*)", s)
        if m:
            ans = ans + ":" + f" XUH pawi{m.group(1)}"
            ans1 = ans1 + ":" + "visarga"
            ans2 = ans2 + ":" + "KaravasAnayorvisarjanIyaH (8.3.15)-> kupvo><ka><pO ca (8.3.37)"
            cont = 0

        m = re.search(r"^XUr\+gaNa(.*)", s)
        if m:
            ans = f"XUrgaNa{m.group(1)}"
            ans1 = "rePa"
            ans2 = "roZsupi (8.2.69)"
            cont = 0

        # if(an=~/^XUr\+gaNa(.*)/){ans =ans.":"." XUH gaNa{m.group(1)}"ans1 =ans1.":"."visarga"ans2 =ans2.":"."roZsupi (8.2.69)->visarjanIyasya saH (8.3.34)"
        m = re.search(r"^XUr\+puwra(.*)", s)
        if m:
            ans = f"XUrpuwra{m.group(1)}"
            ans1 = "rePa"
            ans2 = "roZsupi (8.2.69)-> aharAxInAm pawyAxiRu vA rePaH (vA 4851)"
            cont = 0

        m = re.search(r"^XUr\+puwra(.*)", s)
        if m:
            ans = ans + ":" + f" XUH puwra{m.group(1)}"
            ans1 = ans1 + ":" + "visarga"
            ans2 = ans2 + ":" + "roZsupi (8.2.69)->kupvo><ka><pO ca (8.3.37)"
            cont = 0

        m = re.search(r"^XUr\+puwra(.*)", s)
        if m:
            ans = ans + ":" + f" XU><puwra{m.group(1)}"
            ans1 = ans1 + ":" + "upaXmAnIya"
            ans2 = ans2 + ":" + "roZsupi (8.2.69)-> kupvo><ka><pO ca (8.3.37)"
            cont = 0

        m = re.search(r"^ahan\+ahaH$", s)
        if m:
            ans = f"aharahaH"
            ans1 = "rePa"
            ans2 = "roZsupi (8.2.69)"
            cont = 0

        else:
            m = re.search(r"(.*)([aiuqL])([fNn])\+([aAiIuUqQLeEoO])(.*)", s)
            if m:
                ans = f"{m.group(1)}{m.group(2)}{m.group(3)}{m.group(3)}{m.group(4)}{m.group(5)}"
                ans1 = "famudAgama"
                ans2 = "famo hrasvAxaci famuNniwyam (8.3.32)"
                cont = 0
            else:
                m = re.search(r"(.*)([^aiuqL])([fNn])\+([aAiIuUqQLeEoO])(.*)", s)
                if m:
                    ans = f"{m.group(1)}{m.group(2)}{m.group(3)}{m.group(4)}{m.group(5)}"
                    ans1 = "diPAlta"
                    ans2 = ""
                    cont = 0

        m = re.search(r"(.*)([iIuUqQLeEoO])H\+([aAiIuUqQLeEoOgGfjJFdDNxXnbBmylvh])(.*)", s)
        if m:
            ans = f"{m.group(1)}{m.group(2)}r{m.group(3)}{m.group(4)}"
            ans1 = "rePa"
            ans2 = "sasajuRo ruH (8.2.66)"
            cont = 0

        m = re.search(r"^eRaH\+([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSRsh])(.*)", s)
        if m:
            ans = f"eRa {m.group(1)}{m.group(2)}"
            ans1 = "visargalopa"
            ans2 = "ewawwaxoH sulopoZkoranaFsamAse hali (6.1.132)"
        else:
            m = re.search(r"^saH\+([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSRsh])(.*)", s)
            if m:
                ans = f"sa {m.group(1)}{m.group(2)}"
                ans1 = "visargalopa",
                ans2 = "ewawwaxoH sulopoZkoranaFsamAse hali (6.1.132)"
            else:
                m = re.search(r"(.*)aH\+([gGfjJFdDNxXnbBmyrlvh])(.*)", s)
                if m:
                    ans = f"{m.group(1)}o {m.group(2)}{m.group(3)}"
                    ans1 = "ruwva-> uwva-> guNa"
                    ans2 = "sasajuRo ruH (8.2.66)-> haSi ca (6.1.114)-> Ax guNaH (6.1.87)"
                    cont = 0
                else:
                    m = re.search(r"(.*)([aAiIuUqQLeEoO])H\+([wW])([^sSR].*)", s)
                    if m:
                        ans = f"{m.group(1)}{m.group(2)}s{m.group(3)}{m.group(4)}"
                        ans1 = "sawva"
                        ans2 = "visarjanIyasya saH (8.3.34)"
                        cont = 0

        m = re.search(r"(.*)([aAiIuUqQLeEoO])H\+([cC])(.*)", s)
        if m:
            ans = f"{m.group(1)}{m.group(2)}S{m.group(3)}{m.group(4)}"
            ans1 = "sawva-> Scuwva"
            ans2 = "visarjanIyasya saH (8.3.34)-> swoH ScunA ScuH (8.4.40)"
            cont = 0

        m = re.search(r"(.*)([aAiIuUqQLeEoO])H\+([tT])(.*)", s)
        if m:
            ans = f"{m.group(1)}{m.group(2)}R{m.group(3)}{m.group(4)}"
            ans1 = "sawva-> Rtuwva"
            ans2 = "visarjanIyasya saH (8.3.34)-> RtunA RtuH (8.4.41)"
            cont = 0

        m = re.search(r"(.*)AH\+([gGfjJFdDNxXnbBmyrlvh])(.*)", s)
        if m:
            ans = f"{m.group(1)}A {m.group(2)}{m.group(3)}"
            ans1 = "ruwva-> yawva-> lopa"
            ans2 = "sasajuRo ruH (8.2.66)-> BoBagoaGo apUrvasya yoZSi (8.3.17)-> hali sarveRAm (8.3.22)"
            cont = 0

        m = re.search(r"^BoH\+([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSRsh])(.*)", s)
        if m:
            ans = f"Bos{m.group(1)}{m.group(2)}"
            ans1 = ""
            ans2 = "sasajuRo ruH (8.2.66)-> KaravasAnayorvisarjanIyaH (8.3.15)-> visarjanIyasya saH (8.3.34)"
            cont = 0

        m = re.search(r"^BoH\+([aAiIuUqQLeEoO])(.*)", s)
        if m:
            ans = f"Boy{m.group(1)}{m.group(2)}"
            ans1 = "sawva->yawva->laGuprayawnAxeSaH"
            ans2 = "sasajuRo ruH (8.2.66)->BoBagoaGo apUrvasyayoZSi (8.3.17)->vyorlaGuprayawnawaraH SAkatAyanasya (8.3.18)"
            cont = 0

        m = re.search(r"^BoH\+([aAiIuUqQLeEoO])(.*)", s)
        if m:
            ans = ans + ":" + f"Bo {m.group(1)}{m.group(2)}"
            ans1 = ans1 + ":" + f"sawva->yawva->laGuprayawnABAve yawvalopa"
            ans2 = ans2 + ":" + f"sasajuRo ruH (8.2.66)->BoBagoaGo apUrvasyayoZSi (8.3.17)->owo gArgyasya (8.3.20)"
            cont = 0

        m = re.search(r"^BagoH\+([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSRsh])(.*)", s)
        if m:
            ans = f"Bago {m.group(1)}{m.group(2)}"
            ans1 = "yawvalopaH"
            ans2 = "sasajuRo ruH (8.2.66)->BoBagoaGo apUrvasyayoZSi (8.3.17)->hali sarveRAm (8.3.22)"
            cont = 0

        m = re.search(r"^BagoH\+([aAiIuUqQLeEoO])(.*)", s)
        if m:
            ans = f"Bagoy{m.group(1)}{m.group(2)}"
            ans1 = "sawva->yawva->laGuprayawnAxeSaH"
            ans2 = "sasajuRo ruH (8.2.66)->BoBagoaGo apUrvasyayoZSi (8.3.17)->vyorlaGuprayawnawaraH SAkatAyanasya (8.3.18)"
            cont = 0

        m = re.search(r"^BagoH\+([aAiIuUqQLeEoO])(.*)", s)
        if m:
            ans = ans + ":" + f"Bago {m.group(1)}{m.group(2)}"
            ans1 = ans1 + ":" + "sawva->yawva->laGuprayawnABAve yawvalopa"
            ans2 = ans2 + ":" + "sasajuRo ruH (8.2.66)->BoBagoaGo apUrvasyayoZSi (8.3.17)->owo gArgyasya (8.3.20)"
            cont = 0

        m = re.search(r"^aGoH\+([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSRsh])(.*)", s)
        if m:
            ans = f"aGo {m.group(1)}{m.group(2)}"
            ans1 = "yawvalopaH"
            ans2 = "sasajuRo ruH (8.2.66)->BoBagoaGo apUrvasyayoZSi (8.3.17)->hali sarveRAm (8.3.22)"
            cont = 0

        m = re.search(r"^aGoH\+([aAiIuUqQLeEoO])(.*)", s)
        if m:
            ans = f"aGoy{m.group(1)}{m.group(2)}"
            ans1 = "sawva->yawva->laGuprayawnAxeSaH"
            ans2 = "sasajuRo ruH (8.2.66)->BoBagoaGo apUrvasyayoZSi (8.3.17)->vyorlaGuprayawnawaraH SAkatAyanasya (8.3.18)"
            cont = 0

        m = re.search(r"^aGoH\+([aAiIuUqQLeEoO])(.*)", s)
        if m:
            ans = ans + ":" + f"aGo {m.group(1)}{m.group(2)}"
            ans1 = ans1 + ":" + "sawva->yawva->laGuprayawnABAve yawvalopa"
            ans2 = ans2 + ":" + "sasajuRo ruH (8.2.66)->BoBagoaGo apUrvasyayoZSi (8.3.17)->owo gArgyasya (8.3.20)"
            cont = 0

        m = re.search(r"^miWo\+([aAiIuUqQLeEoO])(.*)", s)
        if m:
            ans = f"miWo {m.group(1)}{m.group(2)}"
            ans1 = "pragqhyawva->prakqwiBAva"
            ans2 = "ow (1.1.15)-> pluwapragqhyA aci niwyam (6.1.125)"
            cont = 0

        m = re.search(r"^ho\+([aAiIuUqQLeEoO])(.*)", s)
        if m:
            ans = f"ho {m.group(1)}{m.group(2)}"
            ans1 = "pragqhyawva->prakqwiBAva"
            ans2 = "ow (1.1.15)-> pluwapragqhyA aci niwyam (6.1.125)"
            cont = 0

        m = re.search(r"^aho\+([aAiIuUqQLeEoO])(.*)", s)
        if m:
            ans = f"aho {m.group(1)}{m.group(2)}"
            ans1 = "pragqhyawva->prakqwiBAva"
            ans2 = "ow (1.1.15)-> pluwapragqhyA aci niwyam (6.1.125)"
            cont = 0

        m = re.search(r"^Aho\+([aAiIuUqQLeEoO])(.*)", s)
        if m:
            ans = f"Aho {m.group(1)}{m.group(2)}"
            ans1 = "pragqhyawva->prakqwiBAva"
            ans2 = "ow (1.1.15)-> pluwapragqhyA aci niwyam (6.1.125)"
            cont = 0

        m = re.search(r"^uwAho\+([aAiIuUqQLeEoO])(.*)", s)
        if m:
            ans = f"uwAho {m.group(1)}{m.group(2)}"
            ans1 = "pragqhyawva->prakqwiBAva"
            ans2 = "ow (1.1.15)-> pluwapragqhyA aci niwyam (6.1.125)"
            cont = 0

        m = re.search(r"^no\+([aAiIuUqQLeEoO])(.*)", s)
        if m:
            ans = f"no {m.group(1)}{m.group(2)}"
            ans1 = "pragqhyawva->prakqwiBAva"
            ans2 = "ow (1.1.15)-> pluwapragqhyA aci niwyam (6.1.125)"
            cont = 0

        m = re.search(r"^aWo\+([aAiIuUqQLeEoO])(.*)", s)
        if m:
            ans = f"aWo {m.group(1)}{m.group(2)}"
            ans1 = "pragqhyawva->prakqwiBAva"
            ans2 = "ow (1.1.15)-> pluwapragqhyA aci niwyam (6.1.125)"
            cont = 0

        m = re.search(r"^([aiuqLeEoO])\+([aAiIuUqQLeEoO])(.*)", s)
        if m:
            ans = f"{m.group(1)} {m.group(2)}{m.group(3)}"
            ans1 = "pragqhyawva->prakqwiBAva"
            ans2 = "nipAwa ekAjanAf (1.1.14)-> pluwapragqhyA aci niwyam (6.1.125)"
            cont = 0

        m = re.search(r"^uF\+iwi", s)
        if m:
            ans = "u iwi"
            ans1 = "vikalpena pragqhyawva-> prakqwiBAva"
            ans2 = "uFaH (1.1.17)-> pluwapragqhyA aci niwyam (6.1.125)"
            cont = 0

        m = re.search(r"^uF\+iwi", s)
        if m:
            ans = ans + ":" + "Uz iwi"
            ans1 = ans1 + ":" + "vikalpena Uz AxeSa->pragqhyawva->prakqwiBAva"
            ans2 = ans2 + ":" + "Uz (1.1.18)-> pluwapragqhyA aci niwyam (6.1.125)"
            cont = 0

        m = re.search(r"uF\+iwi", s)
        if m:
            ans = ans + ":" + "viwi"
            ans1 = ans1 + ":" + "vikalpABAve yaN"
            ans2 = ans2 + ":" + "iko yaNaci (6.1.77)"
            cont = 0

        # if(an=~/(.*)([kKgGfcCjJtTdDNpPbBmwWxXn])u\+([aAiIuUqQLeEoO])(.*)/){ans = f"{m.group(1)}{m.group(2)}v{m.group(3)}{m.group(4)}"ans1 = "vikalpena vAxeSaH"ans2 = "maya uFo vo vA (8.3.33)"
        # if(an=~/(.*)([mfNnJBGDXjbgdxKFCTWctwkp])u\+([aAiIuUqQLeEoO])(.*)/){ans = f"{m.group(1)}{m.group(2)}v{m.group(3)}{m.group(4)}"ans1 = "vikalpena vAxeSaH"ans2 = "maya uFo vo vA (8.3.33)"
        # if(an=~/(.*)([kKgGfcCjJtTdDNpPbBmwWxXn])u\+([aAiIuUqQLeEoO])(.*)/){ans = ans.":"."{m.group(1)}{m.group(2)}u {m.group(3)}{m.group(4)}" ans1 = ans1.":". f"vAxeSABAve->pragqhyawva->prakqwiBAva"ans2 = ans2.":"."uFaH (1.1.17)-> pluwapragqhyA aci niwyam (6.1.125)"
        # Commented the above 2 srules since it produced wrong result with maXu+ariH
        # if(an=~/(.*)([kKgGfcCjJtTdDNpPbBmwWxXn])u\+([aAiIuUqQLeEoO])(.*)/){ans = ans.":"."{m.group(1)}{m.group(2)}u {m.group(3)}{m.group(4)}" ans1 = ans1.":". f"vAxeSABAve->pragqhyawva->prakqwiBAva"ans2 = ans2.":"."uFaH (1.1.17)-> pluwapragqhyA aci niwyam (6.1.125)"

        m = re.search(r"^kRi\+ya(.*)", s)
        if m:
            ans = f"kRayya{m.group(1)}"
            ans1 = "SakyArWe ayAxeSa nipAwana"
            ans2 = "kRayyajayyO SakyArWe (6.1.81)"
            cont = 0

        m = re.search(r"^kRi\+ya(.*)", s)
        if m:
            ans = ans + ":" + f"kReya{m.group(1)}"
            ans1 = ans1 + ":" + f"SakyArWABAve guNa"
            ans2 = ans2 + ":" + f"sArvaXAwukArXaXAwukayoH (7.3.84)"
            cont = 0

        m = re.search(r"^ji\+ya(.*)", s)
        if m:
            ans = f"jayya{m.group(1)}"
            ans1 = "SakyArWe ayAxeSa nipAwana"
            ans2 = "kRayyajayyO SakyArWe (6.1.81)"
            cont = 0

        m = re.search(r"^ji\+ya(.*)", s)
        if m:
            ans = ans + ":" + f"jeya{m.group(1)}"
            ans1 = ans1 + ":" + "SakyArWABAve guNa"
            ans2 = ans2 + ":" + "sArvaXAwukArXaXAwukayoH (7.3.84)"
            cont = 0

        m = re.search(r"^krI\+ya(.*)", s)
        if m:
            ans = f"krayya{m.group(1)}"
            ans1 = "krayaNArhe ayAxeSa nipAwanam"
            ans2 = "krayyaswaxarWe (6.1.82)"
            cont = 0

        m = re.search(r"^krI\+ya(.*)", s)
        if m:
            ans = ans + ":" + f"kreya{m.group(1)}"
            ans1 = ans1 + ":" + "krayaNArhABAve guNa"
            ans2 = ans2 + ":" + "sArvaXAwukArXaXAwukayoH (7.3.84)"
            cont = 0

        m = re.search(r"^aXaH\+paxa(.*)", s)
        if m:
            ans = f"aXaspaxa{m.group(1)}"
            ans1 = "samAse sawva"
            ans2 = "aXaSSirasI paxe (8.3.47)"
            cont = 0

        m = re.search(r"^aXaH\+paxa(.*)", s)
        if m:
            ans = ans + ":" + f"aXa><paxa{m.group(1)}"
            ans1 = ans1 + ":" + "upaXmAnIya"
            ans2 = ans2 + ":" + "kupvo ><ka ><pO ca (8.3.37)"
            cont = 0

        m = re.search(r"^aXaH\+paxa(.*)", s)
        if m:
            ans = ans + ":" + f"aXaH paxa{m.group(1)}"
            ans1 = ans1 + ":" + "visarga"
            ans2 = ans2 + ":" + "kupvo ><ka ><pO ca (8.3.37)"
            cont = 0

        m = re.search(r"^SiraH\+paxa(.*)", s)
        if m:
            ans = f"Siraspaxa{m.group(1)}"
            ans1 = "samAse sawva"
            ans2 = "aXaSSirasI paxe (8.3.47)"
            cont = 0

        m = re.search(r"^SiraH\+paxa(.*)", s)
        if m:
            ans = ans + ":" + f"Sira><paxa{m.group(1)}"
            ans1 = ans1 + ":" + "upaXmAnIya"
            ans2 = ans2 + ":" + "kupvo ><ka ><pO ca (8.3.37)"
            cont = 0

        m = re.search(r"^SiraH\+paxa(.*)", s)
        if m:
            ans = ans + ":" + f"SiraH paxa{m.group(1)}"
            ans1 = ans1 + ":" + "visarga"
            ans2 = ans2 + ":" + "kupvo ><ka ><pO ca (8.3.37)"
            cont = 0

        m = re.search(r"(.*)iH\+([kK])(.*)", s)
        if m:
            ans = f"{m.group(1)}iR{m.group(2)}{m.group(3)}"
            ans1 = "sAmarWye Rawvam"
            ans2 = "isusoH sAmarWye (8.3.44)"
            cont = 0

        m = re.search(r"(.*)iH\+([kK])(.*)", s)
        if m:
            ans = ans + ":" + f"{m.group(1)}i><{m.group(2)}{m.group(3)}"
            ans1 = ans1 + ":" + "RawvABAve jihvAmUlIya"
            ans2 = ans2 + ":" + "kupvo><ka ><pO ca (8.3.37)"
            cont = 0

        m = re.search(r"(.*)iH\+([kK])(.*)", s)
        if m:
            ans = ans + ":" + f"{m.group(1)}iH {m.group(2)}{m.group(3)}"
            ans1 = ans1 + ":" + "RawvABAve visarga"
            ans2 = ans2 + ":" + "kupvo><ka ><pO ca (8.3.37)"
            cont = 0

        m = re.search(r"(.*)iH\+([pP])(.*)", s)
        if m:
            ans = f"{m.group(1)}iR{m.group(2)}{m.group(3)}"
            ans1 = "sAmarWye Rawvam"
            ans2 = "isusoH sAmarWye (8.3.44)"
            cont = 0

        m = re.search(r"(.*)iH\+([pP])(.*)", s)
        if m:
            ans = ans + ":" + f"{m.group(1)}i><{m.group(2)}{m.group(3)}"
            ans1 = ans1 + ":" + "RawvABAve upaxmAnIya"
            ans2 = ans2 + ":" + "kupvo><ka ><pO ca (8.3.37)"
            cont = 0

        m = re.search(r"(.*)iH\+([pP])(.*)", s)
        if m:
            ans = ans + ":" + f"{m.group(1)}iH {m.group(2)}{m.group(3)}"
            ans1 = ans1 + ":" + "RawvABAve visarga"
            ans2 = ans2 + ":" + "kupvo><ka ><pO ca (8.3.37)"
            cont = 0

        m = re.search(r"(.*)uH\+([kK])(.*)", s)
        if m:
            ans = f"{m.group(1)}uR{m.group(2)}{m.group(3)}"
            ans1 = "sAmarWye Rawvam"
            ans2 = "isusoH sAmarWye (8.3.44)"
            cont = 0

        m = re.search(r"(.*)uH\+([kK])(.*)", s)
        if m:
            ans = ans + ":" + f"{m.group(1)}u><{m.group(2)}{m.group(3)}"
            ans1 = ans1 + ":" + "RawvABAve jihvAmUlIya"
            ans2 = ans2 + ":" + "kupvo><ka ><pO ca (8.3.37)"
            cont = 0

        m = re.search(r"(.*)uH\+([kK])(.*)", s)
        if m:
            ans = ans + ":" + f"{m.group(1)}uH {m.group(2)}{m.group(3)}"
            ans1 = ans1 + ":" + "RawvABAve visarga"
            ans2 = ans2 + ":" + "kupvo><ka ><pO ca (8.3.37)"
            cont = 0

        m = re.search(r"(.*)uH\+([pP])(.*)", s)
        if m:
            ans = f"{m.group(1)}uR{m.group(2)}{m.group(3)}"
            ans1 = "sAmarWye Rawvam"
            ans2 = "isusoH sAmarWye (8.3.44)"
            cont = 0

        m = re.search(r"(.*)uH\+([pP])(.*)", s)
        if m:
            ans = ans + ":" + f"{m.group(1)}u><{m.group(2)}{m.group(3)}"
            ans1 = ans1 + ":" + "RawvABAve upaxmAnIya"
            ans2 = ans2 + ":" + "kupvo><ka ><pO ca (8.3.37)"
            cont = 0

        m = re.search(r"(.*)uH\+([pP])(.*)", s)
        if m:
            ans = ans + ":" + f"{m.group(1)}uH {m.group(2)}{m.group(3)}"
            ans1 = ans1 + ":" + "RawvABAve visarga"
            ans2 = ans2 + ":" + "kupvo><ka ><pO ca (8.3.37)"
            cont = 0

    return ans, ans1, ans2, cont

# if the SabxaH or XAxu have xvivacan and the second word will start with 'I' 'U' 'e' then there is prakqwiBAva (IxUxexxvivacanaM pragqhyam)
# if the first word is ending with 'a' or 'A' and the second word is an 'i' Xaxu or 'eX' XAxu started with the letter 'e', or the word is 'UD' then there is vqxXi sanXi. (ewyeXwyUDsu)
# if the first word is either 'amU' or 'amI' then there is not sanXi (axaso mAw)
