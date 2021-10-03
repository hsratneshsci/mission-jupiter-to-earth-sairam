# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the 
# name of the character.

define cap = Character("captain", colour="#e03838")
define la = Character("Laura")
define li = Character("Liza")
define st = Character("steve")
define t = Character("tony")
define tm = Character("team members")
define cc = Character("control center")
define lc = Character("launch center")
define fun = Character("Mr.Funnuat")





# The game starts here.
 

label start:
     
    scene bg deck
    show fun angry at left


fun "hi iam Mr.Funnuat"
fun "i am help you in this story"
fun "do you know abt space and launch events before luanch"


menu:

    "yes a little":
        jump yes

    "no i dont know much":
        jump no

label yes:

    fun "i will teach you more then you know in a fun way"
    "ok lets move on with story"

    jump story

label no:

    cap "you will be getting to know most of mystery"
    "ok lets move on with story"

    jump story

label story:   

"{b}location:earth.{/b}"
hide fun    
show cap normal at left 

menu:

    "Hello friends my name is jim and i am your team captian":
        jump friendly
    "Hi iam jim and i am your captian":
        jump non_friendly

label friendly:

    cap "Hello friends my name is jim and i am your team captian."

    jump story_start

label non_friendly:

    cap " Hi iam jim and i am your captian"

    jump story_start

label story_start:

tm "hello sir!"

show laura normal at right 
la "Hello sir i am laura co-pilot."
hide laura
show liza happy at right
li "Hello cap i am liza para-medical"   
hide liza 
show steve normal at right
st "Hello sir i am steve senior technician and mechanical" 
hide steve
show tony happy at right
t "Hello sir i am tony junior technician and mechanical"
hide tony

cap "i know you guys are well traineed astronaut.we are going to a mission from earth to jupiter."
cap "after finishing our research we are going to mars for another research. so we are going to do two missions."

menu:

    "We will be coming back after 4.5 years so are you ready for the missions.":
        jump years

    "What are you guys up to":
        jump what

label years:
    show laura happy at right
    la "Really i never thaught that will be this much long"

    jump main_timeline

label what:
    show laura happy at right
    la "I think it will take 4.5 years to travel"

    jump main_timeline

label main_timeline:
hide laura

tm "Yes sir. But before going to space can we meat our family members."

cap "Ok after two days we have the launch so come before the launch!"
hide cap
show fun angry at left 
menu:
    
    "Ok after two days we have the launch so come before the launch!":
        jump launch_seq

    "No i dont know much":
        jump cool

label launch_seq:
    show fun angry at left
    fun "I will teach you more then you know in a fun way"
    "Ok lets move on with story"

    jump main_timeline_2

label cool:
    show fun angry at left
    fun "You will be getting to know most of mystery"
    "Ok lets move on with story"

    jump main_timeline_2

label main_timeline_2:
show fun angry at left
fun "The luanch starts on next day "



# launching day team
fun "today launch will be good the launch"
fun "there will be long run tests befre launch"
fun "the launch test will be explain"



hide fun
show cap normal at left

menu:

    "Hello guys are you ready for going to jupiter?":
        jump cool_1

    "what are you guys thinking, we are going to jupiter today":
        jump friends_1

label cool_1:

    la "i bit nevrous but this is good"

    jump story_main_2

label friends_1:

    la"we will be getting to know most of mystery"
    

    jump story_main_2

label story_main_2:

tm "Yes sir we are ready for the mission jupiter."

cap "Get ready for the mission jupiter we are going to takeoff from earth in 10 minutes."
menu:

    "Get ready for the mission jupiter we are going to takeoff from earth in 10 minutes":
        jump main_timeline_3

    "we are going in 10 min":
        jump dont_want

label main_timeline_3:

    cap "Get ready for the mission jupiter we are going to takeoff from earth in 10 minutes."

    jump maintains_2

label dont_want:

    cap "hurry i need this "

    jump maintains_2

label maintains_2:

