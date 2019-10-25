# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:22:05 2019

@author: Robin
"""




# ₁₂₃₄₅₆₇₈₉₀¹²³⁴⁵⁶⁷⁸⁹⁰ # DONE singular
# ∫ᵀ√≠≈≙
# ±ħ∈ℝΘτ̅ΨΩΠ̈∂ΣΔΦΓ↓←∞Λ@ ερθζ̲ψωπασδφγ↑→κλ⇐Ξⁿₙ‘ηº×÷—⇔ # Greek letters are done


# ---------------------------------- Lists l_ ----------------------------------

l_beginning_symbols = ['=','(','{','[']
l_pairs_brackets = [['(',')'],['[',']'],['{','}']]
l_pairs_brackets_special = [['<','>']]
l_pairs_brackets_not_interpreteable = [['{','}'],['[',']']]
l_pairs_quotation = [["\"","\""],["\'","\'"]]
#TODO: Clean this up...:
l_pairs_special_I_D = [["Integral","d","Integral("],["d(",")/d","diff("],["∂(",")/∂","diff("]]
l_pairs_special_I_D_all_Integrals = [["Integral","d","Integral("],["d(",")/d","diff("],["∂(",")/∂","diff("],["integral","d","Integral("],
                                ["Integrate","d","Integral("],["integrate","d","Integral("],["int ","d","Integral("],["Int ","d","Integral("],["∫","d","Integral("]]
l_pairs_special_I_D_Unicode = [["∫","d","Integral("],["d(",")/d","diff("],["∂(",")/∂","diff("]]

l_pairs_special = [["sqrt(",")"],["√(",")"]]
l_seperators = [',']

LIST_l_normal_pairs = [l_pairs_brackets , l_pairs_special_I_D_all_Integrals , l_pairs_special]
LIST_l_normal_pairs_Unicode = [l_pairs_brackets , l_pairs_special_I_D_Unicode , l_pairs_special]
LIST_l_all_pairs = [l_pairs_brackets , l_pairs_brackets_special , l_pairs_quotation , l_pairs_special_I_D , l_pairs_special]


# ---------------------------------- Normal Replacements n_ ----------------------------------

n_standard = [["",""]]
n_standard_integrals = [["integral","Integral"],["Integrate","Integral"],["integrate","Integral"],["int ","Integral"],["Int ","Integral"],["∫","Integral"]]
n_greek_letters = [["\u0391"," Alpha "],["\u03b1"," alpha "],
                   ["\u0392"," Beta "],["\u03b2"," beta "],
                   ["\u0393"," Gamma "],["\u03b3"," gamma "],
                   ["\u0394"," Delta "],["\u03b4"," delta "],
                   ["\u0395"," Epsilon "],["\u03b5"," epsilon "],
                   ["\u0396"," Zeta "],["\u03b6"," zeta "],
                   ["\u0397"," Eta "],["\u03b7"," eta "],
                   ["\u0398"," Theta "],["\u03b8"," theta "],
                   ["\u0399"," Iota "],["\u03b9"," iota "],
                   ["\u039a"," Kappa "],["\u03ba"," kappa "],
                   ["\u039b"," Lamda "],["\u03bb"," lamda "], # Lambda is a function in sympy so they spell the letter lamda
                   ["\u039c"," Mu "],["\u03bc"," mu "],
                   ["\u039d"," Nu "],["\u03bd"," nu "],
                   ["\u039e"," Xi "],["\u03be"," xi "],
                   ["\u039f"," Omicron "],["\u03bf"," omicron "],
                   ["\u03a0"," Pi "],["\u03c0"," pi "],
                   ["\u03a1"," Rho "],["\u03c1"," rho "],
                   ["\u03a3"," Sigma "],["\u03c3"," sigma "],
                   ["\u03a4"," Tau "],["\u03c4"," tau "],
                   ["\u03a5"," Upsilon "],["\u03c5"," upsilon "],
                   ["\u03a6"," Phi "],["\u03c6"," phi "],
                   ["\u03a7"," chi "],["\u03c7"," chi "], #Capital Chi is a function in sympy!!! Converting into lower case chi instead
                   ["\u03a8"," Psi "],["\u03c8"," psi "],
                   ["\u03a9"," Omega "],["\u03c9"," omega "]
                   ]
n_greek_letters_nospace = [["\u0391","Alpha"],["\u03b1","alpha"],
                   ["\u0392","Beta"],["\u03b2","beta"],
                   ["\u0393","Gamma"],["\u03b3","gamma"],
                   ["\u0394","Delta"],["\u03b4","delta"],
                   ["\u0395","Epsilon"],["\u03b5","epsilon"],
                   ["\u0396","Zeta"],["\u03b6","zeta"],
                   ["\u0397","Eta"],["\u03b7","eta"],
                   ["\u0398","Theta"],["\u03b8","theta"],
                   ["\u0399","Iota"],["\u03b9","iota"],
                   ["\u039a","Kappa"],["\u03ba","kappa"],
                   ["\u039b","Lamda"],["\u03bb","lamda"], # Lambda is a function in sympy so they spell the letter lamda
                   ["\u039c","Mu"],["\u03bc","mu"],
                   ["\u039d","Nu"],["\u03bd","nu"],
                   ["\u039e","Xi"],["\u03be","xi"],
                   ["\u039f","Omicron"],["\u03bf","omicron"],
                   ["\u03a0","Pi"],["\u03c0","pi"],
                   ["\u03a1","Rho"],["\u03c1","rho"],
                   ["\u03a3","Sigma"],["\u03c3","sigma"],
                   ["\u03a4","Tau"],["\u03c4","tau"],
                   ["\u03a5","Upsilon"],["\u03c5","upsilon"],
                   ["\u03a6","Phi"],["\u03c6","phi"],
                   ["\u03a7","chi"],["\u03c7","chi"], #Capital Chi is a function in sympy!!! Converting into lower case chi instead
                   ["\u03a8","Psi"],["\u03c8","psi"],
                   ["\u03a9","Omega"],["\u03c9","omega"]
                   ]
n_constants = [["\u03c0"," pi "],["∞"," oo "]]
n_operators = [["^","**"],["·","*"]]
n_operators_special = [["√","sqrt"],["∫","Integral"]]
n_operators_notinv = [["–","-"],["—","-"],["×","*"],["÷","/"]]
n_space = [[" "," "]]

LIST_n_all = [n_standard_integrals , n_greek_letters_nospace , n_constants , n_operators , n_operators_special , n_operators_notinv , n_space]

n_constants_nospace = [["π"," pi "]]
LIST_n_invertable = [n_greek_letters_nospace , n_constants_nospace , n_operators , n_operators_special]
# ---------------------------------- Special Replacements s_ ----------------------------------

s_constants_math = [["i"," I "],["e"," E "]]
s_constants_engineering = [["j"," I "],["e"," E "]]

# ---------------------------------- Replacements Simple to Python r_s_ ----------------------------------

r_s_superscript_numbers = [["¹","**(1)"],["²","**(2)"],["³","**(3)"],["⁴","**(4)"],["⁵","**(5)"],["⁶","**(6)"],["⁷","**(7)"],["⁸","**(8)"],["⁹","**(9)"],["⁰","**(0)"]]
r_s_subscript_numbers = [["₁","_1"],["₂","_2"],["₃","_3"],["₄","_4"],["₅","_5"],["₆","_6"],["₇","_7"],["₈","_8"],["₉","_9"],["₀","_0"]]
r_s_superscript_letters = [["ⁿ","**(n)"]]
r_s_subscript_letters = [["ₙ","_n"]]

LIST_r_s_scripts = [r_s_superscript_numbers , r_s_subscript_numbers , r_s_superscript_letters , r_s_subscript_letters]



# ---------------------------------- Replacements Complex to Python r_c_ ----------------------------------

# number refferences number of parts in addition to symbol replacement
r_c_operators_1 = [["√",""]]
r_c_operators_2 = [[]]
r_c_operators_3 = [["Σ",""],["Π",""]]
r_c_operators_4 = [
                    ["∫",""], # 1: from 2: to 3: f(x) 4: dx
                    []]


# ---------------------------------- PYTHON_TO_LATEX_ ----------------------------------

PYTHON_TO_LATEX_simple_replacements = [
                        ['**', '^'],
                        ['*', ' \\cdot '], ['·', ' \\cdot '],
                        ['math.', ''], ['np.', ''],
                        ['pi', '\\pi'] , ['π', '\\pi'],
                        ['tan', '\\tan'], ['cos', '\\cos'], ['sin', '\\sin'], ['sec', '\\sec'], ['csc', '\\csc']]
PYTHON_TO_LATEX_complex_replacements =[
                        ['^', '{{{i1}}}^{{{i2}}}'],
                        ['_', '{{{i1}}}_{{{i2}}}'],
                        ['/', '\\frac{{{i1}}}{{{i2}}}'],
                        ['sqrt','\\sqrt{{{i2}}}'], ['√','\\sqrt{{{i2}}}']]

# ---------------------------------- MASTERLISTS M_ ----------------------------------

M_pair_LIST_LIST_LIST = [LIST_l_all_pairs]



# ---------------------------------- Keyboard Remapper KR_ ----------------------------------

KR_Map = [
    # Sorted for German Keyboard but mostly compatible with all Keyboards
    # Note that not all Symbols are currently supported
    # This is my custom Layout for my Linux Laptop
    #Normal
        #Shift
            #AltGr
                #AltGr+Shift
                    # ^
    # Line 1 (Numbers)
    ["^","°","′","″"," "],
    ["1","!","∫","₁","¹"],
    ["2","\"","ᵀ","₂","²"],
    ["3","§","√","₃","³"],
    ["4","$","\u2260","₄","⁴"],
    ["5","%","≈","₅","⁵"],
    ["6","&","≙","₆","⁶"],
    ["7","/","{","₇","⁷"],
    ["8","(","[","₈","⁸"],
    ["9",")","]","₉","⁹"],
    ["0","=","}","₀","⁰"],
    ["ß","?","\\","¿"," "],
    ["´","`","≤","≥"," "],
    # Line 2 (QWERTZ...)
    ["q","Q","@","±"," "],
    ["w","W",r" ",r"ħ"," "],
    ["e","E","ε","∈"," "],
    ["r","R","ρ","ℝ"," "],
    ["t","T","θ","Θ"," "],
    ["z","Z","ζ","τ"," "],
    ["u","U","\u0332","\u0305"," "],
    ["i","I","ψ","Ψ"," "],
    ["o","O","ω","Ω"," "],
    ["p","P","π","Π"," "],
    ["ü","Ü","\u0307","\u0308"," "],
    ["+","*","~",r"¯","⁺"],
    # Line 3 (ASD...)
    ["a","A","α","∂"," "],
    ["s","S","σ","Σ"," "],
    ["d","D","δ","Δ"," "],
    ["f","F","φ","Φ"," "],
    ["g","G","γ","Γ"," "],
    ["h","H","↑","↓"," "],
    ["j","J","→","←"," "],
    ["k","K","κ","Λ"," "],
    ["l","L","λ",""," "],
    ["ö","Ö","\u005E"," "," "],
    ["ä","Ä","↳","\u0303"," "],
    ["#",r"'","’"," "," "],
    # Line 4 (YXC...)
    ["<",">","|","⇔"," "],
    ["y","Y","⇒","⇐"," "],
    ["x","X","ξ","Ξ"," "],
    ["c","C","ℂ","ⁿ"," "],
    ["v","V","\u20D7","ₙ"," "],
    ["b","B","β"," "," "],
    ["n","N","ν","η","ⁿ"],
    ["m","M","µ"," "," "],
    [",",";","·","×"," "],
    [".",":","…","÷"," "],
    ["-","_","–","—","⁻"]]

"""
,
    [" "," "," "," "," "]
"""