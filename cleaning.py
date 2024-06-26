import pandas as pd

df = pd.read_csv("Python\\Game Sales\\vgsales.csv")
df = pd.DataFrame(df)

year_dict = {
  "Madden NFL 2004": 2003,
  "FIFA Soccer 2004": 2003,
  "LEGO Batman: The Videogame": 2008,
  "wwe Smackdown vs. Raw 2006": 2005,
  "Space Invaders": 1978,
  "Rock Band": 2007,
  "Frogger's Adventures: Temple of the Frog": 2001,
  "LEGO Indiana Jones: The Original Adventures": 2008,
  "Call of Duty 3": 2006,
  "Call of Duty: Black Ops": 2010,
  "Triple Play 99": 1998,
  "LEGO Harry Potter: Years 5-7": 2011,
  "Adventure": 1980,
  "Combat": 1977,
  "NASCAR Thunder 2003": 2002,
  "Hitman 2: Silent Assassin": 2002,
  "Rock Band": 2007,
  "Legacy of Kain: Soul Reaver": 1999,
  "Donkey Kong Land III": 1997,
  "LEGO Harry Potter: Years 5-7": 2011,
  "Air-Sea Battle": 1977,
  "Suikoden III": 2002,
  "Yakuza 4": 2010,
  "LEGO Harry Potter: Years 5-7": 2011,
  "Wheel of Fortune": 1975,
  "Namco Museum": 1995,
  "Rhythm Heaven": 2006,
  "The Lord of the Rings: War in the North": 2011,
  "Madden NFL 07": 2006,
  "MLB SlugFest 20-03": 2002,
  "Shaun White Snowboarding": 2008,
  "PES 2009: Pro Evolution Soccer": 2008,
  "Madden NFL 11": 2010,
  "WarioWare: Twisted!": 2004,
  "LEGO Harry Potter: Years 5-7": 2011,
  "Test Drive Unlimited 2": 2011,
  "The Chronicles of Narnia: The Lion, The Witch and The Wardrobe": 2005,
  "Test Drive Unlimited 2": 2011,
  "Monster Hunter 2": 2006,
  "Advance Wars: Days of Ruin": 2008,
  "Metal Gear Solid 2: Substance": 2002,
  "The Golden Compass": 2007,
  "Madden NFL 06": 2005,
  "NASCAR: Dirt to Daytona": 2002,
  "Madden NFL 2002": 2001,
  "Def Jam: Fight for NY": 2004,
  "NBA Street Vol. 2": 2003,
  "Fishing Derby": 1980,
  "Wet": 2009,
  "Sonic the Hedgehog": 1991,
  "Karate": 1982,
  "Tiger Woods PGA Tour 07": 2006,
  "Circus Atari": 1980,
  "The Chronicles of Riddick: Escape from Butcher Bay": 2004,
  "Maze Craze: A Game of Cops 'n Robbers": 1980,
  "Silent Hill: Homecoming": 2008,
  "Super Breakout": 1978,
  "Robert Ludlum's The Bourne Conspiracy": 2008,
  "NHL Slapshot": 2010,
  "TERA": 2011,
  "LEGO Harry Potter: Years 5-7": 2011,
  "NFL GameDay 2003": 2002,
  "Silent Hill: Homecoming": 2008,
  "Harvest Moon: Save the Homeland": 2001,
  "Robert Ludlum's The Bourne Conspiracy": 2008,
  "Hangman": 1978,
  "The Golden Compass": 2007,
  "NBA Live 2003": 2002,
  "Bejeweled 3": 2010,
  "Cubix Robots for Everyone: Clash 'n' Bash": 2001,
  "Tropico 4": 2011,
  "Tomb Raider (2013)": 2013,
  "Dragon Ball Z: Budokai Tenkaichi 2 (JP sales)": 2006,
  "Custom Robo": 2004,
  "Final Fantasy XI": 2002,
  "Singularity": 2010,
  "Dragster": 1980,
  "All-Star Baseball 2005": 2004,
  "Star Wars Jedi Knight II: Jedi Outcast": 2002,
  "Slot Machine": 1975,
  "Shrek the Third": 2007,
  "The Dukes of Hazzard II: Daisy Dukes It Out": 2000,
  "Disgaea 3: Absence of Detention": 2011,
  "NBA Live 2003": 2002,
  "Harvest Moon: The Tale of Two Towns": 2010,
  "Nicktoons: Battle for Volcano Island": 2006,
  "Haven: Call of the King": 2002,
  "Unreal Championship 2: The Liandri Conflict": 2005,
  "The Chronicles of Narnia: The Lion, The Witch and The Wardrobe": 2005,
  "Pac-Man Fever": 2002,
  "The Legend of Zelda: The Minish Cap(weekly JP sales)": 2004,
  "Indy 500": 1977,
  "Gun": 2005,
  "Flag Capture": 1978,
  "LEGO Harry Potter: Years 5-7": 2011,
  "Rock Revolution": 2008,
  "Jonah Lomu Rugby Challenge": 1997,
  "College Hoops 2K6": 2005,
  "Mega Man X Collection": 2006,
  "BioShock 2": 2010,
  "Singularity": 2010,
  "Danganronpa: Trigger Happy Havoc": 2010,
  "DanceDanceRevolution II": 2011,
  "Tony Hawk's Downhill Jam": 2006,
  "Big Beach Sports 2": 2008,
  "Jet X20": 2002,
  "Tribes: Aerial Assault": 2002,
  "Move Fitness": 2011,
  "LEGO Harry Potter: Years 5-7": 2011,
  "Yu Yu Hakusho: Dark Tournament": 2004,
  "Ghostbusters II": 2009,
  "Breakaway IV": 1981,
  "Robotech: Battlecry": 2002,
  "Valkyria Chronicles III: Unrecorded Chronicles": 2011,
  "WRC: FIA World Rally Championship": 2010,
  "Famista 64": 1999,
  "Dead Space 3": 2013,
  "Test Drive Unlimited 2": 2011,
  "Pet Zombies": 2011,
  "Star Trek: Legacy": 2006,
  "Trauma Team": 2010,
  "Backbreaker": 2010,
  "Twisted Metal: Small Brawl": 2001,
  "Otomedius Excellent": 2011,
  "NBA Starting Five": 2002,
  "Teen Titans": 2005,
  "Backbreaker": 2010,
  "James Cameron's Dark Angel": 2002,
  "Sword of the Samurai": 1989,
  "Splatterhouse": 2010,
  "Alone in the Dark: The New Nightmare": 2001,
  "Vegas Party": 2010,
  "Jurassic Park: The Game": 2011,
  "Home Run": 1978,
  "eJay Clubworld": 2001,
  "All-Star Baseball 2005": 2004,
  "Our House Party!": 2009,
  "WCW Backstage Assault": 2000,
  "Bejeweled 3": 2010,
  "Disney's Cinderella: Magical Dreams": 2005,
  "Transworld Surf": 2001,
  "Street Fighter IV": 2008,
  "Nintendo Puzzle Collection": 2003,
  "Charm Girls Club: My Fashion Mall": 2009,
  "WRC: FIA World Rally Championship": 2010,
  "Record of Agarest War Zero": 2011,
  "Super Robot Wars OG Saga: Masou Kishin II - Revelation of Evil God": 2011,
  "Saru! Get You! Million Monkeys": 2006,
  "Street Hoops": 2002,
  "Godzilla: Destroy All Monsters Melee": 2002,
  "The Daring Game for Girls": 2009,
  "Rocksmith": 2011,
  "Major League Baseball 2K6": 2006,
  "Happy Feet Two": 2011,
  "Star Trek: Conquest": 2007,
  "GiFTPiA": 2003,
  "Disney's Chicken Little: Ace In Action": 2006,
  "Happy Feet Two": 2011,
  "Atsumare! Power Pro Kun no DS Koushien": 2010,
  "My Healthy Cooking Coach": 2009,
  "Happy Feet Two": 2011,
  "Luminous Arc 2 (JP sales)": 2008,
  "The Daring Game for Girls": 2009,
  "Egg Monster Hero": 2005,
  "Samurai Shodown Anthology": 2009,
  "Demon Chaos": 2005,
  "Action Man-Operation Extreme": 2000,
  "Super Puzzle Fighter II": 1996,
  "Happy Feet Two": 2011,
  "Charm Girls Club: My Fashion Show": 2010,
  "Get Fit with Mel B": 2010,
  "Face Racers: Photo Finish": 2011,
  "Zero: Tsukihami no Kamen": 2008,
  "The Hidden": 1989,
  "Rock Revolution": 2008,
  "Dead Island: Riptide": 2013,
  "Mega Man Battle Network: Operation Shooting Star": 2009,
  "Smashing Drive": 2002,
  "Dream Trigger 3D": 2011,
  "Tornado": 1983,
  "McFarlane's Evil Prophecy": 2004,
  "Drake of the 99 Dragons": 2003,
  "Port Royale 3": 2012,
  "Build-A-Bear Workshop: Friendship Valley": 2010,
  "Alex Rider: Stormbreaker": 2006,
  "Yoostar on MTV": 2009,
  "Rayman Arena": 2001,
  "National Geographic Challenge!": 2011,
  "Port Royale 3": 2012,
  "Jewel Link Chronicles: Mountains of Madness": 2011,
  "Chou Soujuu Mecha MG": 2006,
  "Prinny: Can I Really Be The Hero? (US sales)": 2009,
  "Combat Elite: WWII Paratroopers": 2005,
  "Captain America: Super Soldier": 2011,
  "Flip's Twisted World": 2010,
  "Mobile Ops: The One Year War": 2007,
  "Tom Clancy's Rainbow Six: Critical Hour": 2006,
  "GRID": 2008,
  "Captain America: Super Soldier": 2011,
  "Reader Rabbit 2nd Grade": 1998,
  "Mountain Bike Adrenaline": 2007,
  "Tour de France 2011": 2011,
  "Drill Dozer": 2005,
  "Battle vs. Chess": 2011,
  "The History Channel: Great Battles - Medieval": 2009,
  "Monster Hunter Frontier Online": 2007,
  "RollerCoaster Tycoon": 1999,
  "GRID": 2008,
  "B.L.U.E.: Legend of Water": 1998,
  "Luxor: Pharaoh's Challenge": 2007,
  "NHL Hitz Pro": 2002,
  "Sega Rally 2006": 2006,
  "World of Tanks": 2010,
  "Swords": 2000,
  "Half-Minute Hero 2": 2011,
  "Clockwork Empires": 2016,
  "Housekeeping": 2017,
  "Major League Baseball 2K8": 2008,
  "Sabre Wulf": 2004,
  "Beyond the Labyrinth": 2011,
  "Bikkuriman Daijiten": 1999,
  "Majesty 2: The Fantasy Kingdom Sim": 2009,
  "Fullmetal Alchemist: Brotherhood": 2010,
  "Combat Elite: WWII Paratroopers": 2005,
  "Samurai Spirits: Tenkaichi Kenkakuden": 2005,
  "Battle vs. Chess": 2011,
  "Tom and Jerry in War of the Whiskers": 2002,
  "Super Duper Sumos": 2003,
  "Legacy of Ys: Books I & II": 2009,
  "The King of Fighters: Maximum Impact - Maniax": 2004,
  "Combat Wings: The Great Battles of WWII": 2006,
  "Tube Slider": 2003,
  "Umineko no Naku Koro ni San: Shinjitsu to Gensou no Yasoukyoku": 2011,
  "Wii de Asobu: Metroid Prime": 2009,
  "Payout Poker & Casino": 2006,
  "Saint": 2006,
  "Steal Princess": 2009,
  "Mario Tennis": 2000,
  "Runaway: A Twist of Fate": 2009,
  "Yu-Gi-Oh! 5D's Wheelie Breakers (JP sales)": 2009,
  "Cabela's Alaskan Adventure": 2006,
  "Writing and Speaking Beautiful Japanese DS": 2007,
  "Virtua Quest": 2004,
  "Shonen Jump's Yu-Gi-Oh! GX Card Almanac": 2007,
  "Without Warning": 2005,
  "Football Manager 2007": 2006,
  "Ferrari: The Race Experience": 2010,
  "PDC World Championship Darts 2008": 2008,
  "Dinotopia: The Sunstone Odyssey": 2003,
  "Dance! It's Your Stage": 2010,
  "Jet Impulse": 2006,
  "Dream Dancer": 2011,
  "WRC: FIA World Rally Championship": 2010,
  "Aquaman: Battle for Atlantis": 2003,
  "Homeworld Remastered Collection": 2015,
  "Shorts": 2009,
  "AKB1/48: Idol to Guam de Koishitara...": 2011,
  "Brothers in Arms: Furious 4": 2011,
  "Agarest Senki: Re-appearance": 2010,
  "Freaky Flyers": 2003,
  "Inversion": 2012,
  "Hakuouki: Shinsengumi Kitan": 2008,
  "The Smurfs": 2011
}

