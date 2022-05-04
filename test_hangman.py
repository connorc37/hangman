import unittest
from game import *


class MyTestCase(unittest.TestCase):
    def test_get_title_returns_string(self):
        expected = """
    ==========================================================+
     _    _          _   _  _____ __  __          _   _ _     |
    | |  | |   /\\   | \\ | |/ ____|  \\/  |   /\\   | \\ | | |    O
    | |__| |  /  \\  |  \\| | |  __| \\  / |  /  \\  |  \\| | |   /|\\
    |  __  | / /\\ \\ |     | | |_ | |\\/| | / /\\ \\ |     | |   / \\
    | |  | |/ ____ \\| |\\  | |__| | |  | |/ ____ \\| |\\  |_|
    |_|  |_/_/    \\_\\_| \\_|\\_____|_|  |_/_/    \\_\\_| \\_(_)
    =============================================================
    """
        actual = get_title()
        self.assertEqual(expected, actual)

    def test_get_gallows_good_input_returns_string(self):
        expected = """
        +---+
        |   |
        |   O
        |  /|\\
        |  / \\
        |
        =======\n"""
        actual = get_gallows(7)
        self.assertEqual(expected, actual)

    def test_get_gallows_bad_input_returns_error(self):
        expected = "Key not found in get_gallows()."
        actual = get_gallows(8)
        self.assertEqual(expected, actual)

    def display_game_board(self):
        # TODO: Make the function return a multiline string vs. printing multiple lines so it can be tested.
        pass

    def test_scrape_words(self):
        # Expected is good as of 5/4/2022
        expected = ['LEVIATHAN', 'PIGGYBACK', 'SCHMOOZE', 'ABEYANCE', 'PREDILECTION', 'CONVOLUTED', 'EXCULPATE',
                    'SALIENT', 'ADVERSITY', 'GRIFT', 'DRUTHERS', 'METTLESOME', 'CONSTRUE', 'LIAISON', 'ZOOMORPHIC',
                    'FUNAMBULISM', 'BEMUSE', 'OPPORTUNE', 'VANGUARD', 'TIMELESS', 'RESURRECTION', 'ELICIT', 'POLYGLOT',
                    'IMPRIMATUR', 'JUXTAPOSE', 'SIMULACRUM', 'ASKANCE', 'DEEM', 'HOARY', 'MINION', 'CEREBRAL',
                    'SALT JUNK', 'FLUMMOX', 'NEFARIOUS', 'PROSAIC', 'KITSCH', 'SLOUGH', 'ASKEW', 'FESTER', 'MILIEU',
                    'COMPENDIOUS', 'RIDDLE', 'BESMIRCH', 'TEMPESTUOUS', 'ARCHETYPE', 'UNCOUTH', 'ELUCIDATE',
                    'CRYPTOGRAPHY', 'GREGARIOUS', 'INTERSPERSE', 'LIMERICK', 'NASCENT', 'WEND', 'LARGESSE', 'FURTIVE',
                    'HENCHMAN', 'OSTENSIBLE', 'RECIPROCATE', 'BASTION', 'SPECIOUS', 'IMPETUS', 'DECIMATE', 'PALATABLE',
                    'CHAGRIN', 'MALLEABLE', 'GARBLE', 'OBSEQUIOUS', 'BONA FIDES', 'JETTISON', 'SCHADENFREUDE',
                    'LUGUBRIOUS', 'ADMONISH', 'DISHEVELED', 'YEN', 'PEREMPTORY', 'COLLABORATE', 'REPROBATE',
                    'FASTIDIOUS', 'BILLET-DOUX', 'MEANDER', 'SLAPDASH', 'ECHELON', 'HEW', 'NONCHALANT', 'CANDOR',
                    'INVINCIBLE', 'TRANSPIRE', 'PARABLE', 'UTMOST', 'EMBARRASS', 'WHEREWITHAL', 'ARBITRARY', 'FOUNDER',
                    'REJUVENATE', 'CAPTIOUS', 'PALINDROME', 'ANTITHETICAL', 'SULLY', 'CERULEAN', 'VOLUBLE', 'LAYMAN',
                    'FINESSE', 'AFFABLE', 'TOME', 'STIR-CRAZY', 'MERITORIOUS', 'GLOSS', 'EUPHEMISM', 'SANGUINE',
                    'STOLA', 'WINSOME', 'DEBILITATING', 'NON SEQUITUR', 'DERRING-DO', 'OPINE', 'JUGGERNAUT',
                    'INTEMPERATE', 'QUIP', 'BAMBOOZLE', 'ZIGGURAT', 'MYOPIC', 'CAREER', 'FACTOID', 'HOMOGENEOUS',
                    'DERRICK', 'SMARMY', 'GALVANIZE', 'INTERLOPER', 'COMMODIOUS', 'FOMITE', 'OSTRACIZE', 'MILQUETOAST',
                    'RANKLE', 'PALISADE', 'SECULAR', 'ENIGMA', 'BELEAGUER', 'FLIPPANT', 'TALISMAN', 'ABRASIVE',
                    'VENERATE', 'RATIONALE', 'CONGENIAL', 'HUCKSTER', 'EXASPERATE', 'BENIGN', 'PAUCITY', 'ADVENTITIOUS',
                    'JUBILATE', 'KWANZAA', 'LIVID', 'INSINUATE', 'CARTE BLANCHE', 'ASTUTE', 'ZEITGEIST', 'INANE',
                    'PASSEL', 'LENIENT', 'AD-LIB', 'CAMARADERIE', 'PROPITIATE', 'SOPORIFIC', 'DEMAGOGUE', 'TRUNCATE',
                    'BEVY', 'STEADFAST', 'EDIFY', 'QUALM', 'GRISLY', 'WORMHOLE', 'FACETIOUS', 'NEGOTIATE', 'AMITY',
                    'DRACONIAN', 'TREPIDATION', 'UNIVOCAL', 'ROISTER', 'ENCLAVE', 'FEIGN', 'JOVIAL', "MAITRE D'",
                    'COMMENSURATE', 'MENORAH', 'OBFUSCATE', 'HOITY-TOITY', 'VESTIGE', 'COZEN', 'ADROIT', 'METTLE',
                    'INTRANSIGENT', 'LOLL', 'CAVALIER', 'SCION', 'FRET', 'AMICABLE', 'RESTAURATEUR', 'EXTRICATE',
                    'ODIOUS', 'CABAL', 'EMBELLISH', 'GOSSAMER', 'PERPETUITY', 'ZAFTIG', 'NOMENCLATURE', 'BATTEN',
                    'UNTOWARD', 'DEVOTION', 'BOGUS', 'MIRAGE', 'HECTOR', 'FACILE', 'TREACLE', 'ELOQUENT',
                    'PROCRASTINATE', 'ARCH', 'DOPPELGÄNGER', 'REGNANT', 'DOFF', 'GASCONADE', 'JEOPARDIZE', 'ADAMANTINE',
                    'COIFFURE', 'SUBORN', 'EGREGIOUS', 'BROGUE', 'FULMINATE', 'SEDENTARY', 'ADVERSARY', 'INFLAMMABLE',
                    'RESPONSIVE', 'TRIBULATION', 'EXONERATE', 'PRECARIOUS', 'VIGNETTE', 'LUCID', 'COLLUDE', 'FLEHMEN',
                    'INCHOATE', 'CHASTISE', 'HOBNOB', 'OBTUSE', 'DEDICATION', 'MISBEGOTTEN', 'PARLAY', 'ZEST', 'FILIAL',
                    'PULCHRITUDE', 'EXEMPLARY', 'BERATE', 'FLEXUOUS', 'INFIX', 'MOOT', 'PINK', 'RESILIENCE', 'ABJECT',
                    'GARNISH', 'NIMROD', 'CALLOW', 'KVELL', 'SCUTTLEBUTT', 'UNDULANT', 'BROMIDE', 'TOUSLE',
                    'DEFENESTRATION', 'WINNOW', 'AGHAST', 'SOPHISTRY', 'LIMINAL', 'EMIGRATE', 'CRYPTIC', 'OSSIFY',
                    'FUGITIVE', 'AMENABLE', 'HUBRIS', 'LOLLYGAG', 'NUMINOUS', 'DESULTORY', 'BIJOU', 'GORMANDIZE',
                    'INIMICAL', 'PATRIOT', 'QUONDAM', 'DETER', 'INCUMBENT', 'MULCT', 'ALEATORY', 'CATARACT', 'NONPLUS',
                    'EMPRISE', 'RUTHLESS', 'SHIBBOLETH', 'FLOUNDER', 'OMNISCIENT', 'TORPOR', 'PARRY', 'CAPRICIOUS',
                    'ATTENUATE', 'RECEIPT', 'GUTTURAL', 'EXPROPRIATE', 'LEXICAL', 'HAGIOGRAPHY', 'URBANE', 'JEREMIAD',
                    'BIVOUAC', 'PALAVER', 'WHEREFORE', 'DALLY', 'ANFRACTUOUS', 'COLLEAGUE', 'PEACH', 'RIGMAROLE',
                    'DIDACTIC', 'GLEAN', 'SOLIPSISM', 'BUMPTIOUS', 'ENJOIN', 'MAJUSCULE', 'POIGNANT', 'VIRTUOSO',
                    'TITANIC', 'DERIDE', 'FEALTY', 'JOCUND', 'HARRY', 'CALUMNY', 'ABRUPT', 'PROGENY', 'INVEIGLE',
                    'MIASMA', 'EMERITUS', 'FORSWEAR', 'AFFLUENT', 'THESAURUS', 'DESICCATE', 'WHILOM', 'OAF', 'HALE',
                    'FUSTIAN', 'ABJURE', 'CONCILIATORY', 'SUCCUMB', 'SPRIGHTLY', 'DEEP-SIX', 'ARCHIPELAGO', 'FRUGAL',
                    'PAEAN', 'SHRIVE', 'IMPORTUNATE', 'VERACITY', 'EXHILARATE', 'BLITHESOME', 'HEINOUS', 'MAGNUM OPUS',
                    'DIVERS', 'PERUSE', 'RICTUS', 'COPIOUS', 'ALTRUISM', 'HELIACAL', 'GADFLY', 'CHOUSE', 'BUMBERSHOOT',
                    'DESOLATE', 'FLOTILLA', 'LYMPHATIC', 'INROAD', 'NETTLE', 'ELEGIAC']
        actual = scrape_words()
        self.assertEqual(expected, actual)

    def test_scrape_words_missing_page(self):
        # TODO: Figure out how to test this.
        pass

    def test_scrape_words_no_connection(self):
        # TODO: Figure out how to test this.
        pass

    def test_scrape_hint(self):
        expected = ": characterized by good-humored cheerfulness and conviviality : jolly"
        actual = scrape_hint("jovial")
        self.assertEqual(expected, actual)

    def test_get_guess_good_input(self):
        # TODO: Figure out how to test this without having to do it manually.
        existing_guesses = ["a", "b"]
        expected = "C"
        actual = get_guess(existing_guesses)
        self.assertEqual(expected, actual)

    def test_celebrate(self):
        # TODO: Figure out how to test this without having to do it manually.
        pass

    def test_play_game(self):
        pass


if __name__ == '__main__':
    unittest.main()
