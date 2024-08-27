import re

def process_text(text):
    # Remove numbers and square brackets
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = re.sub(r'\[.*?\]', '', text)  # Remove content inside square brackets

    # Split the text into lines
    lines = text.split('\n')
    
    # Initialize a list to hold the cleaned lines
    cleaned_lines = []
    
    skip_next_line = False
    for line in lines:
        if skip_next_line:
            # Skip this line and reset the flag
            skip_next_line = False
            continue
        
        # Check if the line starts with "Rozdział" and has some content after it
        if re.match(r'Rozdział .*', line):
            # Set the flag to skip the next line
            skip_next_line = True
            # Add 5 empty lines
            cleaned_lines.extend([''] * 5)
            continue
        
        # Strip whitespace and add non-empty lines to the cleaned list
        stripped_line = line.strip()
        if stripped_line:
            cleaned_lines.append(stripped_line)
    
    # Join the cleaned lines back into a single string with proper formatting
    formatted_text = '\n'.join(cleaned_lines)
    
    return formatted_text

def save_chapters_to_files(text):
    # Process the text
    formatted_text = process_text(text)
    
    # Split the formatted text into chapters using 5 empty lines as a delimiter
    chapters = re.split(r'\n{5}', formatted_text)
    
    # Save each chapter into a separate file
    for i, chapter in enumerate(chapters):
        file_name = f"{i+1:02}.txt"  # Name files as 01, 02, 03, etc.
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(chapter.strip())

