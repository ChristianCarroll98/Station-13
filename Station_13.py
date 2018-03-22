class Area:
	def __init__(self, name, visited, desc=None, exits=None, items=None, aliases=None):
		super().__init__()
		self.name = name
		self.visited = visited
		self.desc = desc or ""
		self.exits = exits or []
		self.items = items or []
		self.aliases = aliases or []

class Exit:
	def __init__(self, name, connection, conditions, open, dir_, desc=None, counterpart=None, aliases=None):
		super().__init__()
		self.name = name
		self.connection = connection
		self.conditions = conditions
		self.open = open
		self.dir = dir_
		self.desc = desc or ""
		self.counterpart = counterpart
		self.aliases = aliases or []

class Item:
	def __init__(self, name, seen, container=None, desc=None, items=None, aliases=None):
		super().__init__()
		self.name = name
		self.seen = seen
		self.container = container
		self.desc = desc or ""
		self.items = items or []
		self.aliases = aliases or []

# Game objects & connections

#rooms
hangar1_w = Area("Hangar #1 West", True, "the west section of hangar bay #1")
hangar1_w.aliases.append("hangar")
hangar1_w.aliases.append("Hangar")

hangar1_e = Area("Hangar #1 East", False, "the east section of hangar bay #1")
hangar1_e.aliases.append("hangar")
hangar1_e.aliases.append("Hangar")

maintenance_s = Area("South Maintenance", False, "the southern maintenance room")
maintenance_s.aliases.append("maintenance")
maintenance_s.aliases.append("south maintenance")
maintenance_s.aliases.append("Maintenance")

med_bay = Area("Med Bay", False, "the med bay")
med_bay.aliases.append("maintenance")
med_bay.aliases.append("south maintenance")
med_bay.aliases.append("Maintenance")

rest_dressing_room_ms = Area("Men's restroom and dressing room", False, "The southern restroom.\nA sign on the door reads:\"No Girls Allowed!\".")
rest_dressing_room_ms.aliases.append("Men's Restroom")
rest_dressing_room_ms.aliases.append("men's restroom")
rest_dressing_room_ms.aliases.append("mens restroom")

living_quarters_ms = Area("Men's living quarters", False, "Beds line the walls. The male staff of this station lived here.")
living_quarters_ms.aliases.append("Men's Living Quarters")
living_quarters_ms.aliases.append("men's living quarters")
living_quarters_ms.aliases.append("mens living quarters")

mechanical_utility_storage = Area("Mechanical and Electrical Utility Storage", False, "Mechanical and electrical equipment is stored here.")
mechanical_utility_storage.aliases.append("utility storage")
mechanical_utility_storage.aliases.append("mechanical and electrical utility storage")
mechanical_utility_storage.aliases.append("mechanical storage")
mechanical_utility_storage.aliases.append("Utility Storage")
mechanical_utility_storage.aliases.append("Mechanical Storage")

mess_hall = Area("Mess Hall", False, "Before the crew dissappeared, here is where they ate their meals.")
mess_hall.aliases.append("mess hall")

freezer = Area("the freezer", False, "A place to put food so it doesn't rot. Strangely, it's still quite cold in here.")
freezer.aliases.append("freezer")

lab_3 = Area("Lab #3", False, "The third lab of Station #13.\nThis lab is completely overgrown with plants. Somehow they have thrived these last two years.")
lab_3.aliases.append("Lab 3")
lab_3.aliases.append("lab 3")

lab_1 = Area("Lab #1", False, "The first lab of Station #13.\nThis lab contains a lot of space research equipment.")
lab_1.aliases.append("Lab 1")
lab_1.aliases.append("lab 1")

observatory_research = Area("Observatory (Research Area)", False, "The research side of the Observatory.")
observatory_research.aliases.append("observatory")
observatory_research.aliases.append("Observatory")
observatory_research.aliases.append("observatory research")
observatory_research.aliases.append("observatory research area")
observatory_research.aliases.append("observatory (research area)")
observatory_research.aliases.append("Observatory research area")
observatory_research.aliases.append("Observatory (research area)")

observatory_lounge = Area("Observatory (Lounge Area)", False, "The lounge side of the Observatory. Pool tables, couches, and ooh, snacks!")
observatory_lounge.aliases.append("observatory")
observatory_lounge.aliases.append("Observatory")
observatory_lounge.aliases.append("observatory lounge")
observatory_lounge.aliases.append("observatory lounge area")
observatory_lounge.aliases.append("observatory (lounge area)")
observatory_lounge.aliases.append("Observatory lounge area")
observatory_lounge.aliases.append("Observatory (lounge area)")

control_room = Area("Control Room", False, "Central control. You can turn on Life Support from here!")
control_room.aliases.append("control room")

main_hall = Area("Main Hall", False, "The main hallway. Connects the north and south side of the station.")
main_hall.aliases.append("main hall")

access_room = Area("Access room", False, "This room seems simply to connect to various other important rooms.")
access_room.aliases.append("access room")

elevator_room = Area("Elevator Room", False, "You can access the station's mine from here!")
elevator_room.aliases.append("elevator room")

mine = Area("Mine", False, "The station's asteroid mine. It smells of decay.")
mine.aliases.append("mine")

generator_room = Area("Generator Room", False, "You can turn on the power from here!")
generator_room.aliases.append("generator room")

general_storage = Area("General Ore/Equpiment Storage", False, "A lot of various equipment is stored here, along with crates of ore from the mine.")
general_storage.aliases.append("general ore storage")
general_storage.aliases.append("equipment storage")
general_storage.aliases.append("storage")

lab_4 = Area("Lab #4", False, "The fourth lab of Station #13.\nThis lab was used to extract and research ore obtained from the mine.")
lab_4.aliases.append("Lab 4")
lab_4.aliases.append("lab 4")

lab_2 = Area("Lab #2", False, "The second lab of Station #13\nThe smell of decay. There are strange decomposed bodies of all shapes lying on the floor.\nThere are large broken glass tubes. What were they doing here?\nSome kind of strange genetic experiments?")
lab_2.aliases.append("Lab 2")
lab_2.aliases.append("lab 2")

living_quarters_ln = Area("Ladies' living quarters", False, "Beds line the walls. The female staff of this station lived here.")
living_quarters_ln.aliases.append("Ladies' Living Quarters")
living_quarters_ln.aliases.append("ladies' living quarters")
living_quarters_ln.aliases.append("ladies living quarters")

rest_dressing_room_ln = Area("Ladies' restroom and dressing room", False, "The northern restroom.\nA sign on the door reads:\"No Boys Allowed!\".")
rest_dressing_room_ln.aliases.append("Ladies' Restroom")
rest_dressing_room_ln.aliases.append("ladies' restroom")
rest_dressing_room_ln.aliases.append("ladies restroom")

meeting_room = Area("Meeting Room", False, "This was a general purpose meeting room for the staff.")
meeting_room.aliases.append("meeting room")

maintenance_n = Area("North Maintenance", False, "the northern maintenance area")
maintenance_n.aliases.append("north maintenance")

hangar2_w = Area("Hangar #2 West", False, "the west section of hangar bay #2")
hangar2_w.aliases.append("hangar")
hangar2_w.aliases.append("Hangar")

hangar2_e = Area("Hangar #2 East", False, "the east section of hangar bay #2")
hangar2_e.aliases.append("hangar")
hangar2_e.aliases.append("Hangar")

#exits
hangar1_w_north = Exit("door(Hangar #1 W. N.)", maintenance_s, ["power"], True, "north", "a door to South Maintenance")
hangar1_w_north.aliases.append("n")
hangar1_w_north.aliases.append("North")
hangar1_w_north.aliases.append("Hangar #1 W. N.")
hangar1_w_north.aliases.append("north door")
hangar1_w_east = Exit("door(Hangar #1 W. E.)", hangar1_e, ["power"], True, "east", "a door to Hangar #1 East")
hangar1_w_east.aliases.append("e")
hangar1_w_east.aliases.append("East")
hangar1_w_east.aliases.append("Hangar #1 W. E.")
hangar1_w_east.aliases.append("east door")
#done

hangar1_e_north = Exit("door(Hangar #1 E. N.)", med_bay, ["power"], True, "north", "a door to the Med Bay")
hangar1_e_north.aliases.append("n")
hangar1_e_north.aliases.append("North")
hangar1_e_north.aliases.append("Hangar #1 E. N.")
hangar1_e_north.aliases.append("north door")
hangar1_e_west = Exit("door(Hangar #1 E. W.)", hangar1_w, ["power"], True, "west", "a door to Hangar #1 West")
hangar1_e_west.aliases.append("w")
hangar1_e_west.aliases.append("West")
hangar1_e_west.aliases.append("Hangar #1 E. W.")
hangar1_e_west.aliases.append("west door")
#done

maintenance_s_northwest = Exit("door(Maintenance S. NW.)", lab_1, ["power", "Access Card"], False, "northwest", "a door to Lab #1")
maintenance_s_northwest.aliases.append("nw")
maintenance_s_northwest.aliases.append("Northwest")
maintenance_s_northwest.aliases.append("Maintenance S. NW.")
maintenance_s_northwest.aliases.append("northwest door")
maintenance_s_northeast = Exit("door(Maintenance S. NE.)", lab_3, ["power", "Access Card", "Life Support System"], False, "northeast", "a door to Lab #3")
maintenance_s_northeast.aliases.append("ne")
maintenance_s_northeast.aliases.append("Northeast")
maintenance_s_northeast.aliases.append("Maintenance S. NE.")
maintenance_s_northeast.aliases.append("northeast door")
maintenance_s_west = Exit("door(Maintenance S. W.)", observatory_research, ["power", "Life Support System"], False, "west", "a door to the Observatory (Research Area)")
maintenance_s_west.aliases.append("w")
maintenance_s_west.aliases.append("West")
maintenance_s_west.aliases.append("Maintenance S. W.")
maintenance_s_west.aliases.append("west door")
maintenance_s_east = Exit("door(Maintenance S. E.)", med_bay, ["broken"], False, "east", "a door to the Med Bay")
maintenance_s_east.aliases.append("e")
maintenance_s_east.aliases.append("East")
maintenance_s_east.aliases.append("Maintenance S. E.")
maintenance_s_east.aliases.append("east door")
maintenance_s_south = Exit("door(Maintenance S. S.)", hangar1_w, ["power"], True, "south", "a door to Hangar #1 West")
maintenance_s_south.aliases.append("s")
maintenance_s_south.aliases.append("South")
maintenance_s_south.aliases.append("Maintenance S. S.")
maintenance_s_south.aliases.append("south door")
#done