#control center
#test explain
fun "here the test starts "
fun "these are the main test done before launch"
hide fun
hide cap
cc "Orbiter Test Conductor (OTC) pass"
cc "Tank and Booster Conductor (TBC) pass"
cc "Payload Test Conductor (PTC) pass"
cc "Launch Processing System (LPS) pass"
cc "Flight Director (FLT) pass"
cc "Safety Console Coordinator (SCC) pass"
cc "Landing and Recovery Director (LRD) pass"

cc "Weather check pass"
cc "T-Minus 9 Minutes"
"computer program that handles all activity during the final moments of the countdown, takes control of the countdown sequence"

cc "launch control go for launch"
cc "rocket ready to launch"
cc "T-Minus 7 Minutes, 30 Seconds"
show fun suprised at left
fun "{b}orbiter access arm retracts{/b}"
hide fun
cc "T-Minus 5 Minutes"
show fun suprised at left
fun "{b}orbiter’s auxiliary power units (APU) turns on{/b}"
hide fun
cc "T-Minus 2 Minutes"
show fun suprised at left
fun "{b}The shuttle commander tells fellow crewmates to retract the visors of their entry and launch suits as the GLS maintains automatic countdown control.{/b}"
hide fun
cc "T-Minus 31 Seconds"
show fun suprised at left
fun "{b}Barring any technical issues{/b}"
fun "{b}the GLS shifts countdown control to the computers aboard the space shuttle.{/b}"
hide fun
cc "T-Minus 16 Seconds"
show fun suprised at left
fun "A sound suppression water system is activated"
fun "{b}which serves to protect the space shuttle from the massive sonic energy that is produced during takeoff. The water system can expel up to 900,000 gallons of water per minute{/b}"
hide fun
lc " rocket is ready to launch"


cc "T-Minus 6 Seconds"
show fun suprised at left
fun "The command is relayed to initiate the space shuttle’s three main engines."
hide fun
cc "5.."
cc "4.."
cc "3.."
cc "2.."
cc "1.."
lc" whooo"

# rocket take off
show cap happy  at left
cap "wohoo we are flying in the space."
menu:

    "wohoo we are flying in the space":
        jump minor_2

    "we are flying in space":
        jump minor_1

label minor_2:

    tm "Yes sir we are very excited for this day"

    jump main_timeline_4

label minor_1:

    tm "Yes sir we are very excited for this day"

    jump main_timeline_4

label main_timeline_4:


"{b}day 200{/b}"
show laura normal at right 
la "We are going well in correct direction."
hide laura
show cap normal at left
cap "In this speed we will reach the jupiter in 600 days."


menu:

    "In this speed we will reach the jupiter in 600 days.":
        jump time_1

    "we will reach ":
        jump time_2

label time_1:
    hide cap
    show fun suprised at left
    fun "i will teach you more then you know in a fun way"
    "ok lets move on with story"
    hide fun

    jump main_timeline_5

label time_2:
    show cap happy at left
    cap "you will be getting to know most of mystery"
    "ok lets move on with story"
    hide cap

    jump main_timeline_5

label main_timeline_5:
hide cap
#reaching asteroid belt

cc "be carful you are near asteroid belt "
show cap normal at left
cap "copy that"
cap "we are near asteroid belt between mars and jupiter"
hide cap
show laura happy at right
la "this looks cool in real"
hide laura
show fun suprised at left
show fun scared at left
fun "asteroids sometime reffered as minor planets"
fun "there are some largest asteroids like Ceres,vesta,pellas"
fun "sometimes ceres are reffered as dawrf planet"
hide fun



"{b}Day 400:{/b}"
show laura happy at left
la "There are just few months to reach jupiter"
"liza,steve and tony""we are excited for when we will reach jupiter." 
hide laura
show cap happy at left
cap "come guys lets have a our lunch"
cap "i get this everyday frozen cheese sandwiches"
hide cap
show fun suprised at left

fun "they eat frozen food"
fun "fun fact nasa worked on menu to make it tasty and different food"
fun "now they can eat foods like crackers,fruits,soup"
hide fun
show cap happy at left 
cap "get me some water "

