album = [
(1967, 'DavidBowie'),
(1969, 'SpaceOddity'),
(1970, 'TheManWhoSoldTheWorld'),
(1971, 'HunkyDory'),
(1972, 'TheRiseAndFallOfZiggyStardustAndTheSpidersFromMars'),
(1973, 'AladdinSane'),
(1973, 'PinUps'),
(1974, 'DiamondDogs'),
(1975, 'YoungAmericans'),
(1976, 'StationToStation'),
(1977, 'Low'),
(1977, 'Heroes'),
(1979, 'Lodger'),
(1980, 'ScaryMonstersAndSuperCreeps'),
(1983, 'LetsDance'),
(1984, 'Tonight'),
(1987, 'NeverLetMeDown'),
(1993, 'BlackTieWhiteNoise'),
(1995, '1.Outside'),
(1997, 'Earthling'),
(1999, 'Hours'),
(2002, 'Heathen'),
(2003, 'Reality'),
(2013, 'TheNextDay'),
(2016, 'BlackStar')]

for _ in range(int(input())):
    s, e = map(int, input().split())
    if s < 1967:
        s = 1967
        
    lst = []
    for i in range(s, e+1):
        for j in album:
            if j[0] == i:
                lst.append(j)
                
    print(len(lst))    
    if lst:
        [print(*i) for i in lst]
        