med_bay_north = Exit("door(Med Bay N.)", mess_hall, ["power"], False, "north", "a door to the Mess Hall")
med_bay_north.aliases.append("n")
med_bay_north.aliases.append("North")
med_bay_north.aliases.append("Med Bay N.")
med_bay_north.aliases.append("north door")
med_bay_west = Exit("door(Med Bay W.)", maintenance_s, ["broken"], False, "west", "a door to South Maintenance")
med_bay_west.aliases.append("w")
med_bay_west.aliases.append("West")
med_bay_west.aliases.append("Med Bay W.")
med_bay_west.aliases.append("west door")
med_bay_east = Exit("door(Med Bay E.)", rest_dressing_room_ms, ["power"], True, "east", "a door to the Men's restroom and dressing room")
med_bay_east.aliases.append("e")
med_bay_east.aliases.append("East")
med_bay_east.aliases.append("Med Bay E.")
med_bay_east.aliases.append("east door")
med_bay_south = Exit("door(Med Bay S.)", hangar1_e, ["power"], True, "south", "a door to Hangar #1 East")
med_bay_south.aliases.append("s")
med_bay_south.aliases.append("South")
med_bay_south.aliases.append("Med Bay S.")
med_bay_south.aliases.append("south door")
#done

rest_dressing_room_ms_west = Exit("door(Dressing Room S. W.)", med_bay, ["power"], True, "west", "a door to the Med Bay")
rest_dressing_room_ms_west.aliases.append("w")
rest_dressing_room_ms_west.aliases.append("West")
rest_dressing_room_ms_west.aliases.append("Dressing Room S. W.")
rest_dressing_room_ms_west.aliases.append("west door")
rest_dressing_room_ms_east = Exit("door(Dressing Room S. E.)", living_quarters_ms, ["power"], True, "east", "a door to Men's living quarters")
rest_dressing_room_ms_east.aliases.append("e")
rest_dressing_room_ms_east.aliases.append("East")
rest_dressing_room_ms_east.aliases.append("Dressing Room S. E.")
rest_dressing_room_ms_east.aliases.append("east door")
#done

living_quarters_ms_north = Exit("door(Men's LQ. N.)", mechanical_utility_storage, ["power"], True, "north", "a door to Mechanical and Electrical Utility Storage")
living_quarters_ms_north.aliases.append("n")
living_quarters_ms_north.aliases.append("North")
living_quarters_ms_north.aliases.append("Men's LQ. N.")
living_quarters_ms_north.aliases.append("north door")
living_quarters_ms_west = Exit("door(Men's LQ. W.)", rest_dressing_room_ms, ["power"], True, "west", "a door to the Men's restroom and dressing room")
living_quarters_ms_west.aliases.append("w")
living_quarters_ms_west.aliases.append("West")
living_quarters_ms_west.aliases.append("Men's LQ. W.")
living_quarters_ms_west.aliases.append("west door")
#done

mechanical_utility_storage_northwest = Exit("door(M&E Storage NW.)", access_room, ["power"], True, "northwest", "a door to the Access Room")
mechanical_utility_storage_northwest.aliases.append("nw")
mechanical_utility_storage_northwest.aliases.append("Northwest")
mechanical_utility_storage_northwest.aliases.append("M&E Storage NW.")
mechanical_utility_storage_northwest.aliases.append("northwest door")
mechanical_utility_storage_northeast = Exit("door(M&E Storage NE.)", elevator_room, ["power"], False, "northeast", "a door to the elevator room")
mechanical_utility_storage_northeast.aliases.append("ne")
mechanical_utility_storage_northeast.aliases.append("Northeast")
mechanical_utility_storage_northeast.aliases.append("M&E Storage NE.")
mechanical_utility_storage_northeast.aliases.append("northeast door")
mechanical_utility_storage_west = Exit("door(M&E Storage W.)", mess_hall, ["power"], False, "west", "a door to the mess hall")
mechanical_utility_storage_west.aliases.append("w")
mechanical_utility_storage_west.aliases.append("West")
mechanical_utility_storage_west.aliases.append("M&E Storage W.")
mechanical_utility_storage_west.aliases.append("west door")
mechanical_utility_storage_south = Exit("door(M&E Storage S.)", living_quarters_ms, ["power"], True, "south", "a door to Men's living quarters")
mechanical_utility_storage_south.aliases.append("s")
mechanical_utility_storage_south.aliases.append("South")
mechanical_utility_storage_south.aliases.append("M&E Storage S.")
mechanical_utility_storage_south.aliases.append("south door")
#done

mess_hall_north = Exit("door(Mess Hall N.)", main_hall, ["power"], False, "north", "a door to the main hall")
mess_hall_north.aliases.append("n")
mess_hall_north.aliases.append("North")
mess_hall_north.aliases.append("Mess Hall N.")
mess_hall_north.aliases.append("north door")
mess_hall_west = Exit("door(Mess Hall W.)", lab_3, ["power", "Access Card", "Life Support System"], False, "west", "a door to Lab #3")
mess_hall_west.aliases.append("w")
mess_hall_west.aliases.append("West")
mess_hall_west.aliases.append("Mess Hall W.")
mess_hall_west.aliases.append("west door")
mess_hall_east = Exit("door(Mess Hall E.)", mechanical_utility_storage, ["power"], False, "east", "a door to Mechanical and Electrical Utility Storage")
mess_hall_east.aliases.append("e")
mess_hall_east.aliases.append("East")
mess_hall_east.aliases.append("Mess Hall E.")
mess_hall_east.aliases.append("east door")
mess_hall_southwest = Exit("door(Mess Hall SW.)", med_bay, ["power"], False, "southwest", "a door to the Med Bay")
mess_hall_southwest.aliases.append("sw")
mess_hall_southwest.aliases.append("Southwest")
mess_hall_southwest.aliases.append("Mess Hall SW.")
mess_hall_southwest.aliases.append("southwest door")
mess_hall_southeast = Exit("door(Mess Hall SE.)", freezer, ["power", "Access Card"], False, "southeast", "a door to the freezer")
mess_hall_southeast.aliases.append("se")
mess_hall_southeast.aliases.append("Southeast")
mess_hall_southeast.aliases.append("Mess Hall SE.")
mess_hall_southeast.aliases.append("southeast door")
#done

freezer_north = Exit("door(Freezer N.)", mess_hall, ["power", "Access Card"], False, "north", "a door to the mess hall")
freezer_north.aliases.append("n")
freezer_north.aliases.append("North")
freezer_north.aliases.append("Freezer N.")
freezer_north.aliases.append("north door")
#done

lab_3_north = Exit("door(Lab #3 N.)", main_hall, ["power", "Access Card", "Life Support System"], False, "north", "a door to the main hall")
lab_3_north.aliases.append("n")
lab_3_north.aliases.append("North")
lab_3_north.aliases.append("Lab #3 N.")
lab_3_north.aliases.append("north door")
lab_3_west = Exit("door(Lab #3 W.)", lab_1, ["power", "Access Card", "Life Support System"], False, "west", "a door to Lab #1")
lab_3_west.aliases.append("w")
lab_3_west.aliases.append("West")
lab_3_west.aliases.append("Lab #3 W.")
lab_3_west.aliases.append("west door")
lab_3_east = Exit("door(Lab #3 E.)", mess_hall, ["power", "Access Card", "Life Support System"], False, "east", "a door to ")
lab_3_east.aliases.append("e")
lab_3_east.aliases.append("East")
lab_3_east.aliases.append("Lab #3 E.")
lab_3_east.aliases.append("east door")
lab_3_south = Exit("door(Lab #3 S.)", maintenance_s, ["power", "Access Card", "Life Support System"], False, "south", "a door to South Maintenance")
lab_3_south.aliases.append("s")
lab_3_south.aliases.append("South")
lab_3_south.aliases.append("Lab #3 S.")
lab_3_south.aliases.append("south door")
#done

lab_1_north = Exit("door(Lab #1 N.)", control_room, ["power", "Access Card"], False, "north", "a door to the control room")
lab_1_north.aliases.append("n")
lab_1_north.aliases.append("North")
lab_1_north.aliases.append("Lab #1 N.")
lab_1_north.aliases.append("north door")
lab_1_west = Exit("door(Lab #1 W.)", observatory_research, ["broken"], False, "west", "a door to the Observatory (Research Area)")
lab_1_west.aliases.append("w")
lab_1_west.aliases.append("West")
lab_1_west.aliases.append("Lab #1 W.")
lab_1_west.aliases.append("west door")
lab_1_east = Exit("door(Lab #1 E.)", lab_3, ["power", "Access Card", "Life Support System"], False, "east", "a door to Lab #3")
lab_1_east.aliases.append("e")
lab_1_east.aliases.append("East")
lab_1_east.aliases.append("Lab #1 E.")
lab_1_east.aliases.append("east door")
lab_1_south = Exit("door(Lab #1 S.)", maintenance_s, ["power", "Access Card"], False, "south", "a door to South Maintenance")
lab_1_south.aliases.append("s")
lab_1_south.aliases.append("South")
lab_1_south.aliases.append("Lab #1 S.")
lab_1_south.aliases.append("south door")
#done

observatory_research_north = Exit("door(Observatory R. N.)", observatory_lounge, ["power", "Life Support System"], False, "north", "a door to the Observatory (Lounge Area)")
observatory_research_north.aliases.append("n")
observatory_research_north.aliases.append("North")
observatory_research_north.aliases.append("Observatory R. N.")
observatory_research_north.aliases.append("north door")
observatory_research_east = Exit("door(Observatory R. E.)", lab_3, ["broken"], False, "east", "a door to Lab #3")
observatory_research_east.aliases.append("e")
observatory_research_east.aliases.append("East")
observatory_research_east.aliases.append("Observatory R. E.")
observatory_research_east.aliases.append("east door")
observatory_research_southeast = Exit("door(Observatory R. SE.)", maintenance_s, ["power", "Life Support System"], False, "southeast", "a door to South Maintenance")
observatory_research_southeast.aliases.append("se")
observatory_research_southeast.aliases.append("Southeast")
observatory_research_southeast.aliases.append("Observatory R. SE.")
observatory_research_southeast.aliases.append("south door")
#done

