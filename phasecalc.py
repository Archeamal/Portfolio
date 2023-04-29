import re
import math


pi = (math.pi)

print("Hello!! Welcome to MoonPhaseCalc!")
print("This lil script will tell you what phase the moon was in on any given day!")
repeat = 0
while repeat == 0:
    print("\n")
    iDate = input('Pls type the date in the format MM/DD/YYYY, include slashes\n')
    while "/" in iDate ==False or iDate.isalpha()==True:
        print("Woops Please make sure that date is correct!")
        iDate = input('Pls type the date in the format MM/DD/YYYY, include slashes\n')

    iMonth = re.findall(r'\d+', iDate)[0]
    iDay = re.findall(r'\d+', iDate)[1]
    iYear = re.findall(r'\d+', iDate)[2]
    while int(iMonth) <= 0 or int(iMonth) > 12 or int(iDay) <= 0 or int(iDay) > 31 or int(iYear) < 0 :
        print("Woops Please make sure that date is correct!")
        iDate = input('Pls type the date in the format MM/DD/YYYY, include slashes\n')
        iMonth = re.findall(r'\d+', iDate)[0]
        iDay = re.findall(r'\d+', iDate)[1]
        iYear = re.findall(r'\d+', iDate)[2]
    # first we'll convert the current date to Julien days
    if int(iMonth) == 1 or int(iMonth) == 2:
        iYear = int(iYear)-1
        iMonth = int(iMonth)+12
    A = int(iYear)//100
    B = A//4
    C = 2-A+B
    E = (365.25*(int(iYear)+4716))//1
    F = (30.6001*(int(iMonth)+1))//1
    iJulDays = C+int(iDay)+E+F-1524.5
    # we know that on jan 6th 2000, there was defintely a new moon, 
    # running this thru the calc will give us a value of 2451549.5 in julien days, we'll use this to compare
    julDaysSinceNewMoon = int(iJulDays)-2451549
    fullCyclesSince = julDaysSinceNewMoon//29.530587981
    daysSinceNewMoonFloat = (julDaysSinceNewMoon/29.530587981)
    daysSinceNewMoon = ((round(daysSinceNewMoonFloat, 3))-fullCyclesSince)*29.530587981

    julDaysSinceNewMoon = int(iJulDays)-2451549.5
    fullLunarOrbitsSince = julDaysSinceNewMoon//27.3
    daysSinceNewLunarOrbitFloat = (julDaysSinceNewMoon/27.3)
    daysSinceNewLunarOrbit = ((round(daysSinceNewLunarOrbitFloat, 3))-fullLunarOrbitsSince)*27.3

    julDaysSinceNewYear = int(iJulDays)-2451544 # this is the num of jul days since the new year (1/1/2000)
    fullSolarCyclesSince = julDaysSinceNewYear//365.25
    daysSinceNewYearFloat = (julDaysSinceNewYear/365.25)
    daysSinceNewYear = ((round(daysSinceNewYearFloat, 3))-fullSolarCyclesSince)*365.25
    # now we can see which phase the moon is in currently
    # rn its split evenly into 8th, need to improve accuracy
    if daysSinceNewMoon < 1.0:
        phase = 'New'
    if daysSinceNewMoon >= 1.0 and daysSinceNewMoon < 7.38264699625:
        phase = 'Waxing Crescent'
    if daysSinceNewMoon >= 7.38264699625 and daysSinceNewMoon <= 9.0:
        phase = 'First Quarter'
    if daysSinceNewMoon > 9.0 and daysSinceNewMoon < 14.7652939905:
        phase = 'Waxing Gibbous'
    if daysSinceNewMoon >= 14.7652939905 and daysSinceNewMoon <= 16.0:
        phase = 'Full'
    if daysSinceNewMoon > 16.0 and daysSinceNewMoon < 22.0:
        phase = 'Waning Gibbous'
    if daysSinceNewMoon >= 22.0 and daysSinceNewMoon <= 23.0:
        phase = 'Third Quarter'
    if daysSinceNewMoon > 23.0 and daysSinceNewMoon < 29.530587981:
        phase = 'Waning Crescent'
    if daysSinceNewMoon >= 29.530587981:
        phase = 'New'

    
    nextNew = 30-(daysSinceNewMoon//1)
    if nextNew <= 0:
        nextNew = abs(nextNew)
        if nextNew == 0:
            nextNew = 1
    nextFull = nextNew - 15 
    if nextFull <= 0:
        nextFull = abs(nextFull)
        if nextFull == 0:
            nextFull = 30

    print("\n")
    print("On " + str(iDate) + ", There will be a " + phase + " Moon!!!")
    print(str(iDate) + " is \n" + str(daysSinceNewMoon//1) + " days into the current Lunar cycle." )
    print(str(daysSinceNewLunarOrbit//1) + " days into the current lunar orbit")
    print(str(daysSinceNewYear//1) + " days into the current solar cycle")
    print("\nThe next Full Moon will begin in " + str(nextFull) + " days, And the next New Moon will begin in " + str(nextNew) + " days.")


    # a full (geocentric) sun revolution is 365 days 5 hours 59 min 16 sec (365.25 days)
    # a full (geocentic) moon revolution is 27.3 days
    # it takes the moon 29.5 days to complete a new-new lunar cycle (from a geocentric view)
    # jan 6 2000  at 12:24:01 was a perfect new moon, (6.521 days) into the current solar cycle

    # lets start by setting up our equation, we can define an orbit with a standard circle (x−h)^2+(y−k)^2=r^2  where the center is h,k and the radius is r
    # we already know the length of our orbits, we can plot these by using circumference to get radius c=2PIr

    lunarRad = 27.3/(2*pi)
    solarRad = 365.25/(2*pi)
    # 4.344929946408743
    # 58.131342964314776

    #lunarOrb = (x-a)**2+(y-b)**2 == lunarRad**2  Instead we're gonna use parametric format for these equations
    #solarOrb = (x-a)**2+(y-b)**2 == solarRad**2   x = r * cos(t) + a    ,    y = r * sin(t) + b,     also use t for theta  (angle between 0 and 2pi)

                #lunar orbit splitting

    a = 0
    b = 0
    #The lower this value the higher quality the circle is with more points generated
    stepSize = 0.241 # will give us 27 verticies
    #Generated vertices
    positions = []
    t = 0
    while t < 2 * pi:
        positions.append((lunarRad * math.cos(t) + a, lunarRad * math.sin(t) + b))
        t += stepSize

    # now we can work out some angles with trig, the x and y value for each point on an individual orbit
    # describes how far that point is from the center. so if my point value is 4,-5  we can imagine a triangle
    # with the dist between center and x being 4, an between center and y is 5
    # we can find the angle of the center vertex with inverse tangent of our inversed x,y
    #   tan-1(5/4)=theta' angle 
    # remember that this will give us theta prime!!! theta is 360 - theta prime


    dayPoint = (int(re.findall(r'\d+', str(daysSinceNewLunarOrbit))[0]))-1
    if float(str("." + (re.findall(r'\d+', str(daysSinceNewLunarOrbit))[1]))) > 0.5:
        dayPoint += 1

    num4InvTan = positions[dayPoint]
    reCatA = (num4InvTan)[0]
    reCatB = (num4InvTan)[1]
    lunarA = reCatA
    lunarB = reCatB
    if reCatA < 0:
        reCatA = abs(num4InvTan[0])
    if reCatB < 0:
        reCatB = abs(num4InvTan[1])
   
    invTanVal = (reCatB/reCatA)
    lunarThetaPrimeAng = math.degrees(math.atan(invTanVal))



                #solar orbit splitting

    a = 0
    b = 0
    #The lower this value the higher quality the circle is with more points generated
    stepSize = 0.01723   # will give us 365 verticies
    #Generated vertices
    positions = []
    t = 0
    while t < 2 * pi:
        positions.append((solarRad * math.cos(t) + a, solarRad * math.sin(t) + b))
        t += stepSize

    dayPoint = (int(re.findall(r'\d+', str(daysSinceNewYear))[0]))-1
    if float(str("." + (re.findall(r'\d+', str(daysSinceNewYear))[1]))) > 0.5:
        dayPoint += 1

    num4InvTan = positions[dayPoint]
    reCatA = (num4InvTan)[0]
    reCatB = (num4InvTan)[1]
    solarA = reCatA
    solarB = reCatB
    if reCatA < 0:
        reCatA = abs(num4InvTan[0])
    if reCatB < 0:
        reCatB = abs(num4InvTan[1])
    

    invTanVal = (reCatB/reCatA)
    solarThetaPrimeAng = math.degrees(math.atan(invTanVal))

    #alrighty so now that we know the theta' angle, we can start plugging this into the date, compare the lunar and solar angles, and then decide the phase based on that
    
    #lunarHyp = (math.sqrt((lunarA**2)+(lunarB**2)))  #b
    #solarHyp = (math.sqrt((solarA**2)+(solarB**2)))   #a
    #solarLunarDist = (math.sqrt((solarHyp**2)+(lunarHyp**2)))   #c
    solarLunarDist = math.sqrt((lunarA-solarA)**2 + (lunarB-solarB)**2) #c
    lunarDist = math.sqrt((lunarA-0)**2 + (lunarB-0)**2) #b
    solarDist = math.sqrt((solarA-0)**2 + (solarB-0)**2) #a
    #cosine rule!!!  a^2=b^2+c^2-[2bc cosTheta]
    aSq = solarDist**2
    bSqPcSq = ((lunarDist**2)+(solarLunarDist**2))
    bc2 = (2*lunarDist*solarLunarDist)
    # a^2=(bSqPcSq) - (bc2) cosTheta
    # (bc2)cosTheta = (bSqPcSq) - aSq
    # cosTheta = (bSqPcSq-asq)/(bc2)
    Numr8tr = (bSqPcSq - aSq)
    cosTheta = (Numr8tr/bc2)
    illuminationAngle = math.degrees(math.acos(cosTheta))

    #okay im PRETTY dang sure the math here is right, but the illum angle isnt changing how id expect it to, 
    # sooo maybe theres something wrong with when i concat the x,y values and i need to make sure it keep the negative? 
    #  

    #print(lunarThetaPrimeAng)
    #print(solarThetaPrimeAng)
    #print(illuminationAngle)
    print("\nWould you like to do another?")
    yorn = input("Pls type any number to continue, or 0 to quit\n")
    if int(yorn) == 0:
        repeat += 1