# Example usage
text = """
1 Paweł, Apostoł Jezusa Chrystusa przez wolą Bożą,, wszystkim świętym, którzy są w Ephezie, i wiernym w Chrystusie Jezusie.

2 Łaska wam i pokój od Boga, Ojca naszego, i Pana Jezusa Chrystusa.

3 Błogosławiony Bóg i Ojciec Pana naszego Jezusa Chrystusa, który nas błogosławił wszelakiem błogosławieństwem duchownem w niebieskich w Chrystusie. [1]

4 Jako nas wybrał w nim przed założeniem świata, abyśmy byli świętymi i niepokalanymi przed oczyma jego w miłości.

5 Który nas przenaznaczył ku przysposobieniu za syny przez Jezusa Chrystusa ku sobie, wedle postanowienia woléj swojéj:

6 Ku chwale sławy łaski swojéj, przez którą nas przyjemnymi uczynił w umiłowanym Synie swoim.

7 W którym mamy odkupienie przez krew jego, odpuszczenie grzechów wedle bogactw łaski jego,

8 Która nader obfitowała przeciw nam we wszelakiéj mądrości i roztropności,

9 Aby nam oznajmił tajemnicę woléj swojéj, wedle upodobania swojego, które postanowił w nim,

10 W rozrządzeniu zupełności czasów, aby w Chrystusie wszystko naprawił, co na niebiesiech, i co na ziemi jest: w nim,

11 W którym téż my losem wezwani jesteśmy, przenaznaczeni wedle postanowienia jego, który sprawuje wszystko, wedle rady woléj swojéj,

12 Abyśmy byli ku chwale sławy jego my, którzyśmy wprzód nadzieję pokładali w Chrystusie,

13 W którym i wy, usłyszawszy słowo prawdy, (Ewangelią zbawienia waszego); w którego téż uwierzywszy, jesteście zapieczętowani Duchem obietnice Świętym,

14 Który jest zadatkiem dziedzictwa naszego na okup nabycia, ku chwale sławy jego.

15 Dlatego i ja usłyszawszy wiarę waszę, która jest w Panie Jezusie, i miłość ku wszystkim świętym,

16 Nie przestawam dziękować za was, wzmiankę o was czyniąc w modlitwach moich,

17 Aby Bóg Pana naszego Jezusa Chrystusa, Ojciec chwały, dał wam ducha mądrości i objawienia, w uznaniu jego:

18 Oświecone oczy serca waszego, abyście wiedzieli, która jest nadzieja wezwania jego, i które bogactwa chwały dziedzictwa jego w świętych:

19 I która jest przewyższająca wielkość mocy jego przeciwko nam, którzy wierzymy, według skuteczności mocy siły jego, [2]

20 Którą sprawił w Chrystusie, wzbudziwszy go z martwych i posadziwszy na prawicy swojéj na niebiesiech:

21 Nad wszelakie księstwa i władzą i moc, panowanie, i wszelkie imię, które się mianuje nie tylko w tym wieku, ale téż i w przyszłym.

22 I wszystko poddał pod nogi jego: a jego dał głową, nad wszystkim kościołem, [3]

23 Który jest ciałem jego i napełnieniem tego, który wszystko we wszystkich wypełnia.
Rozdział II
Ephezowie nie podlejsi, niż Żydowie, od grzechów wybawieni, od niewiernych odłączeni, powinni Bogu być wdzięczni.

I was, którzyście byli umarli przez występki i grzechy wasze, [4]

2 W którycheście niekiedy chodzili wedle wieku świata tego, według książęcia władzy powietrza tego, ducha, który teraz moc pokazuje w synach niewierności,

3 Między którymi i my wszyscy obcowaliśmy niekiedy w pożądliwościach ciała naszego, czyniąc wolą ciała i myśli, i byliśmy z przyrodzenia synmi gniewu jako i drudzy.

4 Lecz Bóg, (który jest bogatym w miłosierdziu), dla zbytniéj miłości swojéj, którą nas umiłował,

5 I gdyśmy byli umarłymi przez grzechy, ożywił nas społem w Chrystusie, (którego łaską jesteście zbawieni).

6 I wzbudził pospołu i wespółek posadził na niebiesiech w Chrystusie Jezusie,

7 Aby okazał w nadchodzących wiekach obfite bogactwa łaski swojéj, w dobrotliwości przeciwko nam w Chrystusie Jezusie.

8 Albowiem łaską jesteście zbawieni przez wiarę, (i to nie z was, bo dar Boży jest).

9 Nie z uczynków, aby się kto nie chlubił.

10 Albowiem stworzeniem jego jesteśmy, stworzeni w Chrystusie Jezusie na uczynki dobre, które przedtem Bóg zgotował, abyśmy w nich chodzili.

11 Przetóż pamiętajcie, żeście niekiedy wy poganie w ciele, którzy nazwani jesteście odrzezkiem, od tego, które zowią obrzezaniem na ciele rękoma uczynionem,

12 Którzyście byli na on czas bez Chrystusa, oddaleni od obcowania z Izraelem i obcymi od testamentów obietnice, nadzieje nie mający i bez Boga na tym świecie.

13 A teraz w Chrystusie Jezusie wy, którzyście niekiedy byli daleko, staliście się blizko we krwi Chrystusowéj.

14 Albowiem on jest pokojem naszym, który oboje jednem uczynił i średnią ścianę przegrody rozwalił: nieprzyjaźń w ciele swojem

15 I zakon przykazania wyrokami skaziwszy, aby dwu stworzył w samym sobie w jednego nowego człowieka, czyniąc pokój:

16 I pojednał obudwu w jednem ciele z Bogiem przez krzyż, umorzywszy nieprzyjaźni w samym sobie.

17 I przyszedłszy opowiedział pokój wam, którzyście byli daleko, i pokój tym, którzy blizko.

18 Albowiem przezeń mamy przystęp oboje w jednym Duchu do Ojca. [5]

19 A przeto już nie jesteście goście i przychodnie, aleście mieszczanie z świętymi i domownicy Boży,

20 Wybudowani na fundamencie Apostołów i proroków, gdzie głównym węgielnym kamieniem sam Jezus Chrystus.

21 Na którym wszystko budowanie wywiedzione, rośnie w kościół święty w Panu,

22 Na którym téż i wy pospołu budujecie się na mieszkanie Boże w Duchu.
Rozdział III
Paweł święty miał osobną łaskę poganom Ewangelią kazać ku oświeceniu ich.

Dlatego ja Paweł więzień Chrystusa Jezusa za was pogany:

2 Jeźliście jedno słyszeli o szafowaniu łaski Bożéj, która mi jest do was dana.

3 Przez objawienie oznajmiona mi jest tajemnica, jakom przedtem pisał na krotce:

4 Jako czytając możecie zrozumieć wyrozumienie moje w tajemnicy Chrystusowéj.

5 Która inszych wieków nie była poznana od synów ludzkich, jako teraz objawiona jest świętym Apostołom jego i prorokom w Duchu.

6 Iż poganie są spółdziedzicy i spólcielni i spółuczęstnicy obietnice jego w Chrystusie Jezusie przez Ewangelią.

7 Któréjem się stał sługą wedle daru łaski Bożéj, która mi jest dana wedle skuteczności mocy jego. [6]

8 Mnie najmniejszemu ze wszystkich świętych dana jest łaska ta, abym między pogany przepowiadał niedościgłe bogactwa Chrystusowe,

9 A iżbym objaśnił wszystkim, który jest szalunek tajemnice zakrytéj od wieków w Bogu, który wszystko stworzył,

10 Aby teraz wiadoma była księstwom i zwierzchnościom na niebiosach przez kościół rozliczna mądrość Boża,

11 Wedle przenaznaczenia wieków, które uczynił w Chrystusie Jezusie Panie naszym,

12 W którym mamy bezpieczność i przystęp z ufaniem, przez wiarę jego.

13 Przetóż proszę, abyście nie ustawali w uciskach moich za was, która jest chwała wasza.

14 Dlatego klękam na kolana moje ku Ojcu Pana naszego Jezusa Chrystusa,

15 Z którego wszelkie ojcostwo na niebie i na ziemi jest nazywane,

16 Aby wam dał wedle bogactw chwały swéj, żebyście byli mocą utwierdzeni przez Ducha jego we wnętrznego człowieka,

17 Aby mieszkał Chrystus przez wiarę w sercach waszych: w miłości wkorzenieni i ugruntowani,

18 Żebyście mogli pojąć z wszystkimi świętymi, która jest szerokość i długość i wysokość i głębokość:

19 I poznać miłość Chrystusową przewyższającą naukę, abyście byli napełnieni wszelakiéj zupełności Bożéj.

20 A temu, który mocen jest wszystko daleko obficiéj uczynić, niż prosimy albo rozumiemy, wedle mocy, która w nas skutecznie robi: [7]

21 Jemu chwała w kościele i w Chrystusie Jezusie na wszystkie rodzaje wieku wieków. Amen. [8]
Rozdział IV
Kościół ciału człowieczemu przypodoban i rożnością członków okraszon, o jedność i obyczajów pocześność ma pracować.

Proszę was tedy ja, więzień w Panu, abyście chodzili godnie powołaniu, któremeście powołani: [9]

2 Z wszelaką pokorą i cichością, z cierpliwością, znosząc jeden drugiego w miłości,

3 Starając się, abyście zachowali jedność ducha w związce pokoju. [10]

4 Jedno ciało i jeden duch, jako jesteście wezwani w jednéj nadziei wezwania waszego.

5 Jeden Pan, jedna wiara, jeden chrzest.

6 Jeden Bóg i Ojciec wszystkich, który jest nade wszystkie i po wszystkich i we wszystkich nas. [11]

7 Lecz każdemu z nas dana jest łaska wedle miary daru Chrystusowego. [12]

8 Dlatego mówi: Wstąpiwszy na wysokość, wiódł więźnie poimane, i dał dary ludziom. [13]

9 A to, że wstąpił, cóż jest, jedno iż pierwéj był zstąpił do niższych części ziemie?

10 Który zstąpił, tenżeć jest, który téż wstąpił nad wszystkie niebiosa, aby napełnił wszystko.

11 I tenże dał niektóre Apostoly, a niektóre proroki, a drugie Ewangelisty, a inne pasterze i doktory: [14]

12 Ku wykonaniu świętych, ku robocie posługowania, ku budowaniu ciała Chrystusowego,

13 Ażbyśmy się wszyscy zeszli w jedność wiary i poznania Syna Bożego, w męża doskonałego, w miarę wieku zupełności Chrystusowéj.

14 Abyśmy już nie byli dziećmi chwiejącemi się, i nie byli uniesieni od każdego wiatru nauki przez złość ludzką, przez chytrość na oszukanie błędu.

15 A czyniąc prawdę w miłości, żebyśmy rośli w nim we wszystkiem, który jest głowa, Chrystus, [15]

16 Z którego wszystko ciało złożone i spojone będąc, przez wszystkie stawy dodawania wedle skuteczności podług miary każdego członka, czyni pomnożenie ciała ku zbudowaniu samego siebie w miłości.

17 To tedy powiadam i oświadczam się w Panu, abyście już nie chodzili jako i poganie chodzą, w próżności umysłu swego. [16]

18 Ciemnościami zaćmiony mając rozum, oddaleni od żywota Bożego dla nieumiejętności, która w nich jest, dla zaślepienia serca ich, [17]

19 Którzy przyszedłszy w rozpacz, udali samych siebie na niewstydliwość ku popełnieniu wszelakiéj nieczystości, ku łakomstwu.

20 Lecz wy nie takeście się Chrystusa nauczyli:

21 Jeźliżeście go jednak słuchali i w nim jesteście wyuczeni, (jako jest prawda w Jezusie).

22 Abyście złożyli według dawnego obcowania starego człowieka, który się psuje według żądz błędu.&nbsp[18]

23 A odnówcie się duchem umysłu waszego: [19]

24 I obleczcie się w nowego człowieka, który wedle Boga stworzony jest w sprawiedliwości i świętobliwości prawdy. [20]

25 A przetóż złożywszy kłamstwo, mówcie każdy prawdę z bliźnim swoim; bo jesteście członkami jeden drugiego. [21]

26 Gniewajcie się, a nie grzeszcie; słońce niechaj nie zapada na rozgniewanie wasze. [22]

27 Nie dawajcie miejsca djabłu. [23]

28 Który kradł, niechaj już nie kradnie; lecz raczej niech pracuje, robiąc rękoma swemi co jest dobrego, aby miał zkąd udzielić mającemu potrzebę.

29 Wszelka mowa zła niech z ust waszych nie pochodzi; ale jeżli która dobra ku zbudowaniu wiary, aby łaskę zjednała słuchającym.

30 A nie zasmucajcie Ducha Świętego Bożego, w którym zapieczętowani jesteście na dzień odkupienia.

31 Wszelaka gorzkość, i gniew i zagniewanie i wrzask i bluźnienie niech będzie odjęte od was z wszelaką złością.

32 Ale bądźcie łaskawi jedni przeciw drugim, miłosierni, odpuszczając jeden drugiemu, jako i Bóg w Chrystusie wam odpuścił. [24]
Rozdział V
Którzy łaski Chrystusowéj żądają, mając się wystrzegac grzechów cielesnych, obżarstwa, nieczytości, i przyczyn ich, w małżeństwie téż rządnie się sprawować.

Bądźcież tedy naśladowcami Bożymi, jako synowie najmilsi,

2 A chodźcie w miłości, jako i Chrystus umiłował nas i wydał samego siebie za nas obiatą i ofiarą Bogu na wonność wdzięczności. [25]

3 A porubstwo i wszelka nieczystość, albo łakomstwo niechaj nie będzie ani pomieniono między wami, jako świętym przystoi. [26]

4 Albo sprosność, albo głupia mowa, albo żartowanie, które do rzeczy nie należy, ale raczéj dziękowanie.

5 Bo to wiedzcie rozumiejąc, iż wszelki porubca, albo nieczysty, albo łakomiec, (co jest bałwochwalstwo,) nie ma dziedzictwa w królestwie Chrystusowem i Bożem.

6 Niechaj was nikt nie zwodzi próżnemi słowy; albowiem dlategoć przychodzi gniew Boży na syny niewierności. [27]

7 Nie bądźcież tedy uczęstnikami ich.

8 Albowiemeście byli niekiedy ciemnością; lecz teraz światłością w Panu. Jako synowie światłości chodźcie.

9 Bo owoc światłości jest w wszelakiéj dobrotliwości i sprawiedliwości i prawdzie.

10 Doświadczając, co jest wdzięcznego Bogu:

11 A nie spółkujcie z uczynkami niepożytecznemi ciemności, ale raczéj strofujcie.

12 Albowiem co się od nich potajemnie dzieje, sromota i powiadać.

13 A wszystko, co bywa strofowano, od światłości bywa objawiono; bo wszystko, co objawiono bywa, jest światło.

14 Dlatego mówi: Wstań, który śpisz, i powstań zmartwych, a oświeci cię Chrystus.

15 Patrzcież tedy, bracia! jakobyście ostrożnie chodzili, nie jako niemądrzy, ale jako mądrzy, [28]

16 Czas odkupując, iż dni złe są.

17 A przetóż nie bądźcie nieroztropnymi, ale rozumiejącymi, która jest wola Boża. [29]

18 A nie upijajcie się winem, w którem jest nieczystota, ale bądźcie napełnieni Duchem świętym,

19 Rozmawiając sobie w Psalmiech i w pieśniach i w śpiewaniach duchownych, śpiewając i grając w sercach waszych Panu,

20 Dziękując zawsze za wszystko, w imię Pana naszego Jezusa Chrystusa Bogu i Ojcu,

21 Będąc poddanymi jedni drugim w bojaźni Chrystusowéj.

22 Żony niechaj będą poddane mężom swym, jako Panu; [30]

23 Albowiem mąż jest głową żony, jako Chrystus jest głową kościoła: on Zbawicielem ciała jego. [31]

24 Ale jako kościół poddany jest Chrystusowi, tak téż żony swoim mężom we wszystkiem.

25 Mężowie! miłujcie żony wasze, jako i Chrystus umiłował kościół i samego siebie wydał zań, [32]

27 A sam sobie wystawił kościół chwalebny, nie mający zmazy albo zmarszczku, alebo czego takowego; ale iżby był święty i niepokalany.

28 Tak i mężowie mają miłować żony swoje, jako swoje ciała. Kto miłuje żonę swoję, samego siebie miłuje.

29 Albowiem nigdy żaden ciała swego nie miał w nienawiści; ale je wychowa i ogrzewa, jako i Chrystus kościół.

30 Bo jesteśmy członkami ciała jego, z ciała jego i z kości jego.

31 Dlatego opuści człowiek ojca i matkę swoję i złączy się z żoną swoją. I będą dwoje w jednem ciele.

32 Sakrament[33] to wielki jest: a ja mówię w Chrystusie i w kościele.

33 Wszakże i każdy z was z osobna niechaj miłuje żonę swoję jako siebie samego: a żona niech się boi męża swego.
Rozdział VI
Jako synowie z rodzicami, rodzicowie z syny, panowie z sługami, słudzy z pany swymi mają się obchodzić, i pospolicie wszyscy jako się w cnotach obierać.

Synowie! bądźcie posłuszni rodzicom waszym w Panu; bo to jest sprawiedliwa. [34]

2 Czcij ojca twego i matkę twoję, (które jest pierwsze przykazanie z obietnicą), [35]

3 Abyć się dobrze działo, i abyś był długowieczny na ziemi.

4 A wy ojcowie! nie pobudzajcie ku gniewowi synów waszych; ale je wychowywajcie w karności i w groźbie Pańskiéj.

5 Słudzy! posłuszni bądźcie panom wedle ciała z bojaźnią i ze drżeniem, w prostości serca waszego, jako Chrystusowi: [36]

6 Nie na oko służąc, jakoby ludziom się podobając, ale jako słudzy Chrystusowi, czyniąc wolą Bożą z serca:

7 Z dobrą wolą służąc, jako Panu a nie ludziom:

8 Wiedząc, iż każdy, cokolwiek uczyni dobrego, to odniesie od Pana, choć niewolnik, choć wolny.

9 A wy panowie! tóż im czyńcie, odpuszczając groźby, wiedząc, iż i ich i wasz Pan jest w niebiesiech, a niemasz u niego względu na osoby. [37]

10 Na ostatek bracia! zmacniajcie się w Panu i w sile mocy jego.

11 Obleczcie się w zupełną zbroję Bożą, abyście mogli stać przeciwko zasadzkom djabelskim.

12 Albowiem nie mamy biedzenia przeciw ciału i krwi, ale przeciwko książętom i władzom, przeciwko rządzcom świata tych ciemności, przeciwko duchownym złościom w niebiesiech. [38]

13 A przetóż weźcie zupełną zbroję Bożą, abyście mogli sprzeciwić się w dzień zły i w wszystkiem doskonali stać.

14 Stójcież tedy, przepasawszy biodra wasze prawdą, a oblókłszy pancerz sprawiedliwości,

15 I obuwszy nogi w gotowość Ewangelii pokoju:

16 We wszystkiem biorąc tarczą wiary, którąbyście mogli wszystkie strzały ogniste złośliwego zgasić.

17 I przyłbicę zbawienia weźmijcie i miecz ducha, (które jest słowo Boże). [39]

18 W każdej modlitwie i prośbie modląc się na każdy czas w duchu i w nim czując z wszelką ustawicznością i prośbą za wszystkie święte: [40]

19 I za mię, aby mi była dana mowa w otworzeniu ust moich z dufnością, abym oznajmiał tajemnicę Ewangelii, [41]

20 Dla któréj poselstwo sprawuję w łańcuchu, tak żebym o nie śmiały był, jako mi mówić potrzeba.

21 A iżbyście i wy wiedzieli, co się zemną dzieje, co czynię, wszystko wam oznajmi Tychikus, najmilszy brat i wierny sługa w Panie,

22 Któregom posłał do was na to samo, abyście wiedzieli, co się z nami dzieje, ażeby pocieszył serca wasze.

23 Pokój braciéj i miłość z wiarą od Boga Ojca i Pana Jezusa Chrystusa.

24 Łaska ze wszystkimi, którzy miłują Pana naszego Jezusa Chrystusa w nieskaziteluości. Amen.
"""

save_chapters_to_files(text)


