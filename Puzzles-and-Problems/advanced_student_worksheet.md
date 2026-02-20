This is a proto-assessment. It's being given to you because I've identified that your skills may surpass the outcomes of this class.
If you are able to finish this exercise under assessment conditions (only accessing language documentation; no use of LLMs; no collusion), then I will release the final project to you.

---

# Dungeon Escape Exercise

## Task Description
You are a junior developer at an old-school gaming company.
You have been tasked with making a command-line, text-based adventure, based on the given scenario.
Your product manager has left you the Game Scenario, and your senior developer has written some Acceptance Criteria for you.

## Game Scenario
The player has woken up in a mysterious dungeon.  They need to find the escape. The player is able to do the following actions:
- go (north, east, south, west)
- look around (this shows a deeper description.)
    - investigate (this triggers the secondary event on the room.  )
- check notes

Looking around a room is the primary way to get a room's description, and may trigger a secondary event, such as a hazard.

There are a total of *six rooms*, as follows:
1. The Cell
- description: "You are in a stone cell.  You're not sure how you got here, but you have to get out.  There's a door to the east."
- deeper description: "The door is unlocked.  That doesn't seem right, but you're not going to complain."
- secondary event: none.
- notes: The player starts here.
- exits:
    - east: The Alchemist's Lab

2. The Alchemist's Lab
- description: "It's some kind of alchemical laboratory. There's a lot of concerning looking bubbling flasks."
- deeper description: "Those flasks definitely don't look safe.  You shouldn't get any closer or you might get hurt."
- secondary event: "Noxious gas rises from the flasks, and as you breathe it in, you find yourself losing consciousness.  Better luck next time." & end game
- exits:
    - west: The Cell
    - north: Arcane Library
    - east: Guard's Quarters
    - south: Collapsed Passage

3. Arcane Library
- description: "It's a library.  Probably.  There's certainly a lot of books."
- deeper description: "There's some loose notes on one of the desks.  Actually, those might be useful."
- secondary event: "This looks like some kind of password, written here.  You take the note with you." && set a flag for "having the note"
- notes: the player cannot put the note down again
- exits:
    - south: The Alchemist's Lab

4. Collapsed Passage
- description: "This probably used to be a hallway to somewhere useful, but it's collapsed"
- deeper description: "That's a lot of fallen rocks"
- secondary event: None
- exits:
    - north: The Alchemist's Lab

5. Guard's Quarters
- description: "Looks like the Guard's quarters. You can hear someone patrolling around in here.  Better be careful."
- deeper description: "There's a draft coming through the door to the south.  Maybe it's your way out?  Don't alert the guard."
- secondary event: "You thought you were being quiet, but as you investigate, the guard comes around a shelf and sees you.  They swing their club and you know no more.  Better luck next time." & end game
- exits:
    - west: The Alchemist's Lab
    - south: The Escape Tunnel

6. The Escape Tunnel
- description: "There's a door that definitely goes outside, here!"
- deeper description: "It looks like it needs some kind of special password to open the door.  Did you find anything like that?"
- secondary event:
    This event is special.  If the player has been to the Arcane Library and "has the note", they now have the opportunity to read it (from file).
    Then, they will be asked to enter the password from the note.  If they enter the wrong password, you should tell them "It didn't open.  Are you sure you said the password right?"
    The player has the opportunity to escape entering the password by saying "give up".
    Otherwise, the game should output: "You opened the door! Time to make your escape. Congratulations!" & end game
- exits:
    - north: Guard's Quarters


## Provided artefacts
- A code stub, to give you a hint towards the game's final factoring
- A text file, containing the game's "password"

## Acceptance Criteria
- [ ] The game can be quit at any time, by typing "quit".
- [ ] The game should gracefully turn down "junk" inputs by saying "I don't understand what you mean."
- [ ] The "note" in the Arcane Library *must* be read from a file, not hard-coded into the game.
- [ ] When a player enters a room, the game prints the room's description, as well as a list of possible prompts.
- [ ] If the player tries to exit a room in a direction that is not allowed, the player is told: "There is no door there".
- [ ] All rooms in the Game Scenario must be implemented.
- [ ] You must include a log of all player actions, which are recorded to a file called `log.txt`
- [ ] In your implementation you must include at least 
	- [ ] one list
	- [ ] one dictionary 