observatory_lounge_northeast = Exit("door(Observatory L. NE.)", maintenance_n, ["broken"], False, "northeast", "a door to North Maintenance")
observatory_lounge_northeast.aliases.append("ne")
observatory_lounge_northeast.aliases.append("Northeast")
observatory_lounge_northeast.aliases.append("Observatory L. NE.")
observatory_lounge_northeast.aliases.append("northeast door")
observatory_lounge_east = Exit("door(Observatory L. E.)", lab_2, ["power", "Access Card", "Life Support System", "Research Access Card"], False, "east", "a door to Lab #2")
observatory_lounge_east.aliases.append("e")
observatory_lounge_east.aliases.append("East")
observatory_lounge_east.aliases.append("Observatory L. E.")
observatory_lounge_east.aliases.append("east door")
observatory_lounge_south = Exit("door(Observatory L. S.)", observatory_research, ["power", "Life Support System"], False, "south", "a door to the Observatory (Research Area)")
observatory_lounge_south.aliases.append("s")
observatory_lounge_south.aliases.append("South")
observatory_lounge_south.aliases.append("Observatory L. S.")
observatory_lounge_south.aliases.append("south door")
#done

control_room_north = Exit("door(Control RM. N.)", lab_2, ["broken"], False, "north", "a door to Lab #2")
control_room_north.aliases.append("n")
control_room_north.aliases.append("North")
control_room_north.aliases.append("Control RM. N.")
control_room_north.aliases.append("north door")
control_room_east = Exit("door(Control RM. E.)", main_hall, ["power", "Access Card"], False, "east", "a door to the main hall")
control_room_east.aliases.append("e")
control_room_east.aliases.append("East")
control_room_east.aliases.append("Control RM. E.")
control_room_east.aliases.append("east door")
control_room_south = Exit("door(Control RM. S.)", lab_1, ["power", "Access Card"], False, "south", "a door to Lab #1")
control_room_south.aliases.append("s")
control_room_south.aliases.append("South")
control_room_south.aliases.append("Control RM. S.")
control_room_south.aliases.append("south door")
#done

main_hall_northwest = Exit("door(Main Hall NW.)", lab_4, ["broken"], False, "northwest", "a door to lab #4")
main_hall_northwest.aliases.append("nw")
main_hall_northwest.aliases.append("Northwest")
main_hall_northwest.aliases.append("Main Hall NW.")
main_hall_northwest.aliases.append("northwest door")
main_hall_northeast = Exit("door(Main Hall NE.)", general_storage, ["power"], True, "northeast", "a door to General Ore/Equpiment Storage")
main_hall_northeast.aliases.append("ne")
main_hall_northeast.aliases.append("Northeast")
main_hall_northeast.aliases.append("Main Hall NE.")
main_hall_northeast.aliases.append("northeast door")
main_hall_west = Exit("door(Main Hall W.)", control_room, ["power", "Access Card"], False, "west", "a door to the control room")
main_hall_west.aliases.append("w")
main_hall_west.aliases.append("West")
main_hall_west.aliases.append("Main Hall W.")
main_hall_west.aliases.append("west door")
main_hall_east = Exit("door(Main Hall E.)", access_room, ["pipe"], False, "east", "a door to the access room")
main_hall_east.aliases.append("e")
main_hall_east.aliases.append("East")
main_hall_east.aliases.append("Main Hall E.")
main_hall_east.aliases.append("east door")
main_hall_southwest = Exit("door(Main Hall SW.)", lab_3, ["power", "Access Card, Life Support System"], False, "southwest", "a door to Lab #3")
main_hall_southwest.aliases.append("sw")
main_hall_southwest.aliases.append("Southwest")
main_hall_southwest.aliases.append("Main Hall SW.")
main_hall_southwest.aliases.append("southwest door")
main_hall_southeast = Exit("door(Main Hall SE.)", mess_hall, ["power"], False, "southeast", "a door to the mess hall")
main_hall_southeast.aliases.append("se")
main_hall_southeast.aliases.append("Southeast")
main_hall_southeast.aliases.append("Main Hall SE.")
main_hall_southeast.aliases.append("southeast door")
#done

access_room_north = Exit("door(Access RM. N.)", generator_room, ["broken"], False, "north", "a door to the generator room")
access_room_north.aliases.append("n")
access_room_north.aliases.append("North")
access_room_north.aliases.append("Access RM. N.")
access_room_north.aliases.append("north door")
access_room_west = Exit("door(Access RM. W.)", main_hall, ["pipe"], False, "west", "A door to the main hall. The lock is broken..")
access_room_west.aliases.append("w")
access_room_west.aliases.append("West")
access_room_west.aliases.append("Access RM. W.")
access_room_west.aliases.append("west door")
access_room_east = Exit("door(Access RM. E.)", elevator_room, ["power"], False, "east", "a door to the elevator room")
access_room_east.aliases.append("e")
access_room_east.aliases.append("East")
access_room_east.aliases.append("Access RM. E.")
access_room_east.aliases.append("east door")
access_room_south = Exit("door(Access RM. S.)", mechanical_utility_storage, ["power"], True, "south", "a door to Mechanical and Electrical Utility Storage")
access_room_south.aliases.append("s")
access_room_south.aliases.append("South")
access_room_south.aliases.append("Access RM. S.")
access_room_south.aliases.append("south door")
#done

elevator_room_north = Exit("door(Elevator RM. N.)", generator_room, ["power"], False, "north", "a door to the generator room")
elevator_room_north.aliases.append("n")
elevator_room_north.aliases.append("North")
elevator_room_north.aliases.append("Elevator RM. N.")
elevator_room_north.aliases.append("north door")
elevator_room_west = Exit("door(Elevator RM. W.)", access_room, ["power"], False, "west", "a door to the access room")
elevator_room_west.aliases.append("w")
elevator_room_west.aliases.append("West")
elevator_room_west.aliases.append("Elevator RM. W.")
elevator_room_west.aliases.append("west door")
elevator_room_east = Exit("Elevator", mine, ["power", "Access Card", "Life Support System"], False, "east", "an elevator into the mine")
elevator_room_east.aliases.append("e")
elevator_room_east.aliases.append("East")
elevator_room_east.aliases.append("elevator")
elevator_room_south = Exit("door(Elevator RM. S.)", mechanical_utility_storage, ["power"], False, "south", "a door to Mechanical and Electrical Utility Storage")
elevator_room_south.aliases.append("s")
elevator_room_south.aliases.append("South")
elevator_room_south.aliases.append("Elevator RM. S.")
elevator_room_south.aliases.append("south door")
#done

mine_west = Exit("Elevator", elevator_room, ["power", "Access Card", "Life Support System"], False, "west", "an elevator back to the elevator room")
mine_west.aliases.append("w")
mine_west.aliases.append("West")
mine_west.aliases.append("elevator")
#done

generator_room_north = Exit("door(Generator RM. N.)", living_quarters_ln, ["power"], False, "north", "a door to the Ladies' living quarters")
generator_room_north.aliases.append("n")
generator_room_north.aliases.append("North")
generator_room_north.aliases.append("Generator RM. N.")
generator_room_north.aliases.append("north door")
generator_room_west = Exit("door(Generator RM. W.)", general_storage, ["power"], True, "west", "a door to General Ore/Equipment Storage")
generator_room_west.aliases.append("w")
generator_room_west.aliases.append("West")
generator_room_west.aliases.append("Generator RM. W.")
generator_room_west.aliases.append("west door")
generator_room_southwest = Exit("door(Generator RM. SW.)", access_room, ["broken"], False, "southwest", "a door to the access room")
generator_room_southwest.aliases.append("sw")
generator_room_southwest.aliases.append("Southwest")
generator_room_southwest.aliases.append("Generator RM. SW.")
generator_room_southwest.aliases.append("southwest door")
generator_room_southeast = Exit("door(Generator RM. SE.)", elevator_room, ["power"], False, "southeast", "a door to the elevator room")
generator_room_southeast.aliases.append("se")
generator_room_southeast.aliases.append("Southeast")
generator_room_southeast.aliases.append("Generator RM. SE.")
generator_room_southeast.aliases.append("southeast door")
#done

general_storage_north = Exit("door(General S. N.)", meeting_room, ["power"], True, "north", "a door to the meeting room")
general_storage_north.aliases.append("n")
general_storage_north.aliases.append("North")
general_storage_north.aliases.append("General S. N.")
general_storage_north.aliases.append("north door")
general_storage_west = Exit("door(General S. W.)", lab_4, ["broken"], False, "west", "a door to Lab #4")
general_storage_west.aliases.append("w")
general_storage_west.aliases.append("West")
general_storage_west.aliases.append("General S. W.")
general_storage_west.aliases.append("west door")
general_storage_east = Exit("door(General S. E.)", generator_room, ["power"], True, "east", "a door to the generator room")
general_storage_east.aliases.append("e")
general_storage_east.aliases.append("East")
general_storage_east.aliases.append("General S. E.")
general_storage_east.aliases.append("east door")
general_storage_south = Exit("door(General S. S.)", main_hall, ["power"], True, "south", "a door to the main hall")
general_storage_south.aliases.append("s")
general_storage_south.aliases.append("South")
general_storage_south.aliases.append("General S. S.")
general_storage_south.aliases.append("south door")
#done

