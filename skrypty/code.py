import re

def remove_line_numbers_and_extra_spaces(text):
    # Regular expression to match lines that start with a number followed by a space
    pattern = r'^\d+\s*'

    # Split the text into lines
    lines = text.splitlines()

    # Process each line to remove the number at the start
    cleaned_lines = [re.sub(pattern, '', line) for line in lines]

    # Filter out any empty lines
    cleaned_lines = [line for line in cleaned_lines if line.strip()]

    # Join the cleaned lines back into a single string
    cleaned_text = '\n'.join(cleaned_lines)

    return cleaned_text

# Example usage
input_text = """1 Y Począł drugi mówić, który mówił o mocy królewskiéy.

2 O mężowie, a za nie mocnieyszy są ludzie, którzy morzem y ziemią władną, y wszytkim co na nich iest?

3 A król wszytko przewyższa, y panuio nad nimi, y wszytko cokolwiek im roskaże czyni.

4 Y ieśli ie pośle na żołnierską, idą, y góry, y mury, y wieże rozwalaią,

5 Morduią y mordowani bywaią, a słowa królewskiego nie przestępuią. Bo ieśli zwyćiężą wszytkie łupy których dostali, królowi odnoszą.

6 Także y inni wszyscy, y cokolwiek ich nie walczy a nie woiuie, ale rolą orzą, zaś gdy pożną, przynoszą dań królowi.

7 A on sam ieden ieśli rzecze, Zabiyćie, zabiiaią: rzecze, wypuśćcie, wypusczaią:

8 Rzeczeli, ubiyćie, ubiią: rzeczeli wykorzeńćie, wykorzenią: rzeczeli buduyćie, buduią:

9 Rzeczeli wytnićie, wyćinaią: rzeczeli sczepćie, sczépią.

10 Y wszytek lud y woyska słuchaią go: a na to sam śiedźi, y piie, y spi.

11 A ći go strzegą wokoło, a nie może żaden z nich odéyśdź, y czynić sprawy swoie, ale na słowo go słuchaią.

12 O mężowie, iakóż król nie przewyższa namocnicyszy, który ma takie zalecenie? Y umilkł.

13 Trzeći, który o niewiastach a o prawdźie powiadał, ten iest Zorobabel, począł mówić:

14 Mężowie, nie wielki król, y śiła ludzi, ani wino przewyższa. Któż tedy iest co panuie nad nimi?

15 Aza nie niewiasty urodźiły króla, y wszytek lud który panuie nad morzem y nad źiemią?

16 Y z nich się narodźili, y one wychowały te którzy sadźili winnice, z których bywa wino?

17 Y one wszytkim ludźióm szaty czynią, y one czynią chwałę ludźióm, a nie mogą bydź ludźie odłączeni od niewiast.

18 Ieśli zbierą złoto y śrébro, y wszelką rzecz piękną, a uyźrzą iednę białągłowę podobną y gładką,

19 Wszytko to opuśćiwszy na nię pilnie patrzą, a otworzywszy gębę przypatrują się iéy, y wabią ią więcéy niźli złoto y śrébro, y wszelką rzecz drogą.

20 Opuscza człowiek oyca swego który go wychował, y krainę swoię, a przyłącza się do niewiasty.

21 Y z niewiastą cieszy duszę, y ani na oyca pamięta, ani na matkę, ani na oyczyznę.

22 A z tąd wiedźiéć maćie że niewiasty panuią nad wami. Izali nie żałuiećie?

23 Y bierze człowiek miecz swóy, y idźie na drogę żeby czynił kradźiesz y mężobóystwa, y pływał po morzu y po rzekach.

24 Y widźi lwa, y w ćiemnośći chodzi: a naczyniwszy kradzieży, y zdrady, y łupieży, miłéj swéy przynosi.

25 Ktemu miłuie człowiek żonę swą więcéy niźli oyca abo matkę.

26 Y wiele ich poszalało dla żon swoich, y stali się niewolniki dla nich:

27 Y wicie ich poginęło, y pobito, y zgrzészyło dla niewiast.

28 A teraz wierzcie mi, iż wielki iest król w mocy swéy, bo się go wszytkie źiemie obawiaią dotknąć,

29 Przećiem widział Apamenę córkę Bezaka zacnego nałożnicę królewską, gdy śiedziała podle króla po prawéy stronie,

30 Y źięła koronę z głowy iego, y włożyła na się, a dłonią króla biła od lew.

31 A nad to otworzywszy usta patrzył na nię: a ieśli się nań uśmiechnie, śmieie się: bo iesli się nań rozgniewa, pobłaża iéy, aż go zaśię w łaskę prziymie.

32 O mężowie dla czegóż niewiasty nie są mocnieysze? wielka iest źiemia, y wysokie iest niebo, któż to czyni?

33 Tedy król y panowie poglądali ieden na drugiego: y począł o prawdźie mówić

34 O mężowie, aza nie mocne są niewiasty? Wielkać iest źiemia, y wysokie niebo: y prędki bieg słońca obraca w koło niebo na swe mieysce za ieden dźień.

35 A więc nie wielmożny iest ten który to czyni? Y prawda iest wielka y mocnicysza nad wszytko.

36 Wszytka źiemia prawdy wzywa, niebo téż ią błogosławi, y wszytkie dźieła poruszają się y drżą przed nią, a niemasz u niéy nic nieprawego.

37 Wino nieprawe, nieprawy król, nieprawe niewiasty, nieprawi wszyscy synowie człowieczy, y nieprawe ich wszytkie sprawy, y niemasz w nich prawdy, y poginą w nieprawości swoiéy:

38 A prawda trwa, y wzmaga się na wieki, y żywie, y zwyćięża przez wieki wieków.

39 Y niémasz u niéy brakowania osób, ani różności: ale czyni sprawiedliwość wszytkim niesprawiedliwym y złośćiwym, wszyscy się cieszą z uczynków iéy.

40 Y niémasz w sądzie iéy niesprawiedliwośći, ale moc y królestwo, y możność, y maiestat wszytkich wieków. Błogosławiony Bóg prawdy.

41 Y przestał mówić, y wszyscy ludźie zawołali, y rzekli: Wielka iest prawda, y przewyższa.

42 Tedy król rzékł iemu. Proś ieśli czego chcesz, więcéy niż co na piśmie podano, a dam ći: ponieważeś naleźion mędrszym nad towarzysze, będéiesz siadał tusz podle mnie, a będziesz zwan powinowatym moim.

43 Tedy rzekł królowi: Wspomni na ślub twóy, któryś ślubił zbudować Jeruzalem, onego dnia któregoś dostał królestwa:

44 Y wszytkie naczynia które zabrano z Jeruzalem odesłać: które odłożył Cyrus gdy Babilon pobił, a chćiał ie tam odesłać.

45 A tyś ślubił zbudować kośćiół, który spalili Idumeyczycy, gdy ziemia Żydowska od Chaldcyczyków była spustoszona.

46 A toć iest Panie, czego teraz żądam, y czego proszę, to iest: Maiestaćie, czego od ćiebie żądał abyś wypełnił ślub któryś ślubił królowi niebieskiemu usty twemi.

47 Tedy Dariusz król powstawszy pocałował go, y napisał listy do wszytkich szafarzów, do starost, y panów, aby go prowadźili, y te którzy z nim byli, ćiągnące, aby budowali Jeruzalem.

48 A wszytkim starostom, którzy byli w Syryiéy, y w Phenicyiéy, y na Libanie, pisał listy, aby nawozili drzewa Cedrowego z Libanu do Jeruzalem, aby z nimi miasto budowali.

49 Y napisał list wolnośći wszytkim Żydom, którzy ćiągnęli z królestwa do Żydowskiéy źiemie, aby żaden Pan, ani urzędnik, ani starosta nieśmiał najeżdżać bram ich:

50 Ale iżby wszytka ich źiemia którą otrzymali, wolna im była: a iżby Idumeyczycy puśćili miasteczka Żydowskie które dzierżą.

51 Y na budowanie kośćioła, aby dawano na każdy rok dwadźieśćia talentów, ażby się budowanie dokończyło:

52 A na palenie całopalenia na ołtarzu na każdy dzień, tak iako maią roskazanie, aby dawano drugie dźieśięć talentów na każdy rok.

53 Y wszytkim którzy wyszli z Babilonu budować miasto żeby była wolność, tak samym iako y synom ich, wszytkim kapłanom którzy idą naprzód.

54 Opisał téż y summę, y świętą szatę kazał dać, w któréyby służyli:

55 A Lewitom napisał żeby dano co nakazano, aż do dnia którego będzie dokonany dóm, y Jeruzalem zbudowane:

50 A wszytkim strzegącym miasta, napisał aby część y myto dawano.

57 Y odesłał wszytkie naczynia, którekolwiek był oddzielił Cyrus z Babiloniiéy, y wszytko cokolwiek był Cyrus rzékł: y on roskazał aby uczyniono y odesłano do Jeruzalem.

58 A gdy wyszedł on młodźieniec, podniózszy twarz ku Jeruzalem: błogosławił króla niebieskiego,

59 Y rzékł: Od ćiebieć iest zwycięstwo, y od ćiebie iest mądrość y oświecenie. A iam iest sługa twóy.

60 Błogosławionym iest któryś mi dał mądrość, y tobie wyznawać będę Panie Boże oyców naszych.

61 Y wźiął listy, y iechał do Babilonu, y przyiechał y oznaymił wszytkiéy brsćiéy swéy którzy byli w Babilonie;

62 Y błogosławili Boga oyców swoich, iż im dał folgowanie y ochłodę,

63 Aby szli y budowali Jeruzalem, y kośćiół w którym iest mianowano imię iego, y weselili się z muzyką y z radośćią przez śiedm dni. """

cleaned_text = remove_line_numbers_and_extra_spaces(input_text)
print(cleaned_text)


