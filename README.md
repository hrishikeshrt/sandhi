# How to convert PERL to Python?

Primary changes are when converting `apavAxa_any.pl`.
Fewer changes to `sandhi.pl`.
Rules can be copied directly from `any_sandhi.pl`

## Changes to `apavAxa_any` and `sandhi` Files

0. Simple Replacements
    * `my` declarations are local variables, can be ignored
    * `$var` to `var`
    * Remove `;`
    * Remove `}` (Note: need to remove `{` as well, but that can be useful in
    bulk `if` expression replacement)
1. Replace all regex rules
    * Rules of the form `if ($an =~ /expression/)` become
      `m = re.search(r"expression", s)` followed by `if m:`
    * Rules of the form `$var =~ s/expr/repl/` become `var.replace("expr", "repl")`
    * For `elsif`, do `else:` followed by the condition as earlier, followed by `if m:`
2. Replace all `$vars` such as `$ans`, `$ans1`
    * CAUTION: Don't replace all `$`, since they are used in multiple places,
    such as, regex and positional variables
3. Replace positional variables corresponding to regex matches with `m.group()`,
i.e. `$1` with `m.group(1)`
4. Handle cases where a string being assigned to a variable or being concatenated, starts on a new line