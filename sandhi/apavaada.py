#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Hrishikesh Terdalkar (hrishikeshrt.samskrit@gmail.com)

Perl Source:
    Samsaadhanii Git (sandhi/apavAxa_any.pl)
    (Commit: 30e5216a90e2bd0e80bf1e8ae4cdc97c08b00604) from
    https://github.com/samsaadhanii/scl/pull/5
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


def apavAdaniyamAH(an):
    # my($first,$second,$ans,$ans1,$ans2,$pragqhya_cond,$others,$i,@ans);
    first = ""
    second = ""
    ans = ""
    ans1 = ""
    ans2 = ""
    cont = 1

    match = re.match(r"^([^\+]+)\+(.*)", an)
    if match:
        first = match.group(1)
        second = match.group(2)

    # Following are two special rules where morphological analyser is invoked.
    # if (`echo "$second" | $GlblVar::LTPROCBIN -c $myPATH/morph_bin/all_morf.bin | grep 'upasarga:Af'`) {
    #    if($an=~/^(.*)[aA]\+(.*)/) {$ans = "$1$2";$ans1="pararUpa";$ans2="omAfoSca(6.1.95)"; $cont = 0;} # To do:show morph analysis in a tooltip
    # }
    # else {
    # The original Perl code has a brace here. In Python, it's handled by indentation.
    if match := re.search(r"^(axy)a\+i(fKawi)", an):
        ans = f"{match.group(1)}e{match.group(2)}"
        ans1 = "ekAxeSa"
        ans2 = "omAfoSca(6.1.95)"
        cont = 0
    elif match := re.search(r"^(axy)a\+u(fKawi)", an):
        ans = f"{match.group(1)}o{match.group(2)}"
        ans1 = "ekAxeSa"
        ans2 = "omAfoSca(6.1.95)"
        cont = 0
    # } elsif ($first =~ /[IUe]$/) {
    # @ans = split(/\//,`echo "$first" | $GlblVar::LTPROCBIN -c $myPATH/morph_bin/all_morf.bin`);

    # $pragqhya_cond = 0;
    # $others = 0;
    # for ($i=1; $i<=$#ans && !$found;$i++){
    #     if($ans[$i] =~ /<vacanam:xvi>/) { $pragqhya_cond = 1;} else { $others = 1;}
    # }
    # if($pragqhya_cond) {
    #    $ftmp = $first;
    #    #$ftmp =~ s/I$/i/;	kavI + ewO -> kavI ewO, and not kavi ewO
    #    #$ftmp =~ s/U$/u/;
    #         if($others == 1) { $cont = 1;} else { $cont = 0;}
    #    $ans = $ftmp." ".$second;$ans1="pragqhya";$ans2="IxUxexxvivacanam pragqhyam (1.1.11)-> pluwapragqhyA aci niwyam (6.1.125); *$first paxasya xvivacana-viSleRaNam aXikqwya";
    #         }
    # }

    # From here onwards it is just a pattern matching.

    # $ans contains the answer after sandhi
    # $ans1 contains the short name of the sandhi
    # $ans2 contains the Panini's suutras
    # $cont tells whether to continue with regular rules after applying these exceptional rules.

    if match := re.search(r"^akRa\+Uhin(.*)", an):
        ans = f"akROhiN{match.group(1)}"
        ans1 = "vqxXi"
        ans2 = "akRAxUhinyAmupasaMKyAnam (vA 3604)"
        cont = 0
    if match := re.search(r"^sva\+Iri([nN].*)", an):
        ans = f"svEri{match.group(1)}"
        ans1 = "vqxXi"
        ans2 = "svAxIreriNoH (vA 3606)"
        cont = 0
    if match := re.search(r"^sva\+IraH", an):
        ans = "svEraH"
        ans1 = "vqxXi"
        ans2 = "svAxIreriNoH (vA 3606)"
        cont = 0
    if match := re.search(r"^pra\+U([hD].*)", an):
        ans = f"prO{match.group(1)}"
        ans1 = "vqxXi"
        ans2 = "prAxUhoDoDyeRERyeRu (vA 3605)"
        cont = 0
    if match := re.search(r"^pra\+eR(.*)", an):
        ans = f"prER{match.group(1)}"
        ans1 = "vqxXi"
        ans2 = "prAxUhoDoDyeRERyeRu (vA 3605)"
        cont = 0

    # Since the suutras are different, we have two rules. I need to check if pra can be removed from the vaartika
    if match := re.search(r"^(vawsawar|kambal|vasan|qN|xaS)a\+qN(.*)", an):
        ans = f"{match.group(1)}ArN{match.group(2)}"
        ans1 = "vqxXi"
        ans2 = "pravawsawarakambalavasanArNaxaSAnAmqNe (vA 3608-9)"
        cont = 0
    if match := re.search(r"^pra\+qN(.*)", an):
        ans = f"prArN{match.group(1)}"
        ans1 = "vqxXi"
        ans2 = "pravawsawarakambalavasanArNaxaSAnAmqNe (vA 3608-9)"
        cont = 0
    elif match := re.search(r"^pra\+q(.*)", an):
        ans = f"prAr{match.group(1)}"
        ans1 = "vqxXi"
        ans2 = "upasargAxqwi XAwoH (6.1.91)"
        cont = 0

    if match := re.search(r"(.*)o\+yam$", an):
        ans = f"{match.group(1)}avyam"
        ans1 = "vAnwa"
        ans2 = "vAnwo yi prawyaye (6.1.79)"
        cont = 0
    if match := re.search(r"(.*)O\+yam$", an):
        ans = f"{match.group(1)}Avyam"
        ans1 = "vAnwa"
        ans2 = "vAnwo yi prawyaye (6.1.79)"
        cont = 0
    if match := re.search(r"^go\+yUw(.*)", an):
        ans = f"gavyUw{match.group(1)}"
        ans1 = "vAnwa"
        ans2 = "aXvaparimANe ca (vA 3544)"
        cont = 0

    if match := re.search(r"^(Saka|karka)\+anXuH$", an):
        ans = f"{match.group(1)}nXuH"
        ans1 = "pararUpa"
        ans2 = "SakanXvAxiRu pararUpam vAcyam (vA 3632)"
        cont = 0
    if match := re.search(r"^kula\+atA$", an):
        ans = "kulatA"
        ans1 = "pararUpa"
        ans2 = "SakanXvAxiRu pararUpam vAcyam (vA 3632)"
        cont = 0
    if match := re.search(r"^hala\+IRA$", an):
        ans = "halIRA"
        ans1 = "pararUpa"
        ans2 = "SakanXvAxiRu pararUpam vAcyam (vA 3632)"
        cont = 0
    if match := re.search(r"^lAfgala\+IRA$", an):
        ans = "lAfgalIRA"
        ans1 = "pararUpa"
        ans2 = "SakanXvAxiRu pararUpam vAcyam (vA 3632)"
        cont = 0
    if match := re.search(r"^manas\+IRA$", an):
        ans = "manIRA"
        ans1 = "pararUpa"
        ans2 = "SakanXvAxiRu pararUpam vAcyam (vA 3632)"
        cont = 0
    if match := re.search(r"^mArwa\+aNdaH$", an):
        ans = "mArwaNdaH"
        ans1 = "pararUpa"
        ans2 = "SakanXvAxiRu pararUpam vAcyam (vA 3632)"
        cont = 0
    if match := re.search(r"^pawaw\+aFjaliH$", an):
        ans = "pawaFjaliH"
        ans1 = "pararUpa"
        ans2 = "SakanXvAxiRu pararUpam vAcyam (vA 3632)"
        cont = 0
    if match := re.search(r"^sIman\+anwaH$", an):
        ans = "sImanwaH"
        ans1 = "pararUpa"
        ans2 = "sImanwaH keSaveSe (vA 3633)"
        cont = 0
    if match := re.search(r"^sAra\+afg(.*)", an):
        ans = f"sArafg{match.group(1)}"
        ans1 = "pararUpa"
        ans2 = "sArafgaH paSupakRiNoH (gaNa sUwram 136)"
        cont = 0
    if match := re.search(r"(.*)([aA])\+owuH", an):
        ans = f"{match.group(1)}owuH"
        ans1 = "pararUpa"
        ans2 = "owvoRTayoH samAse vA (vA 3634)"
        cont = 1
    if match := re.search(r"(.*)([aA])\+oRT(.*)", an):
        ans = f"{match.group(1)}oRT{match.group(3)}"
        ans1 = "pararUpa"
        ans2 = "owvoRTayoH samAse vA (vA 3634)"
        cont = 1

    if match := re.search(r"^kaH\+kaH$", an):
        ans = "kaskaH"
        ans1 = "sakAra"
        ans2 = "kaskAxiRu ca (8.3.48)"
        cont = 0
    if match := re.search(r"^kOwaH\+kuwaH$", an):
        ans = "kOwaskuwaH"
        ans1 = "sakAra"
        ans2 = "kaskAxiRu ca (8.3.48)"
        cont = 0
    if match := re.search(r"^BrAwuH\+puwraH$", an):
        ans = "BrAwuRpuwraH"
        ans1 = "sakAra"
        ans2 = "kaskAxiRu ca (8.3.48)"
        cont = 0
    if match := re.search(r"^SunaH\+karNaH$", an):
        ans = "SunaskarNaH"
        ans1 = "sakAra"
        ans2 = "kaskAxiRu ca (8.3.48)"
        cont = 0
    if match := re.search(r"^saxyaH\+(kAlaH|krIH|kaH)$", an):
        ans = f"saxyas{match.group(1)}"
        ans1 = "sakAra"
        ans2 = "kaskAxiRu ca (8.3.48)"
        cont = 0
    if match := re.search(r"^kAMH\+kAn$", an):
        ans = "kAMskAn"
        ans1 = "sakAra"
        ans2 = "kaskAxiRu ca (8.3.48)"
        cont = 0
    if match := re.search(r"^sarpiH\+kuNdikA$", an):
        ans = "sarpiRkuNdikA"
        ans1 = "sakAra"
        ans2 = "kaskAxiRu ca (8.3.48)"
        cont = 0
    if match := re.search(r"^XanuH\+kapAlam$", an):
        ans = "XanuRkapAlam"
        ans1 = "sakAra"
        ans2 = "kaskAxiRu ca (8.3.48)"
        cont = 0
    if match := re.search(r"^(bar?hi)H\+palam$", an):
        ans = f"{match.group(1)}Rpalam"
        ans1 = "sakAra"
        ans2 = "kaskAxiRu ca (8.3.48)"
        cont = 0
    if match := re.search(r"^yajuH\+pAwram$", an):
        ans = "yajuRpAwram"
        ans1 = "sakAra"
        ans2 = "kaskAxiRu ca (8.3.48)"
        cont = 0
    if match := re.search(r"^ayaH\+kAnwaH$", an):
        ans = "ayaskAnwaH"
        ans1 = "sakAra"
        ans2 = "kaskAxiRu ca (8.3.48)"
        cont = 0
    if match := re.search(r"^(wama|aya)H\+kANdaH$", an):
        ans = f"{match.group(1)}skANdaH"
        ans1 = "sakAra"
        ans2 = "kaskAxiRu ca (8.3.48)"
        cont = 0
    if match := re.search(r"^mexaH\+piNdaH$", an):
        ans = "mexaspiNdaH"
        ans1 = "sakAra"
        ans2 = "kaskAxiRu ca (8.3.48)"
        cont = 0
    if match := re.search(r"^(BA|aha)H\+karaH$", an):
        ans = f"{match.group(1)}skaraH"
        ans1 = "sakAra"
        ans2 = "kaskAxiRu ca (8.3.48)"
        cont = 0

    if match := re.search(r"^(nama|pura)H\+([kp].*)", an):
        ans = f"{match.group(1)}s{match.group(2)}"
        ans1 = "sakAra"
        ans2 = "namaspurasorgawyoH (8.3.40)"
        cont = 0

    if match := re.search(r"^wiraH\+([kp].*)", an):
        ans = f"wiras{match.group(1)}:wiraH {match.group(1)}"
        ans1 = "sakAra:sawwvABAve"
        ans2 = "wirasoZnyawarasyAm (8.3.42)"
        cont = 0

    if match := re.search(r"^(ap|av|up)a\+q(.*)", an):
        ans = f"{match.group(1)}Ar{match.group(2)}"
        ans1 = "vqxXi"
        ans2 = "upasargAxqwi XAwoH(6.1.91)"
        cont = 0

    if match := re.search(r"(.*)pra\+([eo].*)", an):
        ans = f"{match.group(1)}pr{match.group(2)}"
        ans1 = "pararUpa"
        ans2 = "efi pararUpam (6.1.94)"
        cont = 0
    if match := re.search(r"(.*[aAou])pa\+([eo].*)", an):
        ans = f"{match.group(1)}p{match.group(2)}"
        ans1 = "pararUpa"
        ans2 = "efi pararUpam(6.1.94)"
        cont = 0
    if not re.search(r"wava\+([eo].*)", an):
        if match := re.search(r"(.*[aA])va\+([eo].*)", an):
            ans = f"{match.group(1)}v{match.group(2)}"
            ans1 = "pararUpa"
            ans2 = "efi pararUpam(6.1.94)"
            cont = 0

    if match := re.search(r"(.*)a\+(o[mzfFnN].*)", an):
        ans = f"{match.group(1)}{match.group(2)}"
        ans1 = "pararUpa"
        ans2 = "omAfoSca(6.1.95)"
        cont = 0

    if match := re.search(r"^go\+a(.*)", an):
        ans = f"go a{match.group(1)}:gavA{match.group(1)}"
        ans1 = "prakqwiBAva:avafAxeSa"
        ans2 = "sarvawra viBARA goH(6.1.122):avaf sPotAyanasya(6.1.123)-> akaH savarNe xIrGaH (6.1.101)"
        cont = 1

    # Why was it necessary to give another suutra inxre ca? Already with 6.1.123 '^i' is covered.
    if match := re.search(r"^go\+inxr(.*)", an):
        ans = f"gavenxr{match.group(1)}"
        ans1 = "avafAxeSa"
        ans2 = "inxre ca(6.1.124)-> Ax guNaH (6.1.87)"
        cont = 0
    elif match := re.search(r"^go\+([iI])(.*)", an):
        ans = f"gave{match.group(2)}"
        ans1 = "avafAxeSa"
        ans2 = "avaf sPotAyanasya(6.1.123)-> Ax guNaH (6.1.87)"
        cont = 0

    if match := re.search(r"^go\+([uU])(.*)", an):
        ans = f"gavo{match.group(2)}"
        ans1 = "avafAxeSa"
        ans2 = "avaf sPotAyanasya(6.1.123)-> Ax guNaH (6.1.87)"
        cont = 0
    if match := re.search(r"^go\+([qQ])(.*)", an):
        ans = f"gavar{match.group(2)}"
        ans1 = "avafAxeSa"
        ans2 = "avaf sPotAyanasya(6.1.123)-> Ax guNaH (6.1.87)"
        cont = 0
    if match := re.search(r"^go\+(L)(.*)", an):
        ans = f"gaval{match.group(2)}"
        ans1 = "avafAxeSa"
        ans2 = "avaf sPotAyanasya(6.1.123)-> Ax guNaH (6.1.87)"
        cont = 0
    if match := re.search(r"^go\+([eE])(.*)", an):
        ans = f"gavE{match.group(2)}"
        ans1 = "avafAxeSa"
        ans2 = "avaf sPotAyanasya(6.1.123)-> Ax guNaH (6.1.87)"
        cont = 0
    if match := re.search(r"^go\+([oO])(.*)", an):
        ans = f"gavO{match.group(2)}"
        ans1 = "avafAxeSa"
        ans2 = "avaf sPotAyanasya(6.1.123)-> Ax guNaH (6.1.87)"
        cont = 0

    if match := re.search(r"(.*)[tTdDN]\+n(Am|avawi|agar.*)$", an):
        ans = f"{match.group(1)}NN{match.group(2)}"
        ans1 = "jaSwva-> RtuwvaniReXaH-> Nawva"
        ans2 = "JalAM jaSoZnwe # (8.2.39)-> RtunA RtuH # (8.4.41)[Rtuwve prApwe]-> na paxAnwAttoranAm # (8.4.42)-> anAmnavawinagarINAmiwi vAcyam(vA 5016)-> yaroZnunAsikeZnunAsiko vA (8.4.45)-> prawyaye BARAyAm niwyam (vA 5017)"
        cont = 0
    if match := re.search(r"^am([IU])\+(.*)", an):
        ans = f"am{match.group(1)} {match.group(2)}"
        ans1 = "prakqwiBAva"
        ans2 = "axaso mAw(1.1.12)"
        cont = 0

    if match := re.search(r"^uw\+sWA(.*)", an):
        ans = f"uwWA{match.group(1)}:uwWWA{match.group(1)}"
        ans1 = "pUrvasavarNaH->lopaH:pUrvasavarNaH->lopABAvaH"
        ans2 = "uxaH sWAswamBoH pUrvasya (8.4.61)->Jaro Jari savarNe (8.4.65)"
        cont = 0

    if match := re.search(r"^uw\+swamB(.*)", an):
        ans = f"uwwamB{match.group(1)}:uwWwamB{match.group(1)}"
        ans1 = "pUrvasavarNaH->lopaH:pUrvasavarNaH->lopABAvaH"
        ans2 = "uxaH sWAswamBoH pUrvasya (8.4.61)->Jaro Jari savarNe (8.4.65)"
        cont = 0

    if match := re.search(r"(.*)([kKgG])\+S([aAiIuUqQLeEoOhyvr])(.*)", an):
        ans = f"{match.group(1)}kC{match.group(3)}{match.group(4)}"
        ans1 = "jaSwva->carwva->Cawva"
        ans2 = "JalAM jaSoZnwe (8.2.39)->Kari ca (8.4.55)->SaSCoZti (8.4.63)"
        cont = 1

    if match := re.search(r"(.*)([cCjJ])\+S([aAiIuUqQLeEoOhyvr])(.*)", an):
        ans = f"{match.group(1)}cC{match.group(3)}{match.group(4)}"
        ans1 = "jaSwva->carwva->Cawva"
        ans2 = "JalAM jaSoZnwe (8.2.39)->Kari ca (8.4.55)->SaSCoZti (8.4.63)"
        cont = 1

    if match := re.search(r"(.*)([tTdD])\+S([aAiIuUqQLeEoOhyvr])(.*)", an):
        ans = f"{match.group(1)}tC{match.group(3)}{match.group(4)}"
        ans1 = "jaSwva->carwva->Cawva"
        ans2 = "JalAM jaSoZnwe (8.2.39)->Kari ca (8.4.55)->SaSCoZti (8.4.63)"
        cont = 1

    if match := re.search(r"(.*)([wWxX])\+S([aAiIuUqQLeEoOhyvr])(.*)", an):
        ans = f"{match.group(1)}cC{match.group(3)}{match.group(4)}"
        ans1 = "jaSwva->Scuwva->carwva->Cawva"
        ans2 = "JalAM jaSoZnwe (8.2.39)->swoH ScunA ScuH (8.4.40)->Kari ca (8.4.55)->SaSCoZti (8.4.63)"
        cont = 1

    if match := re.search(r"(.*)([pPbB])\+S([aAiIuUqQLeEoOhyvr])(.*)", an):
        ans = f"{match.group(1)}pC{match.group(3)}{match.group(4)}"
        ans1 = "jaSwva->carwva->Cawva"
        ans2 = "JalAM jaSoZnwe (8.2.39)->Kari ca (8.4.55)->SaSCoZti (8.4.63)"
        cont = 1

    if match := re.search(r"(.*)(n)\+S([aAiIuUqQLeEoOhyvr])(.*)", an):
        ans = f"{match.group(1)}FC{match.group(3)}{match.group(4)}:{match.group(1)}FcC{match.group(3)}{match.group(4)}"
        ans1 = "wugAgama->Scuwva->carwva->Cawva->lopaH:wugAgama->Scuwva->carwva->Cawva->lopABAvaH"
        ans2 = "Si wuk (8.3.31)->swoH ScunA ScuH (8.4.40)->Kari ca (8.4.55)->SaSCoZti (8.4.63)->Jaro Jari savarNe (8.4.65):wugAgama->Scuwva->carwva->Cawva->lopABAvaH"
        ans2 = (
            ans2
            + ":"
            + "Si wuk (8.3.31)->swoH ScunA ScuH (8.4.40)->Kari ca (8.4.55)->SaSCoZti (8.4.63)"
        )
        cont = 1

    if match := re.search(r"(.*)([kKgG])\+S([lfmFNn])(.*)", an):
        ans = f"{match.group(1)}kC{match.group(3)}{match.group(4)}:{match.group(1)}kS{match.group(3)}{match.group(4)}"
        ans1 = "jaSwva->carwva->Cawva:jaSwva->carwva->CawvABAva"
        ans2 = "JalAM jaSoZnwe (8.2.39)->Kari ca (8.4.55)->CawvamamIwi vAcyam (vA 5025):JalAM jaSoZnwe (8.2.39)->Kari ca (8.4.55)"
        cont = 0

    if match := re.search(r"(.*)([cCjJ])\+S([lFmfNn])(.*)", an):
        ans = f"{match.group(1)}cC{match.group(3)}{match.group(4)}:{match.group(1)}cS{match.group(3)}{match.group(4)}"
        ans1 = "jaSwva->carwva->Cawva:jaSwva->carwva->CawvABAva"
        ans2 = "JalAM jaSoZnwe (8.2.39)->Kari ca (8.4.55)->CawvamamIwi vAcyam (vA 5025):JalAM jaSoZnwe (8.2.39)->Kari ca (8.4.55)"
        cont = 0

    if match := re.search(r"(.*)([tTdD])\+S([lFmfNn])(.*)", an):
        ans = f"{match.group(1)}tC{match.group(3)}{match.group(4)}:{match.group(1)}tS{match.group(3)}{match.group(4)}"
        ans1 = "jaSwva->carwva->Cawva:jaSwva->carwva->CawvABAva"
        ans2 = "JalAM jaSoZnwe (8.2.39)->Kari ca (8.4.55)->CawvamamIwi vAcyam (vA 5025):JalAM jaSoZnwe (8.2.39)->Kari ca (8.4.55)"
        cont = 0

    if match := re.search(r"(.*)([wWxX])\+S([lFmfNn])(.*)", an):
        ans = f"{match.group(1)}cC{match.group(3)}{match.group(4)}:{match.group(1)}cS{match.group(3)}{match.group(4)}"
        ans1 = "jaSwva->Scuwva->carwva->Cawva:jaSwva->carwva->CawvABAva"
        ans2 = "JalAM jaSoZnwe (8.2.39)->swoH ScunA ScuH (8.4.40)->Kari ca (8.4.55)->CawvamamIwi vAcyam (vA 5025):JalAM jaSoZnwe (8.2.39)->swoH ScunA ScuH (8.4.40)->Kari ca (8.4.55)"
        cont = 0

    if match := re.search(r"(.*)([pPbB])\+S([lfFmnN])(.*)", an):
        ans = f"{match.group(1)}pC{match.group(3)}{match.group(4)}:{match.group(1)}pS{match.group(3)}{match.group(4)}"
        ans1 = "jaSwva->carwva->Cawva:jaSwva->carwva->CawvABAva"
        ans2 = "JalAM jaSoZnwe (8.2.39)->Kari ca (8.4.55)->CawvamamIwi vAcyam (vA 5025):JalAM jaSoZnwe (8.2.39)->Kari ca (8.4.55)"
        cont = 0

    if match := re.search(r"^praSAn\+([cC])([aAiIuUqQLeEoOhyvr])(.*)", an):
        ans = f"praSAF{match.group(1)}{match.group(2)}{match.group(3)}"
        ans1 = "ruwvaniReXa->Scuwva"
        ans2 = "naSCavyapraSAn (8.3.7)-> swoH ScunA ScuH (8.4.40)"
        cont = 0
    if match := re.search(r"^praSAn\+([tT])([aAiIuUqQLeEoOhyvr])(.*)", an):
        ans = f"praSAN{match.group(1)}{match.group(2)}{match.group(3)}"
        ans1 = "ruwvaniReXa->Rtuwva"
        ans2 = "naSCavyapraSAn (8.3.7)-> RtunA RtuH (8.4.41)"
        cont = 0
    if match := re.search(r"^praSAn\+([wW])([aAiIuUqQLeEoOhyvr])(.*)", an):
        ans = f"praSAn{match.group(1)}{match.group(2)}{match.group(3)}"
        ans1 = "ruwvaniReXa"
        ans2 = "naSCavyapraSAn (8.3.7)"
        cont = 0

    if match := re.search(r"(.*)n\+([cC])([aAiIuUqQLeEoOhyvr])(.*)", an):
        ans = f"{match.group(1)}zS{match.group(2)}{match.group(3)}{match.group(4)}:{match.group(1)}MS{match.group(2)}{match.group(3)}{match.group(4)}"
        ans1 = "ruwva:ruwva"
        ans2 = "naSCavyapraSAn (8.3.7)-> awrAnunAsikaH pUrvasya wu vA (8.3.2)-> KaravasAnayorvisarjanIyaH (8.3.15)-> visarjanIyasya saH (8.3.34)-> swoH ScunA ScuH (8.4.40):naSCavyapraSAn (8.3.7)-> awrAnunAsikaH pUrvasya wu vA (8.3.2)-> KaravasAnayorvisarjanIyaH (8.3.15)-> visarjanIyasya saH (8.3.34)-> swoH ScunA ScuH (8.4.40)"
        cont = 0

    if match := re.search(r"(.*)n\+([tT])([aAiIuUqQLeEoOhyvr])(.*)", an):
        ans = f"{match.group(1)}zR{match.group(2)}{match.group(3)}{match.group(4)}:{match.group(1)}MR{match.group(2)}{match.group(3)}{match.group(4)}"
        ans1 = "ruwva:ruwva"
        ans2 = "naSCavyapraSAn (8.3.7)->awrAnunAsikaH pUrvasya wu vA (8.3.2)->KaravasAnayorvisarjanIyaH (8.3.15)->visarjanIyasya saH (8.3.34)->RtunA RtuH (8.4.41):naSCavyapraSAn (8.3.7)->anunAsikAw paroZnusvAraH (8.3.4)->KaravasAnayorvisarjanIyaH (8.3.15)->visarjanIyasya saH (8.3.34)->RtunA RtuH (8.4.41)"
        cont = 0

    if match := re.search(r"(.*)n\+([wW])([aAiIuUqQLeEoOhyvr])(.*)", an):
        ans = f"{match.group(1)}zs{match.group(2)}{match.group(3)}{match.group(4)}:{match.group(1)}Ms{match.group(2)}{match.group(3)}{match.group(4)}"
        ans1 = "ruwva:ruwva"
        ans2 = "naSCavyapraSAn (8.3.7)->awrAnunAsikaH pUrvasya wu vA (8.3.2)->KaravasAnayorvisarjanIyaH (8.3.15)->visarjanIyasya saH (8.3.34) :naSCavyapraSAn (8.3.7)->anunAsikAw paroZnusvAraH (8.3.4)->KaravasAnayorvisarjanIyaH (8.3.15)->visarjanIyasya saH (8.3.34)"
        cont = 0

    if match := re.search(r"^nQn\+p(.*)", an):
        ans = f"nQz><p{match.group(1)}:nQM><p{match.group(1)}:nQzHp{match.group(1)}:nQMHp{match.group(1)}:nQnp{match.group(1)}"
        ans1 = "ruwva:ruwva:ruwva:ruwva:ruwvABAve"
        ans2 = "nQnpe (8.3.10)->awrAnunAsikaH pUrvasya wu vA (8.3.2)->KaravasAnayorvisarjanIyaH (8.3.15)->kupvoH><ka><pO ca (8.3.37):nQnpe (8.3.10)->anunAsikAw paroZnusvAraH (8.3.4)->KaravasAnayorvisarjanIyaH (8.3.15)->kupvoH><ka><pO ca (8.3.37):nQnpe (8.3.10)->awrAnunAsikaH pUrvasya wu vA (8.3.2)->KaravasAnayorvisarjanIyaH (8.3.15)->visarjanIyasya saH (8.3.34):nQnpe (8.3.10)->anunAsikAw paroZnusvAraH (8.3.4)->KaravasAnayorvisarjanIyaH (8.3.15)->visarjanIyasya saH (8.3.34):nQnpe (8.3.10)"
        cont = 0

    if match := re.search(r"^kAn\+kAn$", an):
        ans = "kAzskAn:kAMskAn"
        ans1 = "ruwva:ruwva"
        ans2 = "kAnAmrediwe (8.3.12)->awrAnunAsikaH pUrvasya wu vA (8.3.2)->KaravasAnayorvisarjanIyaH (8.3.15)->saMpuMkAnAM so vakwavyaH (vA 4892):kAnAmrediwe (8.3.12)->awrAnunAsikaH pUrvasya wu vA (8.3.2)->KaravasAnayorvisarjanIyaH (8.3.15)->saMpuMkAnAM so vakwavyaH (vA 4892)"
        cont = 0

    if match := re.search(r"pum\+([kKcCtTwWpP])([aAiIuUqQLeEoOhyvr])(.*)", an):
        ans = f"puMs{match.group(1)}{match.group(2)}{match.group(3)}:puzs{match.group(1)}{match.group(2)}{match.group(3)}"
        ans1 = "ruwva:ruwva"
        ans2 = "pumaH Kayyampare (8.3.6)->anunAsikAw paroZnusvAraH (8.3.4)->KaravasAnayorvisarjanIyaH (8.3.15)->saMpuMkAnAM so vakwavyaH (vA 4892):pumaH Kayyampare (8.3.6)->awrAnunAsikaH pUrvasya wu vA (8.3.2)->KaravasAnayorvisarjanIyaH (8.3.15)->saMpuMkAnAM so vakwavyaH (vA 4892)"
        cont = 0

    if match := re.search(r"(.*)H\+([KPCTWctwkpSRs])([SRs])(.*)", an):
        ans = f"{match.group(1)}H {match.group(2)}{match.group(3)}{match.group(4)}"
        ans1 = "visarga"
        ans2 = "Sarpare visarjanIyaH (8.3.35)"
        cont = 0

    if match := re.search(r"(.*)H\+([SRs])([KPCTWctwkpSRs])(.*)", an):
        ans = f"{match.group(1)} {match.group(2)}{match.group(3)}{match.group(4)}:{match.group(1)}H {match.group(2)}{match.group(3)}{match.group(4)}:{match.group(1)}{match.group(2)}{match.group(2)}{match.group(3)}{match.group(4)}"
        ans1 = "visargalopaH:visargalopABAve:sawva"
        ans2 = "Karpare Sari vA visargalopo vakwavyaH (vA 4906):Karpare Sari vA visargalopo vakwavyaH (vA 4906):visarjanIyasya saH (8.3.34)"
        cont = 0

    if match := re.search(r"^sam\+rAt", an):
        ans = "samrAt"
        ans1 = "mawva"
        ans2 = "mo rAji samaH kvO (8.2.35)"
        cont = 0

    if match := re.search(r"(.*)m\+hm(.*)", an):
        ans = (
            f"{match.group(1)}n hm{match.group(2)}:{match.group(1)}M hm{match.group(2)}"
        )
        ans1 = "mawva:anusvAraH"
        ans2 = "he mapare vA (8.3.26):moZnusvAraH (8.3.23)"
        cont = 0

    if match := re.search(r"(.*)m\+h([yvl])(.*)", an):
        ans = f"{match.group(1)}{match.group(2)}z h{match.group(2)}{match.group(3)}:{match.group(1)}M h{match.group(2)}{match.group(3)}"
        ans1 = "anunAsika:anusvAraH"
        ans2 = "yavalapare yavalA vewi vakwavyam (vA 4902):moZnusvAraH (8.3.23)"
        cont = 0

    if match := re.search(r"(.*)m\+hn(.*)", an):
        ans = (
            f"{match.group(1)}n hn{match.group(2)}:{match.group(1)}M hn{match.group(2)}"
        )
        ans1 = "nawva:anusvAraH"
        ans2 = "na pare naH (8.3.27):moZnusvAraH (8.3.23)"
        cont = 0

    if match := re.search(r"^(eRa|sa)H\+([gGfcCjJFtTdDNwWxXnbBmyrlvh])(.*)", an):
        ans = f"{match.group(1)} {match.group(2)}{match.group(3)}"
        ans1 = "visargalopa"
        ans2 = "ewawwaxoH sulopoZkoranaFsamAse hali (6.1.132)"
        cont = 0

    if match := re.search(
        r"(.*)[aA]\+e(wi|Ri|mi|wA|wArO|wAraH|wAsi|wAsWaH|wAsWa|wAsmi|wAsvaH|wAsmaH|Ryawi|RyawaH|Ryanwi|Ryasi|RyaWaH|RyaWa|RyAmi|RyAvaH|RyAmaH|wu)$",
        an,
    ):
        ans = f"{match.group(1)}E{match.group(2)}"
        ans1 = "vqxXi"
        ans2 = "ewyeXawyUTsu (6.1.86)"
        cont = 0
    if match := re.search(
        r"(.*)[aA]\+E(w|wAm|H|wam|wa|va|ma|Ryaw|RyawAm|Ryan|RyaH|Ryawam|Ryawa|Ryam|RyAva|RyAma)$",
        an,
    ):
        ans = f"{match.group(1)}E{match.group(2)}"
        ans1 = "vqxXi"
        ans2 = "ewyeXawyUTsu (6.1.86)"
        cont = 0

    if match := re.search(r"(.*)[aA]\+[eE]X(.*)", an):
        ans = f"{match.group(1)}EX{match.group(2)}"
        ans1 = "vqxXi"
        ans2 = "ewyeXawyUTsu (6.1.86)"
        cont = 0

    if match := re.search(r"(.*)[aA]\+Uha(.*)", an):
        ans = f"{match.group(1)}Oha{match.group(2)}"
        ans1 = "vqxXi"
        ans2 = "ewyeXawyUTsu (6.1.86)"
        cont = 0

    if match := re.search(r"^ahan\+(rUpa|rAwr|raWanwara)(.*)", an):
        ans = f"aho {match.group(1)}{match.group(2)}"
        ans1 = "ruwva-> uwva-> guNa"
        ans2 = "roZsupi (8.2.69)(prApwe) -> rUparAwri raWanwareRuruwvam vAcyam (vA 4847)-> haSi ca (6.1.114)-> Ax guNaH (6.1.87)"
        cont = 0

    if match := re.search(r"^ahan\+(pawi|puwra)(.*)", an):
        ans = f"ahar{match.group(1)}{match.group(2)}:ahaH {match.group(1)}{match.group(2)}:aha><{match.group(1)}{match.group(2)}"
        ans1 = "rePa:visarga:upaXmAnIya"
        ans2 = "roZsupi (8.2.69)-> KaravasAnayorvisarjanIyaH (8.3.15) (prApwe)-> aharAxInAm pawyAxiRu vA rePaH (vA 4851):roZsupi (8.2.69) -> KaravasAnayorvisarjanIyaH (8.3.15)-> kupvo><ka><pO ca (8.3.37):roZsupi (8.2.69) -> KaravasAnayorvisarjanIyaH (8.3.15)-> kupvo><ka><pO ca (8.3.37)"
        cont = 0

    if match := re.search(r"^ahan\+gaNa(.*)", an):
        ans = f"ahargaNa{match.group(1)}"
        ans1 = "rePa"
        ans2 = "roZsupi (8.2.69)"
        cont = 0

    if match := re.search(r"^gIr\+(pawi|puwra)(.*)", an):
        ans = f"gIr{match.group(1)}{match.group(2)}:gI><{match.group(1)}{match.group(2)}:gIH {match.group(1)}{match.group(2)}"
        ans1 = "rePa:upaXmAnIya:visarga"
        ans2 = "KaravasAnayorvisarjanIyaH (8.3.15)(prApwe) -> aharAxInAm pawyAxiRu vA rePaH (vA 4851):KaravasAnayorvisarjanIyaH (8.3.15)-> kupvo><ka><pO ca (8.3.37):KaravasAnayorvisarjanIyaH (8.3.15)-> kupvo><ka><pO ca (8.3.37)"
        cont = 0

    if match := re.search(r"^gIr\+gaNa(.*)", an):
        ans = f"gIrgaNa{match.group(1)}"
        ans1 = "rePa"
        ans2 = "roZsupi (8.2.69)"
        cont = 0

    if match := re.search(r"^XUr\+(pawi|puwra)(.*)", an):
        ans = f"XUr{match.group(1)}{match.group(2)}:XU><{match.group(1)}{match.group(2)}:XUH {match.group(1)}{match.group(2)}"
        ans1 = "rePa:upaXmAnIya:visarga"
        ans2 = "KaravasAnayorvisarjanIyaH (8.3.15)(prApwe)-> aharAxInAm pawyAxiRu vA rePaH (vA 4851):KaravasAnayorvisarjanIyaH (8.3.15)-> kupvo><ka><pO ca (8.3.37):KaravasAnayorvisarjanIyaH (8.3.15)-> kupvo><ka><pO ca (8.3.37)"
        cont = 0

    if match := re.search(r"^XUr\+gaNa(.*)", an):
        ans = f"XUrgaNa{match.group(1)}"
        ans1 = "rePa"
        ans2 = "roZsupi (8.2.69)"
        cont = 0

    if match := re.search(r"^ahan\+ahaH$", an):
        ans = "aharahaH"
        ans1 = "rePa"
        ans2 = "roZsupi (8.2.69)"
        cont = 0
    elif match := re.search(r"(.*)([aiuqL])([fNn])\+([aAiIuUqQLeEoO])(.*)", an):
        ans = f"{match.group(1)}{match.group(2)}{match.group(3)}{match.group(3)}{match.group(4)}{match.group(5)}"
        ans1 = "famudAgama"
        ans2 = "famo hrasvAxaci famuNniwyam (8.3.32)"
        cont = 0
    elif match := re.search(r"(.*)([^aiuqL])([fNn])\+([aAiIuUqQLeEoO])(.*)", an):
        ans = f"{match.group(1)}{match.group(2)}{match.group(3)}{match.group(4)}{match.group(5)}"
        ans1 = "diPAlta"
        ans2 = ""
        cont = 0

    if match := re.search(
        r"(.*)([iIuUqQLeEoO])H\+([aAiIuUqQLeEoOgGfjJFdDNxXnbBmylvh])(.*)", an
    ):
        ans = f"{match.group(1)}{match.group(2)}r{match.group(3)}{match.group(4)}"
        ans1 = "rePa"
        ans2 = "sasajuRo ruH (8.2.66)"
        cont = 0

    if match := re.search(r"^(eRa|sa)H\+([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSRsh])(.*)", an):
        ans = f"{match.group(1)} {match.group(2)}{match.group(3)}"
        ans1 = "visargalopa"
        ans2 = "ewawwaxoH sulopoZkoranaFsamAse hali (6.1.132)"
        cont = 0
    elif match := re.search(r"(.*)aH\+([gGfjJFdDNxXnbBmyrlvh])(.*)", an):
        ans = f"{match.group(1)}o {match.group(2)}{match.group(3)}"
        ans1 = "ruwva-> uwva-> guNa"
        ans2 = "sasajuRo ruH (8.2.66)-> haSi ca (6.1.114)-> Ax guNaH (6.1.87)"
        cont = 0
    elif match := re.search(r"^BoH\+([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSRsh])(.*)", an):
        ans = f"Bos{match.group(1)}{match.group(2)}"
        ans1 = ""
        ans2 = "sasajuRo ruH (8.2.66)-> KaravasAnayorvisarjanIyaH (8.3.15)-> visarjanIyasya saH (8.3.34)"
        cont = 0
    elif match := re.search(
        r"^(Bago|aGo)H\+([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSRsh])(.*)", an
    ):
        ans = f"{match.group(1)} {match.group(2)}{match.group(3)}"
        ans1 = "yawvalopaH"
        ans2 = "sasajuRo ruH (8.2.66)->BoBagoaGo apUrvasyayoZSi (8.3.17)->hali sarveRAm (8.3.22)"
        cont = 0
    elif match := re.search(r"^(Bo|Bago|aGo)H\+([aAiIuUqQLeEoO])(.*)", an):
        ans = f"{match.group(1)}y{match.group(2)}{match.group(3)}:{match.group(1)} {match.group(2)}{match.group(3)}"
        ans1 = "sawva->yawva->laGuprayawnAxeSaH sawva->yawva->laGuprayawnABAve yawvalop"
        ans2 = "sasajuRo ruH (8.2.66)->BoBagoaGo apUrvasyayoZSi (8.3.17)->vyorlaGuprayawnawaraH SAkatAyanasya (8.3.18):sasajuRo ruH (8.2.66)->BoBagoaGo apUrvasyayoZSi (8.3.17)->owo gArgyasya (8.3.20)"
        cont = 0
    elif match := re.search(r"(.*)([aAiIuUqQLeEoO])H\+([wW])([^sSR].*)", an):
        ans = f"{match.group(1)}{match.group(2)}s{match.group(3)}{match.group(4)}"
        ans1 = "sawva"
        ans2 = "visarjanIyasya saH (8.3.34)"
        cont = 0
    elif match := re.search(r"(.*)([aAiIuUqQLeEoO])H\+([cC])(.*)", an):
        ans = f"{match.group(1)}{match.group(2)}S{match.group(3)}{match.group(4)}"
        ans1 = "sawva-> Scuwva"
        ans2 = "visarjanIyasya saH (8.3.34)-> swoH ScunA ScuH (8.4.40)"
        cont = 0
    elif match := re.search(r"(.*)([aAiIuUqQLeEoO])H\+([tT])(.*)", an):
        ans = f"{match.group(1)}{match.group(2)}R{match.group(3)}{match.group(4)}"
        ans1 = "sawva-> Rtuwva"
        ans2 = "visarjanIyasya saH (8.3.34)-> RtunA RtuH (8.4.41)"
        cont = 0
    elif match := re.search(r"(.*)AH\+([gGfjJFdDNxXnbBmyrlvh])(.*)", an):
        ans = f"{match.group(1)}A {match.group(2)}{match.group(3)}"
        ans1 = "ruwva-> yawva-> lopa"
        ans2 = "sasajuRo ruH (8.2.66)-> BoBagoaGo apUrvasya yoZSi (8.3.17)-> hali sarveRAm (8.3.22)"
        cont = 0

    if match := re.search(
        r"^(miWo|ho|aho|Aho|uwAho|no|aWo)\+([aAiIuUqQLeEoO])(.*)", an
    ):
        ans = f"{match.group(1)} {match.group(2)}{match.group(3)}"
        ans1 = "pragqhyawva->prakqwiBAva"
        ans2 = "ow (1.1.15)-> pluwapragqhyA aci niwyam (6.1.125)"
        cont = 0

    if match := re.search(r"^([aiuqLeEoO])\+([aAiIuUqQLeEoO])(.*)", an):
        ans = f"{match.group(1)} {match.group(2)}{match.group(3)}"
        ans1 = "pragqhyawva->prakqwiBAva"
        ans2 = "nipAwa ekAjanAf (1.1.14)-> pluwapragqhyA aci niwyam (6.1.125)"
        cont = 0

    if match := re.search(r"^uF\+iwi", an):
        ans = "u iwi:Uz iwi:viwi"
        ans1 = "vikalpena pragqhyawva-> prakqwiBAva:vikalpena Uz AxeSa->pragqhyawva->prakqwiBAva :vikalpABAve yaN"
        ans2 = "uFaH (1.1.17)-> pluwapragqhyA aci niwyam (6.1.125):Uz (1.1.18)-> pluwapragqhyA aci niwyam (6.1.125):iko yaNaci (6.1.77)"
        cont = 0

    if match := re.search(r"^(kR|j)i\+ya(.*)", an):
        ans = (
            f"{match.group(1)}ayya{match.group(2)}:{match.group(1)}eya{match.group(2)}"
        )
        ans1 = "SakyArWe ayAxeSa nipAwana:SakyArWABAve guNa"
        ans2 = "kRayyajayyO SakyArWe (6.1.81):sArvaXAwukArXaXAwukayoH (7.3.84"
        cont = 0

    if match := re.search(r"^krI\+ya(.*)", an):
        ans = f"krayya{match.group(1)}:kreya{match.group(1)}"
        ans1 = "krayaNArhe ayAxeSa nipAwanam:krayaNArhABAve guNa"
        ans2 = "krayyaswaxarWe (6.1.82):sArvaXAwukArXaXAwukayoH (7.3.84)"
        cont = 0

    if match := re.search(r"^(aXa|Sira)H\+paxa(.*)", an):
        ans = f"{match.group(1)}spaxa{match.group(2)}:{match.group(1)}><paxa{match.group(2)}:{match.group(1)}H paxa{match.group(2)}"
        ans1 = "samAse sawva:upaXmAnIya:visarga"
        ans2 = "aXaSSirasI paxe (8.3.47):kupvo ><ka ><pO ca (8.3.37):kupvo ><ka ><pO ca (8.3.37)"
        cont = 0

    if match := re.search(r"(.*[iu])H\+([kKpP])(.*)", an):
        ans = f"{match.group(1)}R{match.group(2)}{match.group(3)}:{match.group(1)}><{match.group(2)}{match.group(3)}:{match.group(1)}H {match.group(2)}{match.group(3)}"
        ans1 = "sAmarWye Rawvam:RawvABAve jihvAmUlIya:RawvABAve visarga"
        ans2 = "isusoH sAmarWye (8.3.44):kupvo><ka ><pO ca (8.3.37):kupvo><ka ><pO ca (8.3.37)"
        cont = 0

    # print "ans = $ans\n";
    # print "ans1 = $ans1\n";
    # print "ans2 = $ans2\n";
    # print "cont = $cont\n";
    ### $cont = 1 indicates, the regular rules are to be applied after these exceptional rules.
    ## $cont = 0  means after these exce[tional rules are applied, do not apply the regular rules.
    return (ans, ans1, ans2, cont)


# if the SabxaH or XAxu have xvivacan and the second word will start with 'I' 'U' 'e' then there is prakqwiBAva (IxUxexxvivacanaM pragqhyam)
# if the first word is ending with 'a' or 'A' and the second word is an 'i' Xaxu or 'eX' XAxu started with the letter 'e', or the word is 'UD' then there is vqxXi sanXi. (ewyeXwyUDsu)
# if the first word is either 'amU' or 'amI' then there is no sanXi (axaso mAw)