lab_4_north = Exit("door(Lab #4 N.)", maintenance_n, ["power", "Access Card", "Life Support System"], False, "north", "a door to North Maintenance")
lab_4_north.aliases.append("n")
lab_4_north.aliases.append("North")
lab_4_north.aliases.append("Lab #4 N.")
lab_4_north.aliases.append("north door")
lab_4_west = Exit("door(Lab #4 W.)", lab_2, ["power", "Access Card", "Life Support System", "Research Access Card"], False, "west", "a door to Lab #2")
lab_4_west.aliases.append("w")
lab_4_west.aliases.append("West")
lab_4_west.aliases.append("Lab #4 W.")
lab_4_west.aliases.append("west door")
lab_4_east = Exit("door(Lab #4 E.)", general_storage, ["broken"], False, "east", "a door to General Ore/Equipment Storage")
lab_4_east.aliases.append("e")
lab_4_east.aliases.append("East")
lab_4_east.aliases.append("Lab #4 E.")
lab_4_east.aliases.append("east door")
lab_4_south = Exit("door(Lab #4 S.)", main_hall, ["broken"], False, "south", "a door to the main hall")
lab_4_south.aliases.append("s")
lab_4_south.aliases.append("South")
lab_4_south.aliases.append("Lab #4 S.")
lab_4_south.aliases.append("south door")
#done

lab_2_north = Exit("door(Lab #2 N.)", maintenance_n, ["broken"], False, "north", "a door to North Maintenance")
lab_2_north.aliases.append("n")
lab_2_north.aliases.append("North")
lab_2_north.aliases.append("Lab #2 N.")
lab_2_north.aliases.append("north door")
lab_2_west = Exit("door(Lab #2 W.)", observatory_lounge, ["power", "Access Card", "Life Support System", "Research Access Card"], False, "west", "a door to the Observatory (Lounge Area)")
lab_2_west.aliases.append("w")
lab_2_west.aliases.append("West")
lab_2_west.aliases.append("Lab #2 W.")
lab_2_west.aliases.append("west door")
lab_2_east = Exit("door(Lab #2 E.)", lab_4, ["power", "Access Card", "Life Support System", "Research Access Card"], False, "east", "a door to Lab #4")
lab_2_east.aliases.append("e")
lab_2_east.aliases.append("East")
lab_2_east.aliases.append("Lab #2 E.")
lab_2_east.aliases.append("east door")
lab_2_south = Exit("door(Lab #2 S.)", control_room, ["broken"], False, "south", "a door to the control room")
lab_2_south.aliases.append("s")
lab_2_south.aliases.append("South")
lab_2_south.aliases.append("Lab #2 S.")
lab_2_south.aliases.append("south door")
#done

living_quarters_ln_west = Exit("door(Ladies' Living Quarters W.)", rest_dressing_room_ln, ["broken"], True, "west", "a door to the Ladies' restroom and dressing room")
living_quarters_ln_west.aliases.append("w")
living_quarters_ln_west.aliases.append("West")
living_quarters_ln_west.aliases.append("Ladies' Living Quarters W.")
living_quarters_ln_west.aliases.append("west door")
living_quarters_ln_south = Exit("door(Ladies' Living Quarters S.)", generator_room, ["power"], False, "south", "a door to the generator room")
living_quarters_ln_south.aliases.append("s")
living_quarters_ln_south.aliases.append("South")
living_quarters_ln_south.aliases.append("Ladies' Living Quarters S.")
living_quarters_ln_south.aliases.append("south door")
#done

rest_dressing_room_ln_west = Exit("door(Ladies RR. W.)", meeting_room, ["broken"], False, "west", "a door to the meeting room")
rest_dressing_room_ln_west.aliases.append("w")
rest_dressing_room_ln_west.aliases.append("West")
rest_dressing_room_ln_west.aliases.append("Ladies RR. W.")
rest_dressing_room_ln_west.aliases.append("west door")
rest_dressing_room_ln_east = Exit("door(Ladies RR. E.)", living_quarters_ln, ["broken"], True, "east", "a door to the Ladies' living quarters")
rest_dressing_room_ln_east.aliases.append("e")
rest_dressing_room_ln_east.aliases.append("East")
rest_dressing_room_ln_east.aliases.append("Ladies RR. E.")
rest_dressing_room_ln_east.aliases.append("east door")
#done

meeting_room_north = Exit("door(Meeting RM. N.)", hangar2_e, ["power"], True, "north", "a door to Hangar #2 East")
meeting_room_north.aliases.append("n")
meeting_room_north.aliases.append("North")
meeting_room_north.aliases.append("Meeting RM. N.")
meeting_room_north.aliases.append("north door")
meeting_room_west = Exit("door(Meeting RM. W.)", maintenance_n, ["broken"], False, "west", "a door to North Maintenance")
meeting_room_west.aliases.append("w")
meeting_room_west.aliases.append("West")
meeting_room_west.aliases.append("Meeting RM. W.")
meeting_room_west.aliases.append("west door")
meeting_room_east = Exit("door(Meeting RM. E.)", rest_dressing_room_ln, ["broken"], False, "east", "a door to the Ladies' restroom and dressing room")
meeting_room_east.aliases.append("e")
meeting_room_east.aliases.append("East")
meeting_room_east.aliases.append("Meeting RM. E.")
meeting_room_east.aliases.append("east door")
meeting_room_south = Exit("door(Meeting RM. S.)", general_storage, ["power"], True, "south", "a door to General Ore/Equipment Storage")
meeting_room_south.aliases.append("s")
meeting_room_south.aliases.append("South")
meeting_room_south.aliases.append("Meeting RM. S.")
meeting_room_south.aliases.append("south door")
#done

maintenance_n_north = Exit("door(Maintenance N. N.)", hangar2_w, ["power"], True, "north", "a door to Hangar #2 West")
maintenance_n_north.aliases.append("n")
maintenance_n_north.aliases.append("North")
maintenance_n_north.aliases.append("Maintenance N. N.")
maintenance_n_north.aliases.append("north door")
maintenance_n_west = Exit("door(Maintenance N. W.)", observatory_lounge, ["broken"], False, "west", "a door to the Observatory (Lounge Area)")
maintenance_n_west.aliases.append("w")
maintenance_n_west.aliases.append("West")
maintenance_n_west.aliases.append("Maintenance N. W.")
maintenance_n_west.aliases.append("west door")
maintenance_n_east = Exit("door(Maintenance N. E.)", meeting_room, ["broken"], False, "east", "a door to the meeting room")
maintenance_n_east.aliases.append("e")
maintenance_n_east.aliases.append("East")
maintenance_n_east.aliases.append("Maintenance N. E.")
maintenance_n_east.aliases.append("east door")
maintenance_n_southwest = Exit("door(Maintenance N. SW.)", lab_2, ["broken"], False, "southwest", "a door to Lab #2")
maintenance_n_southwest.aliases.append("sw")
maintenance_n_southwest.aliases.append("Southwest")
maintenance_n_southwest.aliases.append("Maintenance N. SW.")
maintenance_n_southwest.aliases.append("southwest door")
maintenance_n_southeast = Exit("door(Maintenance N. SE.)", lab_4, ["power", "Access Card", "Life Support System"], False, "southeast", "a door to Lab #4")
maintenance_n_southeast.aliases.append("se")
maintenance_n_southeast.aliases.append("Southeast")
maintenance_n_southeast.aliases.append("Maintenance N. SE.")
maintenance_n_southeast.aliases.append("southeast door")
#done

hangar2_w_east = Exit("door(Hangar #2 W. E.)", hangar2_e, ["broken"], False, "east", "a door to Hangar #2 East")
hangar2_w_east.aliases.append("e")
hangar2_w_east.aliases.append("East")
hangar2_w_east.aliases.append("Hangar #2 W. E.")
hangar2_w_east.aliases.append("east door")
hangar2_w_south = Exit("door(Hangar #2 W. S.)", maintenance_n, ["power"], True, "south", "a door to North Maintenance")
hangar2_w_south.aliases.append("s")
hangar2_w_south.aliases.append("South")
hangar2_w_south.aliases.append("Hangar #2 W. S.")
hangar2_w_south.aliases.append("south door")
#done

hangar2_e_west = Exit("door(Hangar #2 E. W.)", hangar2_w, ["broken"], False, "west", "a door to Hangar #2 West. You can see a ship through the window!!!")
hangar2_e_west.aliases.append("w")
hangar2_e_west.aliases.append("West")
hangar2_e_west.aliases.append("Hangar #2 E. W.")
hangar2_e_west.aliases.append("west door")
hangar2_e_south = Exit("door(Hangar #2 E. S.)", meeting_room, ["power"], True, "south", "a door to the meeting room")
hangar2_e_south.aliases.append("s")
hangar2_e_south.aliases.append("South")
hangar2_e_south.aliases.append("Hangar #2 E. S.")
hangar2_e_south.aliases.append("south door")
#done

#attach doors to their opposite side
hangar1_w_east.counterpart = hangar1_e_west
hangar1_e_west.counterpart = hangar1_w_east

hangar1_w_north.counterpart = maintenance_s_south
maintenance_s_south.counterpart = hangar1_w_north

med_bay_south.counterpart = hangar1_e_north
hangar1_e_north.counterpart = med_bay_south

observatory_research_southeast.counterpart = maintenance_s_west
maintenance_s_west.counterpart = observatory_research_southeast

med_bay_west.counterpart = maintenance_s_east
maintenance_s_east.counterpart = med_bay_west

med_bay_east.counterpart = rest_dressing_room_ms_west
rest_dressing_room_ms_west.counterpart = med_bay_east

rest_dressing_room_ms_east.counterpart = living_quarters_ms_west
living_quarters_ms_west.counterpart = rest_dressing_room_ms_east

lab_1_south.counterpart = maintenance_s_northwest
maintenance_s_northwest.counterpart = lab_1_south

lab_3_south.counterpart = maintenance_s_northeast
maintenance_s_northeast.counterpart = lab_3_south

mess_hall_southwest.counterpart = med_bay_north
med_bay_north.counterpart = mess_hall_southwest

mechanical_utility_storage_south.counterpart = living_quarters_ms_north
living_quarters_ms_north.counterpart = mechanical_utility_storage_south

observatory_research_east.counterpart = lab_1_west
lab_1_west.counterpart = observatory_research_east

lab_1_east.counterpart = lab_3_west
lab_3_west.counterpart = lab_1_east

lab_3_east.counterpart = mess_hall_west
mess_hall_west.counterpart = lab_3_east

mess_hall_southeast.counterpart = freezer_north
freezer_north.counterpart = mess_hall_southeast

