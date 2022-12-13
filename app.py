from flask import Flask, jsonify, redirect, render_template, request, url_for, session, make_response
from flask_socketio import SocketIO, emit
from mongo import *
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex()
app.jinja_env.globals.update(enumerate=enumerate)

socket = SocketIO(app)

@app.route("/home", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        form = request.form

        username = form["username"]
        password = form["password"]

        user = find(username=username, password=password)

        if user:
            return render_template("skeletal.html", username=username)
        else:
            return render_template("login.html")

    return render_template("skeletal.html", username="")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/leaderboard")
def leaderboard():
    return render_template("leaderboard.html", top=get_top())

@app.route("/signup_validator", methods=["POST"])
def signup_validator():
    form = request.form
    username = form["username"]
    password = form["password"]
    if len(username) < 3:
        return "Username too short"
    invalid_username = ['aeolus', 'ahole', 'anilingus', 'anus', 'areola', 'areole', 'arrse', 'aryan', 'axwound', 'azazel', 'azz', 'ballbag', 'balllicker', 'ballsack', 'bampot', 'bareback', 'barenaked', 'barf', 'barface', 'barfface', 'bastard', 'bastardo', 'bastards', 'bastinado', 'bawdy', 'bazongas', 'bazooms', 'bbw', 'bdsm', 'beaner', 'beaners', 'beardedclam', 'beastial', 'beastiality', 'beatch', 'beater', 'beatyourmeat', 'beaver', 'beer', 'beeyotch', 'bellend', 'bender', 'beotch', 'bestial', 'bestiality', 'biatch', 'bicurious', 'bigbastard', 'bigger', 'bimbo', 'bimbos', 'bint', 'birdlock', 'bloodclaat', 'bloody', 'blowjob', 'blowjobs', 'blumpkin', 'boang', 'bod', 'bodily', 'bogan', 'bohunk', 'boink', 'boiolas', 'bollick', 'bollock', 'bollocks', 'bollok', 'bollox', 'bomd', 'bondage', 'bone', 'boned', 'boner', 'boners', 'bong', 'boob', 'booger', 'bookie', 'boong', 'boonga', 'booob', 'boooob', 'booooob', 'booooooob', 'bootee', 'bootie', 'booty', 'booze', 'boozer', 'boozy', 'bosom', 'bosomy', 'bowel', 'bowels', 'breast', 'buceta', 'bugger', 'buggered', 'buggery', 'bukkake', 'bullcrap', 'bulldike', 'bulldyke', 'bullturds', 'bum', 'bumclat', 'bummer', 'bung', 'bunga', 'bunghole', 'busty', 'butchdike', 'butchdyke', 'caca', 'cahone', 'cameltoe', 'camgirl', 'camslut', 'carpetmuncher', 'cawk', 'cervix', 'chesticle', 'chin', 'chinc', 'chincs', 'chink', 'chinky', 'choad', 'choade', 'chode', 'chodes', 'cipa', 'circlejerk', 'climax', 'clit', 'clitface', 'clitoris', 'clitorus', 'clits', 'clitty', 'clogwog', 'clunge', 'cnut', 'cocain', 'cocaine', 'coital', 'cok', 'cokmuncher', 'coksucka', 'commie', 'condom', 'coochie', 'coochy', 'coon', 'coons', 'cooter', 'coprolagnia', 'coprophilia', 'corksucker', 'cornhole', 'cox', 'crabs', 'crack', 'cracker', 'crap', 'crappy', 'creampie', 'cretin', 'crikey', 'cripple', 'crotte', 'cunilingus', 'cunillingus', 'cunn', 'cunnie', 'cunnilingus', 'cunntt', 'cunny', 'cunt', 'cyalis', 'cyberfuc', 'dago', 'dagos', 'dammit', 'damn', 'damned', 'damnit', 'darkie', 'darn', 'deepthroat', 'deggo', 'dendrophilia', 'diddle', 'dike', 'dildo', 'dildos', 'diligaf', 'dillweed', 'dimwit', 'dingle', 'dingleberries', 'dingleberry', 'dink', 'dinks', 'dipship', 'dirsa', 'dirty', 'dlck', 'doggiestyle', 'doggin', 'dogging', 'dolcett', 'domination', 'dominatrix', 'dommes', 'dong', 'donkeypunch', 'donkeyribber', 'doochbag', 'doofus', 'dookie', 'doosh', 'dopey', 'doublelift', 'douche', 'douchebag', 'douchebags', 'douchewaffle', 'douchey', 'duche', 'dumbcunt', 'dvda', 'dyke', 'dykes', 'ecchi', 'ejaculate', 'ejaculated', 'ejaculates', 'ejaculating', 'ejaculation', 'ejakulate', 'erect', 'erotic', 'erotism', 'escort', 'essohbee', 'eunuch', 'extacy', 'extasy', 'facial', 'fack', 'fag', 'fagbag', 'fagg', 'fagged', 'fagging', 'faggit', 'faggitt', 'faggot', 'faggs', 'fagot', 'fags', 'fagtard', 'faig', 'faigt', 'fanny', 'fannybandit', 'fannyflaps', 'fanyy', 'fartknocker', 'fat', 'fcuk', 'fcuker', 'fcuking', 'fecal', 'feck', 'fecker', 'felch', 'felcher', 'felching', 'fellate', 'fellatio', 'feltch', 'feltcher', 'femdom', 'fenian', 'figging', 'fingerbang', 'fingering', 'fisted', 'fisting', 'fisty', 'flamer', 'flange', 'flaps', 'fleshflute', 'floozy', 'foad', 'foah', 'fondle', 'foobar', 'fook', 'fooker', 'footjob', 'footlicker', 'foreskin', 'freex', 'frigg', 'frigga', 'frotting', 'fubar', 'fuc', 'fudgepacker', 'fuq', 'futanari', 'fux', 'fvck', 'fxck', 'gae', 'gai', 'gangbang', 'ganja', 'gash', 'genitals', 'gey', 'gfy', 'ghay', 'ghey', 'gigolo', 'ginger', 'gippo', 'git', 'glans', 'goatcx', 'goatse', 'godamn', 'godamnit', 'goddam', 'goddammit', 'goddamn', 'goddamned', 'goddamnit', 'godsdamn', 'gokkun', 'goldenshower', 'golliwog', 'gonad', 'gonads', 'gonorrehea', 'gooch', 'gook', 'gooks', 'goregasm', 'gringo', 'grope', 'gspot', 'gtfo', 'guido', 'guro', 'handjob', 'hardcore', 'hebe', 'heeb', 'hemp', 'hentai', 'heroin', 'herp', 'herpes', 'herpy', 'heshe', 'hitler', 'hiv', 'ho', 'hoar', 'hoare', 'hobag', 'hoer', 'homey', 'homo', 'homoerotic', 'homoey', 'honkey', 'honky', 'hooch', 'hookah', 'hooker', 'hoor', 'hootch', 'hooter', 'hooters', 'hore', 'horniest', 'horny', 'hump', 'humped', 'humping', 'hun', 'hussy', 'hymen', 'iap', 'inbred', 'incest', 'injun', 'intercourse', 'jackhole', 'jackoff', 'jaggi', 'jagoff', 'jailbait', 'jap', 'japs', 'jigaboo', 'jiggaboo', 'jiggerboo', 'jism', 'jiz', 'jizm', 'jizz', 'jizzed', 'jock', 'juggs', 'junglebunny', 'junkie', 'junky', 'kafir', 'kawk', 'kike', 'kikes', 'kinbaku', 'kinkster', 'kinky', 'klan', 'knob', 'knobbing', 'knobead', 'knobed', 'knobend', 'knobhead', 'knobjocky', 'knobjokey', 'kock', 'kondum', 'kondums', 'kooch', 'kooches', 'kootch', 'kraut', 'kum', 'kummer', 'kumming', 'kums', 'kunilingus', 'kunja', 'kunt', 'kwif', 'kyke', 'labia', 'lech', 'leper', 'lesbo', 'lesbos', 'lez', 'lezbian', 'lezbians', 'lezbo', 'lezbos', 'lezza', 'lezzie', 'lezzies', 'lezzy', 'lmao', 'lmfao', 'loin', 'loins', 'lolita', 'looney', 'lovemaking', 'lube', 'lust', 'lusting', 'lusty', 'mafugly', 'mams', 'masochist', 'masterbat', 'masterbate', 'masterbating', 'masterbation', 'masterbations', 'masturbate', 'masturbating', 'masturbation', 'maxi', 'mcfagget', 'menses', 'menstruate', 'menstruation', 'meth', 'mick', 'midget', 'milf', 'minge', 'minger', 'mofo', 'molest', 'mong', 'moolie', 'moron', 'muff', 'muffdiver', 'muffdiving', 'munging', 'munter', 'mutha', 'muthafecker', 'muther', 'nad', 'nads', 'naked', 'nambla', 'napalm', 'nappy', 'nawashi', 'nazi', 'negro', 'neonazi', 'nigaboo', 'niggle', 'niglet', 'nimphomania', 'nimrod', 'ninny', 'nipple', 'nipples', 'nob', 'nobhead', 'nobjocky', 'nobjokey', 'nonce', 'nooky', 'nude', 'nudity', 'numbnuts', 'nutsack', 'nutter', 'nympho', 'nymphomania', 'omorashi', 'opiate', 'opium', 'orally', 'orgasim', 'orgasims', 'orgasm', 'orgasmic', 'orgasms', 'orgies', 'orgy', 'ovary', 'ovum', 'ovums', 'paddy', 'paedophile', 'paki', 'panooch', 'pansy', 'pantie', 'panties', 'panty', 'pastie', 'pasty', 'pawn', 'pcp', 'pecker', 'peckerhead', 'pee', 'peepee', 'pegging', 'penetrate', 'penetration', 'penial', 'penile', 'penis', 'penisbanger', 'penispuffer', 'perversion', 'peyote', 'phalli', 'phallic', 'phuck', 'phuk', 'phuked', 'phuking', 'phukked', 'phukking', 'phuks', 'phuq', 'pikey', 'pillowbiter', 'pimp', 'pimpis', 'pinko', 'piss', 'pissed', 'pisser', 'pissers', 'pisses', 'pissflaps', 'pissin', 'pissing', 'pissoff', 'pisspig', 'playboy', 'pms', 'polack', 'polesmoker', 'pollock', 'ponyplay', 'poof', 'poon', 'poonani', 'poonany', 'poontang', 'porchmonkey', 'porn', 'porno', 'pornography', 'pornos', 'potty', 'prick', 'pricks', 'prickteaser', 'prig', 'prod', 'pron', 'prude', 'psycho', 'pthc', 'pube', 'pubes', 'pubic', 'pubis', 'punani', 'punanny', 'punany', 'punky', 'punta', 'puss', 'pusse', 'pussi', 'pussies', 'pust', 'puto', 'queaf', 'queef', 'queer', 'queerbait', 'queerhole', 'queero', 'queers', 'quicky', 'quim', 'racy', 'raghead', 'rapist', 'raunch', 'rectal', 'rectum', 'rectus', 'reefer', 'reetard', 'reich', 'renob', 'revue', 'rimjaw', 'rimjob', 'rimming', 'ritard', 'rtard', 'rubbish', 'rum', 'rump', 'rumprammer', 'ruski', 'sadism', 'sadist', 'sambo', 'sandbar', 'sandler', 'sanger', 'santorum', 'scag', 'scantily', 'scat', 'schizo', 'schlong', 'scissoring', 'screw', 'screwed', 'screwing', 'scroat', 'scrog', 'scrot', 'scrote', 'scrotum', 'scrud', 'seaman', 'seamen', 'seduce', 'seks', 'semen', 'shag', 'shagger', 'shaggin', 'shagging', 'shamedame', 'shemale', 'shibari', 'shiz', 'shiznit', 'shota', 'shrimping', 'skag', 'skank', 'skeet', 'slag', 'slanteye', 'sleaze', 'sleazy', 'slope', 'slut', 'slutbag', 'slutdumper', 'slutkiss', 'sluts', 'smeg', 'smegma', 'smut', 'smutty', 'snatch', 'sniper', 'snowballing', 'snuff', 'sodom', 'sodomize', 'sodomy', 'souse', 'soused', 'spac', 'spade', 'sperm', 'spic', 'spick', 'spik', 'spiks', 'splooge', 'spooge', 'spook', 'spunk', 'steamy', 'stiffy', 'stoned', 'strapon', 'strappado', 'strip', 'stroke', 'sumofabiatch', 'swinger', 'taff', 'taig', 'tampon', 'tard', 'tart', 'tawdry', 'teabagging', 'teat', 'teets', 'teez', 'terd', 'teste', 'testee', 'testes', 'testical', 'testicle', 'testis', 'threesome', 'throating', 'thrust', 'thundercunt', 'tinkle', 'toke', 'toots', 'topless', 'tosser', 'towelhead', 'tramp', 'tranny', 'trashy', 'tribadism', 'trumped', 'tubgirl', 'turd', 'tush', 'tushy', 'twat', 'twathead', 'twatlips', 'twats', 'twatty', 'twatwaffle', 'twink', 'twinkie', 'twunt', 'twunter', 'undies', 'undressing', 'unwed', 'upskirt', 'urinal', 'urine', 'urophilia', 'uterus', 'uzi', 'vag', 'vagina', 'vajayjay', 'valium', 'veqtable', 'viagra', 'vibrator', 'vixen', 'vjayjay', 'vorarephilia', 'voyeur', 'vulgar', 'vulva', 'wank', 'wanker', 'wankjob', 'wanky', 'wazoo', 'wedgie', 'weed', 'weenie', 'weewee', 'weiner', 'wench', 'wetback', 'whitey', 'whiz', 'whoar', 'whoralicious', 'whoring', 'wigger', 'willies', 'willy', 'wog', 'womb', 'woody', 'wop', 'yaoi', 'yeasty', 'yid', 'yiffy', 'yobbo', 'zoophile', 'zoophilia']
    #alphabetical bad word
    invalid_username_num = ['2g1c', '4r5e', '5h1t', '5hit', 'a2m', 'a54', 'a55', 'a55hole', 'ar5e', 'assh0le', 'assho1e', 'b00bs', 'b17ch', 'b1tch', 'c0ck', 'c0cksucker', 'cl1t', 'd0ng', 'd0uch3', 'd0uche', 'd1ck', 'd1ld0', 'd1ldo', 'douch3', 'f4nny', 'fux0r', 'h0m0', 'h0mo', 'he11', 'hom0', 'j3rk0ff', 'jerk0ff', 'l3itch', 'm0f0', 'm0fo', 'm45terbate', 'ma5terb8', 'ma5terbate', 'masterb8', 'masterbat3', 'mof0', 'n1gga', 'n1gger', 'nigg3r', 'nigg4h', 'p0rn', 's0b', 'sh1t', 't1t', 't1tt1e5', 't1tties', 'tittie5', 'tw4t', 'v14gra', 'v1gra', 'w00se', 'wh0re', 'wh0reface', '2g1c', '4r5e', '5h1t', '5hit', 'a2m', 'a54', 'a55', 'a55hole', 'ar5e', 'assh0le', 'assho1e', 'b00bs', 'b17ch', 'b1tch', 'c0ck', 'c0cksucker', 'cl1t', 'd0ng', 'd0uch3', 'd0uche', 'd1ck', 'd1ld0', 'd1ldo', 'douch3', 'f4nny', 'fux0r', 'h0m0', 'h0mo', 'he11', 'hom0', 'j3rk0ff', 'jerk0ff', 'l3itch', 'm0f0', 'm0fo', 'm45terbate', 'ma5terb8', 'ma5terbate', 'masterb8', 'masterbat3', 'mof0', 'n1gga', 'n1gger', 'nigg3r', 'nigg4h', 'p0rn', 's0b', 'sh1t', 't1t', 't1tt1e5', 't1tties', 'tittie5', 'tw4t', 'v14gra', 'v1gra', 'w00se', 'wh0re', 'wh0reface']
    #digital bad word
    invalid_username_sym = ['2 girls 1 cup', 'a_s_s', 'alabama hot pocket', 'alaskan pipeline', 'anal impaler', 'anal leakage', 'ass fuck', 'ass hole', 'auto erotic', 'baby batter', 'baby juice', 'ball gag', 'ball gravy', 'ball kicking', 'ball licking', 'ball sack', 'ball sucking', "bang (one's) box", 'barely legal', 'batty boy', 'beaver cleaver', 'beaver lips', 'beef curtain', 'beef curtains', 'big black', 'big breasts', 'big knockers', 'big tits', 'bitch tit', 'black cock', 'blonde action', 'blonde on blonde action', 'bloody hell', 'blow job', 'blow me', 'blow mud', 'blow your load', 'blue waffle', 'booty call', 'brown showers', 'brunette action', 'bull shit', 'bullet vibe', 'bum boy', 'bung hole', 'bunny fucker', 'bust a load', 'butt fuck', 'butt plug', 'c.0.c.k', 'c.o.c.k.', 'c.u.n.t', 'camel toe', 'carpet muncher', 'chi-chi man', 'chick with a dick', 'choc ice', 'chocolate rosebuds', 'chota bags', 'cleveland steamer', 'clit licker', 'clitty litter', 'clover clamps', 'cock pocket', 'cock snot', 'cock sucker', 'cocksuck ', 'coffin dodger', 'cop some wood', 'corp whore', 'cum chugger', 'cum dumpster', 'cum freak', 'cum guzzler', 'cunt hair', 'cuntlick ', 'cuntlicker ', 'cut rope', 'date rape', 'deep throat', 'dick head', 'dick hole', 'dick shy', 'dirty pillows', 'dirty sanchez', 'dog style', 'doggie style', 'doggy style', 'donkey punch', 'double dong', 'double penetration', 'dp action', 'dry hump', 'dumb ass', 'eat a dick', 'eat hair pie', 'eat my ass', 'f u c k', 'f u c k e r', 'f.u.c.k', 'f_u_c_k', 'female squirting', 'fingerfuck ', 'fingerfucker ', 'fist fuck', 'fistfucker ', 'flog the log', 'foot fetish', 'fuck buttons', 'fuck hole', 'fuck off', 'fuck puppet', 'fuck trophy', 'fuck yo mama', 'fuck you', 'fuckme ', 'fudge packer', 'gang bang', 'gassy ass', 'gay sex', 'gender bender', 'giant cock', 'girl on', 'girl on top', 'girls gone wild', 'god damn', 'golden shower', 'goo girl', 'group sex', 'ham flap', 'hand job', 'hard core', 'hard on', 'holy shit', 'hot carl', 'hot chick', 'how to kill', 'how to murdep', 'how to murder', 'huge fat', 'iberian slap', 'jack off', 'jail bait', 'jelly donut', 'jerk off', 'jungle bunny', 'knob end', 'leather restraint', 'leather straight jacket', 'lemon party', 'make me come', 'male squirting', 'menage a trois', 'middle finger', 'missionary position', 'moo moo foo foo', 'mother fucker', 'mound of venus', 'mr hands', 'muff diver', 'muff puff', 'need the dick', 'nig nog', 'nob jokey', 'nsfw images', 'nut butter', 'nut sack', 'old bag', 'one cup two girls', 'one guy one jar', 'p.u.s.s.y.', 'phone sex', 'piece of shit', 'piss off', 'piss pig', 'pissed off', 'pleasure chest', 'pole smoker', 'poop chute', 'porch monkey', 'prince albert piercing', 'pussy fart', 'pussy palace', 'raging boner', 'reverse cowgirl', 'rosy palm', 'rosy palm and her 5 sisters', 'rusty trombone', 's hit', 's.h.i.t.', 's.o.b.', 's_h_i_t', 'sand nigger', 'sausage queen', 'shaved beaver', 'shaved pussy', 'shirt lifter', 'shit ass', 'shit fucker', 'slut bucket', 'sod off', 'son of a bitch', 'son of a motherless goat', 'son of a whore', 'splooge moose', 'spread legs', 'strap on', 'strip club', 'style doggy', 'suicide girls', 'sultry women', 'tainted love', 'taking the piss', 'taste my', 'tea bagging', 'tied up', 'tight white', 'tit wank', 'tongue in a', 'tub girl', 'two fingers', 'two fingers with tongue', 'two girls one cup', 'urethra play', 'venus mound', 'violet wand', 'wet dream', 'white power', 'window licker', 'wrapping men', 'wrinkled starfish', 'yellow showers', 'zoophilia2 girls 1 cup', 'a_s_s', 'alabama hot pocket', 'alaskan pipeline', 'anal impaler', 'anal leakage', 'ass fuck', 'ass hole', 'auto erotic', 'baby batter', 'baby juice', 'ball gag', 'ball gravy', 'ball kicking', 'ball licking', 'ball sack', 'ball sucking', "bang (one's) box", 'barely legal', 'batty boy', 'beaver cleaver', 'beaver lips', 'beef curtain', 'beef curtains', 'big black', 'big breasts', 'big knockers', 'big tits', 'bitch tit', 'black cock', 'blonde action', 'blonde on blonde action', 'bloody hell', 'blow job', 'blow me', 'blow mud', 'blow your load', 'blue waffle', 'booty call', 'brown showers', 'brunette action', 'bull shit', 'bullet vibe', 'bum boy', 'bung hole', 'bunny fucker', 'bust a load', 'butt fuck', 'butt plug', 'c.0.c.k', 'c.o.c.k.', 'c.u.n.t', 'camel toe', 'carpet muncher', 'chi-chi man', 'chick with a dick', 'choc ice', 'chocolate rosebuds', 'chota bags', 'cleveland steamer', 'clit licker', 'clitty litter', 'clover clamps', 'cock pocket', 'cock snot', 'cock sucker', 'cocksuck ', 'coffin dodger', 'cop some wood', 'corp whore', 'cum chugger', 'cum dumpster', 'cum freak', 'cum guzzler', 'cunt hair', 'cuntlick ', 'cuntlicker ', 'cut rope', 'date rape', 'deep throat', 'dick head', 'dick hole', 'dick shy', 'dirty pillows', 'dirty sanchez', 'dog style', 'doggie style', 'doggy style', 'donkey punch', 'double dong', 'double penetration', 'dp action', 'dry hump', 'dumb ass', 'eat a dick', 'eat hair pie', 'eat my ass', 'f u c k', 'f u c k e r', 'f.u.c.k', 'f_u_c_k', 'female squirting', 'fingerfuck ', 'fingerfucker ', 'fist fuck', 'fistfucker ', 'flog the log', 'foot fetish', 'fuck buttons', 'fuck hole', 'fuck off', 'fuck puppet', 'fuck trophy', 'fuck yo mama', 'fuck you', 'fuckme ', 'fudge packer', 'gang bang', 'gassy ass', 'gay sex', 'gender bender', 'giant cock', 'girl on', 'girl on top', 'girls gone wild', 'god damn', 'golden shower', 'goo girl', 'group sex', 'ham flap', 'hand job', 'hard core', 'hard on', 'holy shit', 'hot carl', 'hot chick', 'how to kill', 'how to murdep', 'how to murder', 'huge fat', 'iberian slap', 'jack off', 'jail bait', 'jelly donut', 'jerk off', 'jungle bunny', 'knob end', 'leather restraint', 'leather straight jacket', 'lemon party', 'make me come', 'male squirting', 'menage a trois', 'middle finger', 'missionary position', 'moo moo foo foo', 'mother fucker', 'mound of venus', 'mr hands', 'muff diver', 'muff puff', 'need the dick', 'nig nog', 'nob jokey', 'nsfw images', 'nut butter', 'nut sack', 'old bag', 'one cup two girls', 'one guy one jar', 'p.u.s.s.y.', 'phone sex', 'piece of shit', 'piss off', 'piss pig', 'pissed off', 'pleasure chest', 'pole smoker', 'poop chute', 'porch monkey', 'prince albert piercing', 'pussy fart', 'pussy palace', 'raging boner', 'reverse cowgirl', 'rosy palm', 'rosy palm and her 5 sisters', 'rusty trombone', 's hit', 's.h.i.t.', 's.o.b.', 's_h_i_t', 'sand nigger', 'sausage queen', 'shaved beaver', 'shaved pussy', 'shirt lifter', 'shit ass', 'shit fucker', 'slut bucket', 'sod off', 'son of a bitch', 'son of a motherless goat', 'son of a whore', 'splooge moose', 'spread legs', 'strap on', 'strip club', 'style doggy', 'suicide girls', 'sultry women', 'tainted love', 'taking the piss', 'taste my', 'tea bagging', 'tied up', 'tight white', 'tit wank', 'tongue in a', 'tub girl', 'two fingers', 'two fingers with tongue', 'two girls one cup', 'urethra play', 'venus mound', 'violet wand', 'wet dream', 'white power', 'window licker', 'wrapping men', 'wrinkled starfish', 'yellow showers']
    #symbolic bad word
    unban_word = ["documantary","document","documentation",
                  "cockadoodledoo","cockadoodledo","cockadodledoo","cockadodledo","cockadoddledoo","cockadoddledo"]
    #TODO hi i mess up my sorting thing so can you help me

@app.route('/username_and_pass_api')
def rickroll():
    return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')


# Sockets

@socket.on("add")
def add(user, amount):
    # TODO: check apple amount
    add_apple(user, amount)

@socket.on("init")
def init(user):
    user_data = find(username=user)
    emit("apple", user_data["apple"])
    emit("inv", user_data["inventory"])
    emit("shop", SHOP)

@socket.on("buy")
def buy(user, item):
    print(user, item)
    user_data = find(username=user)
    price = SHOP[item] * 1.1 ** user_data["inventory"][item]
    apple = user_data["apple"]

    if apple >= price:
        add_apple(user, -price)
        add_item(user, item, 1)

        user_data["apple"] -= price
        user_data["inventory"][item] += 1

        emit("apple", user_data["apple"])
        emit("item", (item, user_data["inventory"][item]))
        emit("shop", SHOP)

    else:
        # TODO: handle not enough apple
        pass
        



if __name__ == "__main__":
    socket.run(app, debug=True)