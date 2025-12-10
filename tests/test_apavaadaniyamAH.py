# test_apavAdaniyamAH.py
import subprocess
import sys
from sandhi.apavaada import apavAdaniyamAH


def test_apavaadas():
    perl_script_path = "apavaadaniyamAH.pl"

    test_cases = [
        # rule: (axy)a\+i(fKawi)
        "axya+ifKawi",
        # rule: (axy)a\+u(fKawi)
        "axya+ufKawi",
        # rule: akRa\+Uhin(.*)
        "akRa+Uhini",
        # rule: sva\+Iri([nN].*)
        "sva+Irina",
        "sva+IriNI",
        "sva+IrinI",
        # rule: sva\+IraH
        "sva+IraH",
        # rule: pra\+U([hD].*)
        "pra+UhaH",
        "pra+UDaH",
        # rule: pra\+eR(.*)
        "pra+eRaH",
        # rule: (vawsawar|kambal|vasan|qN|xaS)a\+qN(.*)
        "vawsawara+qNaH",
        "kambala+qNam",
        # rule: pra\+qN(.*)
        "pra+qNam",
        # rule: pra\+q(.*) (must not be pra+qN)
        "pra+qwam",
        # # rule: (.*)o\+yam$
        "go+yam",
        # rule: (.*)O\+yam$
        "nO+yam",
        # rule: go\+yUw(.*)
        "go+yUwiH",
        # rule: (Saka|karka)\+anXuH$
        "Saka+anXuH",
        "karka+anXuH",
        # rule: kula\+atA$
        "kula+atA",
        # rule: hala\+IRA$
        "hala+IRA",
        # rule: lAfgala\+IRA$
        "lAfgala+IRA",
        # # rule: manas\+IRA$
        "manas+IRA",
        # rule: mArwa\+aNdaH$
        "mArwa+aNdaH",
        # rule: pawaw\+aFjaliH$
        "pawaw+aFjaliH",
        # rule: sIman\+anwaH$
        "sIman+anwaH",
        # rule: sAra\+afg(.*)
        "sAra+afgaH",
        # rule: (.*)([aA])\+owuH
        "upagoSa+owuH",
        # rule: (.*)([aA])\+oRT(.*)
        "upasargaA+oRTaH",
        # rule: kaskAxiRu group
        "kaH+kaH",
        "kOwaH+kuwaH",
        "BrAwuH+puwraH",
        "SunaH+karNaH",
        "saxyaH+kAlaH",
        "kAMH+kAn",
        "sarpiH+kuNdikA",
        "XanuH+kapAlam",
        "barhiH+palam",
        "barbiH+palam",  # test with optional 'r'
        "yajuH+pAwram",
        "ayaH+kAnwaH",
        "wamaH+kANdaH",
        "ayaH+kANdaH",
        "mexaH+piNdaH",
        "BAH+karaH",
        "ahaH+karaH",
        # rule: (nama|pura)H\+([kp].*)
        "namaH+karowi",
        "puraH+prawi",
        # rule: wiraH\+([kp].*)
        "wiraH+karowi",
        # rule: (ap|av|up)a\+q(.*)
        "apa+qwam",
        "ava+qwam",
        "upa+qwam",
        # rule: (.*)pra\+([eo].*)
        "pra+ejate",
        # rule: (.*[aAou])pa\+([eo].*)
        "upa+owuH",
        # rule: (.*[aA])va\+([eo].*) (but not wava+)
        "Bava+ewaw",
        # rule: (.*)a\+(o[mzfFnN].*)
        "Bava+om",
        # rule: go\+a(.*)
        "go+agram",
        # rule: go\+inxr(.*)
        "go+inxraH",
        # rule: go\+([iI])(.*) (but not go+inxr)
        "go+iwam",
        # rule: go\+([uU])(.*)
        "go+UhaH",
        # rule: go\+([qQ])(.*)
        "go+qwam",
        # rule: go\+(L)(.*)
        "go+Lkwam",
        # rule: go\+([eE])(.*)
        "go+ewaw",
        # rule: go\+([oO])(.*)
        "go+owuH",
        # rule: (.*)[tTdDN]\+n(Am|avawi|agar.*)$
        "Raw+nAm",
        "RaD+navawi",
        "san+nagari",
        # rule: am([IU])\+(.*)
        "amU+AswAm",
        "amI+iha",
        # rule: uw\+sWA(.*)
        "uw+sWAnam",
        # rule: uw\+swamB(.*)
        "uw+swamBanam",
        # rule: Cawva rules ([kKgG], [cCjJ], etc. + S + vowel/semivowel)
        "vAk+SuraH",  # kKgG group
        "rAj+Sobane",  # cCjJ group
        "Bavat+Sete",  # tTdD group
        "rAw+Sete",  # wWxX (ṭ वर्ग) group
        "gup+SAsiwum",  # pPbB group
        "paxAnwAn+SAsiwum",  # n group
        # # rule: Cawva rules with following [lfmFNn]
        "vAk+SlokaH",  # kKgG group
        "vAc+SmaSru",  # cCjJ group
        "Bavat+SmaSru",  # tTdD group
        "rAw+SmaSru",  # tTdD group
        "gup+SmaSru",  # pPbB group
        # rule: praSAn\+([cC])
        "praSAn+cinowi",
        # rule: praSAn\+([tT])
        "praSAn+TikawAm",
        # rule: praSAn\+([wW])
        "praSAn+wIkate",  # using 'w' for 'ṭ'
        # rule: (.*)n\+([cC])
        "BavAn+cinowi",
        # rule: (.*)n\+([tT])
        "BavAn+TikawAm",
        # rule: (.*)n\+([wW])
        "BavAn+wIkate",
        # rule: nQn\+p(.*)
        "nQn+pAhi",
        # rule: kAn\+kAn$
        "kAn+kAn",
        # rule: pum\+([kKcCtTwWpP]).*
        "pum+kAmam",
        "pum+calawi",
        # rule: (.*)H\+([KPCTWctwkpSRs])([SRs])(.*)
        "kaviH+SSete",  # H + ś + ś
        # rule: (.*)H\+([SRs])([KPCTWctwkpSRs])(.*)
        "devaH+sTarawi",  # H + s + ṭh
        # rule: sam\+rAt
        "sam+rAt",
        # rule: (.*)m\+hm(.*)
        "kim+hmalayati",
        # rule: (.*)m\+h([yvl])(.*)
        "kim+hyas",
        "kim+hvalayati",
        # rule: (.*)m\+hn(.*)
        "kim+hnuwe",
        # rule: (eRa|sa)H\+([gGf...soft consonants...])(.*)
        "saH+gacCawi",
        "eRaH+yAwi",
        # rule: [aA]\+e(wi|Ri|mi|wA...)
        "Bava+ewi",
        # rule: [aA]\+E(w|wAm|H|wam...)
        "Bava+EwAm",
        # rule: [aA]\+[eE]X(.*)
        "Bava+eXawAm",
        # rule: [aA]\+Uha(.*)
        "Bava+UhaH",
        # rule: ahan\+(rUpa|rAwr|raWanwara)(.*)
        "ahan+rUpam",
        "ahan+rAwrI",
        # rule: ahan\+(pawi|puwra)(.*)
        "ahan+pawiH",
        "ahan+puwraH",
        # rule: ahan\+gaNa(.*)
        "ahan+gaNaH",
        # rule: gIr\+(pawi|puwra)(.*)
        "gIr+pawiH",
        # rule: gIr\+gaNa(.*)
        "gIr+gaNaH",
        # rule: XUr\+(pawi|puwra)(.*)
        "XUr+puwraH",
        # rule: XUr\+gaNa(.*)
        "XUr+gaNaH",
        # rule: ahan\+ahaH$
        "ahan+ahaH",
        # rule: (.*)([aiuqL])([fNn])\+([aAi...vowel...])(.*)
        "pratyaN+AwmA",
        # rule: (.*)([^aiuqL])([fNn])\+([aAi...vowel...])(.*)
        "mahAn+iva",
        # rule: (.*)([iIuUqQLeEoO])H\+([aAi...soft...])(.*)
        "kaviH+gacCawi",
        "BAnuH+uwewi",
        # rule: (eRa|sa)H\+([kKg...hard/soft...])(.*)
        "saH+karowi",
        # rule: (.*)aH\+([gGf...soft...])(.*)
        "rAmaH+gacCawi",
        # rule: ^BoH\+([kKg...hard/soft...])(.*)
        "BoH+xeva",
        # rule: ^(Bago|aGo)H\+([kKg...hard/soft...])(.*)
        "BagoH+namaswe",
        # rule: ^(Bo|Bago|aGo)H\+([aAi...vowel...])(.*)
        "BoH+iha",
        # rule: (.*)([aAi...vowel...])H\+([wW])([^sSR].*)
        "kaviH+wIkate",
        # rule: (.*)([aAi...vowel...])H\+([cC])(.*)
        "kaviH+calawi",
        # rule: (.*)([aAi...vowel...])H\+([tT])(.*)
        "kaviH+tarawi",
        # rule: (.*)AH\+([gGf...soft...])(.*)
        "devAH+gacCanwi",
        # rule: ^(miWo|ho|aho|...)\+([aAi...vowel...])(.*)
        "aho+Aho",
        "no+aham",
        # rule: ^([aiuqLeEoO])\+([aAi...vowel...])(.*)
        "i+indra",
        # rule: ^uF\+iwi
        "uF+iwi",
        # rule: ^(kR|j)i\+ya(.*)
        "kRi+yam",
        "ji+yam",
        # rule: ^krI\+ya(.*)
        "krI+yam",
        # rule: ^(aXa|Sira)H\+paxa(.*)
        "aXaH+paxam",
        "SiraH+paxam",
        # rule: (.*[iu])H\+([kKpP])(.*)
        "niH+karowi",
        "catuH+pAwram",
        # rule: a case that matches none of the above
        "no+match_for_this",
    ]

    passed_count = 0
    failed_count = 0

    for i, case in enumerate(test_cases):
        # 1. Get Python result
        try:
            py_result_tuple = apavAdaniyamAH(case)
            # Convert to a list of strings for consistent comparison
            py_result = [str(item) for item in py_result_tuple]
        except Exception as e:
            print(f"  [!] PYTHON ERROR: {e}")
            failed_count += 1
            continue

        # 2. Get Perl result
        try:
            process = subprocess.run(
                ["perl", perl_script_path, case],
                capture_output=True,
                text=True,
                check=True,
                encoding="utf-8",
            )
            perl_output_str = process.stdout.strip()
            # Perl script returns 4 comma-separated values
            pl_result = perl_output_str.split(",")
            # Handle cases where Perl might return fewer than 4 values on empty match
            while len(pl_result) < 4:
                pl_result.append("")

        except FileNotFoundError:
            print(
                f"  [!] PERL ERROR: Perl interpreter not found or '{perl_script_path}' does not exist."
            )
            sys.exit(1)
        except subprocess.CalledProcessError as e:
            print(f"  [!] PERL SCRIPT ERROR: Exit code {e.returncode}")
            print(f"      STDOUT: {e.stdout}")
            print(f"      STDERR: {e.stderr}")
            failed_count += 1
            continue
        except Exception as e:
            print(f"  [!] UNKNOWN ERROR executing Perl: {e}")
            failed_count += 1
            continue

        # 3. Compare results
        if py_result == pl_result:
            passed_count += 1
        else:
            print("  [✗] FAIL")
            print(f"\n[{i+1}/{len(test_cases)}] Testing input: {case}")
            print(f"    - Python Output: {py_result}")
            print(f"    - Perl Output  : {pl_result}")
            failed_count += 1

    print("\n--- Test Summary ---")
    print(f"Total tests: {len(test_cases)}")
    print(f"Passed: {passed_count}")
    print(f"Failed: {failed_count}")
    print("--------------------")


if __name__ == "__main__":
    test_apavaadas()