mess_hall_east.counterpart = mechanical_utility_storage_west
mechanical_utility_storage_west.counterpart = mess_hall_east

control_room_south.counterpart = lab_1_north
lab_1_north.counterpart = control_room_south

main_hall_southwest.counterpart = lab_3_north
lab_3_north.counterpart = main_hall_southwest

main_hall_southeast.counterpart = mess_hall_north
mess_hall_north.counterpart = main_hall_southeast

access_room_south.counterpart = mechanical_utility_storage_northwest
mechanical_utility_storage_northwest.counterpart = access_room_south

elevator_room_south.counterpart = mechanical_utility_storage_northeast
mechanical_utility_storage_northeast.counterpart = elevator_room_south

observatory_lounge_south.counterpart = observatory_research_north
observatory_research_north.counterpart = observatory_lounge_south

control_room_east.counterpart = main_hall_west
main_hall_west.counterpart = control_room_east

main_hall_east.counterpart = access_room_west
access_room_west.counterpart = main_hall_east

access_room_east.counterpart = elevator_room_west
elevator_room_west.counterpart = access_room_east

elevator_room_east.counterpart = mine_west
mine_west.counterpart = elevator_room_east

lab_2_south.counterpart = control_room_north
control_room_north.counterpart = lab_2_south

lab_4_south.counterpart = main_hall_northwest
main_hall_northwest.counterpart = lab_4_south

general_storage_south.counterpart = main_hall_northeast
main_hall_northeast.counterpart = general_storage_south

generator_room_southwest.counterpart = access_room_north
access_room_north.counterpart = generator_room_southwest

generator_room_southeast.counterpart = elevator_room_north
elevator_room_north.counterpart = generator_room_southeast

observatory_lounge_east.counterpart = lab_2_west
lab_2_west.counterpart = observatory_lounge_east

lab_2_east.counterpart = lab_4_west
lab_4_west.counterpart = lab_2_east

lab_4_east.counterpart = general_storage_west
general_storage_west.counterpart = lab_4_east

general_storage_east.counterpart = generator_room_west
generator_room_west.counterpart = general_storage_east

maintenance_n_southwest.counterpart = lab_2_north
lab_2_north.counterpart = maintenance_n_southwest

maintenance_n_southeast.counterpart = lab_4_north
lab_4_north.counterpart = maintenance_n_southeast

meeting_room_south.counterpart = general_storage_north
general_storage_north.counterpart = meeting_room_south

living_quarters_ln_south.counterpart = generator_room_north
generator_room_north.counterpart = living_quarters_ln_south

maintenance_n_west.counterpart = observatory_lounge_northeast
observatory_lounge_northeast.counterpart = maintenance_n_west

maintenance_n_east.counterpart = meeting_room_west
meeting_room_west.counterpart = maintenance_n_east

meeting_room_east.counterpart = rest_dressing_room_ln_west
rest_dressing_room_ln_west.counterpart = meeting_room_east

rest_dressing_room_ln_east.counterpart = living_quarters_ln_west
living_quarters_ln_west.counterpart = rest_dressing_room_ln_east

hangar2_e_south.counterpart = maintenance_n_north
maintenance_n_north.counterpart = hangar2_e_south

hangar2_w_south.counterpart = meeting_room_north
meeting_room_north.counterpart = hangar2_w_south

hangar2_w_east.counterpart = hangar2_e_west
hangar2_e_west.counterpart = hangar2_w_east

#append exits
hangar1_w.exits.append(hangar1_w_north)
hangar1_w.exits.append(hangar1_w_east)

hangar1_e.exits.append(hangar1_e_north)
hangar1_e.exits.append(hangar1_e_west)

maintenance_s.exits.append(maintenance_s_northwest)
maintenance_s.exits.append(maintenance_s_northeast)
maintenance_s.exits.append(maintenance_s_west)
maintenance_s.exits.append(maintenance_s_east)
maintenance_s.exits.append(maintenance_s_south)

med_bay.exits.append(med_bay_north)
med_bay.exits.append(med_bay_west)
med_bay.exits.append(med_bay_east)
med_bay.exits.append(med_bay_south)

rest_dressing_room_ms.exits.append(rest_dressing_room_ms_west)
rest_dressing_room_ms.exits.append(rest_dressing_room_ms_east)

living_quarters_ms.exits.append(living_quarters_ms_north)
living_quarters_ms.exits.append(living_quarters_ms_west)

mechanical_utility_storage.exits.append(mechanical_utility_storage_northwest)
mechanical_utility_storage.exits.append(mechanical_utility_storage_northeast)
mechanical_utility_storage.exits.append(mechanical_utility_storage_west)
mechanical_utility_storage.exits.append(mechanical_utility_storage_south)

mess_hall.exits.append(mess_hall_north)
mess_hall.exits.append(mess_hall_west)
mess_hall.exits.append(mess_hall_east)
mess_hall.exits.append(mess_hall_southwest)
mess_hall.exits.append(mess_hall_southeast)

freezer.exits.append(freezer_north)

lab_3.exits.append(lab_3_north)
lab_3.exits.append(lab_3_west)
lab_3.exits.append(lab_3_east)
lab_3.exits.append(lab_3_south)

lab_1.exits.append(lab_1_north)
lab_1.exits.append(lab_1_west)
lab_1.exits.append(lab_1_east)
lab_1.exits.append(lab_1_south)

observatory_research.exits.append(observatory_research_north)
observatory_research.exits.append(observatory_research_east)
observatory_research.exits.append(observatory_research_southeast)

observatory_lounge.exits.append(observatory_lounge_northeast)
observatory_lounge.exits.append(observatory_lounge_east)
observatory_lounge.exits.append(observatory_lounge_south)

control_room.exits.append(control_room_north)
control_room.exits.append(control_room_east)
control_room.exits.append(control_room_south)

main_hall.exits.append(main_hall_northwest)
main_hall.exits.append(main_hall_northeast)
main_hall.exits.append(main_hall_west)
main_hall.exits.append(main_hall_east)
main_hall.exits.append(main_hall_southwest)
main_hall.exits.append(main_hall_southeast)

access_room.exits.append(access_room_north)
access_room.exits.append(access_room_west)
access_room.exits.append(access_room_east)
access_room.exits.append(access_room_south)

elevator_room.exits.append(elevator_room_north)
elevator_room.exits.append(elevator_room_west)
elevator_room.exits.append(elevator_room_east)
elevator_room.exits.append(elevator_room_south)

mine.exits.append(mine_west)

generator_room.exits.append(generator_room_north)
generator_room.exits.append(generator_room_west)
generator_room.exits.append(generator_room_southwest)
generator_room.exits.append(generator_room_southeast)

general_storage.exits.append(general_storage_north)
general_storage.exits.append(general_storage_west)
general_storage.exits.append(general_storage_east)
general_storage.exits.append(general_storage_south)

lab_4.exits.append(lab_4_north)
lab_4.exits.append(lab_4_west)
lab_4.exits.append(lab_4_east)
lab_4.exits.append(lab_4_south)

lab_2.exits.append(lab_2_north)
lab_2.exits.append(lab_2_west)
lab_2.exits.append(lab_2_east)
lab_2.exits.append(lab_2_south)

living_quarters_ln.exits.append(living_quarters_ln_west)
living_quarters_ln.exits.append(living_quarters_ln_south)

rest_dressing_room_ln.exits.append(rest_dressing_room_ln_west)
rest_dressing_room_ln.exits.append(rest_dressing_room_ln_east)

meeting_room.exits.append(meeting_room_north)
meeting_room.exits.append(meeting_room_west)
meeting_room.exits.append(meeting_room_east)
meeting_room.exits.append(meeting_room_south)

maintenance_n.exits.append(maintenance_n_north)
maintenance_n.exits.append(maintenance_n_west)
maintenance_n.exits.append(maintenance_n_east)
maintenance_n.exits.append(maintenance_n_southwest)
maintenance_n.exits.append(maintenance_n_southeast)

hangar2_w.exits.append(hangar2_w_east)
hangar2_w.exits.append(hangar2_w_south)

hangar2_e.exits.append(hangar2_e_west)
hangar2_e.exits.append(hangar2_e_south)

#items
useless_junk = Item("pile of useless junk", True, hangar1_w, "useless bits of your ship and the station from the crash")
useless_junk.aliases.append("pile")
useless_junk.aliases.append("junk pile")
useless_junk.aliases.append("junk")
useless_junk.aliases.append("useless junk")

medkit = Item("medkit", False, med_bay, "Just what you needed! Dont worry, you can use it through your suit.\njust inject yourself with the biofoam. your suit will seal itself.")

broken_pipe = Item("broken pipe", False, rest_dressing_room_ms, "Somebody should call a plumber.")
broken_pipe.aliases.append("pipe")

repair_kit = Item("repair kit", False, mechanical_utility_storage, "Broke something? No problem! For all your machanical repair needs!")

desk = Item("wooden desk", False, living_quarters_ln, "A wooden desk. There are some drawers. What could be inside...")
desk.aliases.append("desk")

access_card = Item("Access Card (Regular-A)", False, desk, "An Access Card. This will help you get into certain places.")
access_card.aliases.append("Regular Access Card")
access_card.aliases.append("regular access card")
access_card.aliases.append("access card")
access_card.aliases.append("Access Card")
access_card.aliases.append("ac")
access_card.aliases.append("AC")

skeleton = Item("skeleton", False, mine, "Wearing a tattered labcoat, this old scientist must have been down here a very very long time.\nHe may have something you need...")
skeleton.aliases.append("Skeleton")
special_access_card = Item("Access Card (Research-S)", False, skeleton, "A special Scientist Access Card. Senior security level, this will get you anywhere.")
special_access_card.aliases.append("research access card")
special_access_card.aliases.append("Research Access Card")
special_access_card.aliases.append("sac")
special_access_card.aliases.append("SAC")
skeleton.items.append(special_access_card)

oven = Item("oven", False, mess_hall, "An oven. You can use this to cook things.")

steak = Item("large raw steak", False, freezer, "A huge steak. A product from Space-Food 4U, a company that went out of business last year in a huge scandal.\nSomething about people mutating into monstrous cow beasts.. Oh well, it'll do! It needs to be cooked though..")
steak.aliases.append("steak")
steak.aliases.append("meat")

