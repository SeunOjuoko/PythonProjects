import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

#Creates a list for the state column
allStates = data.state.to_list()
#print(allStates)

CorrectGuesses = []
#print(data["state"])

while len(CorrectGuesses) < 50:
    answer = screen.textinput(title = f"[{len(CorrectGuesses)}/50] Guess The State", prompt = "Name the US state: ").title()

    if answer == "Exit":
        statesMissed = [state for state in allStates if state not in CorrectGuesses]
        # statesMissed = []
        # for states in allStates:
        #    if states not in CorrectGuesses:
        #        statesMissed.append(states)
        # print(f"You missed the states {statesMissed}")

        # Coverts to a dataframe to
        dataFrame = pandas.DataFrame(statesMissed)
        dataFrame.to_csv("MissingStates.csv")
        break
        
    if answer in allStates:
        CorrectGuesses.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        #Taps into the attributes within the csv file
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer)

    #turtle.onscreenclick(get_mouse_click_coordinates)
turtle.mainloop()

  