show liza happy at right 
li "ok cap"
hide liza
hide cap
show fun suprised at left
fun "they would normaly add water to packets to eat"
hide fun
#we reach jupiter
"{b}day 600{/b}"
show cap happy at left 
cap "Hello team members we are going to land to planet jupiter'moon."
hide cap 
show fun suprised at left
fun "fun fact jupiter has 79 moons "
fun " Io, Europa, Ganymede and Callisto are the four main moons"
hide fun

#After landing on the planet jupiter moon europa
"landed on europa ~jupiter's moon~"
show cap normal at left 
cap "Hello everyone we have landed on the planet jupiter moon europa"
show cap suprised at left 
cap "i am proud to be the first person land on moon europa"
hide cap

cc "*first person to set step on moon is jim*"

tm "Finally we reached our destination."
show cap happy at left
show laura happy at right
la "this is cool see this in real better than pics "

cap "Don't be excited be carefull we don't know what is the situation on this planet."
hide laura
tm "COPY THAT"
"{b}Day 602:{/b}"
show laura happy at right
la "Sir its solar system is made of molecular hydrogen and helium and other chemical"
la "compounds are present only in small and include methane,ammonia,hydrogen sulphide and water."
la "ice is present here i will pick some for testing"
hide laura
hide cap
show fun suprised at left

fun "fun fact there are water and ice traces on moons of jupiter"
hide fun
show cap happy at left
cap "ok take some "
cap "it has low gravity too"

show tony scared at left
t "i wish there are no aliens here"
hide tony
show steve happy at left
st "yep"
hide steve

show cap angry at left
cap "guys no pop culture refernce"
hide cap


# leaving europa
"{b}Day 700:{/b}"
"{b}leaving europa{/b}"
show cap normal at left
cap "so finally we are returning back to our planet earth after a long time."
hide cap 
tm "Yes sir we were away from from home for a long time but now we are very "
tm "excited for when will we reach our planet and see our family members."
show cap normal at left
cap "Have patience we will be at home soon."
hide cap


#way back home
show laura happy at right
la "caption you need to look at this"
show cap normal at left
cap "yes what is the problem"
show laura normal at right
la "there is an obstacle i think it must be  asteroid from before"
show cap normal at left 
cap "try changing flight path"
hide cap 
hide laura
cc "do you guys have visual of asteroid" 
show tony scared at left
t "aare you crazy a asteriod is coming towards us and you are doing nothing?"
hide tony
show cap scared at left
cap "everyone dont panic sit in your seats"
hide cap 
show fun suprised at left 
fun "all mordern spacecrafts have pre alert system and evacuation plan  "
show fun suprised at right
fun "in these kind of cases the the control center takes control"
hide fun
show cap happy at left
cap "problem sloved"
hide cap
tm "that was a close call"
show cap happy at left
cap "we will reach home in 80 days"
hide cap

#earth landing 
show cap happy at left
cap "is everyone ready to land on earth"
hide cap
tm "yes"
show cap happy at left
cap "..."
cap"everyone get back to their seats"
hide cap
tm "yes cap"
show cap happy at left
cap "we are entering earth orbit"
cap "we are going to land in indian ocean"
hide cap

cc "how was your trip guys"
show cap happy at left
cap "that was too good "
hide cap
show fun suprised at left
fun "normally astronaut been in space for long time will have hard times in earth "
show fun scared at left
fun "astronaut cant walk because of gravity"

fun "story ends here  "



show fun suprised at left

#quiz opition
fun "do you wish to take a qwiz in here"


menu:

    "yes i would love to have them":
        jump yes_answer

    "nope sry":
        jump no_answer

label yes_answer:

    fun "thats cool the test starts now"

    jump qwiz

label no_answer:

    fun"no prob "

    jump qwiz

label qwiz:
#qwiz starts here





"your result"
fun "you are doing great keep it up"

fun "no worry better luck next time"

return