ship = Item("Spaceship", False, hangar2_w, "Your escape route! A miracle!")
ship.aliases.append("ship")
ship.aliases.append("spaceship")

console = Item("console", False, control_room, "you can use this to turn on the Life Support System!")
console.aliases.append("Console")

generator = Item("generator", False, generator_room, "you can use this to turn on the power! It's broken though, which explains the loss of power. Maybe you can repair it?")
generator.aliases.append("Generator")

fuel_tank = Item("fuel tank", False, general_storage, "A fuel tank. It's full of a substance that smells like fuel..")
fuel_tank.aliases.append("fuel")

checklist = Item("traveller's checklist", False, maintenance_n, "A list of everything one might need before undertaking a voyage through space! You'll need to use this to get home.")
checklist.aliases.append("checklist")
checklist.aliases.append("list")

water_tank = Item("water tank", False, hangar2_e, "A large tank of water. You think it could last you all the way to the colony spaceport near your home.")
water_tank.aliases.append("water")

hangar_door_controls = Item("hangar door control switch", False, hangar2_w, "A control switch for the hangar bay doors. Useful if you want to leave the station.")
hangar_door_controls.aliases.append("control switch")
hangar_door_controls.aliases.append("switch")
hangar_door_controls.aliases.append("door control switch")

#append items
desk.items.append(access_card)

living_quarters_ln.items.append(desk)

hangar1_w.items.append(useless_junk)

rest_dressing_room_ms.items.append(broken_pipe)

med_bay.items.append(medkit)

mess_hall.items.append(oven)

freezer.items.append(steak)

mechanical_utility_storage.items.append(repair_kit)

control_room.items.append(console)

generator_room.items.append(generator)

mine.items.append(skeleton)

hangar2_w.items.append(ship)
hangar2_w.items.append(hangar_door_controls)

maintenance_n.items.append(checklist)

general_storage.items.append(fuel_tank)

hangar2_e.items.append(water_tank)

# Game state
current_area = hangar1_w
timeUntilDeath = 21
timeUntilSuffocation = 200
conditionsMet = []
inventory = []
actionable = []
gameOver = False
shipFuled = False
checklistUsed = False
bayDoorsOpen = False
oopsCounter = 0

# Logic
def isAlias(noun):
	for item in actionable:
		for alias in item.aliases:
			if(noun == alias):
				return item.name
	for exit_ in current_area.exits:
		for alias in exit_.aliases:
			if noun == alias:
				return exit_.name
	for alias in current_area.aliases:
		if noun == alias:
			return current_area.name
	return noun

def describe(thing):
	desc = [thing.name, thing.desc]
	if hasattr(thing, "exits") and thing.exits:
		exit_desc = []
		for exit_ in thing.exits:
			if(exit_.open):
				door = "n open"
			else:
				door = " closed"
			text = "a%s %s to the %s" % (door, exit_.name, exit_.dir)
			exit_desc.append(text)
		if len(exit_desc) > 1:
			exit_desc[-1] = "and " + exit_desc[-1]
		text = "You see " + ", ".join(exit_desc) + "."
		desc.append(text)
	if hasattr(thing, "items") and thing.items:
		item_desc = []
		for item in thing.items:
			try:
				actionable.index(item)
			except:
				actionable.append(item)
			text = "a %s" % (item.name,)
			item_desc.append(text)
		if len(item_desc) > 1:
			item_desc[-1] = "and " + item_desc[-1]
		text = "There is " + ", ".join(item_desc) + "."
		desc.append(text)
		for item in thing.items:
			if(item.seen and len(item.items)>0):
				item_desc = []
				for item_ in item.items:
					try:
						actionable.index(item_)
					except:
						actionable.append(item_)
					text = "a %s" % (item_.name,)
					item_desc.append(text)
				if len(item_desc) > 1:
					item_desc[-1] = "and " + item_desc[-1]
				text = "Inside the %s there is " % (item.name,) + ", ".join(item_desc) + "."
				desc.append(text)
	return "\n".join(desc)

def look(noun):
	noun = isAlias(noun)
	if(noun == "commands" or noun == "Commands"):
		return listCommands(noun)
	for item in actionable:
		if noun == item.name:
			container_ = item.container
			while(hasattr(container_, 'container')):
				container_ = container_.container
			if(container_ == inventory or container_ == current_area):
				if not(item.seen):
					item.seen = True
				return describe(item)
	for exit_ in current_area.exits:
		if noun == exit_.name or noun == exit_.dir:
			return describe(exit_)
	if noun in ("", "around", "everything", "area", current_area.name):
		return describe(current_area)
	return "you don't see any " + noun

def openDoor(noun):
	noun = isAlias(noun)
	global current_area
	global bayDoorsOpen
	for exit_ in current_area.exits:
		if (noun == exit_.name or noun == exit_.dir):
			if (exit_.open):
				return "The door is already open!"
			else:
				if((conditionsMet.count("Life Support System") == 1)and(exit_.name=="door(Hangar #1 W. N.)" or exit_.name=="door(Hangar #1 W. E.)" or exit_.name=="door(Maintenance S. S.)" or exit_.name=="door(Hangar #1 E. W.)" )):
					return "This door is sealing a breach. It cannot be opened while Life Support is on."
				elif(bayDoorsOpen and exit_.name=="door(Hangar #2 W. S.)" or exit_.name=="door(Maintenance N. N.)" ):
					return "This door cannot be opened while Life Support is on and the hangar bay doors are open."
				elif(exit_.conditions[0] == "broken"):
					return "This door is broken. It cannot be opened."
				elif(exit_.conditions[0] == "pipe" and inventory.count(broken_pipe) == 1):
					exit_.open=True
					exit_.counterpart.open=True
					return "You manage to pry open the door using the pipe. You can get through now!"
				elif(exit_.conditions[0] == "pipe"):
					return "You try to pull open the door but you can't get enough leverage.\nMaybe you could use something to pry open the door?"
				else:
					if conditions_met(exit_):
						exit_.open=True
						exit_.counterpart.open=True
						return("You open "+noun)
					else:
						result = "To open this door you need:"
						for condition in exit_.conditions:
							result+="\n"+str(condition)
						return result
	return "There is no %s."%noun

def closeDoor(noun):
	noun = isAlias(noun)
	global current_area
	for exit_ in current_area.exits:
		if (noun == exit_.name or noun == exit_.dir):
			if not(exit_.open):
				return "The door is already closed!"
			else:
				if(exit_.conditions[0] == "broken"):
					return "This door is broken. It cannot be closed."
				elif(exit_.conditions[0] == "pipe"):
					return "It's stuck open."
				else:
					if conditions_met(exit_):
						exit_.open=False
						exit_.counterpart.open=False
						return("You close "+noun)
					else:
						result = "To close this door you need:"
						for condition in exit_.conditions:
							result+="\n"+str(condition)
						return result
	return "There is no %s."%noun

def conditions_met(exit):
	for condition in exit.conditions:
		global conditionsMet
		if (conditionsMet.count(condition) == 0):
			return False
	return True

def go(noun):
	noun = isAlias(noun)
	global current_area
	for exit_ in current_area.exits:
		if noun == exit_.name or noun == exit_.dir:
			if(exit_.open):
				current_area = exit_.connection
				#print("current room visited?: "+str(current_area.visited))
				if not(current_area.visited):
					current_area.visited = True
					return describe(current_area)
				else:
					return(current_area.name)
			else:
				return("You have to open the door..")
	return "you can't go that way"

def unrecognized(noun):
	global oopsCounter
	if(oopsCounter<10):
		oopsCounter=oopsCounter+1
		return "You can't do that. (Try typing something else?...)"
	else:
		oopsCounter = 0
		return "You can't do that. (Remember you can see what you can do by typing \"commands\"!)"

def listCommands(noun):
	return "You can:\ngo (somewhere)\nlook/examine (something, or everything)\nuse (something)\npick up (something)\ndrop (something)\nopen doors\nclose doors\nlook at (a direction) to see where the door goes\ncheck (inventory, power or Life Support System(LSS))\nor quit!"

def check(noun):
	if(noun=="inv" or noun=="inventory" or noun=="Inventory"):
		return getInventory(noun)
	elif(noun == "power" or noun == "Power"):
		if (conditionsMet.count("power") == 1):
			return "The power is on!"
		else:
			return "The power is still off."
	elif(noun == "Life Support System" or noun == "LSS" or noun == "lss"):
		if (conditionsMet.count("Life Support System") == 1):
			return "Life Support is on!"
		else:
			return "Life Support is still off."
	else:
		return "You can't check that. Try something else."

