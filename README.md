A 3-d game for associates to learn the fundmentals of stacking boxes, loading belt, and stacking non-con

Game purpose is to educate users using a more realistic approach to box stacking than existing games.

- It achieves this by simulating a 3d world
- Introduces time contraints such as:
    - scan rate (average 180 packages per hour or 3 per minute)
    - belt stops twice in a minute (load reaches 100 for belt to stop)

- Balancing Non-Con load with Auto-Scan load
    - if non-con goes over 100, you lose (non con reaches 100 boxes unscanned)
    - if auto-scan goes over 100, you lose (belt stops 2 times in a min or something)

Two separate Games:

    Unload Truck Game:
        - stack non-con from side
        - if too many non-cons go up and auto side stops 2 times in a min (auto-side reaches 100 boxes 
        twice in a minute) you lose!
        - if too many non-cons get taken off (non-con reaches 100 capacity) you lose!
        - if stack collapses (heavy - meduim - light ratio is off), you lose!
        - if boxes go outside of pallet, instability meter increases. once instability reaches threshold, you lose!

    Auto-side Stack game
        - if you don't scan 3 packages per min, you lose!
        - if stack collapses, you lose! (instability meter reaches threshold)
     
Objects:

    Boxes (load count):
        - boxes who are long -> +3 
        - boxes who are heavy -> +5
        - boxes who are wide -> +3
        - boxes who are long and wide -> (3+3) || 6
        - boxes who are long and wide and heavy -> (5+3+3) || 11
        - boxes who are small -> +1
        - boxes who are light -> +1
        - boxes who are meduim (size) -> +2
        - boxes who are meduim (weight) -> +2

    Boxes (weight count):
        - heavy : 40+ lbs
        - medium: 10-39 lbs
        - light: 0-9 lbs

    Auto-side:
        - limit is 100 load

    Non-con: 
        - limit is 100 load

    Stack:
        - bottom must be 50% or more weigtht of entire stack
        - middle must be 40% or less than entire stack
        - top must be 10% or less than entire stack

    Processing:
        - big / heavy packages take longest to process 
        - ^ this logic continues down the line with medium, then small...

    Vars:
        load - amount of volume possible (auto-side and non-con)
        weight - heavy (increases load significantly), light (increases load trivially)
        size - large (increases load significantly), light (increases load trivially)
        stability - 50% of containers weight must be on bottom, 40% in the middle, and 10% on top
                  - 90% of boxes must be within the boundaries of the pallet
                  - 4 sides of pallet must share weight equally, close to 1/4 per quarter. 
                  "Close" as in one side can't equal 1/8 or less of total weight.

    Ways to Lose:
        - time expires to unload a truck
        - belt stops twice due to overload on auto (surpasses capacity twice)
        - non-con surpasses capacity 
        - pallet collapses

    Bugs to Fix:
        - when box reaches top, it just disappears. ideally would like
        box to disappear pixel line by pixel line as the object moves 
        past the screen
        - this only occurs when box reaches top because it appears that when the box starts to emerge on the bottom, it's being built pixel line by pixel line and not just instantly being destroyed or deallocated like when it reaches the top


How to Get Started (the hardest part):

    First, what are benefits of making this:
        - demonstrate to amazon executives my interest in the company and my value
        - learn how to create a fully functional game that has real world implications
        - develop my skills by developing something that captivates me and a topic i have first hand knowledge of
        - a game is a more attractive option for others to test than say a website 
        - because i work in the warehouse, i can tweak the game when changes are made in the 
            warehouse, making it up to date with the real world
        - lots of opportunities to pivot to other educational games as there are many tasks
            that require training in the warehouse and in places of work in general
        - can advertise this game in my portfolio for employers and capture their attention by 
            highlighting that it is an educational game for employees to become more knowledgable and skilled
            in their work 
    
    Okay, what are the cons?
        - time consuming
        - could easily get discouraged as i don't even know if this game will be desriable to employers
        - easily discouraged by coding challenges i will encounter when developing
        - doesn't really help me learn web development which has been a mission of mine
        - a much more skilled dev could catch wind of my game and develop their own superior version 
        - may serve as a distraction in me learning web development 

    Solutions to cons:
        - yes, it's going to take time but time coding is time well spent 
        - if it isn't desirable, pivot into an educational game that could be more attractive
        - coding challenges is how you learn
        - make sure you are spending at least an hour a day on web dev
        - yes, someone could steal idea. if they do, pivot to other educational game
        - make sure you are spending at least an hour a day on web dev