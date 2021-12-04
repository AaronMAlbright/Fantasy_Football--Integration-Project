"""Integration project: Fantasy football themed project"""

__author__ = "Aaron Albright"

# reference: https://www.geeksforgeeks.org/python-statistics-stdev/
# - Used for import statistics to receive stdev() formula

import statistics
import random
import math


def main():
    """- implements a calculator for an individual football player's fantasy
    point total ( from a one game sample) -
       - Calculates a fantasy score per player in relation to the user's
       fantasy team's roster size -
       - Based on the calculated fantasy scores, the function determines a
       start or sit decision. The individual player's score is compared
       to the average of the team's points scored. The quality of the start
       /sit is analyzed based on relation standard deviations above mean and
        the mean itself-
       - User also has option to quit using the program and exit the program
       from the menu
       """

    game = "fantasy football "
    program = "Score calculator and Start/Sit Decision program"
    print("Hello " * 2, "! Welcome to the " + game.capitalize() + program,
          ":", " program", end=' ')
    print('12', '4', '2021', sep='-')
    positions = ['QB', 'WR', 'RB', 'TE', 'FLEX']
    qb = 0
    wr = 0
    rb = 0
    te = 0
    flex = 0
    # Number of roster spots is neccessary in order to calculate the average
    # score per fantasy player
    continue_program = True
    while continue_program:
        try:
            qb = int(input("number of qb spots?"))
            wr = int(input("number of rb spots?"))
            rb = int(input("number of wr spots?"))
            te = int(input("number of te spots?"))
            flex = int(input("number of flex spots?"))
            break
        except ValueError:
            print("must be in numerical form")

    spots = qb + rb + wr + te + flex
    print("Player Spots", spots)
    continue_program = True
    while continue_program:
        try:
            yards = int(input("number of yards did your "
                              "player pass/rush/receive?:"))
            break
        except ValueError:
            print("Error. Must be a whole number")
    print("Player Spots", spots)
    # Main scoring difference in leagues is based upon how many times a player
    # -cont., catches a ball. Catching a ball is thought to be more of a skill
    # rather than just getting the ball handed off or throwing the ball
    # randomScoringSelector-https://stackabuse.com/how-to-randomly-select-elements-from-a-list-in-python/
    # I wanted the program to randomly pick a scoring format based on catches
    # Catch = reception
    # tight ends usually catch the ball less compared to a Wide receiver
    # Running backs can catch the ball as-well but they usually carry the ball
    # Quarterbacks essentially have no opportunity to catch the ball
    pts_per_reception_list = [0, 0.5, 1]
    r = random.choice(pts_per_reception_list)
    print(r, "Points per reception")
    if r > 0:
        print("non-standard scoring")
    elif 0 < r < 1:
        print("Full PPR scoring")
    elif r < 0.5:
        print("standard scoring")
    # touchdown = 6 points
    td = 6
    # QBs throw more touchdowns comparatively, so passing touchdowns are worth
    # less
    pts_per_passing_td = 6 // 1.5
    print("[Player #1: Point Calculator]")
    print("Yards", yards)
    # every 10 yards is 1 point
    # QBs accumulate more yards than other positions
    # So passing yards are worth less than receiving/rushing yards
    rush_yard_points = float(yards / 10)
    print(rush_yard_points, "points - rushing")
    pts_per_passing_yards = yards // 20
    print(pts_per_passing_yards, "points- passing")
    receiving_yard_points = float(yards / 10)
    print(receiving_yard_points, "points - receiving ")
    while continue_program:
        try:
            tds = int(input("How many touchdowns did the player score?:"))
            break
        except ValueError:
            print("must be numerical value")
    touchdown_points = tds * td
    while continue_program:
        try:
            receptions = int(
                input("How many times did the player catch the ball?"))
            break
        except ValueError:
            print("must be numerical value")
    # ppr points are the points per reception made. PPR value will depend on
    # the randomly selected scoring format from earlier in the program
    ppr_points = r * receptions
    passing_touchdown_points = pts_per_passing_td * tds
    # total points adds touchdowns,yards,and receptions(if player catches the
    # ball)
    print("Scores: Based on position")
    total_points_for_WR = touchdown_points + receiving_yard_points + ppr_points
    total_points_for_RB = touchdown_points + rush_yard_points + ppr_points
    total_points_for_QB = passing_touchdown_points + pts_per_passing_yards
    total_points_for_TE = touchdown_points + receiving_yard_points + ppr_points
    print(total_points_for_WR, "Wr")
    print(total_points_for_RB, "Rb")
    print(total_points_for_QB, "Qb")
    print(total_points_for_TE, "Te")
    continue_program = True
    # User interface selection menu
    while continue_program:
        try:
            print("Enter the choice for what you would like to see")
            print('[1. Point calculator: Entire Team]')
            print("[2. Sit/start]")
            print("[3.quit]")
            # calculates fantasy player scores based on roster spots
            user_choice = int(input())
            if user_choice == 1:
                n = 0
                for i in range(spots):
                    if n != spots:
                        while continue_program:
                            try:
                                yards = float(input(
                                    "enter yards receiving/passing/rushing: "))
                                break
                            except ValueError:
                                print("Please input numerical value for yards")
                        print(yards)
                        # every 10 yards is 1 point
                        # QBs accumulate more yards than other positions
                        # So passing yards are worth less than receiving/
                        # rushing yards
                        rush_yard_points = float(yards / 10)
                        print(rush_yard_points, "points - rushing")
                        pts_per_passing_yards = yards // 20
                        print(pts_per_passing_yards, "points- passing")
                        receiving_yard_points = float(yards / 10)
                        print(receiving_yard_points, "points - receiving ")
                        touchdown_points = tds * td
                        ppr_points = r * receptions
                        while continue_program:
                            try:
                                tds = int(input("Enter touchdowns scored"))
                                break
                            except ValueError:
                                print("must be numerical value")
                        while continue_program:
                            try:
                                receptions = int(
                                    input("Enter number of receptions"))
                                break
                            except ValueError:
                                print("must be numerical value")
                        passing_touchdown_points = pts_per_passing_td * tds
                        # total points adds touchdowns,yards,and receptions
                        # (if player catches the ball)
                        print("Scores: Based on position")
                        total_points_for_WR = touchdown_points \
                                              + receiving_yard_points + \
                                              ppr_points
                        total_points_for_RB = touchdown_points \
                                              + rush_yard_points + \
                                              ppr_points
                        total_points_for_QB = passing_touchdown_points \
                                              + pts_per_passing_yards
                        total_points_for_TE = touchdown_points \
                                              + receiving_yard_points + \
                                              ppr_points
                        print(total_points_for_WR, "Wr")
                        print(total_points_for_RB, "Rb")
                        print(total_points_for_QB, "Qb")
                        print(total_points_for_TE, "Te")
                        n += 1
                    else:
                        return
            elif user_choice == 2:
                # sit start is the decision made weekly by fantasy managers
                # sit means the players score is too low to give the fantasy
                # manager a winning chance
                # start is reserved for players that score an amount of
                # points over a certain threshold
                # in this case  the threshold is the average points per team
                print("[sit - start:]")
                while continue_program:
                    n = 0
                    try:
                        start_selector = input(str("enter position"))
                    except ValueError:
                        print("Please type using alphabet")
                    if n == 0:
                        if len(start_selector) > 2:
                            print("Type in position by abbreviation")
                        elif len(start_selector) == 2:
                            n = + 1
                    if n >= 1:
                        break
                # Reference:https://www.youtube.com/watch?v=v_SfdDk3Wyk
                # "How to take a user
                # input for list in python
                print("enter each players score calculated score")
                points = []
                for i in range(spots):
                    try:
                        data = float(input())
                        points.append(data)
                    except ValueError:
                        print("Please print score in numerical form")

                sum_of_points = sum(points)
                total_players = len(points)
                average_points = sum_of_points / total_players
                print(average_points)
                stdev = statistics.pstdev(points)
                # stdev is used here as a factor to gauge the performance
                # of the fantasy player in comparison to the average points
                # scored per player
                if start_selector == "qb" or "QB":
                    if total_points_for_QB >= average_points:
                        if total_points_for_QB >= average_points + stdev:
                            score = "Above Average - start-able"
                        elif total_points_for_QB >= average_points + stdev / 2:
                            score = "Average - startable"
                        elif total_points_for_QB >= average_points:
                            score = "start if no other option"
                    else:
                        score = "Must sit"
                if start_selector == "rb" or "RB":
                    if total_points_for_RB >= average_points:
                        if total_points_for_RB >= average_points + stdev:
                            score = "Above Average - start-able"
                        elif total_points_for_RB >= average_points + stdev / 2:
                            score = "Average - startable"
                        elif total_points_for_RB >= average_points:
                            score = "start if no other option"
                    else:
                        score = "Must sit"
                if start_selector == "wr" or "WR":
                    if total_points_for_WR >= average_points:
                        if total_points_for_WR >= average_points + stdev:
                            score = "Above Average - start-able"
                        elif total_points_for_WR >= average_points + stdev / 2:
                            score = "Average - startable"
                        elif total_points_for_WR >= average_points:
                            score = "start if no other option"
                    else:
                        score = "Must sit"
                if start_selector == "te" or "TE":
                    if total_points_for_TE > average_points / 2:
                        if total_points_for_TE >= average_points / 2 + stdev:
                            score = "Above Average - start-able"
                        elif total_points_for_TE >= average_points / 2 + \
                                stdev / 2:
                            score = "Average - startable"
                        elif total_points_for_TE >= average_points / 2 - stdev:
                            score = "start if no other option"
                    else:
                        score = "Must sit"
                print("Your average points per player is: ", average_points)
                print("The standard deviation of points is", stdev)
                print(start_selector)
                print("_____your player start/sit:_______", score)
                print(total_points_for_TE, "Te")
                print(total_points_for_RB, "Rb")
                print(total_points_for_QB, "Qb")
                print(total_points_for_WR, "Wr")
            elif user_choice == 3:
                # demonstration of the project's requirements that were not
                # achieved in the function. And or not relevant to the
                # theme of the project. Includes % and ** operators
                print("demonstration of missing requirements")
                exponent = total_points_for_QB ** 2
                modulus = total_points_for_QB % 3
                print(exponent, modulus)

                print("thank you for using the program")
                print("3")
                print("2")
                print("1")
                return
            else:
                if user_choice not in range(1, 3):
                    print("not in range")
        except ValueError:
            print("must be numerical value")


main()