def use(noun):
	noun = isAlias(noun)
	global gameOver
	global conditionsMet
	global timeUntilSuffocation
	global shipFuled
	global checklistUsed
	global bayDoorsOpen
	for item in actionable:
		if(noun==item.name):
			container_ = item.container
			while(hasattr(container_, 'container')):
				container_ = container_.container
			if(container_ == inventory or container_ == current_area):
				if(noun==medkit.name):
					actionable.remove(medkit)
					try:
						current_area.items.remove(medkit)
					except:
						inventory.remove(medkit)
					global timeUntilDeath
					timeUntilDeath = -1
					return "You use the medkit. You can feel the biofoam sealing your body and repairing tissues.\nYou are out of immediate danger, but you must still find a way to restore power to the station."
				elif(noun==useless_junk.name):
					return "What would you do with that?? It's useless junk."
				elif(noun==broken_pipe.name):
					if(current_area == access_room):
						conditionsMet.append("Pipe")
						return "You think you can pry open the west door with the pipe."
						openDoor("west")
						conditionsMet.pop[conditionsMet.index("Pipe")]
					else:
						return "You bang the pipe on the floor and walls. Nothing happens."
				elif(noun ==  repair_kit.name):
					if(current_area == generator_room):
						try:
							current_area.items.remove(repair_kit)
						except:
							inventory.remove(repair_kit)
						if(conditionsMet.count("power") == 0):
							conditionsMet.append("power")
						return "You manage to repair the generator with the kit! the intercom starts up agian, finishing its statement:\"...nice stay!\""
					else:
						return("Use it on what? everything looks fine in this room.")
				elif(noun==generator.name):
					return "Maybe you can repair the generator with a repair kit?"
				elif(noun==console.name):
					print("beep boop beep!")
					if(conditionsMet.count("Life Support System") == 1):
						return "Life Support is already on, and you can't see much else you can do here."
					elif((not hangar1_w_north.open) and (not hangar1_w_east.open)):
						timeUntilSuffocation = -1
						if(conditionsMet.count("Life Support System") == 0):
							conditionsMet.append("Life Support System")
						return "The console whirs to life as you punch in the commands for Life Support!\nthe Station fills with oxygen and you remove your helmet for a moment, glad to finally get a breath of fresh(ish) air."
					else:
						return "You hit the \"Engage Life Support\" command, but nothing happens. Words scroll across the console:\n\"ERROR! LOW PRESSURE! POSSIBLE BREACH! SEAL DOORS AROUND BREACHED AREA!\""
				elif(noun==desk.name):
					return "You sit at the desk for a minute before remembering that you have things to do."
				elif(noun==access_card.name or noun==special_access_card.name):
					return "You can open doors that require this card now!"
				elif(noun==skeleton.name):
					return "You use his bones to play the beat of \"Spooky Scary Skeletons\". Just kidding, you won't touch the skeleton.."
				elif(noun == oven.name):
					if(conditionsMet.count("power") == 1):
						if(inventory.count(steak) == 1 and steak.name == "large raw steak"):
							steak.name = "large cooked steak"
							steak.desc = "A huge steak, cooked nicely. A product from Space-Food 4U, a company that went out of business last year in a huge scandal.\nSomething about people mutating into monstrous cow beasts.. Oh well, it'll do!"
							return "You cook the steak in the oven. Tasty!"
						elif(inventory.count(steak) == 1 and steak.name == "large cooked steak"):
							steak.name = "large burnt steak"
							steak.desc = "A huge steak. It's a little burnt.. A product from Space-Food 4U, a company that went out of business last year in a huge scandal.\nSomething about people mutating into monstrous cow beasts.. Oh well, it'll do!"
							return "You cook the steak in the oven. Agian. It's burnt now."
						elif(inventory.count(steak) == 1 and steak.name == "large burnt steak"):
							return "You don't think cooking it agian is a good idea.."
						else:
							return "You turn on the oven, and climb in... Just kidding, you dont have anything to cook."
					else:
						return "The oven needs power to turn on. It's electric."
				elif(noun == steak.name):
					if(steak.name == "large raw steak"):
						return "Maybe you can cook it with an oven?.."
					elif(steak.name == "large cooked steak"):
						return "You take a bite.. A strange feeling comes over you, you start shaking, and begin to scream as the transformation begins- Haha, just kidding. It's pretty tasty."
					elif(steak.name == "large burnt steak"):
						return "You think about taking a bite.. A strong burnt smell assaults your nostrils. On second thought... You should save it for the trip home."
				elif(noun == checklist.name):
					result = ""
					result += "\n+--------------------------+"
					result += "\n|                          |"
					result += "\n|  Traveller's Checklist   |"
					result += "\n|  ---------------------   |"
					result += "\n|                          |"
					result += "\n|  +---+                   |"
					if(shipFuled):
						result += "\n|  | √ | Plenty o' Fuel    |"
					else:
						result += "\n|  |   | Plenty o' Fuel    |"
					result += "\n|  +---+                   |"
					result += "\n|                          |"
					result += "\n|  +---+                   |"
					if(inventory.count(steak) == 1 and steak.name != "large raw steak"):
						result += "\n|  | √ |  Extra Munchies   |"
					else:
						result += "\n|  |   |  Extra Munchies   |"
					result += "\n|  +---+                   |"
					result += "\n|                          |"
					result += "\n|  +---+                   |"
					if(inventory.count(water_tank) == 1):
						result += "\n|  | √ | Quenching Liquid  |"
					else:
						result += "\n|  |   | Quenching Liquid  |"
					result += "\n|  +---+                   |"
					result += "\n|                          |"
					result += "\n+--------------------------+"
					checklistUsed = True
					return result
				elif(noun == water_tank.name):
					return "You take a sip of water. It tastes stale."
				elif(noun == fuel_tank.name):
					if(current_area == hangar2_w):
						if(shipFuled):
							return "The ship is already fuled, and the tank is empty..."
						else:
							shipFuled = True
							fuel_tank.desc = "A fuel tank. It's empty. It still smells like fuel."
							if(inventory.count(checklist)==1):
								return "The ship has fuel! I'ts ready to fly. Be sure to check your list before you leave!"
							else:
								return "The ship has fuel! I'ts ready to fly."
					else:
						return "Use it for what? Nothing needs fuel here."
				elif(noun == hangar_door_controls.name):
					if(conditionsMet.count("power") == 1):
						if not(hangar2_w_south.open):
							if(bayDoorsOpen):
								bayDoorsOpen = False
								return "A voice on the intercom announces that the bay doors are closing."
							else:
								bayDoorsOpen = True
								return "The hangar doors open to reveal the blackness of space."
						else:
							return "The station's mechanical announcement voice informs you that the hangar needs to be sealed before the doors can open."
					else:
						return "The power must be on in order to operate these controls."
				elif(noun == ship.name):
					if(shipFuled):
						if not(bayDoorsOpen):
							return "You'll need to open the bay doors before taking off."
						print("You board the ship. It's an older model, but it'll fly straight enough. You put your coodinates into the ship's console and")
						print("a happy voice speaks from the ships intercom:\"Coordinates accepted. Beginning liftoff sequence!\" As you begin your long journey home,")
						print("you release a long sigh of relief at having finally made it out of Station 13.")
						if(inventory.count(steak) == 1 and inventory.count(water_tank) == 1):
							if(checklistUsed):
								print("\nFollowing the checklist to the letter, you prepared well for the journey. After many weeks, you arrive on your colony's station\nto welcome your beautiful wife and daughter with open arms and the story of a lifetime.")
							else:
								print("\nWith the help of the food and water you brought with you, you survive the journey home. After many weeks, you arrive on your colony's station\nto welcome your beautiful wife and daughter with open arms and the story of a lifetime.")
						elif(inventory.count(water_tank) == 1):
							print("\nHowever... You've forgotten an important part of any voyage. You have no extra food. Try as you might, clawing at the walls, breaking every box,\nThis ship was stripped of supplies so there is nothing useful or edible on board.\nYou slowly grow weaker and weaker, hungrier and hungrier. You cannot survive on water alone for this long.\nYour ship arrives at your colony's spaceport on autopilot. It's only a matter of time before they discover your frail body..\nYou starved to death on the journey home.")
						else:
							print("\nHowever... You've forgotten one of the most essential parts of any voyage. Extra water. You frantically search the ship for a single drop of that life saving liquid,\nwith no luck. After a matter of days your body begins failing, and you wither away inside the ship only a week after your journey began.\nYou died of dehydration.")
					else:
						return "You'll need to fuel up the ship before it can fly."
					gameOver = True
					return "                                                       ~~GAME OVER~~"
			else:
				return "You can't use the "+noun+" right now."
	return "What "+noun+"?"

def pickUp(noun):
	noun = isAlias(noun)
	global conditionsMet
	for item in actionable:
		if noun == item.name:
			container_ = item.container
			while(hasattr(container_, 'container')):
				container_ = container_.container
			if(container_ == current_area):
				if (noun == console.name):
					return("You try to rip the console out of the wall... Nothing happens.")
				elif (noun == generator.name):
					return("You try to lift the generator. You strain so much that you think you might have to change your undersuit. It stays where it is.")
				elif (noun == desk.name):
					return("You attempt to lift the desk, but it has been bolted to the floor.")	
				elif(noun==skeleton.name):
					return "You feel it's better to let the poor guy rest in peace."
				elif(noun==ship.name):
					return "Don't be rediculous."
				elif(noun==hangar_door_controls.name):
					return "The switch won't come off the wall. Wait, why are you trying to do that?"
				elif(noun==oven.name):
					return "You attempt to pick up the oven, but stop when sparks fly in several directions. You hope it still works.."
				else:
					if(noun==access_card.name):
						if(conditionsMet.count("Access Card") == 0):
							conditionsMet.append("Access Card")
					if(noun==special_access_card.name):
						if(conditionsMet.count("Research Access Card") == 0):
							skeleton.desc = "Wearing a tattered labcoat, this old scientist must have been down here a very very long time."
							conditionsMet.append("Research Access Card")
					inventory.append(item)
					try:
						#print(item.name)
						item.container.items.remove(item)
					except:
						print("ERROR: could not remove %s from its container!"%item.name)
					item.container = inventory
					return "you picked up a(n) "+noun
			elif(container_ == inventory):
				return "You already have that!"
	return "There's no "+noun+" here."

def drop(noun):
	noun = isAlias(noun)
	for item in actionable:
		if(noun == item.name):
			container_ = item.container
			while(hasattr(container_, 'container')):
				container_ = container_.container
			if(container_ == inventory):
				if(noun == access_card.name):
					conditionsMet.pop[conditionsMet.index("Access Card")]
				if(noun == special_access_card.name):
					conditionsMet.pop[conditionsMet.index("Research Access Card")]
				current_area.items.append(item)
				try:
					item.container.items.remove(item)
				except:
					inventory.remove(item)
				item.container = current_area
				return "you dropped a(n) "+noun
	return "You dont have a(n) "+noun+"."

def getInventory(noun):
	global inventory
	if(len(inventory)==0):
		return("You are not carrying anything.")
	result = "You have these items:"
	for item in inventory:
		result+="\n"+item.name
	return result

