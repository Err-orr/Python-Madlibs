import random
#This is added so the random function will work
import climage
#This is added so an image can get turned into pixel art
import time
#This is added so users can have time to read things or add suspense
option = input("Enter what type of story you want (Madlibs, Custom, Random) ")
#The user is asked what type of story they want. There's also some secrets if you scroll down in the code ;)
while option != "STOP":
  #If the user types stop, the while loop will end.
  if option == "Madlibs":
    #If they typed this then the code will be focused here.
    madlibs = random.randint(1, 4)
    #This will be our randomly generated madlibs, pre-existing (Madlibs), literally randomly generated from a website (Random), or custom ones made by me (Custom). Every time you run the code, it will always generate a random madlibs
    #The first if statement will be considered an example
    if madlibs == 1:
      #The print statement is our title, showing what kind of madlibs it is.
      print("Madlibs: Totally Tie-Dyed")
      #Below is all of our variables. Because the same variable names will get reused multiple times you might see a letter at the front or a number at the end. For example, pnoun means the variable name of what the user is typing, a plural noun. Then the number at the end, we'll say 4, shows how many times it was used before in the story.
      pnoun = input("Type a plural noun: ")
      cele = input("Type a celebrity's name: ")
      cloth = input("Type a piece of clothing: ")
      adj = input("Type an adjective: ")
      noun = input("Type a noun: ")
      pnoun2 = input("Type a plural noun: ")
      cloth2 = input("Type a piece of clothing: ")
      verb = input("Type a verb: ")
      pnoun3 = input("Type a plural noun: ")
      liquid = input("Type a liquid: ")
      adj2 = input("Type an adjective: ")
      noun2 = input("Type a noun: ")
      verb2 = input("Type a verb: ")
      adj3 = input("Type an adjective: ")
      liquid2 = input("Type a liquid: ")
      noun3 = input("Type a noun: ")
      #Then, after the words the user types, the wacky story will get printed and will be setup like this for the below if statements.
      print("Loading story...")
      #Fake loading screen for fun
      time.sleep(5)
      #The user has to wait 5 seconds for their story to get printed.
      print(
        "In the " + str(1960) + "s, tie-dyed " + pnoun +
        " became a popular fashion fad after " + cele +
        " wore a psychedelic " + cloth +
        " at a concert. Soon after, hippies donned this " + adj +
        " apparel while promoting peace and " + noun +
        ". Today, anyone can create colorful " + pnoun2 +
        " in their own backyard. First, take a damp " + cloth2 + ", " + verb +
        " and roll the fabric, then tie it tight with some rubber " + pnoun3 +
        ". Next, dip sections into vats of colored " + liquid +
        ". The longer it soaks, the more " + adj2 +
        " the colors become! Finally, soak your creation in a mixture of " +
        noun2 + " and vinegar. This tangy solvent helps " + verb2 +
        " the dye, keeping colors looking " + adj3 +
        " for years, And if tie-dye isn't your cup of " + liquid2 +
        ", it might make a radical gift for that special " + noun3 +
        " in your life!")
      #But if the number is not one, then it will skip all of this and look for the if statements below that has the correct number.
      print("Creating image theme...")
      time.sleep(15)
      #The user waits for 15 seconds to have the image printed while they're reading the story
      print(climage.convert('cover6.jpg', is_unicode=True))
      #An image will get printed depending on the theme of the story
    if madlibs == 2:
      print("Madlibs: A Letter From George")
      pnoun = input("Type a pnoun: ")
      occup = input("Type an occupation: ")
      place = input("Type a place: ")
      num = int(input("Type a number: "))
      adj = input("Type an adjective: ")
      verbing = input("Type a verb ending with 'ing': ")
      pnoun2 = input("Type a plural noun: ")
      place2 = input("Type a place: ")
      adj2 = input("Type an adjective: ")
      pnoun3 = input("Type a plural noun: ")
      verbing2 = input("Type a verb ending in 'ing': ")
      pnoun4 = input("Type a plural noun: ")
      adj3 = input("Type an adjective: ")
      noun = input("Type a noun: ")
      body = input("Type a part of the body: ")
      verb = input("Type a verb: ")
      adj4 = input("Type an adjective: ")
      body2 = input("Type a part of the body: ")
      print("Loading story...")
      time.sleep(5)
      print("Hello, my fellow " + pnoun + " in " + str(2020) +
        ", it's me, George Washington, the first " + occup +
        ". I am writing from (the) " + place +
        ", where I have been secretly living for the past " + str(num) +
        " years. I am concerned by the " + adj +
        " state of affairs in America these days. It seems that your politicians are more concerned with "
        + verbing + " one another than with listening to the " + pnoun2 +
        " of the people. When we declared our independence from (the) " +
        place2 + ", we set forth on a/an " + adj2 +
        " path guided by the voices of the everyday " + pnoun3 +
        ". If we're going to keep " + verbing2 +
        ", then we need to learn how to respect all " + pnoun4 +
        ". Don't get me wrong; we had " + adj3 +
        " problems in my day, too. Benjamin Franklin once called me a/an " +
        noun + " and kicked me in the " + body +
        ". Bu at the end of the day, we were able to " + verb +
        " in harmony. Let us find that " + adj4 +
        " spirit once again, or else I'm taking my " + body2 +
        " off the quarter!")
    if madlibs == 3:
      print("Madlibs: If I Were President...")
      name = input("Type a name: ")
      num = int(input("Type a number: "))
      adj = input("Type an adjective: ")
      color = input("Type a color: ")
      noun = input("Type a noun: ")
      pfood = input("Type something that can be eaten that ends with 's': ")
      noun2 = input("Type a noun: ")
      verbing = input("Type a verb ending in 'ing': ")
      cloth = input("Type a piece of clothing: ")
      adj = input("Type an adjective: ")
      cele = input("Type a celebrity's name: ")
      num2 = int(input("Type a number: "))
      name2 = input("Type a name: ")
      noun3 = input("Type a noun: ")
      name3 = input("Type a name: ")
      occup = input("Type an occupation: ")
      print("Loading story...")
      time.sleep(5)
      print(
        "My name is " + name + " and I am " + str(num) +
        " years old. If I were president, I'd do a whole bunch of " + adj +
        " things:\n\t" + str(1) + ". I would drive the biggest " + color +
        " car in the country. And that car would go faster than any other " +
        noun + " in the world!\n\t" + str(2) + ". Everyone would eat " +
        pfood + " for dinner.\n\t" + str(3) +
        ". I would live in the Statue of " + noun2 + " and build a " +
        verbing + " pool at her feet.\n\t" + str(4) + ". I would wear a/an " +
        cloth + " on my head, and everyone would say I look " + adj +
        " like " + cele + ". \n\t" + str(5) + ". School would be open only " +
        str(num2) + " days a year.\n\t" + str(6) +
        ". I would give my friends the best jobs. I would nominate " + name2 +
        " to be secretary of (the) " + noun3 + ". and " + name3 +
        " could be vice " + occup + ".")
    if madlibs == 4:
      print("Madlibs: Dining Room Wars")
      noun = input("Type a noun: ")
      noun2 = input("Type a noun: ")
      pnoun = input("Type a plural noun: ")
      adj = input("Type an adjective: ")
      adj2 = input("Type an adjective: ")
      adj3 = input("Type an adjective: ")
      noun3 = input("Type a noun: ")
      adverb = input("Type an adverb: ")
      pnoun2 = input("Type a plural noun: ")
      adj4 = input("Type an adjective: ")
      adj5 = input("Type an adjective: ")
      pbody = input("Type a part of the body ending in 's': ")
      pnoun3 = input("Type a plural noun: ")
      pbody2 = input("Type a part of the body ending in 's': ")
      pbody3 = input("Type a part of the body ending in 's': ")
      pnoun4 = input("Type a plural noun: ")
      noun4 = input("Type a noun: ")
      pbody4 = input("Type a part of the body ending in 's': ")
      print("Loading story...")
      time.sleep(5)
      print(
        "Our dining " + noun + " used to be a war " + noun2 +
        ". I thought the battles about correct table " + pnoun +
        " would never end. It was us kids versus Mom, and it seemed like a fight that would last to the "
        + adj + " end. But tonight Dad finally declared a/an " + adj2 +
        " truce, and we negotiated a/an " + adj3 + " peace " + noun3 +
        ". Mom promised to no longer get " + adverb +
        " upset and shoot us dirty " + pnoun2 + " and make " + adj4 +
        " remarks when we do " + adj5 +
        " things she doesn't like. We in turn aggreed to:\n\t" + str(1) +
        ") Use naplins to wipe our " + pbody + " and not our " + pnoun3 +
        ".\n\t" + str(2) + ") Keep our " + pbody2 + " off the table.\n\t" +
        str(3) + ") Not use our " + pbody3 + " to pick up " + pnoun4 +
        " from our plates--except for sandwiches or pieces of " + noun4 +
        ".\n\t" + str(4) + ") Never talk with food in our " + pbody4 + ".")
  if option == "Custom":
    emote = input("Type an emotion: ")
    verb = input("Type a verb: ")
    pnoun = input("Type a plural noun: ")
    verbing = input("Type a verb ending in 'ing': ")
    pnoun2 = input("Type a plural noun: ")
    adverb = input("Type an adverb: ")
    verbed = input("Type a verb ending in 'ed': ")
    noun = input("Type a noun: ")
    verb2 = input("Type a verb: ")
    num = int(input("Type a number: "))
    size = input("Type a size: ")
    print("Loading story...")
    time.sleep(5)
    print("Paul was " + emote + " that he got to " + verb + " with his " +
          pnoun + ". He also excels in " + verbing + " electronic " + pnoun2 +
          ". Mr. Sousa believes Paul will have a(n) " + adverb +
          " future. Paul also said he " + verbed + " his " + noun +
          " that includes the Nintendo " + verb2 + " and the Nintendo " +
          str(num) + "DS" + size + ".")
    print("Creating image theme...")
    print(climage.convert('istockphoto-175440771-612x612.jpg',
                          is_unicode=True))
  if option == "Random":
    rng = random.randint(1, 2)
    if rng == 1:
      print("Random: A Conerning Development")
      verb = input("Type a verb: ")
      noun = input("Type a noun: ")
      noun2 = input("Type a noun: ")
      pnoun = input("Type a plural noun: ")
      pnoun2 = input("Type a plural noun: ")
      verbing = input("Type a verb ending in 'ing': ")
      verb2 = input("Type a verb: ")
      verb3 = input("Type a verb: ")
      noun3 = input("Type a noun: ")
      verb4 = input("Type a verb")
      pnoun3 = input("Type a plural noun ")
      noun4 = input("Type a noun: ")
      noun5 = input("Type a noun: ")
      noun6 = input("Type a noun: ")
      print("Loading story...")
      time.sleep(5)
      print("It was a concerning development that he couldn't " + verb +
            " out of his " + noun + ". He'd had many " + noun2 +
            " throughout his early " + pnoun + " and had fond " + pnoun2 +
            " of " + verbing + " with them, but he couldn't " + verb2 +
            " how it had all " + verb3 + ". There was some " + noun3 +
            " as he grew up that he " + verb4 + " with each of his " + pnoun3 +
            " for the very last " + noun4 + ", and he had no " + noun5 +
            " that it would be the " + noun6 + ".")
      print("Creating image theme...")
      time.sleep(15)
      print(climage.convert('worried-guy-1488909269.jpg', is_unicode=True))
    if rng == 2:
      print("Random: Planning Ahead")

      print(
        "I've rented a car in Las Vegas and have reserved a hotel in Twentynine Palms which is just north of Joshua Tree. We'll drive from Las Vegas through Mojave National Preserve and possibly do a short hike on our way down. Then spend all day on Monday at Joshua Tree. We can decide the next morning if we want to do more in Joshua Tree or Mojave before we head back."
      )
  if option == "G":
    #Secret #1
    print(
      "This letter is special because it was the most used letter during development"
    )
  if option == "Pokemon":
    print(
      "I wanna be the very best Like no one ever was To catch them is my real test To train them is my cause I will travel across the land Searching far and wide Teach Pokémon to understand The power that’s inside [Chorus] (Pokémon, gotta catch ’em all) It’s you and me I know it’s my destiny (Pokémon) Oh, you’re my best friend In a world we must defend (Pokémon, gotta catch ’em all) A heart so true Our courage will pull us through You teach me and I’ll teach you Pokémon! (Gotta catch ’em all) Gotta catch ’em all (Pokémon!)"
    )
    print(climage.convert('victini-hed-1242653.png', is_unicode=True))
    #Secret 2
  option = input(
    "Enter what type of story you want (Madlibs, Custom, Random). Type STOP to exit "
  )
