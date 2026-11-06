"""The opposite of contractions.py: I'm → I am, don't → do not. Used for the "Contractions: off" version of every phrase."""
import re

PARTICIPLE = (r"(?:been|done|seen|made|gone|taken|written|given|found|got|gotten|had|put|read|said|told|heard|known|shown|sent|built|lost|run|left|"
              r"understood|chosen|broken|forgotten|begun|never|already|just|finished|lived|worked|changed|improved|moved|started|arrived|left)")
# -ed words after he's / she's / it's are usually adjectives (He's tired, She's worried), so only these verbs count as "has".
SIMPLE = [("can't", "cannot"), ("won't", "will not"), ("shan't", "shall not"),
          ("don't", "do not"), ("doesn't", "does not"), ("didn't", "did not"), ("isn't", "is not"), ("aren't", "are not"),
          ("wasn't", "was not"), ("weren't", "were not"), ("haven't", "have not"), ("hasn't", "has not"), ("hadn't", "had not"),
          ("couldn't", "could not"), ("wouldn't", "would not"), ("shouldn't", "should not"), ("mustn't", "must not"),
          ("I'm", "I am"), ("you're", "you are"), ("we're", "we are"), ("they're", "they are"),
          ("I'll", "I will"), ("you'll", "you will"), ("we'll", "we will"), ("they'll", "they will"), ("he'll", "he will"),
          ("she'll", "she will"), ("it'll", "it will"), ("that'll", "that will"),
          ("I've", "I have"), ("you've", "you have"), ("we've", "we have"), ("they've", "they have"),
          ("should've", "should have"), ("could've", "could have"), ("would've", "would have")]
S_WORDS = ["he", "she", "it", "that", "there", "here", "what", "who", "how", "where", "when"]   # 's = is, or has before a participle
D_WORDS = ["I", "you", "we", "they", "he", "she"]                                              # 'd = would, or had before better/a participle


def _case(src, rep):
    return rep[0].upper() + rep[1:] if src[0].isupper() else rep


def expand(text):
    for a, b in SIMPLE:
        text = re.sub(rf"\b{re.escape(a)}\b", lambda m: _case(m.group(0), b), text, flags=re.I)
    def s_rep(m):
        word, nxt = m.group(1), m.group(2) or ""
        verb = "has" if re.match(rf"\s+{PARTICIPLE}\b", nxt, re.I) and not re.match(r"\s+\w+ed\s+(?:by|to)\b", nxt) else "is"
        return f"{word} {verb}{nxt}"
    text = re.sub(rf"\b({'|'.join(S_WORDS)})'s\b(\s+\w+)?", s_rep, text, flags=re.I)
    def d_rep(m):
        word, nxt = m.group(1), m.group(2) or ""
        verb = "had" if re.match(rf"\s+(?:better|{PARTICIPLE})\b", nxt, re.I) else "would"
        return f"{word} {verb}{nxt}"
    text = re.sub(rf"\b({'|'.join(D_WORDS)})'d\b(\s+\w+)?", d_rep, text, flags=re.I)
    return text