#def hackStuff(noun):
#	global conditionsMet
#	if(noun == "power on" and conditionsMet.count("power") == 0):
#		conditionsMet.append("power")
#		return "Power on! HACKS!"
#	elif(noun == "power on"):
#		return "Power is already on."
#	elif(noun == "power off" and conditionsMet.count("power") == 1):
#		conditionsMet.pop[conditionsMet.index("power")]
#		return "Power off! HACKS!"
#	elif(noun == "power off"):
#		return "Power is already off."
#	elif(noun == "LSS on" and conditionsMet.count("Life Support System") == 0):
#		conditionsMet.append("Life Support System")
#		return "Life Support System on! HACKS!"
#	elif(noun == "LSS on"):
#		return "Life Support System is already on."
#	elif(noun == "LSS off" and conditionsMet.count("Life Support System") == 1):
#		conditionsMet.pop[conditionsMet.index("Life Support System")]
#		return "Life Support System off! HACKS!"
#	elif(noun == "LSS off"):
#		return "Life Support System is already off."
#	elif(noun == "actionable"):
#		for item in actionable:
#			print(item.name)
#		return "/\ACTIONABLE ITEMS/\ "
#	return "Wrong code brah."
	
handlers = {"go":go, "walk":go, "n":go, "s":go, "e":go, "w":go,
			"north":go, "south":go, "east":go, "west":go,
			"North":go, "South":go, "East":go, "West":go,
			"nw":go, "sw":go, "ne":go, "se":go,
			"northwest":go, "southwest":go, "northeast":go, "southeast":go,
			"Northwest":go, "Southwest":go, "Northeast":go, "Southeast":go,
			"look":look, "examine":look,
			"commands":listCommands, "Commands":listCommands, "list":listCommands,
			"inv": getInventory, "inventory": getInventory, "Inventory": getInventory,
			"use":use,
			"Pick":pickUp, "pick":pickUp, "take":pickUp, "grab": pickUp,
			"drop":drop,
			"open":openDoor,
			"close":closeDoor,
			"check":check,
#			"hack":hackStuff
			}

print("         Welcome to Station 13! This is version 1.3, so its nice and polished up. press ENTER to begin!")
input()
import os
os.system('cls')
print("           You are on your way home after your 3 month long deployment to Mine & Research Station 15.")
print("                 Suddenly, you are knocked off your feet, your ship begins to shake violently!")
print("          Sirens echo throughout the spacecraft. Lights flash as you struggle to regain your balance.")
print("    The monitor shows the damage to the right wing. An asteroid impact! Your ship is essentially inoperable.")
print("                 Your Life Support System is down and your suit's oxygen supply is limited.")
print("             If you dont do something, there's little time before you inhale your last breath.")
print("                    The intercom notifies you of a space station 30 kilometers ahead.")
print("                The large station comes into view as you check your remaining equipment.")
print("                                               Station 13.")
print("Attached to the largest asteroid in this sector, it went dark two years ago and no one bothered to investigate.")
print("                           It may be your only hope. You'll have to try to land.")
print("                                             What will you do?\n")

introCounter = 15

command = input("> ")

while not (
command=="land" or
command=="engage landing gear" or
command=="go forward" or
command=="go to station" or
command=="go to Station" or
command=="station" or
command=="Station" or
command=="Land ship" or
command=="land ship" or
command=="Land" or
command=="land the ship" or
command=="land spaceship" or
command=="land the spaceship" or
command=="try to land" or
command=="go to station 13" or
command=="go to Station 13" or
command=="attempt to land" or
command=="land at station" or

command=="dont land" or
command=="don't land" or
command=="go home" or
command=="leave" or
command=="dont land at station" or
command=="keep flying" or
command=="keep going" or
command=="pass station" or
command=="fly away" or
command=="nothing" or
command=="stop" or

command=="q" or
command=="quit" or
command=="Quit"
):
	if(introCounter==10):
		print("The best course of action would be to try to land at the station.")
	elif(introCounter==5):
		print("Try landing the ship!")
	elif(introCounter<=0):
		print("Really?... Type \"try to land\".")
	else:
		print("What? That doesnt make any sense. Try something else. Hurry!")
	print()
	command = input("> ")
	introCounter=introCounter-1

if(
command=="land" or 
command=="engage landing gear" or
command=="go forward" or
command=="go to station" or
command=="go to Station" or
command=="station" or
command=="Station" or
command=="Land ship" or
command=="land ship" or
command=="Land" or
command=="land the ship" or
command=="land spaceship" or
command=="land the spaceship" or
command=="try to land" or
command=="go to station 13" or
command=="go to Station 13" or
command=="attempt to land" or
command=="land at station"):

	print("\n You manage to aim your ship towards the station, but thats about it. You brace for impact as you speed towards the hangar bay.")
	print("        Just before your ship smashes into the station, you catch a glipse of the hangar's label: \"Hangar #1 West\".")
	print("                                 You hear a massive crash and everything goes dark.\n")
	print("                                                       .....\n")
	print("          You regain conciousness. It seems either all the doors were closed, or the entire station was vented,")
	print("                             as there was no rush of air escaping the breach.")
	print("             With no oxygen there was no fire, although your ship is in tatters, lying on it's side.")
	print("           You manage to unbuckle yourself. You fall to the ground, and pull yourself out of the ship.")
	print("    You are obviously injured, you need to find your medical supplies. Unfortunately, your onboard supplies are obliterated.")
	print("            You will have to use what's on the station to heal yourself before it's too late, and to find a way home.")
	print("                                 You hear a faint automated voice on the station's intercom.")
	print("It says:\"Welcome to Station 13! If you get lost, you can simply type the keyword  \"commands\". Have a nice Sta.....\" before dying out completely.")
	print("         You assume the tiny amount of reserve power left ran out while playing that message. What will you do from here?\n")
	print(look("")+"\n")
	
	while True:
		command = input("> ")
		if command == "q" or command == "quit" or command == "Quit": break
		try:
			command = command.split(" ")
			if(command[1] == "to"):command.pop(1)
			if(command[1] == "up"):command.pop(1)
			if(command[1] == "at"):command.pop(1)
			if(command[1] == "the"):command.pop(1)
			verb = command.pop(0)
			noun = " ".join(command)
		except:
			if(command):
				verb = command.pop(0)
				if(verb=="n" or verb=="s" or verb=="e" or verb=="w" or 
				verb=="north" or verb=="south" or verb=="east" or verb=="west" or 
				verb=="North" or verb=="South" or verb=="East" or verb=="West" or 
				verb=="nw" or verb=="sw" or verb=="ne" or verb=="se" or
				verb=="northwest" or verb=="southwest" or verb=="northeast" or verb=="southeast" or
				verb=="Northwest" or verb=="Southwest" or verb=="Northeast" or verb=="Southeast"):
					noun = verb
				else:
					noun = ""
			else:
				verb = noun = ""
		handler = handlers.get(verb, unrecognized)
		result = handler(noun)
		print(result)
		
		if (timeUntilDeath>-1):
			timeUntilDeath=timeUntilDeath-1
		if(timeUntilDeath==20):
			print("Remember, you're injured! you need to find medical supplies.")
		if(timeUntilDeath==15):
			if(med_bay.visited):
				print("Try using the medkit.")
			else:
				print("Hurry up and find those supplies. You feel lightheaded.")
		if(timeUntilDeath==11):
			if(med_bay.visited):
				print("Hurry up and use the medkit, you're hurt.")
			else:
				print("You're hurt, you need to find the med bay.")
		if(timeUntilDeath==8):
			if(med_bay.visited):
				print("You feel dizzy. Use the kit!")
			else:
				print("You feel dizzy. You need to find the med bay soon.")
		if(timeUntilDeath==5):
			if(med_bay.visited):
				print("You are losing blood. Use the medkit quickly!")
			else:
				print("You are losing blood. Find the Med Bay now!")
		if(timeUntilDeath==3):
			print("You are bleeding out. You don't have much time left!")
		if(timeUntilDeath==1):
			print("You can barely move. Your eyelids are heavy. This is your last chance.")
		if(timeUntilDeath==0):
			print("You cant keep your eyes open anymore. You lose conciousness and soon die from blood loss.")
			print("                                                       ~~GAME OVER~~")
			gameOver = True
		
		if (timeUntilSuffocation>-1):
			timeUntilSuffocation=timeUntilSuffocation-1
		if(timeUntilSuffocation==180):
			print("Don't forget, you need to turn on the station's Life Support System somehow.")
		if(timeUntilSuffocation==130):
			if(conditionsMet.count("power") == 1):
				print("You have power. Now you need to find a way to turn on life support.")
			else:
				print("Dont lose hope! There must be a way to restore power before you run out of air.")
		if(timeUntilSuffocation==100):
			if(conditionsMet.count("power") == 1):
				print("Hurry up, the air's getting thinner.")
			elif(generator_room.visited):
				print("There must be a way to repair the generator!")
			else:
				print("There must be a generator room somewhere!")
		if(timeUntilSuffocation==70):
			if(conditionsMet.count("power") == 1 and control_room.visited):
				print("You have to turn on the Life Support System as soon as possible.")
			elif(conditionsMet.count("power") == 1):
				print("You have to turn on the Life Support System as soon as possible. Look for the control room!")
			elif(generator_room.visited):
				print("Use the repair kit on the generator.")
			else:
				print("Find the generator room now! you're low on oxygen.")
		if(timeUntilSuffocation==50):
			print("Your suit beeps at you, warning that your oxygen supply is getting low.")
		if(timeUntilSuffocation==30):
			print("You dont have much oxygen left. you can only last so long.")
		if(timeUntilSuffocation==15):
			print("You're getting lightheaded. Hurry up!")
		if(timeUntilSuffocation==5):
			print("You're basically holding your breath. you only have a couple of minutes!")
		if(timeUntilSuffocation==1):
			print("Your vision begins to go dark. This is your last chance!")
		if(timeUntilSuffocation==0):
			print("Your vision fades to black. You lose conciousness and soon die from suffocation.")
			print("                                                       ~~GAME OVER~~")
			gameOver = True
		
		if(gameOver):
			break
		
		print()
elif(
command=="q" or
command=="quit" or
command=="Quit"
):
	pass
else:
	print("\n         You start to turn your ship away, holding onto hope that some cargo ship or something will find you before you run out of air.")
	print("                                   The agitated beeping of your ship's console increases in volume.")
	print("The automated voice on the intercom cherily explains that the ship's structure, engines, and other systems are about to expirence catasrophic failure.")
	print(" Your eyes widen as you realize you missed your chance. You start to scream, but you are cut off by the massive explosion eminating from the engines.")
	print("                                  The explosion vaporizes you. You are utterly, and exteremely, dead.")
	print("                                                       ~~GAME OVER~~")