pub_dict = {
  "wwe Smackdown vs. Raw 2006": "Yuke's",
  "Triple Play 99": "EA Games",
  "Shrek / Shrek 2 2-in-1 Gameboy Advance Video": "Vivendi Universal Games",
  "Bentley's Hackpack": "WayForward Technologies",
  "Nicktoons Collection: Game Boy Advance Video Volume 1": "Majesco",
  "SpongeBob SquarePants: Game Boy Advance Video Volume 1": "Majesco",
  "SpongeBob SquarePants: Game Boy Advance Video Volume 2": "Majesco",
  "Sonic the Hedgehog": "Sega",
  "The Fairly Odd Parents: Game Boy Advance Video Volume 1": "Majesco",
  "The Fairly Odd Parents: Game Boy Advance Video Volume 2": "Majesco",
  "Dragon Ball Z: Budokai Tenkaichi 2 (JP sales)": "Spike",
  "Cartoon Network Collection: Game Boy Advance Video Platinum Edition": "Majesco",
  "The Legend of Zelda: The Minish Cap(weekly JP sales)": "Capcom",
  "Sonic X: Game Boy Advance Video Volume 1": "Majesco",
  "Dora the Explorer: Game Boy Advance Video Volume 1": "Majesco",
  "Cartoon Network Collection: Game Boy Advance Video Volume 1": "Majesco",
  "All Grown Up!: Game Boy Advance Video Volume 1": "Majesco",
  "Nicktoons Collection: Game Boy Advance Video Volume 2": "Majesco",
  "Yu Yu Hakusho: Dark Tournament": "Tose",
  "SpongeBob SquarePants: Game Boy Advance Video Volume 3": "Majesco",
  "Thomas the Tank Engine & Friends": "THQ",
  "Dragon Ball GT: Game Boy Advance Video Volume 1": "Majesco",
  "Codename: Kids Next Door: Game Boy Advance Video Volume 1": "Majesco",
  "Teenage Mutant Ninja Turtles: Game Boy Advance Video Volume 1": "Majesco",
  "Stronghold 3": "Firefly Studios",
  "Cartoon Network Collection: Game Boy Advance Video Special Edition": "Majesco",
  "Pokémon: Johto Photo Finish: Game Boy Advance Video": "Nintendo",
  "Strawberry Shortcake: Game Boy Advance Video Volume 1": "Majesco",
  "Farming Simulator 2011": "Giants Software",
  "Super Robot Wars OG Saga: Masou Kishin II - Revelation of Evil God": "Banpresto",
  "Disney Channel Collection Vol. 1": "Artificial Mind & Movement",
  "Atsumare! Power Pro Kun no DS Koushien": "Konami",
  "Action Man-Operation Extreme": "Natsume",
  "Cartoon Network Collection: Game Boy Advance Video Volume 2": "Majesco",
  "Chou Soujuu Mecha MG": "Takara Tomy",
  "Prinny: Can I Really Be The Hero? (US sales)": "NIS America",
  "Monster Hunter Frontier Online": "Capcom",
  "B.L.U.E.: Legend of Water": "Glodia",
  "World of Tanks": "Wargaming",
  "Housekeeping": "Spearhead Games",
  "Bikkuriman Daijiten": "Konami",
  "Silverlicious": "GameMill Entertainment",
  "UK Truck Simulator": "SCS Software",
  "Umineko no Naku Koro ni San: Shinjitsu to Gensou no Yasoukyoku": "07th Expansion",
  "Xia-Xia": "Black Lantern Studios",
  "Mario Tennis": "Nintendo",
  "Nicktoons Collection: Game Boy Advance Video Volume 3": "Viacom New Media",
  "Demolition Company: Gold Edition": "GIANTS Software",
  "Moshi, Kono Sekai ni Kami-sama ga Iru to suru Naraba.": "5pb.",
  "Dream Dancer": "5pb.",
  "Homeworld Remastered Collection": "Gearbox Software",
  "AKB1/48: Idol to Guam de Koishitara...": "Bandai Namco Entertainment",
  "Super Robot Monkey Team: Game Boy Advance Video Volume 1": "Viacom New Media",
  "Brothers in Arms: Furious 4": "Gearbox Software",
  "Dance with Devils": "Rejet",
  "Legends of Oz: Dorothy's Return": "Summertime Entertainment",
  "Driving Simulator 2011": "Excalibur Publishing",
  "Bound By Flame": "Spiders"
}

def cleaning():
    # Cleaning Publishers
    for pub in list(pub_dict.keys()):
        df.loc[df['Name'] == pub, 'Publisher'] = pub_dict[pub]

    df.loc[df['Publisher'] == "Valve Entertainment", 'Publisher'] = "Valve"
    df.loc[df['Publisher'] == "EA Games", 'Publisher'] = "Electronic Arts"

    # Cleaning Years
    for game in list(year_dict.keys()):
        df.loc[df['Name'] == game, 'Year'] = str(year_dict[game])
    
    df['Year'] = df['Year'].astype(int)
    df['Year'] = df['Year'].astype(str)

    df.to_csv("Python\\Game Sales\\vgsales_clean.csv")

cleaning()

